/*
©Panagopoulos Nikolaos, 2025
All rights reserved.

Smart City System - Arduino Uno R3
*/

// ========== PIN DEFINITIONS ==========
const int LED1_PIN = 2;
const int LED2_PIN = 3;
const int LED3_PIN = 4;
const int LED4_PIN = 5;
const int LED5_PIN = 6;

const int RED_LED = 7;
const int ORANGE_LED = 8;
const int GREEN_LED = 9;

const int PIR_PIN = 10;
const int ECHO_PIN = 11;
const int TRIG_PIN = 12;
const int PIEZO_PIN = 13;
const int PHOTORESISTOR_PIN = A0;

// ========== CONSTANTS ==========
const int LIGHT_ON_THRESHOLD  = 930;
const int LIGHT_OFF_THRESHOLD = 960;

const unsigned long LIGHT_SAMPLE_MS = 2000;
const unsigned long FADE_DELAY_MS   = 5000;
const int FADE_STEP_DELAY_MS        = 10;

const int HC_MIN_CM = 2;
const int HC_MAX_CM = 400;
const unsigned long HC_MIN_PERIOD_MS = 60;
const unsigned long HC_ECHO_TIMEOUT_US = 30000UL;

const unsigned long TELEMETRY_MS = 500;

// Security sound only (NOT PIR sound)
const unsigned int SEC_ON_MS_CLOSE = 90;
const unsigned int SEC_OFF_MS_CLOSE = 90;

const unsigned int SEC_ON_MS_MED = 90;
const unsigned int SEC_OFF_MS_MED = 260;

const unsigned int SEC_ON_MS_FAR = 70;
const unsigned int SEC_OFF_MS_FAR = 900;

// ========== GLOBAL STATE ==========
unsigned long systemStartTime = 0;

unsigned long lastMotionTime = 0;
unsigned long lastLightSampleTime = 0;
unsigned long lastTelemetryTime = 0;

bool isNightTime = false;
bool streetLightsOn = false;
bool selfTestPassed = false;

// PIR state tracking (for print-on-change only)
bool pirWasActive = false;

// HC state
float lastUltrasonicCm = -1.0f;
bool ultrasonicValid = false;
int currentSecurityState = -1;

// Beeper state (SECURITY ONLY)
struct Beeper {
  bool on = false;
  unsigned long nextMs = 0;
  int freq = 0;
  unsigned int onMs = 0;
  unsigned int offMs = 0;
  bool active = false;
} beeper;

// ========== FORWARD DECLARATIONS ==========
void printHardwareConfig();
void detectNightTime();

void handleLightingSystem();
void handleSecuritySystem();
void handleSoundSystem();

void turnStreetLightsOn();
void turnStreetLightsOff(bool quiet);
void fadeStreetLightsOff();

void runSelfTest();
void waitForUserConfirmation();

enum USReadResult { US_TOO_SOON = 0, US_OK = 1, US_TIMEOUT = 2 };
USReadResult readUltrasonicCm(float &outCm);

void beeperStop();
void beeperSet(int freq, unsigned int onMs, unsigned int offMs);
void beeperUpdate();

// ========== SETUP ==========
void setup() {
  Serial.begin(9600);
  delay(500);

  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  pinMode(LED4_PIN, OUTPUT);
  pinMode(LED5_PIN, OUTPUT);

  pinMode(RED_LED, OUTPUT);
  pinMode(ORANGE_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  pinMode(PIR_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(PIEZO_PIN, OUTPUT);

  turnStreetLightsOff(true);
  digitalWrite(RED_LED, LOW);
  digitalWrite(ORANGE_LED, LOW);
  digitalWrite(GREEN_LED, LOW);
  noTone(PIEZO_PIN);

  printHardwareConfig();
  runSelfTest();

  systemStartTime = millis();
  lastLightSampleTime = millis();
  lastTelemetryTime = millis();
}

// ========== MAIN LOOP ==========
void loop() {
  if (!selfTestPassed) {
    static unsigned long lastBlink = 0;
    if (millis() - lastBlink > 500) {
      digitalWrite(RED_LED, digitalRead(RED_LED) ? LOW : HIGH);
      lastBlink = millis();
    }
    delay(50);
    return;
  }

  detectNightTime();

  handleLightingSystem();
  handleSecuritySystem();
  handleSoundSystem();

  delay(20);
}

// ========== HARDWARE CONFIG ==========
void printHardwareConfig() {
  Serial.println(F("=========================================="));
  Serial.println(F("SMART CITY - PIN CONFIG"));
  Serial.println(F("=========================================="));
  Serial.println(F("Street LEDs: D2..D6"));
  Serial.println(F("Alarm LEDs:  D7=RED, D8=ORANGE, D9=GREEN"));
  Serial.println(F("PIR:         D10"));
  Serial.println(F("HC-SR04:     ECHO=D11, TRIG=D12"));
  Serial.println(F("Piezo:       D13"));
  Serial.println(F("LDR:         A0"));
  Serial.println(F("==========================================\n"));
  delay(500);
}

// ========== SELF-TEST ==========
void runSelfTest() {
  Serial.println(F("\n+----------------------------------------+"));
  Serial.println(F("| SMART CITY SELF-TEST SUITE             |"));
  Serial.println(F("+----------------------------------------+\n"));

  // TEST 1: Alarm LEDs
  Serial.println(F("[TEST 1] Alarm LEDs"));
  digitalWrite(RED_LED, HIGH); delay(200); digitalWrite(RED_LED, LOW);
  digitalWrite(ORANGE_LED, HIGH); delay(200); digitalWrite(ORANGE_LED, LOW);
  digitalWrite(GREEN_LED, HIGH); delay(200); digitalWrite(GREEN_LED, LOW);
  Serial.println(F("OK"));

  // TEST 2: Street LEDs (individual)
  Serial.println(F("[TEST 2] Street LEDs"));
  const int leds[] = {LED1_PIN, LED2_PIN, LED3_PIN, LED4_PIN, LED5_PIN};
  for (int i = 0; i < 5; i++) {
    digitalWrite(leds[i], HIGH); delay(150);
    digitalWrite(leds[i], LOW);  delay(80);
  }
  Serial.println(F("OK"));

  // TEST 3: Piezo - SECURITY signature only (no PIR sound)
  Serial.println(F("[TEST 3] Piezo signature demo"));
  Serial.println(F("  A) Security CLOSE (high+fast)"));
  beeperSet(2200, 90, 90);
  unsigned long t0 = millis();
  while (millis() - t0 < 800) beeperUpdate();
  beeperStop();
  delay(300);

  Serial.println(F("  B) Security FAR (low+slow)"));
  beeperSet(420, 70, 900);
  t0 = millis();
  while (millis() - t0 < 1500) beeperUpdate();
  beeperStop();
  Serial.println(F("OK"));

  // TEST 4: Photoresistor basic sanity
  Serial.println(F("[TEST 4] Photoresistor"));
  int light = analogRead(PHOTORESISTOR_PIN);
  Serial.print(F("  Value=")); Serial.println(light);
  if (light <= 2 || light >= 1021) Serial.println(F("  WARNING: extreme value; check wiring/divider."));

  // TEST 5: Ultrasonic basic read (3 attempts, correct pacing)
  Serial.println(F("[TEST 5] HC-SR04"));
  bool gotUS = false;
  for (int i = 0; i < 3; i++) {
    float cm = -1;
    delay(100);
    USReadResult r = readUltrasonicCm(cm);
    if (r == US_OK) {
      Serial.print(F("  Distance=")); Serial.print(cm, 1); Serial.println(F(" cm"));
      gotUS = true;
      break;
    }
    Serial.println(F("  No echo (ok if no target / far / angle)."));
  }
  if (!gotUS) Serial.println(F("  NOTE: If you want to verify, place object ~20-100cm in front."));

  // TEST 6: PIR warm-up + motion verify
  Serial.println(F("[TEST 6] PIR warm-up (10s) then motion verify (10s)"));
  Serial.println(F("  Warm-up: keep still..."));
  unsigned long warm = millis();
  while (millis() - warm < 10000) {
    delay(50);
  }
  Serial.println(F("  Now wave hand (10s) ..."));
  bool pirSawHigh = false;
  unsigned long w = millis();
  while (millis() - w < 10000) {
    if (digitalRead(PIR_PIN) == HIGH) { pirSawHigh = true; break; }
    delay(50);
  }
  Serial.println(pirSawHigh ? F("  PIR motion detected: OK") : F("  PIR stayed LOW: WARNING (try again after full 60s warm-up)."));

  Serial.println(F("\nType 'Y' then ENTER to start..."));
  waitForUserConfirmation();
}

void waitForUserConfirmation() {
  while (true) {
    if (Serial.available()) {
      char c = Serial.read();
      if (c >= 'a' && c <= 'z') c = c - 32;
      if (c == 'Y' || c == 'F') {
        selfTestPassed = true;
        Serial.println(F("System Started.\n"));
        return;
      }
    }
    delay(50);
  }
}

// ========== NIGHT/DAY TIMER ==========
void detectNightTime() {
  unsigned long elapsed = millis() - systemStartTime;
  unsigned long cycle = elapsed % 60000UL;
  bool prev = isNightTime;
  isNightTime = (cycle < 30000UL);

  if (prev != isNightTime) {
    Serial.println(F("\n------------------------------------------------"));
    Serial.println(isNightTime ? F("TIME CHANGE: NIGHT MODE") : F("TIME CHANGE: DAY MODE"));
    Serial.println(F("------------------------------------------------"));
  }
}

// ========== STREET LIGHTING (LDR + PIR) ==========
void handleLightingSystem() {
  unsigned long now = millis();
  if (now - lastLightSampleTime < LIGHT_SAMPLE_MS) {
    // motion timeout still runs
    if (streetLightsOn && (now - lastMotionTime > FADE_DELAY_MS)) {
      int lightLevel = analogRead(PHOTORESISTOR_PIN);
      if (lightLevel > LIGHT_OFF_THRESHOLD) {
        Serial.println(F("[LIGHTS] No motion for 5s (bright) -> fading OFF"));
        fadeStreetLightsOff();
        streetLightsOn = false;
      } else {
        lastMotionTime = now;
      }
    }
    return;
  }
  lastLightSampleTime = now;

  int lightLevel = analogRead(PHOTORESISTOR_PIN);
  int pir = digitalRead(PIR_PIN);

  // Darkness override: lights ON
  if (lightLevel < LIGHT_ON_THRESHOLD) {
    if (!streetLightsOn) {
      Serial.print(F("[LIGHTS] DARK (")); Serial.print(lightLevel); Serial.println(F(") -> ON"));
      turnStreetLightsOn();
      streetLightsOn = true;
    }
    lastMotionTime = now; // prevent fade while dark
    
    // PIR state change print (even if dark)
    if (pir == HIGH && !pirWasActive) {
      Serial.println(F("[PIR] Motion detected"));
      pirWasActive = true;
    } else if (pir == LOW && pirWasActive) {
      Serial.println(F("[PIR] Motion stopped"));
      pirWasActive = false;
    }
    return;
  }

  // Bright: use PIR for energy saving
  if (pir == HIGH) {
    if (!streetLightsOn) {
      Serial.println(F("[LIGHTS] PIR motion (bright) -> ON"));
      turnStreetLightsOn();
      streetLightsOn = true;
    }
    lastMotionTime = now;
    
    // PIR state change print
    if (!pirWasActive) {
      Serial.println(F("[PIR] Motion detected"));
      pirWasActive = true;
    }
  } else {
    // PIR state change print (when motion stops)
    if (pirWasActive) {
      Serial.println(F("[PIR] Motion stopped"));
      pirWasActive = false;
    }
    
    if (streetLightsOn && (now - lastMotionTime > FADE_DELAY_MS)) {
      Serial.println(F("[LIGHTS] Bright + no motion -> fading OFF"));
      fadeStreetLightsOff();
      streetLightsOn = false;
    }
  }

  // Telemetry (low spam, state info only)
  if (now - lastTelemetryTime > TELEMETRY_MS) {
    Serial.print(F("[STATUS] Light: "));
    Serial.print(lightLevel);
    Serial.print(F(" | PIR: "));
    Serial.print(pir);
    Serial.print(F(" | StreetLights: "));
    Serial.print(streetLightsOn ? F("ON") : F("OFF"));
    Serial.print(F(" | Night: "));
    Serial.println(isNightTime ? F("YES") : F("NO"));
    lastTelemetryTime = now;
  }
}

// ========== SECURITY (ULTRASONIC, NIGHT ONLY) ==========
void handleSecuritySystem() {
  if (!isNightTime) {
    // Day: disable alarm indicators
    if (currentSecurityState != -1) {
      digitalWrite(RED_LED, LOW);
      digitalWrite(ORANGE_LED, LOW);
      digitalWrite(GREEN_LED, LOW);
      currentSecurityState = -1;
    }
    ultrasonicValid = false;
    lastUltrasonicCm = -1.0f;
    return;
  }

  float cm = -1.0f;
  USReadResult us = readUltrasonicCm(cm);

  if (us == US_OK) {
    lastUltrasonicCm = cm;
    ultrasonicValid = true;
  } else if (us == US_TIMEOUT) {
    ultrasonicValid = false;
  }

  if (!ultrasonicValid) {
    if (currentSecurityState != -1) {
      digitalWrite(RED_LED, LOW);
      digitalWrite(ORANGE_LED, LOW);
      digitalWrite(GREEN_LED, LOW);
      currentSecurityState = -1;
    }
    return;
  }

  // LEDs and state
  if (lastUltrasonicCm <= 25.0f) {
    if (currentSecurityState != 2) {
      Serial.print(F("[SECURITY] RED zone. Dist=")); Serial.print(lastUltrasonicCm, 1); Serial.println(F(" cm"));
      currentSecurityState = 2;
    }
    digitalWrite(RED_LED, HIGH);
    digitalWrite(ORANGE_LED, LOW);
    digitalWrite(GREEN_LED, LOW);
  } else if (lastUltrasonicCm <= 50.0f) {
    if (currentSecurityState != 1) {
      Serial.print(F("[SECURITY] ORANGE zone. Dist=")); Serial.print(lastUltrasonicCm, 1); Serial.println(F(" cm"));
      currentSecurityState = 1;
    }
    digitalWrite(RED_LED, LOW);
    digitalWrite(ORANGE_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);
  } else {
    if (currentSecurityState != 0) {
      Serial.print(F("[SECURITY] GREEN zone. Dist=")); Serial.print(lastUltrasonicCm, 1); Serial.println(F(" cm"));
      currentSecurityState = 0;
    }
    digitalWrite(RED_LED, LOW);
    digitalWrite(ORANGE_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
  }
}

// ========== SOUND ROUTING (SECURITY ONLY, NO PIR SOUND) ==========
void handleSoundSystem() {
  // Only SECURITY sound (distance-based, night-only)
  bool securitySound = (isNightTime && ultrasonicValid);

  if (securitySound) {
    float d = lastUltrasonicCm;

    if (d <= 25.0f) {
      beeperSet(2200, SEC_ON_MS_CLOSE, SEC_OFF_MS_CLOSE);
    } else if (d <= 50.0f) {
      beeperSet(1100, SEC_ON_MS_MED, SEC_OFF_MS_MED);
    } else {
      // far: low freq + long silence
      beeperSet(420, SEC_ON_MS_FAR, SEC_OFF_MS_FAR);
    }

    beeperUpdate();
    return;
  }

  // No security sound = stop all beeping
  beeperStop();
}

// ========== BEEPER CORE ==========
void beeperStop() {
  if (beeper.active) {
    noTone(PIEZO_PIN);
    beeper.active = false;
    beeper.on = false;
  }
}

void beeperSet(int freq, unsigned int onMs, unsigned int offMs) {
  // avoid resetting schedule unless pattern actually changes
  if (beeper.active && beeper.freq == freq && beeper.onMs == onMs && beeper.offMs == offMs) return;

  beeper.freq = freq;
  beeper.onMs = onMs;
  beeper.offMs = offMs;
  beeper.active = true;
  beeper.on = false;
  beeper.nextMs = 0; // force immediate start
}

void beeperUpdate() {
  if (!beeper.active) return;

  unsigned long now = millis();
  if (beeper.nextMs != 0 && now < beeper.nextMs) return;

  if (beeper.on) {
    noTone(PIEZO_PIN);
    beeper.on = false;
    beeper.nextMs = now + beeper.offMs;
  } else {
    tone(PIEZO_PIN, beeper.freq);
    beeper.on = true;
    beeper.nextMs = now + beeper.onMs;
  }
}

// ========== STREET LIGHT ACTUATORS ==========
void turnStreetLightsOn() {
  digitalWrite(LED1_PIN, HIGH);
  analogWrite(LED2_PIN, 255);
  digitalWrite(LED3_PIN, HIGH);
  analogWrite(LED4_PIN, 255);
  analogWrite(LED5_PIN, 255);
}

void turnStreetLightsOff(bool quiet) {
  digitalWrite(LED1_PIN, LOW);
  analogWrite(LED2_PIN, 0);
  digitalWrite(LED3_PIN, LOW);
  analogWrite(LED4_PIN, 0);
  analogWrite(LED5_PIN, 0);

  if (!quiet) Serial.println(F("[LIGHTS] OFF"));
}

void fadeStreetLightsOff() {
  for (int i = 255; i >= 0; i--) {
    analogWrite(LED2_PIN, i);
    analogWrite(LED4_PIN, i);
    analogWrite(LED5_PIN, i);
    delay(FADE_STEP_DELAY_MS);
  }
  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED3_PIN, LOW);
}

// ========== HC-SR04 READ ==========
USReadResult readUltrasonicCm(float &outCm) {
  static unsigned long lastPingMs = 0;

  if (millis() - lastPingMs < HC_MIN_PERIOD_MS) return US_TOO_SOON;
  lastPingMs = millis();

  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  unsigned long duration = pulseIn(ECHO_PIN, HIGH, HC_ECHO_TIMEOUT_US);
  if (duration == 0) return US_TIMEOUT;

  outCm = (float)duration / 58.0f;
  return US_OK;
}

// Ultrasonic distance sensor with enhanced accuracy
// Features: median filtering, temperature compensation, proper timing, timeout handling

#define TRIGGER_PIN  3
#define ECHO_PIN     2

// Configuration parameters
const uint8_t NUM_SAMPLES = 7;            // Odd number for true median calculation
const unsigned long PULSE_TIMEOUT = 30000UL; // 30ms timeout (~5m max range)
const uint16_t BETWEEN_PINGS_MS = 50;     // Delay between measurements
float ambientTempC = 20.0f;               // Ambient temperature for sound speed calculation

unsigned long durations[NUM_SAMPLES];

void setup() {
    Serial.begin(9600);
    pinMode(TRIGGER_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    digitalWrite(TRIGGER_PIN, LOW);
    delay(50);  // Delay for sensor stabilization
    Serial.println(F("Ultrasonic Sensor Distance Measurement"));
}

static inline void triggerPing() {
    // Generate 10µs trigger pulse per HC-SR04 datasheet
    digitalWrite(TRIGGER_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
}

static inline unsigned long readEcho() {
    // Read echo pulse duration with timeout
    return pulseIn(ECHO_PIN, HIGH, PULSE_TIMEOUT);
}

static inline float speedOfSoundCmPerUs(float tempC) {
    // Calculate temperature-compensated sound speed
    // Formula: c = 331.3 + 0.606*T (m/s) converted to cm/µs
    return ((331.3f + 0.606f * tempC) * 100.0f) / 1000000.0f;
}

static float medianDistanceCm(uint8_t count) {
    // Sort durations using insertion sort
    for (uint8_t i = 1; i < count; ++i) {
        unsigned long key = durations[i];
        int8_t j = i - 1;
        while (j >= 0 && durations[j] > key) {
            durations[j + 1] = durations[j];
            --j;
        }
        durations[j + 1] = key;
    }

    // Calculate distance from median duration
    unsigned long us = durations[count / 2];
    float c = speedOfSoundCmPerUs(ambientTempC);
    // Distance = (time * speed) / 2 for round trip
    return (us * c) * 0.5f;
}

float measureDistanceCm() {
    uint8_t kept = 0;

    // Collect valid samples
    for (uint8_t i = 0; i < NUM_SAMPLES; ++i) {
        triggerPing();
        unsigned long us = readEcho();
        if (us > 0 && us < PULSE_TIMEOUT) {
            durations[kept++] = us;
        }
        delay(BETWEEN_PINGS_MS);
    }

    if (kept == 0) {
        return NAN; // No valid measurements
    }

    // Calculate median from collected samples
    return medianDistanceCm(kept);
}

void loop() {
    float distanceCm = measureDistanceCm();

    if (isnan(distanceCm)) {
        Serial.println(F("Distance: out of range"));
    } else {
        Serial.print(F("Distance: "));
        Serial.print(distanceCm, 1); // Display with one decimal place
        Serial.println(F(" cm"));
    }

    delay(250); // Update rate: ~4 times per second
}

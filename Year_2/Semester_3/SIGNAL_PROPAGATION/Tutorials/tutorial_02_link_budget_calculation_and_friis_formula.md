# Εργαστηριακός Οδηγός 2: Υπολογισμός Προϋπολογισμού Ζεύξης (Link Budget) και Εξίσωση Friis σε Python

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η πλήρης ανάλυση και ο υπολογισμός ασύρματης ραδιοζεύξης (Point-to-Point Microwave Link / Wi-Fi outdoor link), ο υπολογισμός των απωλειών ελεύθερου χώρου (FSPL) και ο προσδιορισμός του περιθωρίου διαλείψεων (Fade Margin).

---

## 2. Εργαστηριακό Σενάριο
- **Συχνότητα Λειτουργίας ($f$):** $5.8\text{ GHz}$ (Μήκος κύματος $\lambda = c/f = \frac{3 \times 10^8}{5.8 \times 10^9} \approx 0.0517\text{ m} = 5.17\text{ cm}$)
- **Απόσταση Ζεύξης ($d$):** $15\text{ km}$
- **Ισχύς Πομπού ($P_{tx}$):** $500\text{ mW} = 0.5\text{ W} = +27\text{ dBm}$
- **Κέρδος Κεραίας Πομπού ($G_{tx}$):** $24\text{ dBi}$ (Παραβολικό κάτοπτρο)
- **Κέρδος Κεραίας Δέκτη ($G_{rx}$):** $24\text{ dBi}$
- **Απώλειες Καλωδίων & Συνδετήρων ($L_{c}$):** $2\text{ dB}$ στον πομπό και $2\text{ dB}$ στον δέκτη (Σύνολο $4\text{ dB}$)
- **Ευαισθησία Δέκτη ($P_{rx,min}$):** $-82\text{ dBm}$

---

## 3. Πλήρες Script Υπολογισμού σε Python

```python
import numpy as np

def calculate_link_budget(freq_ghz=5.8, dist_km=15.0, p_tx_dbm=27.0, 
                          g_tx_dbi=24.0, g_rx_dbi=24.0, 
                          loss_tx_db=2.0, loss_rx_db=2.0, 
                          rx_sensitivity_dbm=-82.0):
    
    # 1. Υπολογισμός FSPL
    freq_mhz = freq_ghz * 1000.0
    fspl_db = 32.44 + 20 * np.log10(dist_km) + 20 * np.log10(freq_mhz)

    # 2. Υπολογισμός EIRP (Equivalent Isotropically Radiated Power)
    eirp_dbm = p_tx_dbm - loss_tx_db + g_tx_dbi

    # 3. Υπολογισμός Λαμβανόμενης Ισχύος Prx
    p_rx_dbm = eirp_dbm - fspl_db + g_rx_dbi - loss_rx_db

    # 4. Υπολογισμός Fade Margin
    fade_margin_db = p_rx_dbm - rx_sensitivity_dbm

    # 5. Ακτίνα 1ης Ζώνης Fresnel στο μέσο της διαδρομής (d1 = d2 = d/2)
    c = 3e8
    wavelength = c / (freq_ghz * 1e9)
    d_meters = dist_km * 1000.0
    r1_fresnel = np.sqrt((wavelength * (d_meters / 2) * (d_meters / 2)) / d_meters)

    print("=== APOTELESMATA LINK BUDGET ===")
    print(f"Syxnotita: {freq_ghz} GHz | Apostasi: {dist_km} km")
    print(f"Apoleies Eleftherou Xorou (FSPL): {fspl_db:.2f} dB")
    print(f"EIRP Pompou: {eirp_dbm:.2f} dBm")
    print(f"Lamvanomeni Isxys (P_rx): {p_rx_dbm:.2f} dBm")
    print(f"Evaisthisia Dekti: {rx_sensitivity_dbm:.2f} dBm")
    print(f"Perithorio Dialeipseon (Fade Margin): {fade_margin_db:.2f} dB")
    print(f"Aktina 1is Zonis Fresnel (sto kentro): {r1_fresnel:.2f} m")
    
    if fade_margin_db >= 15.0:
        print("Katastasi Zefksis: EXCELLENT (Fade Margin >= 15 dB)")
    elif fade_margin_db >= 10.0:
        print("Katastasi Zefksis: ACCEPTABLE (Fade Margin >= 10 dB)")
    else:
        print("Katastasi Zefksis: POOR / UNRELIABLE (Fade Margin < 10 dB)")

if __name__ == "__main__":
    calculate_link_budget()
```

---

## 4. Εκτέλεση
```bash
python3 link_budget_calc.py
```


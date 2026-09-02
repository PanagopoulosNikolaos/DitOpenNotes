# Διάλεξη 4: Μηχανές Πεπερασμένων Καταστάσεων (FSM) και Εισαγωγή στη VHDL

## 1. Μηχανές Πεπερασμένων Καταστάσεων (FSM)

Μια σύγχρονη ακολουθιακή μηχανή περιγράφεται από το μοντέλο Mealy ή Moore:
- **Μηχανή Moore:** Οι έξοδοι εξαρτώνται **αποκλειστικά από την τρέχουσα κατάσταση** ($Y = g(S)$). Οι αλλαγές εξόδου είναι σύγχρονες με το ρολόι.
- **Μηχανή Mealy:** Οι έξοδοι εξαρτώνται **τόσο από την τρέχουσα κατάσταση όσο και από τις τρέχουσες εισόδους** ($Y = f(S, X)$). Οι έξοδοι μπορούν να ανταποκριθούν ασύγχρονα σε μεταβολές των εισόδων.

---

## 2. Βήματα Σχεδίασης FSM
1. Διάγραμμα Μεταβάσεων Καταστάσεων (State Diagram).
2. Πίνακας Καταστάσεων (State Table) και Ελαχιστοποίηση Καταστάσεων.
3. Κωδικοποίηση Καταστάσεων (Binary, Gray, One-Hot).
4. Πίνακας Διέγερσης των Flip-Flops (Excitation Table).
5. Εξαγωγή λογικών εξισώσεων εισόδων Flip-Flop και εξόδων μέσω χαρτών Karnaugh.
6. Σχηματική σχεδίαση του κυκλώματος.

---

## 3. Περιγραφή Υλικού με VHDL

Η γλώσσα VHDL (VHSIC Hardware Description Language) αποτελείται από δύο βασικά τμήματα:
1. **Entity (Οντότητα):** Ορίζει τη διασύνδεση και τις θύρες εισόδου/εξόδου (ports).
2. **Architecture (Αρχιτεκτονική):** Περιγράφει τη λειτουργική ή δομική συμπεριφορά του κυκλώματος.

### Παράδειγμα: D Flip-Flop με Σύγχρονο Reset σε VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity d_flipflop_sync is
    Port (
        clk   : in  STD_LOGIC;
        reset : in  STD_LOGIC;
        d     : in  STD_LOGIC;
        q     : out STD_LOGIC
    );
end d_flipflop_sync;

architecture Behavioral of d_flipflop_sync is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if reset = '1' then
                q <= '0';
            else
                q <= d;
            end if;
        end if;
    end process;
end Behavioral;
```


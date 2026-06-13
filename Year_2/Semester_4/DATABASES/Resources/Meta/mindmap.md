# Bases Dedomenon (Mindmap)

## Eisagogi & Basikes Ennoies

### Dedomena, Pliroforia kai Gnosi

- Epeksergasia akatergaston dedomenon (Data)
- Paragogi pliroforias (Information)
- Dimioyrgia gnosis gia lipsi apofaseon (Knowledge)

### Pliroforiaka Systimata (PS)

- Yliko (Hardware)
- Logismiko (Software)
- Dedomena (Data)
- Diadikasies (Processes)
- Anthropoi (People - Xristes, Diacheiristes)

### Systimata Diacheirisis Vaseon Dedomenon (SDVD / DBMS)

- Apothikefsi, anaktici kai apodotiki diacheirisi
- Prostasia dedomenon kai politikes asfaleias
- Tautochroni prosvasis apo pollaplous xristes (Concurrency)
- Elachistopoiisi pleonasmou kai asynepeias dedomenon

## Kyklos Zois & Schediasmos Vasis Dedomenon

### Vima 1: Syllogi & Analysi Apaitiseon

- Kathorismos anachon xriston kai organismou
- Apotyposi epicheirisiakon leitourgon kai prodiagrafon

### Vima 2: Ennoiologiki Schediasi

- Dimioyrgia Montelou Ontotiton-Sychetiseon (ER Model)
- Schimatiki optikopoiisi tis logikis domis

### Vima 3: Logiki Schediasi

- Metavasi sto Schesiako Montelo Dedomenon
- Metatropi ennoiologikou montelou se exartomenous pinakes

### Vima 4: Fysiki Schediasi & Ylopoiiisi

- Esoteriki organosi archeion sto systima
- Programmatismos me SQL kai dimioyrgia fysikon domon

## Montelo Ontotiton-Sychetiseon (E-R)

### Ontotites (Entities)

- **Ischyes Ontotites** (Anexartiti yparksi, kanonika orthogonia)
- **Astheneis Ontotites** (Exartomenes yparxiaka, dipla orthogonia)

### Gnorismata (Attributes)

- **Apla** (Mi diaireta) kai **Syntheta** (P.x. Onomateponymo)
- **Monotima** (Mia timi) kai **Pleiotima** (Polles times, diples elleipseis)
- **Paragomena** (Ypologizomena apo alla pedia, diakekomenes elleipseis)

### Sychetiseis (Relationships)

- **Vathmos sychetisis** (Monadiaia/Anadromiki, Dyadiki, Triadiki)
- **Anaparastasi me romvous** (aplous i diplous)

### Periorismoi Plithikotitas (Cardinality Constraints)

- **Ena-pros-Ena** (1:1)
- **Ena-pros-Polla** (1:N)
- **Polla-pros-Polla** (N:M)

## Schesiako Montelo & Schesiaki Algevra

### Vasika Stoicheia Schesiakou Montelou

- **Scheseis** (Antistoichoun stous Pinakes / Tables)
- **Pleiades** (Antistoichoun stis Engrafes / Grammes / Rows)
- **Gnorismata** (Antistoichoun stis Stiles / Columns)
- **Pedia Orismou** (Domains - Epitreptes times ana pedio)

### Periorismoi kai Kleidia

- **Ypochifia Kleidia** (Candidate Keys - Synola idiotiton monadikotitas)
- **Proteon Kleidi** (Primary Key - To epilegmeno ypochifio kleidi)
- **Xeno Kleidi** (Foreign Key - Gefyra syndesis pinakon)
- **Akeraiotita ontotiton** (Kanena PK null) kai **anaforiki akeraiotita**

### Prakseis Schesiakis Algebras

- **Theorias Synolon**: Enosi (Union), Tomi (Intersection), Diafora (Difference), Kartesianino Ginomeno (Cartesian Product)
- **Eidikes Schesiakes**: Epilogi (Selection), Provoli (Projection)
- **Synenoseis**: Esoteriki synenosi (Inner Join)

## Glossa SQL: Orismos Dedomenon (DDL - Data Definition Language)

### Diacheirisi Vaseon Dedomenon

- **CREATE DATABASE / SCHEMA** (Dimiourgia neas VD)
- **DROP DATABASE** (Oliki diagrafi VD)
- **USE** (Epilogi energis VD gia to trechon session)
- **SHOW DATABASES** (Provoli olon ton diathesimon VD)

### Diacheirisi Pinakon (Domi/Schima)

- **CREATE TABLE** (Dimiourgia pinaka, orismos pedion, typon kai Primary Key)
- **DROP TABLE** (Oristiki diagrafi pinaka)
- **DESCRIBE / EXPLAIN** (Provoli tou schimatos/metadata tou pinaka)

### Tropopoiisi Schimatos Pinaka (ALTER TABLE)

- **ADD** (Prosthesi neas stilis sto telos)
- **MODIFY** (Allagi tou typou dedomenon mias yparxousas stilis)
- **CHANGE** (Metonomasia stilis me taytochroni dilosi neou typou)
- **DROP COLUMN** (Afairesi stilis - prokalei apoleia dedomenon)

## Glossa SQL: Cheirismos & Erotimata (DML & DQL)

### Cheirismos Dedomenon (DML - Data Manipulation Language)

- **INSERT INTO** (Eisagogi neon engrafon/pleiadon se enan pinaka)
- **UPDATE ... SET ... WHERE** (Enimerosi/tropopoiisi yparxonton dedomenon)
- **DELETE FROM ... WHERE** (Diagrafi sygkekrimenon engrafon vasi synthikis)

### Erotimata & Anaktisi (DQL - Data Query Language)

- **Basiki domi**: SELECT (Ti anakta), FROM (Apo pou), WHERE (Me poious orous)
- **Provoli sygkekrimenon stilon i synolou afton (*)**
- **Filtarisma, telestes sygrisis (=, >, <) kai logikoi telestes (AND, OR, NOT)**

## Praktiki Efarmogi & Perivallonta Anaptyxis

### Ergaleia, Systimata & Architektoniki

- **MySQL Server** (To Backend systima diacheirisis)
- **MySQL Workbench** (Grafiko perivallon diacheirisis / GUI Client)
- **XAMPP & phpMyAdmin** (Paketo web diacheirisis kai ypiresion)

### Ylopoiiisi se Pragmatikes Synthikes

- Prosdiorismos katallilon typon dedomenon (INT, VARCHAR, DATE k.a.)
- Ylopoiiisi periorismon (NOT NULL, UNIQUE, DEFAULT)
- Syndesi pinakon meso Xenon Kleidion (Dilosi FOREIGN KEY ... REFERENCES)
- Diacheirisi scheseon "polla-pros-polla" (Analysi se 1:N meso endiamesou pinaka)
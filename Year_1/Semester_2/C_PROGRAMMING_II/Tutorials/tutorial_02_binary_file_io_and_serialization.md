# Tutorial 02: Binary File I/O and Structured Serialization

## Context and Grounding
This tutorial provides a complete walkthrough of serializing, persisting, and querying structured records in binary files using C standard streams. It reinforces the techniques practiced in `Exercises/File_Handling/src/exercise1.c` through `exercise15.c`.

---

## 1. Objectives and Technical Scope
1. Define fixed-width record structures.
2. Open streams in `"wb"` and `"rb"` modes.
3. Serialize arrays of structures using `fwrite()`.
4. Perform random-access queries using `fseek()` and `fread()`.
5. Update records in-place using `"r+b"` mode.

---

## 2. Implementation Walkthrough

### 2.1 Defining the Record Structure
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 32

typedef struct {
    int id;
    char name[MAX_NAME_LEN];
    float salary;
} EmployeeRecord;
```

### 2.2 Writing Records to Binary Storage
```c
int writeDatabase(const char *filepath, const EmployeeRecord *records, size_t count) {
    FILE *fp = fopen(filepath, "wb");
    if (fp == NULL) {
        perror("Failed to open file for writing");
        return -1;
    }
    
    size_t written = fwrite(records, sizeof(EmployeeRecord), count, fp);
    fclose(fp);
    
    return (written == count) ? 0 : -1;
}
```

### 2.3 Direct-Access Record Query
```c
int getRecordByIdx(const char *filepath, size_t index, EmployeeRecord *out_rec) {
    FILE *fp = fopen(filepath, "rb");
    if (fp == NULL) return -1;
    
    long offset = (long)(index * sizeof(EmployeeRecord));
    if (fseek(fp, offset, SEEK_SET) != 0) {
        fclose(fp);
        return -1;
    }
    
    size_t read_count = fread(out_rec, sizeof(EmployeeRecord), 1, fp);
    fclose(fp);
    
    return (read_count == 1) ? 0 : -1;
}
```

### 2.4 In-Place Update Routine
```c
int updateSalary(const char *filepath, size_t index, float new_salary) {
    FILE *fp = fopen(filepath, "r+b");
    if (fp == NULL) return -1;
    
    long offset = (long)(index * sizeof(EmployeeRecord));
    if (fseek(fp, offset, SEEK_SET) != 0) {
        fclose(fp);
        return -1;
    }
    
    EmployeeRecord rec;
    if (fread(&rec, sizeof(EmployeeRecord), 1, fp) != 1) {
        fclose(fp);
        return -1;
    }
    
    rec.salary = new_salary;
    
    /* Rewind stream position back to record boundary before writing */
    fseek(fp, offset, SEEK_SET);
    size_t written = fwrite(&rec, sizeof(EmployeeRecord), 1, fp);
    fclose(fp);
    
    return (written == 1) ? 0 : -1;
}
```

---

## 3. Testing and Verification
Compile and run the test driver:

```bash
gcc -Wall -Wextra -std=c11 serialization_driver.c -o serialization_driver
./serialization_driver
```

Expected Output:
```text
Database initialized with 3 records.
Record at index 1: ID=102, Name=Alice Bob, Salary=65000.00
Updated record at index 1: New Salary=72000.00
Verification read: ID=102, Name=Alice Bob, Salary=72000.00
```


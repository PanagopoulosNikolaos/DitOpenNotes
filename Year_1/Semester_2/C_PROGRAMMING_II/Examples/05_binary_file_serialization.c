/**
 * Demonstrates binary file I/O and random access record serialization in C.
 * Uses fwrite, fread, fseek, and ftell for structured data persistence.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "students_records.dat"
#define NAME_LENGTH 32

/**
 * Student record stored in binary file.
 */
typedef struct StudentRecord {
    int id;
    char name[NAME_LENGTH];
    double grade;
} StudentRecord;

/**
 * Writes an array of student records to a binary file.
 * Args:
 * filename (const char*): Path to target binary file.
 * records (const StudentRecord*): Array of records.
 * count (size_t): Number of records.
 * Returns:
 * bool: true upon success, false otherwise.
 */
int writeRecords(const char *filename, const StudentRecord *records, size_t count) {
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("Failed to open binary file for writing");
        return 0;
    }
    size_t written = fwrite(records, sizeof(StudentRecord), count, fp);
    fclose(fp);
    return written == count;
}

/**
 * Reads a record at a specific 0-based index using fseek.
 * Args:
 * filename (const char*): Path to target binary file.
 * index (long): Record index to fetch.
 * out_record (StudentRecord*): Destination buffer.
 * Returns:
 * int: 1 on success, 0 on failure.
 */
int readRecordByIndex(const char *filename, long index, StudentRecord *out_record) {
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("Failed to open binary file for reading");
        return 0;
    }
    long offset = index * (long)sizeof(StudentRecord);
    if (fseek(fp, offset, SEEK_SET) != 0) {
        fclose(fp);
        return 0;
    }
    size_t read_count = fread(out_record, sizeof(StudentRecord), 1, fp);
    fclose(fp);
    return read_count == 1;
}

int main(void) {
    StudentRecord cohort[] = {
        {101, "Alexandros", 8.75},
        {102, "Eleni", 9.20},
        {103, "Dimitrios", 7.50},
        {104, "Maria", 9.80}
    };
    size_t count = sizeof(cohort) / sizeof(cohort[0]);

    if (!writeRecords(FILENAME, cohort, count)) {
        return EXIT_FAILURE;
    }
    printf("Successfully wrote %zu records to %s\n", count, FILENAME);

    StudentRecord fetched;
    long target_idx = 2; // Dimitrios
    if (readRecordByIndex(FILENAME, target_idx, &fetched)) {
        printf("Random access read at index %ld:\n", target_idx);
        printf("  ID:    %d\n", fetched.id);
        printf("  Name:  %s\n", fetched.name);
        printf("  Grade: %.2f\n", fetched.grade);
    }

    // Clean up temporary binary test file
    remove(FILENAME);

    return EXIT_SUCCESS;
}

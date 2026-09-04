/**
 * Demonstrates structured binary file I/O and random-access record updates.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 32

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    double gpa;
} StudentRecord;

/**
 * Appends a student record to a binary file stream.
 * Args:
 *   file_path (const char*): Path to binary destination file.
 *   record_ptr (const StudentRecord*): Pointer to record to persist.
 * Returns:
 *   int: 1 on success, 0 on failure.
 */
int appendRecord(const char *file_path, const StudentRecord *record_ptr) {
    FILE *stream_ptr = fopen(file_path, "ab");
    if (stream_ptr == NULL) {
        return 0; /* Failed to open file */
    }

    size_t items_written = fwrite(record_ptr, sizeof(StudentRecord), 1, stream_ptr);
    fclose(stream_ptr); /* Flushes write buffers and releases OS file handle */

    return (items_written == 1) ? 1 : 0;
}

/**
 * Reads a single record from a binary file at a specified zero-based index.
 * Args:
 *   file_path (const char*): Path to binary database file.
 *   record_index (long): Zero-based record index to fetch.
 *   dest_record (StudentRecord*): Target memory location for record data.
 * Returns:
 *   int: 1 on success, 0 on seek or read failure.
 */
int readRecordByIndex(const char *file_path, long record_index, StudentRecord *dest_record) {
    FILE *stream_ptr = fopen(file_path, "rb");
    if (stream_ptr == NULL) {
        return 0;
    }

    long byte_offset = record_index * (long)sizeof(StudentRecord);
    if (fseek(stream_ptr, byte_offset, SEEK_SET) != 0) {
        fclose(stream_ptr);
        return 0; /* Invalid seek position */
    }

    size_t items_read = fread(dest_record, sizeof(StudentRecord), 1, stream_ptr);
    fclose(stream_ptr);

    return (items_read == 1) ? 1 : 0;
}

int main(void) {
    const char *db_filename = "students_demo.bin";

    StudentRecord s1 = {101, "Alice Smith", 3.85};
    StudentRecord s2 = {102, "Bob Jones", 3.42};

    /* Initialize database with records */
    remove(db_filename); /* Removes previous artifact if present */
    appendRecord(db_filename, &s1);
    appendRecord(db_filename, &s2);

    /* Direct query of second record */
    StudentRecord queried_rec;
    if (readRecordByIndex(db_filename, 1, &queried_rec)) {
        printf("Read Record Index 1:\n");
        printf("ID: %d\nName: %s\nGPA: %.2f\n", queried_rec.id, queried_rec.name, queried_rec.gpa);
    } else {
        fprintf(stderr, "Failed to read record at index 1\n");
    }

    remove(db_filename); /* Cleans up temporary demo binary */
    return EXIT_SUCCESS;
}


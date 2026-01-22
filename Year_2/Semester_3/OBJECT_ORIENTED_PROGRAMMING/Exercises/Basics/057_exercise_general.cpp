/*
 * Exercise 12: University Management System
 * 
 * Create a base class Person with:
 * - Protected members: name (string), id (string)
 * - Constructor initializing both
 * - Pure virtual method displayRole()
 * - Virtual destructor
 * 
 * Create two derived classes:
 * - Professor: additional members department (string), salary (double); 
 *   implement displayRole() and method giveGrade(string studentName, double grade)
 * - Student: additional members gpa (double), enrolledCourses (vector of strings); 
 *   implement displayRole() and method enrollCourse(string courseName)
 * 
 * Create a University class with:
 * - Private member: members (vector of Person pointers)
 * - Method addMember(Person*) to add professors or students
 * - Method displayAllMembers() displaying polymorphically
 * - Method findMemberById(string id) returning Person pointer or nullptr
 * - Destructor freeing all memory
 * 
 * In main(), create a university with 3 professors and 5 students from user input, 
 * display all members, have professors give grades and students enroll in courses (stored and retrieved), 
 * display updated information, and ensure proper cleanup.
 */

#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main() {
    // Your code here
    
    return 0;
}

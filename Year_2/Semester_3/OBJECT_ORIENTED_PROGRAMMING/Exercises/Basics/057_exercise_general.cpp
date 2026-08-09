/*
 * Άσκηση 12: Σύστημα Διαχείρισης Πανεπιστημίου
 *
 * Δημιουργήστε μια βασική κλάση Person με:
 * - Προστατευόμενα μέλη: name (string), id (string)
 * - Κατασκευαστή που αρχικοποιεί και τα δύο
 * - Καθαρά εικονική μέθοδο displayRole()
 * - Εικονικό καταστροφέα
 *
 * Δημιουργήστε δύο παράγωγες κλάσεις:
 * - Professor: επιπλέον μέλη department (string), salary (double);
 *   υλοποιήστε displayRole() και μέθοδο giveGrade(string studentName, double grade)
 * - Student: επιπλέον μέλη gpa (double), enrolledCourses (διάνυσμα strings);
 *   υλοποιήστε displayRole() και μέθοδο enrollCourse(string courseName)
 *
 * Δημιουργήστε μια κλάση University με:
 * - Ιδιωτικό μέλος: members (διάνυσμα δεικτών Person)
 * - Μέθοδο addMember(Person*) για προσθήκη καθηγητών ή μαθητών
 * - Μέθοδο displayAllMembers() που εμφανίζει πολυμορφικά
 * - Μέθοδο findMemberById(string id) που επιστρέφει δείκτη Person ή nullptr
 * - Καταστροφέα που απελευθερώνει όλη τη μνήμη
 *
 * Στο main(), δημιουργήστε ένα πανεπιστήμιο με 3 καθηγητές και 5 μαθητές από είσοδο χρήστη,
 * εμφανίστε όλα τα μέλη, αφήστε τους καθηγητές να δώσουν βαθμούς και τους μαθητές να εγγραφούν σε μαθήματα (αποθηκεύονται και ανακτώνται),
 * εμφανίστε ενημερωμένες πληροφορίες, και βεβαιωθείτε ότι η καθαριότητα γίνεται σωστά.
 */

#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main() {
    // Ο κώδικάς σας εδώ

    return 0;
}

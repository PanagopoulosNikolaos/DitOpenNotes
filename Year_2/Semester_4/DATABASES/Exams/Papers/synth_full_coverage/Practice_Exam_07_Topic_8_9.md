# Exam 7: Relational Algebra, JOINs & Security Policies

Multiple Choice Question 1. Which of the following statements is correct about the Natural Join;
[ ] 1. It retains duplicate columns for the common attributes.
[✓] 2. It automatically merges columns with the same name and returns the common column once.
[ ] 3. It returns all possible combinations of tuples, like the Cartesian Product.
[ ] 4. It fills unmatched rows with NULL.
---
*solution:*
The Natural Join automatically performs an equality check on the common fields and merges the common column, preventing its duplicate appearance.
---

Multiple Choice Question 2. Which password cracking technique uses pre-computed lookup tables (pre-computed hashes) to find the original value of a hash;
[ ] 1. Dictionary Attack
[ ] 2. Brute Force Attack
[✓] 3. Rainbow Table Attack
[ ] 4. Phishing
---
*solution:*
Rainbow Tables allow almost instantaneous hash lookup by using ready-made, pre-computed tables to match against passwords.
---

Multiple Choice Question 3. A Social Engineering threat is based mainly on:
[ ] 1. Hardware bugs.
[ ] 2. Cryptography algorithms with flaws.
[✓] 3. Manipulation and deception of the system's users.
[ ] 4. Testing all combinations of characters.
---
*solution:*
Social Engineering exploits human weaknesses, trust or ignorance in order to extract sensitive data (e.g., through Phishing or Tailgating).
---

Exercise 4. Given the tables Customer(Code, Name) with 5 records and Order(Order_Code, Customer_Code) with 10 records. How many records will the Cartesian Product (CROSS JOIN) of the two tables return;
---
*solution:*
The Cartesian Product combines each record of the first table with each record of the second table.
Therefore: 5 records * 10 records = 50 records.
---

Exercise 5. According to information security policies, what are the basic characteristics of a "Strong Password" regarding length and frequency of change;
---
*solution:*
Based on the golden rules of the security policy:
- Minimum password length: At least 15 characters.
- Change frequency: Mandatory change at least every 6 months.
(Additionally: it must contain a combination of uppercase letters, lowercase letters, numbers and symbols, and must not be a dictionary word).
---

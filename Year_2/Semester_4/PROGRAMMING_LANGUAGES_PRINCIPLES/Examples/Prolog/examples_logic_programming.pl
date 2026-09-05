/* =============================================================================
   Module     : examples_logic_programming.pl
   Description: Declarative Logic Programming Demonstrations in SWI-Prolog
   Department : Informatics and Telecommunications, University of Ioannina
   =============================================================================

   Illustrates foundational declarative logic programming concepts:
   - Facts, rules, and knowledge base querying
   - First-order unification and resolution
   - Structural recursion on lists (member, append, reverse, length)
   - Backtracking and the Cut (!) operator for search pruning
   ============================================================================= */

% =============================================================================
% 1. Knowledge Base: Academic Course Pre-requisites and Enrollments
% =============================================================================

% course(Code, Title, ECTS).
course(101, 'C Programming I', 6).
course(104, 'Logic Design', 6).
course(201, 'C Programming II', 6).
course(204, 'Networking', 6).
course(301, 'Computer Architecture', 6).
course(302, 'Object Oriented Programming', 6).
course(305, 'Data Structures and Algorithms', 6).
course(401, 'Principles of Programming Languages', 6).
course(402, 'Operating Systems', 6).
course(403, 'Computer Networks', 6).

% prerequisite(PrereqCode, CourseCode).
prerequisite(101, 201).
prerequisite(104, 301).
prerequisite(201, 301).
prerequisite(201, 302).
prerequisite(201, 305).
prerequisite(201, 401).
prerequisite(302, 401).
prerequisite(305, 401).
prerequisite(301, 402).
prerequisite(305, 402).
prerequisite(204, 403).

% =============================================================================
% 2. Transitive Rules: Dependent Course Hierarchy
% =============================================================================

% Checks direct or indirect prerequisite dependency via transitive closure.
hasPrerequisite(Course, Prereq) :-
    prerequisite(Prereq, Course).

hasPrerequisite(Course, Prereq) :-
    prerequisite(Intermediate, Course),
    hasPrerequisite(Intermediate, Prereq).

% =============================================================================
% 3. Recursive List Processing
% =============================================================================

% Computes the length of a list.
listLength([], 0).
listLength([_|Tail], Length) :-
    listLength(Tail, TailLen),
    Length is TailLen + 1.

% Sums elements of a numeric list.
sumList([], 0).
sumList([Head|Tail], Sum) :-
    sumList(Tail, RestSum),
    Sum is Head + RestSum.

% Custom member check using unification.
elementMember(X, [X|_]).
elementMember(X, [_|Tail]) :-
    elementMember(X, Tail).

% Reverses a list using an accumulator to achieve linear time complexity O(N).
reverseList(List, Reversed) :-
    reverseAcc(List, [], Reversed).

reverseAcc([], Acc, Acc).
reverseAcc([Head|Tail], Acc, Reversed) :-
    reverseAcc(Tail, [Head|Acc], Reversed).

% =============================================================================
% 4. Search Pruning via the Cut (!) Operator
% =============================================================================

% Deterministic maximum of two numbers using green cut.
maxNumber(X, Y, X) :- X >= Y, !.
maxNumber(_, Y, Y).

% Finds the first prerequisite of a course and halts search immediately.
firstPrerequisite(Course, FirstPrereq) :-
    prerequisite(FirstPrereq, Course),
    !.


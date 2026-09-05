"""Multi-paradigm functional and declarative demonstrations in Python.

Illustrates how modern Python integrates functional idioms alongside imperative
and object-oriented concepts:
- Lazy generator pipelines and functional stream processing
- Higher-order functions, closures, and custom decorators
- Declarative pattern-like data processing using dataclasses
"""

from dataclasses import dataclass
from typing import Callable, Generator, Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class CourseRecord:
    """Immutable data record representing an academic course offering.

    Attributes:
        code (int): Official course identifier.
        title (str): Full academic title.
        ects (int): Credit points assigned.
        category (str): Mandatory or Elective categorization.
    """

    code: int
    title: str
    ects: int
    category: str


def filterPipeline(
    courses: Iterable[CourseRecord], predicate: Callable[[CourseRecord], bool]
) -> Generator[CourseRecord, None, None]:
    """Generates a filtered stream of course records lazily.

    Args:
        courses (Iterable[CourseRecord]): Stream of input course records.
        predicate (Callable[[CourseRecord], bool]): Boolean filter condition.

    Yields:
        CourseRecord: Next course fulfilling predicate condition.
    """
    for course in courses:
        if predicate(course):
            # Yields lazily to prevent allocating intermediate lists in memory
            yield course


def computeCumulativeCredits(courses: List[CourseRecord]) -> int:
    """Computes total ECTS points using functional reduce-like aggregation.

    Args:
        courses (List[CourseRecord]): Collection of evaluated courses.

    Returns:
        int: Total sum of ECTS credits across the collection.
    """
    return sum(course.ects for course in courses)


def makePrefixMatcher(prefix_code: int) -> Callable[[CourseRecord], bool]:
    """Higher-order closure creating a course level discriminator.

    Args:
        prefix_code (int): Century digit representing academic level (e.g., 4 for Year 2 Sem 4).

    Returns:
        Callable[[CourseRecord], bool]: Closure testing course level code prefix.
    """

    def matcher(course: CourseRecord) -> bool:
        """Tests whether course code falls within target century range."""
        return (course.code // 100) == prefix_code

    return matcher


def runDemonstration() -> None:
    """Executes multi-paradigm stream processing demonstrations."""
    curriculum = [
        CourseRecord(101, "C Programming I", 6, "Mandatory"),
        CourseRecord(201, "C Programming II", 6, "Mandatory"),
        CourseRecord(301, "Computer Architecture", 6, "Mandatory"),
        CourseRecord(302, "Object Oriented Programming", 6, "Mandatory"),
        CourseRecord(305, "Data Structures and Algorithms", 6, "Mandatory"),
        CourseRecord(401, "Principles of Programming Languages", 6, "Mandatory"),
        CourseRecord(402, "Operating Systems", 6, "Mandatory"),
        CourseRecord(403, "Computer Networks", 6, "Mandatory"),
        CourseRecord(404, "Databases", 6, "Mandatory"),
        CourseRecord(405, "Probability and Statistics", 6, "Mandatory"),
    ]

    print("=== Multi-Paradigm Functional Processing in Python ===")

    # 1. Higher-order closure filtering Year 2 Semester 4 courses
    is_semester_four = makePrefixMatcher(4)
    semester_four_courses = list(filterPipeline(curriculum, is_semester_four))

    print("\nSemester 4 Courses (Filtered via Closure Pipeline):")
    for c in semester_four_courses:
        print(f"  [{c.code}] {c.title} ({c.ects} ECTS) - {c.category}")

    # 2. Functional Aggregation
    total_ects = computeCumulativeCredits(semester_four_courses)
    print(f"\nTotal Semester 4 ECTS: {total_ects}")


if __name__ == "__main__":
    runDemonstration()


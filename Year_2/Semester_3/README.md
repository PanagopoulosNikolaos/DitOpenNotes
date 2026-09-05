# Year 2 - Semester 3

Welcome to the comprehensive academic course archive for **Year 2, Semester 3** of the Department of Informatics and Telecommunications at the University of Ioannina.

---

## Curriculum Overview

Semester 3 advances students into core computer systems architecture, foundational data structures and algorithm analysis, modern object-oriented software engineering, continuous and discrete signals and systems, and electromagnetic wave propagation and antenna systems.

| Code | Course Name | ECTS | Category | Primary Focus |
|:---|:---|:---:|:---|:---|
| **301** | [Computer Architecture](COMPUTER_ARCHITECTURE) | 6 | Mandatory | Instruction set architecture, MIPS datapath, 5-stage pipelining, hazards, memory hierarchy, cache mapping, superscalar execution |
| **302** | [Object Oriented Programming](OBJECT_ORIENTED_PROGRAMMING) | 6 | Mandatory | C++17 class design, encapsulation, virtual polymorphism, vtables, RAII, Rule of Five, templates, STL, design patterns |
| **303** | [Signals and Systems](SIGNALS_AND_SYSTEMS) | 6 | Mandatory | Continuous/discrete signals and systems, linearity, time-invariance, convolution, Fourier series/transforms, Laplace transform |
| **304** | [Signal Propagation](SIGNAL_PROPAGATION) | 6 | Mandatory | Maxwell's equations in media, plane wave propagation, Poynting vector, antenna theory, dipoles, arrays, beamforming, link budget |
| **305** | [Data Structures and Algorithms](DSA_DATA_STRUCTURES_ALGORITHMS) | 6 | Mandatory | Asymptotic complexity, recurrences, dynamic arrays, balanced BSTs, AVL rotations, heaps, hashing, graph traversals, shortest paths |

---

## Standard Course Directory Structure

Each course directory adheres strictly to the department's standardized academic curriculum organization:

```text
Course_Directory/
├── README.md               # Course syllabus, prerequisites, outcomes, and directory index
├── Lectures/               # Structured theory lecture modules and curriculum guides
├── Exercises/              # Comprehensive problem sets and step-by-step solved drills
├── Examples/               # Executable code, simulation models, and interactive demonstrations
├── Assignments/            # Practical laboratory project assignments and rubrics
├── Tutorials/              # Hands-on tooling guides (MARS/SPIM, GDB, Valgrind, SciPy)
├── Projects/               # Comprehensive capstone term design projects
├── Exams/                  # Past examination papers, model practice exams, and rubrics
│   ├── Papers/             # Scanned test papers and exam figures
│   └── Solutions/          # Complete worked exam solutions
└── Resources/              # Study notes, textbooks, curriculum mindmaps, and references
    ├── Books/              # Reference textbooks and official literature
    ├── Meta/               # Curriculum topic mindmaps
    ├── Notes/              # Granular chapter and topic study notes
    └── resources.md        # Curated bibliography, official standards, and external links
```

---

## Getting Started

1. **Tooling Environment**:
   * **Computer Architecture**: MIPS assembly simulators (`mars` or `spim`), GNU C/C++ compiler (`gcc`/`g++`), and Arduino CLI for embedded AVR interfacing.
   * **Object-Oriented Programming**: Modern C++ compiler supporting C++17 (`g++` or `clang++`), GNU Debugger (`gdb`), GNU Make, and Valgrind (`valgrind`) for memory leak detection.
   * **Data Structures and Algorithms**: C++17 compiler (`g++`), Python 3 for algorithmic benchmarking, and standard diagnostic tooling.
   * **Signals and Systems**: Python 3 with NumPy, SciPy, and Matplotlib; modern web browser for interactive HTML signal visualizers.
   * **Signal Propagation**: Python 3 with NumPy and Matplotlib for RF link budget calculations and antenna radiation pattern synthesis.
2. **Recommended Study Order**: Begin each topic by reviewing the theoretical principles in `Lectures/` and `Resources/Notes/`, followed by hands-on execution of `Examples/` and drilling through `Exercises/`.
3. **Assessment Preparation**: Implement the programming assignments in `Assignments/` and self-evaluate understanding using mock examinations in `Exams/`.

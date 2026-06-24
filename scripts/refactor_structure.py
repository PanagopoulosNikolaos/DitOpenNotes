import os
import shutil
from pathlib import Path

ROOT_DIR = Path('/home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes')
STANDARD_FOLDERS = ['Lectures', 'Exercises', 'Examples', 'Quizzes', 'Exams', 'Resources']

def main():
    print("Starting refactoring...")

    # 1. Rename DISCREET_MATHEMATICS
    discreet_path = ROOT_DIR / 'Year_2' / 'Semester_2' / 'DISCREET_MATHEMATICS'
    discrete_path = ROOT_DIR / 'Year_2' / 'Semester_2' / 'DISCRETE_MATHEMATICS'
    if discreet_path.exists() and not discrete_path.exists():
        discreet_path.rename(discrete_path)
        print("Renamed DISCREET_MATHEMATICS to DISCRETE_MATHEMATICS")

    # 2. Iterate through all courses
    for year_dir in ROOT_DIR.glob('Year_*'):
        if not year_dir.is_dir(): continue
        for sem_dir in year_dir.glob('Semester_*'):
            if not sem_dir.is_dir(): continue
            for course_dir in sem_dir.iterdir():
                if not course_dir.is_dir() or course_dir.name == 'README.md': continue
                
                print(f"Processing course: {course_dir.name}")
                
                # a) Rename Assignments to Exercises
                assignments_dir = course_dir / 'Assignments'
                exercises_dir = course_dir / 'Exercises'
                if assignments_dir.exists() and not exercises_dir.exists():
                    assignments_dir.rename(exercises_dir)
                    print(f"  Renamed Assignments to Exercises in {course_dir.name}")
                elif assignments_dir.exists() and exercises_dir.exists():
                    print(f"  WARNING: Both Assignments and Exercises exist in {course_dir.name}!")
                
                # b) Create missing standard folders
                for folder in STANDARD_FOLDERS:
                    target_dir = course_dir / folder
                    target_dir.mkdir(parents=True, exist_ok=True)
                
                # c) Ensure Quizzes is moved out of Resources if it exists there
                res_quizzes = course_dir / 'Resources' / 'Quizzes'
                root_quizzes = course_dir / 'Quizzes'
                if res_quizzes.exists():
                    for item in res_quizzes.iterdir():
                        shutil.move(str(item), str(root_quizzes / item.name))
                    res_quizzes.rmdir()
                    print(f"  Moved Quizzes out of Resources in {course_dir.name}")

    # 3. Fix specific file typos
    prob_stat_dir = ROOT_DIR / 'Year_2' / 'Semester_4' / 'PROBABILITY_STATISTICS'
    if prob_stat_dir.exists():
        bad_diff = prob_stat_dir / 'Exams' / 'Papers' / 'difficluty.md'
        good_diff = prob_stat_dir / 'Exams' / 'Papers' / 'difficulty.md'
        if bad_diff.exists() and not good_diff.exists():
            bad_diff.rename(good_diff)
            print("Fixed typo: difficluty.md -> difficulty.md")
            
        bad_map = prob_stat_dir / 'Resources' / 'Meta' / 'minedmap.md'
        good_map = prob_stat_dir / 'Resources' / 'Meta' / 'mindmap.md'
        if bad_map.exists() and not good_map.exists():
            bad_map.rename(good_map)
            print("Fixed typo: minedmap.md -> mindmap.md")

    discrete_math_dir = ROOT_DIR / 'Year_2' / 'Semester_2' / 'DISCRETE_MATHEMATICS'
    if discrete_math_dir.exists():
        bad_jpg = discrete_math_dir / 'Exams' / 'Papers' / 'images' / ' Finals.jpg'
        good_jpg = discrete_math_dir / 'Exams' / 'Papers' / 'images' / 'Finals.jpg'
        if bad_jpg.exists() and not good_jpg.exists():
            bad_jpg.rename(good_jpg)
            print("Fixed typo: ' Finals.jpg' -> 'Finals.jpg'")

    # 4. Fix nested Resources in SIGNALS_AND_SYSTEMS
    ss_dir = ROOT_DIR / 'Year_2' / 'Semester_3' / 'SIGNALS_AND_SYSTEMS'
    if ss_dir.exists():
        nested_res = ss_dir / 'Resources' / 'Resources'
        if nested_res.exists():
            for item in nested_res.iterdir():
                dest = ss_dir / 'Resources' / item.name
                if not dest.exists():
                    shutil.move(str(item), str(dest))
            nested_res.rmdir()
            print("Fixed nested Resources in SIGNALS_AND_SYSTEMS")

    # 5. Move COMPUTER_ARCHITECTURE/Arduino
    ca_dir = ROOT_DIR / 'Year_2' / 'Semester_3' / 'COMPUTER_ARCHITECTURE'
    if ca_dir.exists():
        arduino_dir = ca_dir / 'Arduino'
        dest_arduino = ca_dir / 'Examples' / 'Arduino'
        if arduino_dir.exists() and not dest_arduino.exists():
            dest_arduino.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(arduino_dir), str(dest_arduino))
            print("Moved Arduino folder in COMPUTER_ARCHITECTURE")

    # 6. Delete notes.old
    db_dir = ROOT_DIR / 'Year_2' / 'Semester_4' / 'DATABASES'
    if db_dir.exists():
        notes_old = db_dir / 'Resources' / 'notes.old'
        if notes_old.exists():
            shutil.rmtree(str(notes_old))
            print("Deleted notes.old from DATABASES")

    # 7. Delete __pycache__ in DIGITAL_ELECTRONICS
    de_dir = ROOT_DIR / 'Year_1' / 'Semester_2' / 'DIGITAL_ELECTRONICS'
    if de_dir.exists():
        pycache_dir = de_dir / 'Examples' / 'VHDL_CODE_EXEC' / '__pycache__'
        if pycache_dir.exists():
            shutil.rmtree(str(pycache_dir))
            print("Deleted __pycache__ from DIGITAL_ELECTRONICS")

    # 8. Move Textbooks from Lectures to Resources/Books
    books_to_move = [
        (ROOT_DIR / 'Year_1' / 'Semester_1' / 'LINEAR_ALGEBRA' / 'Lectures' / 'Linear_Algebra_and_its_application.pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'DSA_DATA_STRUCTURES_ALGORITHMS' / 'Lectures' / 'Data Structures, Algorithms And Applications In C++ - PDF Room.pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'OBJECT_ORIENTED_PROGRAMMING' / 'Lectures' / 'C++ Crash Course A Fast-Paced Introduction by Josh Lospinoso.pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'OBJECT_ORIENTED_PROGRAMMING' / 'Lectures' / 'Hands-On Machine Learning with C++ by Kirill Kolodiazhnyi (z-lib.org).pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'SIGNAL_PROPAGATION' / 'Lectures' / 'Antenna Theory Analysis and Design 3rd ed.pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'SIGNALS_AND_SYSTEMS' / 'Lectures' / '_OceanofPDF.com_Signals_and_Systems_-_Fatos_Tunay_Yarman_Vural.pdf'),
        (ROOT_DIR / 'Year_2' / 'Semester_3' / 'SIGNALS_AND_SYSTEMS' / 'Lectures' / 'Think DSP.pdf')
    ]
    
    for book_path in books_to_move:
        if book_path.exists():
            course_dir = book_path.parent.parent
            books_dir = course_dir / 'Resources' / 'Books'
            books_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(book_path), str(books_dir / book_path.name))
            print(f"Moved book {book_path.name} to Resources/Books")

    print("Refactoring complete.")

if __name__ == '__main__':
    main()

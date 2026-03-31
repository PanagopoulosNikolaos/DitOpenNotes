#!/usr/bin/env python3
"""
Repository Restructuring Script for DitOpenNotes
==================================================

This script performs a comprehensive restructuring of the repository to:
1. Standardize folder naming (fix "MATHEMATICAL ANALYSIS" → "MATHEMATICAL_ANALYSIS")
2. Create unified folder structure for all courses
3. Move existing content to appropriate new locations
4. Handle exam papers and images specially
5. Remove Quizzes and outdated legacy folders
6. Dynamically zip all Quartus projects to save space

IMPORTANT: Run this script from a NEW BRANCH (e.g., refactor/full-restructure)
to ensure safety and easy rollback if needed.
"""

import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
LOG_FILE = SCRIPTS_DIR / f"restructure_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# New standardized folder structure
NEW_COURSE_FOLDERS = [
    "Lectures",
    "Tutorials",      # Renamed from Examples
    "Assignments",    # Renamed from Exercises
    "Examples",       # Keep for code examples if they exist
    "Exams",
    "Resources",
    "Projects"
]

# Mapping of old folder names to new folder names
FOLDER_RENAME_MAP = {
    "Exercises": "Assignments",
    "Examples": "Tutorials",
    "Quizzes": None,  # Will be removed
}

# Specific paths to remove (Outdated / Legacy)
PATHS_TO_REMOVE = [
    REPO_ROOT / "Year_1" / "Semester_2" / "C_PROGRAMMING_II" / "Examples" / "ScientificCalculator"
]

# Course directories that need renaming
COURSES_TO_RENAME = {
    "MATHEMATICAL ANALYSIS": "MATHEMATICAL_ANALYSIS"
}

# Patterns that indicate exam papers (for moving to Exams/Papers)
EXAM_PATTERNS = [
    "Exam_paper",
    "ΛΣ_ΘΕΜΑΤΑ",
    "Λύσεις Προόδου",
    "Εξέταση Προόδου",
    "Εξέταση_Προόδου",
    "Εξέταση",
    "Θέματα",
    "Λύσεις",
]

# Patterns that indicate images folder (to be moved to Exams/Papers/images)
IMAGES_FOLDERS = ["images"]


def logMessage(message: str, dry_run: bool = False):
    """Logs message to console and file."""
    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"{prefix}{message}")
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{prefix}{message}\n")


def isExamPaper(filename: str) -> bool:
    """Checks if a filename matches exam paper patterns."""
    return any(pattern.lower() in filename.lower() for pattern in EXAM_PATTERNS)


def isImageFolder(folder_name: str) -> bool:
    """Checks if folder is an images folder."""
    return folder_name.lower() in [name.lower() for name in IMAGES_FOLDERS]


def getAllCourseDirectories() -> list:
    """Gets all course directories in the repository."""
    courses = []
    year_dirs = [d for d in REPO_ROOT.iterdir() if d.is_dir() and d.name.startswith("Year_")]
    
    for year_dir in sorted(year_dirs):
        semester_dirs = [d for d in year_dir.iterdir() if d.is_dir() and d.name.startswith("Semester_")]
        for semester_dir in sorted(semester_dirs):
            course_dirs = [d for d in semester_dir.iterdir() 
                          if d.is_dir() and d.name not in ["README.md"]]
            for course_dir in sorted(course_dirs):
                courses.append(course_dir)
    
    return courses


def renameCourseFolders(dry_run: bool = False):
    """Renames course folders to standardized names."""
    logMessage("\n=== Step 1: Renaming Course Folders ===", dry_run)
    
    courses = getAllCourseDirectories()
    
    for course_path in courses:
        old_name = course_path.name
        if old_name in COURSES_TO_RENAME:
            new_name = COURSES_TO_RENAME[old_name]
            new_path = course_path.parent / new_name
            
            if dry_run:
                logMessage(f"Would rename: {course_path} → {new_path}", dry_run)
            else:
                if new_path.exists():
                    logMessage(f"WARNING: Target already exists: {new_path}", dry_run)
                else:
                    shutil.move(str(course_path), str(new_path))
                    logMessage(f"Renamed: {old_name} → {new_name}", dry_run)


def createNewFolderStructure(dry_run: bool = False):
    """Creates new standardized folder structure in all courses."""
    logMessage("\n=== Step 2: Creating New Folder Structure ===", dry_run)
    
    courses = getAllCourseDirectories()
    
    for course_path in courses:
        logMessage(f"\nProcessing: {course_path.name}", dry_run)
        
        # Create new folders
        for folder_name in NEW_COURSE_FOLDERS:
            new_folder = course_path / folder_name
            if not new_folder.exists():
                if dry_run:
                    logMessage(f"  Would create: {new_folder}", dry_run)
                else:
                    new_folder.mkdir(parents=True, exist_ok=True)
                    logMessage(f"  Created: {folder_name}", dry_run)
        
        # Create Exams subfolders
        exams_papers = course_path / "Exams" / "Papers"
        exams_solutions = course_path / "Exams" / "Solutions"
        if not exams_papers.exists():
            if dry_run:
                logMessage(f"  Would create: {exams_papers}", dry_run)
            else:
                exams_papers.mkdir(parents=True, exist_ok=True)
                logMessage(f"  Created: Exams/Papers", dry_run)
        
        if not exams_solutions.exists():
            if dry_run:
                logMessage(f"  Would create: {exams_solutions}", dry_run)
            else:
                exams_solutions.mkdir(parents=True, exist_ok=True)
                logMessage(f"  Created: Exams/Solutions", dry_run)


def moveContentToNewStructure(dry_run: bool = False):
    """Moves existing content to new folder structure."""
    logMessage("\n=== Step 3: Moving Content to New Structure ===", dry_run)
    
    # First, handle specific removals of outdated paths
    for path in PATHS_TO_REMOVE:
        if path.exists():
            if dry_run:
                logMessage(f"Would remove outdated path: {path}", dry_run)
            else:
                if path.is_dir():
                    shutil.rmtree(str(path))
                else:
                    path.unlink()
                logMessage(f"Removed outdated path: {path.name}", dry_run)

    courses = getAllCourseDirectories()
    
    for course_path in courses:
        logMessage(f"\nProcessing: {course_path.name}", dry_run)
        
        # Process existing subdirectories
        for item in course_path.iterdir():
            if not item.is_dir():
                continue
                
            old_name = item.name
            
            # Skip new folders we just created
            if old_name in NEW_COURSE_FOLDERS:
                continue
            if old_name == "Exams":
                continue
                
            # Determine new location
            if old_name in FOLDER_RENAME_MAP:
                new_folder_name = FOLDER_RENAME_MAP[old_name]
                
                if new_folder_name is None:
                    # Folder to be removed (Quizzes)
                    if dry_run:
                        logMessage(f"  Would remove folder: {item}", dry_run)
                    else:
                        if item.exists():
                            shutil.rmtree(str(item))
                            logMessage(f"  Removed: {old_name}", dry_run)
                else:
                    # Rename and move folder
                    target = course_path / new_folder_name
                    
                    if item != target:  # Don't move to self
                        if dry_run:
                            logMessage(f"  Would move: {item} → {target}", dry_run)
                        else:
                            # Merge contents if target exists
                            if target.exists():
                                # Move contents of item to target
                                for subitem in item.iterdir():
                                    dest = target / subitem.name
                                    if dest.exists():
                                        logMessage(f"    WARNING: Skipping existing: {dest}", dry_run)
                                    else:
                                        shutil.move(str(subitem), str(dest))
                                # Remove empty old folder
                                shutil.rmtree(str(item))
                                logMessage(f"  Moved contents: {old_name} → {new_folder_name}", dry_run)
                            else:
                                shutil.move(str(item), str(target))
                                logMessage(f"  Moved: {old_name} → {new_folder_name}", dry_run)
            
            # Handle images folders (move to Exams/Papers/images)
            elif isImageFolder(old_name):
                target = course_path / "Exams" / "Papers" / "images"
                if dry_run:
                    logMessage(f"  Would move images: {item} → {target}", dry_run)
                else:
                    if target.exists():
                        # Merge contents
                        for subitem in item.iterdir():
                            dest = target / subitem.name
                            if dest.exists():
                                logMessage(f"    WARNING: Skipping existing: {dest}", dry_run)
                            else:
                                shutil.move(str(subitem), str(dest))
                        shutil.rmtree(str(item))
                        logMessage(f"  Moved images to Exams/Papers/images", dry_run)
                    else:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(item), str(target))
                        logMessage(f"  Moved images to Exams/Papers/images", dry_run)
            
            # Handle other folders (keep as is, but log)
            else:
                logMessage(f"  Keeping folder as is: {old_name}", dry_run)
        
        # Process files in course root (move to appropriate folders)
        for item in course_path.iterdir():
            if item.is_dir():
                continue
            
            filename = item.name
            
            # Skip README and common files
            if filename in ["README.md", ".gitignore", "LICENSE"]:
                continue
            
            # Check if it's an exam paper
            if isExamPaper(filename):
                target = course_path / "Exams" / "Papers" / filename
                if dry_run:
                    logMessage(f"  Would move exam paper: {item} → {target}", dry_run)
                else:
                    if target.exists():
                        logMessage(f"    WARNING: Skipping existing: {target}", dry_run)
                    else:
                        shutil.move(str(item), str(target))
                        logMessage(f"  Moved exam paper to Exams/Papers/", dry_run)
            else:
                # Move other files to Resources
                target = course_path / "Resources" / filename
                if dry_run:
                    logMessage(f"  Would move to Resources: {item} → {target}", dry_run)
                else:
                    if target.exists():
                        logMessage(f"    WARNING: Skipping existing: {target}", dry_run)
                    else:
                        shutil.move(str(item), str(target))
                        logMessage(f"  Moved to Resources/", dry_run)


def handleSpecialCases(dry_run: bool = False):
    """Handles special cases like dynamic Quartus project zipping."""
    logMessage("\n=== Step 4: Handling Special Cases (Quartus) ===", dry_run)
    
    # Dynamically find all Quartus project directories
    # Matches any folder containing "Quartus" in its name
    quartus_projects = list(REPO_ROOT.rglob("*Quartus*"))
    
    # Filter to only keep directories and ensure we aren't zipping within the .git folder
    quartus_projects = [p for p in quartus_projects if p.is_dir() and ".git" not in p.parts]
    
    if not quartus_projects:
        logMessage("  No Quartus projects found.", dry_run)
        return

    for project_path in quartus_projects:
        if project_path.exists():
            zip_name = project_path.name
            # make_archive appends .zip automatically
            zip_full_path = project_path.parent / (zip_name + ".zip")
            
            if dry_run:
                logMessage(f"  Would zip: {project_path} → {zip_full_path}", dry_run)
            else:
                logMessage(f"  Zipping: {project_path.name}", dry_run)
                try:
                    shutil.make_archive(str(project_path.parent / zip_name), 'zip', 
                                      root_dir=str(project_path.parent), 
                                      base_dir=project_path.name)
                    # Remove original directory after successful zipping
                    shutil.rmtree(str(project_path))
                    logMessage(f"    Success: Created zip and removed original directory", dry_run)
                except Exception as e:
                    logMessage(f"    FAILED to zip {project_path.name}: {str(e)}", dry_run)


def updateGitignore(dry_run: bool = False):
    """Updates .gitignore to exclude build artifacts."""
    logMessage("\n=== Step 5: Updating .gitignore ===", dry_run)
    
    gitignore_path = REPO_ROOT / ".gitignore"
    
    # Additional patterns to add
    additional_patterns = [
        "",
        "# Quartus project files",
        "*.qpf",
        "*.qsf", 
        "*.qws",
        "*.vhd.bak",
        "db/",
        "incremental_db/",
        "output_files/",
        "simulation/",
        "",
        "# Build artifacts",
        "*.zip",  # Zipped projects
    ]
    
    if dry_run:
        logMessage(f"  Would add to .gitignore:", dry_run)
        for pattern in additional_patterns:
            logMessage(f"    {pattern}", dry_run)
    else:
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            f.write("\n".join(additional_patterns) + "\n")
        logMessage(f"  Updated .gitignore with new patterns", dry_run)


def generateSummaryReport(dry_run: bool = False):
    """Generates a summary report of changes."""
    logMessage("\n=== Summary Report ===", dry_run)
    
    courses = getAllCourseDirectories()
    logMessage(f"Total courses processed: {len(courses)}", dry_run)
    
    # Count folders
    folder_counts = {}
    for course in courses:
        for subfolder in course.iterdir():
            if subfolder.is_dir():
                folder_counts[subfolder.name] = folder_counts.get(subfolder.name, 0) + 1
    
    logMessage("\nFolder distribution across courses:", dry_run)
    for folder, count in sorted(folder_counts.items()):
        logMessage(f"  {folder}: {count} courses", dry_run)
    
    logMessage(f"\nLog file saved to: {LOG_FILE}", dry_run)


def main():
    parser = argparse.ArgumentParser(description='Restructure DitOpenNotes repository')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    args = parser.parse_args()
    
    logMessage("Starting repository restructuring...", args.dry_run)
    logMessage(f"Repository root: {REPO_ROOT}", args.dry_run)
    logMessage(f"Mode: {'DRY-RUN' if args.dry_run else 'ACTUAL CHANGES'}", args.dry_run)
    
    try:
        # Step 1: Rename course folders
        renameCourseFolders(args.dry_run)
        
        # Step 2: Create new folder structure
        createNewFolderStructure(args.dry_run)
        
        # Step 3: Move content to new structure
        moveContentToNewStructure(args.dry_run)
        
        # Step 4: Handle special cases (Quartus)
        handleSpecialCases(args.dry_run)
        
        # Step 5: Update .gitignore
        updateGitignore(args.dry_run)
        
        # Step 6: Generate summary
        generateSummaryReport(args.dry_run)
        
        logMessage("\nRestructuring completed successfully!", args.dry_run)
        
    except Exception as e:
        logMessage(f"\nERROR: {str(e)}", args.dry_run)
        logMessage("Restructuring failed. Please check the log and try again.", args.dry_run)
        raise


if __name__ == "__main__":
    main()

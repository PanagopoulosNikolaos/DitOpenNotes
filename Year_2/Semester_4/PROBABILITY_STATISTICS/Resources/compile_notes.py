import os
import re

def getSortKey(file_path):
    """
    Extracts phase and section numbers from the filename for sorting.
    Example: 'phase_1_2_measures.md' -> (1, 2)
    """
    filename = os.path.basename(file_path)
    match = re.search(r'phase_(\d+)_(\d+)', filename)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    # For files that don't match the pattern, push them to the end or beginning
    # We'll return a high value for non-matching files to keep them at the end
    return (999, 999)

def compileNotes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lectures_dir = os.path.join(base_dir, '..', 'Lectures')
    output_file = os.path.join(lectures_dir, 'StatisticsNotes.md')
    
    md_files = []
    for root, dirs, files in os.walk(lectures_dir):
        for file in files:
            if file.endswith('.md') and file != 'StatisticsNotes.md':
                md_files.append(os.path.join(root, file))
    
    # Filter only files that follow the phase pattern to ensure correct ordering
    # as per user request.
    phase_files = [f for f in md_files if re.search(r'phase_\d+_\d+', os.path.basename(f))]
    phase_files.sort(key=getSortKey)
    
    print(f"Found {len(phase_files)} phase files to merge.")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# Statistics Notes - Full Compilation\n\n")
        outfile.write("Generated from individual lecture phases.\n\n---\n\n")
        
        for file_path in phase_files:
            relative_path = os.path.relpath(file_path, lectures_dir)
            print(f"Appending: {relative_path}")
            
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                # Ensure each section starts on a new page/large break
                outfile.write(f"<!-- Source: {relative_path} -->\n")
                outfile.write(content)
                outfile.write("\n\n---\n\n")
                
    print(f"\nSuccessfully created: {output_file}")

if __name__ == "__main__":
    compileNotes()

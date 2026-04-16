"""
Extracts textual content from OpenDocument XML paragraph tags.
"""

import xml.etree.ElementTree as ET
import sys
import os


def extractTextFromXml(xml_path: str) -> None:
    """
    Parses an XML file and prints the text content of all paragraph elements.
    
    Args:
        xml_path (str): The file path to the XML document.
        
    Returns:
        None
    """
    try:
        tree = ET.parse(xml_path)  # Loads the XML file into an ElementTree object.
        root = tree.getroot()  # Retrieves the root element of the XML tree.
        
        for elem in root.iter():  # Traverses every element in the document tree.
            # Identifies paragraph elements regardless of namespace format.
            if elem.tag.endswith('}p') or elem.tag.endswith(':p') or elem.tag == 'p':
                # Concatenates text from all child nodes and removes surrounding whitespace.
                text = "".join(elem.itertext()).strip()
                if text:
                    # print(text)  
                    with open("../fetched_xml_text.txt", "a") as f:
                        f.write(text + "\n")
    except Exception as e:
        print(f"Error parsing {xml_path}: {e}")


if __name__ == "__main__":
    target_file = "../How_a_switch_works_converted.xml"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        
    if os.path.exists(target_file):
        extractTextFromXml(target_file)
    else:
        print(f"File not found: {target_file}")

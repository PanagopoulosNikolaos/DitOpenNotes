"""
Provides functionality to convert PowerPoint (PPTX) files to XML format locally.
"""

import subprocess
import os
import sys

class PptxConverter:
    """
    Handles the conversion of presentation files using system tools.
    """

    def convertToXml(self, input_path: str, output_name: str = None) -> bool:
        """
        Converts a PPTX file to a Flat XML ODF Presentation (.xml) using LibreOffice.

        Args:
            input_path (str): The path to the source .pptx file.
            output_name (str): Optional custom name for the resulting XML file.

        Returns:
            bool: True if the conversion was successful, False otherwise.
        """
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' does not exist.")
            return False

        # Flat XML ODF Presentation (FODP) is the most accurate XML representation of ODF.
        try:
            command = [
                "libreoffice",
                "--headless",
                "--convert-to", "fodp",
                input_path,
                "--outdir", os.path.dirname(os.path.abspath(input_path))
            ]
            
            # Execute the conversion command.
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            
            # The output file defaults to [basename].fodp.
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            fodp_file = os.path.join(os.path.dirname(input_path), f"{base_name}.fodp")
            
            if os.path.exists(fodp_file):
                final_xml = output_name if output_name else f"{base_name}_converted.xml"
                os.replace(fodp_file, os.path.join(os.path.dirname(input_path), final_xml))
                print(f"Success: Created '{final_xml}' from '{input_path}'.")
                return True
            
            return False

        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e.stderr}")
            return False
        except FileNotFoundError:
            print("Error: LibreOffice is not installed or not in the system path.")
            return False

if __name__ == "__main__":
    converter = PptxConverter()
    
    target_pptx = "../How_a_switch_works.pptx"
    
    if len(sys.argv) > 1:
        target_pptx = sys.argv[1]

    if target_pptx.lower().endswith(".pptx"):
        converter.convertToXml(target_pptx)
    else:
        print("Please provide a valid .pptx file.")

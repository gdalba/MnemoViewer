import os
import json
import glob
import argparse

def create_excel_files_index(folder_path, output_json_path):
    """
    Creates a JSON file listing all Excel files in a folder
    
    Args:
        folder_path: Path to folder containing Excel files
        output_json_path: Path where JSON index will be saved
    """
    # Find all .xlsx files in the folder
    xlsx_files = glob.glob(os.path.join(folder_path, "*.xlsx"))
    
    # Extract just the filenames
    filenames = [os.path.basename(file) for file in xlsx_files]
    
    # Sort filenames
    filenames.sort()
    
    # Write to JSON file
    with open(output_json_path, 'w') as f:
        json.dump(filenames, f, indent=2)
    
    print(f"Created index with {len(filenames)} Excel files at {output_json_path}")
    print(f"First few files: {filenames[:5]}")

def parse_arguments():
    """
    Parses command line arguments for folder path and output JSON file
    """
    parser = argparse.ArgumentParser(description="Create JSON index of Excel files in a folder")
    parser.add_argument("folder_path", type=str, help="Path to folder containing Excel files")
    parser.add_argument("output_json_path", type=str, help="Path where JSON index will be saved")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    excel_folder = args.folder_path
    json_output = args.output_json_path
    create_excel_files_index(excel_folder, json_output)
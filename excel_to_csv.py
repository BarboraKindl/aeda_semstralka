import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def convert_xlsx_to_csv():
    """
    Convert an .xlsx file to .csv format using paths from .env file.
    """
    input_file = os.getenv('INPUT_FILE')  # Read input file path from .env
    output_file = os.getenv('OUTPUT_FILE')  # Read output file path from .env

    if not input_file or not output_file:
        print("Error: Missing file paths in .env file.")
        return

    try:
        # Read the Excel file
        df = pd.read_excel(input_file)
        # Save it as a CSV file
        df.to_csv(output_file, index=False)
        print(f"File successfully converted to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
convert_xlsx_to_csv()

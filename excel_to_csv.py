import pandas as pd
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(
    filename="excel_to_csv.log",  # Log file
    level=logging.INFO,  # Logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
)

# Load .env variables
load_dotenv()

def convert_xlsx_to_csv():
    """
    Converts an Excel (.xlsx) file to a CSV file.
    Reads input and output file paths from a .env configuration file.
    Logs progress and errors for debugging.
    """
    logging.info("Starting Excel to CSV conversion process.")

    input_file = os.getenv('INPUT_FILE')
    output_file = os.getenv('OUTPUT_FILE')

    # Validate environment variables
    if not input_file or not output_file:
        logging.error("Missing INPUT_FILE or OUTPUT_FILE in .env file.")
        print("Error: Please ensure INPUT_FILE and OUTPUT_FILE are set in the .env file.")
        return

    logging.info(f"Input file: {input_file}")
    logging.info(f"Output file: {output_file}")

    try:
        # Read the Excel file
        logging.info(f"Reading Excel file: {input_file}")
        df = pd.read_excel(input_file)

        # Save as a CSV file
        logging.info(f"Writing data to CSV file: {output_file}")
        df.to_csv(output_file, index=False)
        logging.info(f"Successfully converted {input_file} to {output_file}.")
        print(f"File successfully converted: {output_file}")
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        logging.exception("An unexpected error occurred during conversion.")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_xlsx_to_csv()

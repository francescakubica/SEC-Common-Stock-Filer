import pandas as pd
import requests
import os

def download_files_from_links(excel_file, output_directory="downloaded_files"):
    """
    Takes an Excel file, looks for the 'LINK' column, downloads the file at each link,
    and saves it as a .txt file in the specified output directory.

    Parameters:
        excel_file (str): Path to the Excel file.
        output_directory (str): Directory where the downloaded files will be saved.
    """
    # Load the Excel file into a DataFrame
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return
    
    # Check if 'LINK' column exists
    if "LINK" not in df.columns:
        print("The column 'LINK' does not exist in the Excel file.")
        return
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Iterate through each link in the 'LINK' column
    for index, link in enumerate(df["LINK"]):

        headers = { # Let them know it's from USC
        'User-Agent': 'University of Southern California fkubica@usc.edu'
        }
        try:
            # Fetch the content from the link
            response = requests.get(link, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            
            # Save the content to a .txt file
            filename = os.path.join(output_directory, f"file_{index + 1}.txt")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            
            print(f"Downloaded and saved: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download from {link}: {e}")

# Example usage
excel_file_path = "13D.xlsx"  # Replace with your Excel file path
download_files_from_links(excel_file_path)

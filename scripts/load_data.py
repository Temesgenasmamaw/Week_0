import pandas as pd

def load_csv_files(file_paths):
    """
    Load multiple CSV files into pandas DataFrames.

    Parameters:
    file_paths (list): List of paths to the CSV files.

    Returns:
    dict: A dictionary where keys are file names and values are DataFrames.
    """
    dataframes = {}
    for path in file_paths:
        try:
            df = pd.read_csv(path)
            file_name = path.split('/')[-1]  # Extract the file name from the path
            dataframes[file_name] = df
            print(f"{file_name} loaded successfully with shape {df.shape}.")
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return dataframes

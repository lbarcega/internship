import os
import pandas as pd
from azure.storage.blob import BlobServiceClient

from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

def upload_blob(blob_name):
    # Define your connection string and container name
    connection_string = os.environ.get('AZURE_CONNECTION_STRING')
    container_name = os.environ.get('AZURE_CONTAINER_NAME')
    blob_name = blob_name

    # Define the file paths
    file_path = os.path.dirname(os.path.abspath(__file__))
    export_path = os.path.join(file_path, "export")
    blob_path = os.path.join(export_path, blob_name)

    # Setup the blob service client and blob clients
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    try:
        # Upload the file
        with open(blob_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"{blob_name} uploaded to {container_name}.")
    except Exception as e:
        print(f"Failed to upload {blob_name} to {container_name}: {e}")

def merge_and_clean(folder_name, export_name):
    # Get the current script directory and build paths
    file_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(file_path, folder_name)
    export_path = os.path.join(file_path, "export")

    # List all files in the directory and filter only CSV files
    folder_contents = os.listdir(data_path)
    file_name = [f for f in folder_contents if f.endswith('.csv') and os.path.isfile(os.path.join(data_path, f))]

    # Read all CSV files into dataframes
    dfs = [pd.read_csv(os.path.join(data_path, file)) for file in file_name]

    # Start with the first DataFrame, no rows will be dropped
    merged_df = dfs[0]

    # Merge all subsequent DataFrames on 'TaskID' with an outer join, ensuring no rows are dropped
    for df in dfs[1:]:
        merged_df = merged_df.merge(df, on="TaskID", how="outer")

    # Drop rows where only 2 values are non-NaN (excluding ID and TaskID)
    relevant_columns = [col for col in merged_df.columns if col not in ['ID', 'TaskID']]
    merged_df = merged_df[merged_df[relevant_columns].count(axis=1) > 2]

    # Drop original "SprintID" and turn "SprintName" into new "SprintID"
    merged_df.drop(columns=["SprintID"], inplace=True)
    merged_df.rename(columns={"SprintName": "SprintID"}, inplace=True)
    merged_df['SprintID'] = merged_df['SprintID'].str.replace('Sprint_', '')

    # Add the 'ID' column as the first column, with unique values starting from 1
    merged_df.insert(0, 'ID', range(1, len(merged_df) + 1))

    # Reorder columns to make sure 'TaskID' is the second column (after 'ID')
    cols = ['ID', 'TaskID'] + [col for col in merged_df.columns if col not in ['ID', 'TaskID']]
    merged_df = merged_df[cols]

    # Ensure export path exists, if not create it
    if not os.path.exists(export_path):
        os.makedirs(export_path)

    # Write the merged DataFrame to an Excel file
    ctr = 0
    full_export_path = os.path.join(export_path, export_name)
    temp_name = ''
    while os.path.exists(f"{full_export_path}.xlsx"):
            ctr += 1
            temp_name = os.path.join(export_path, temp_name)
            full_export_path = (f"{export_path}/{export_name} ({ctr})")
    merged_df.to_excel(f"{full_export_path}.xlsx", index=False)


merge_and_clean("data", "demo")
upload_blob("demo.xlsx")


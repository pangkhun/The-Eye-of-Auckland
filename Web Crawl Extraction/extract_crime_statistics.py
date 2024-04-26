import requests

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")

# Download URL
file_url = "https://public.tableau.com/vizql/w/VictimisationsTimeandPlace/v/Summary/tempfile/sessions/F1EE63DB53544958B9E031E0CBC81BC4-0:0/?key=1904627848&keepfile=yes&attachment=yes"
# Save path
save_path = "./crime_data.csv"

# Call the download function
download_file(file_url, save_path)

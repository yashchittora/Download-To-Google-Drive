import os
import urllib.parse
import requests
from tqdm import tqdm
from google.colab import drive

def mount_drive():
    """Mount Google Drive for saving the downloaded file."""
    print("🔗 Mounting Google Drive...")
    drive.mount('/content/drive')
    print("✅ Drive mounted successfully!")

def get_user_input():
    """Prompt the user for the file URL and desired filename."""
    file_url = input("\n🔗 Enter the direct URL of the file to download: ").strip()
    file_name = input("📂 Enter the desired filename (including extension): ").strip()
    
    if not file_url or not file_name:
        print("⚠️ Error: Both URL and filename are required.")
        return None, None
    
    # Validate and encode URL
    file_url = urllib.parse.quote(file_url, safe=":/?&=")  
    return file_url, file_name

def download_file(file_url, file_name):
    """Download a file with a progress bar and save it to Google Drive."""
    save_path = f"/content/drive/My Drive/{file_name}"

    print(f"\n🎯 Downloading file from: {file_url}")
    print(f"💾 Saving to: {save_path}\n")

    response = requests.get(file_url, stream=True)
    
    if response.status_code != 200:
        print("❌ Error: Unable to download the file. Check the URL.")
        return
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(save_path, "wb") as file, tqdm(
        desc="📥 Download Progress",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        ncols=80,
        colour="green"
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
            bar.update(len(chunk))

    print(f"\n✅ Download completed successfully: {save_path}")

if __name__ == "__main__":
    mount_drive()
    file_url, file_name = get_user_input()
    
    if file_url and file_name:
        download_file(file_url, file_name)

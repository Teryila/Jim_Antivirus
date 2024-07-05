import os
import hashlib
import magic
import pyfiglet
import requests

VIRUS_DEFINITIONS_URL = "http://10.105.41.80:8080/virus_definitions.txt"

def display_banner():
    banner = pyfiglet.figlet_format("J ANTIVIRUS")
    print(banner)

def get_file_hashes(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
    return sha256_hash

def identify_file_type(file_path):
    file_type = magic.from_file(file_path)
    return file_type

def check_for_virus_signatures(file_path, virus_signatures):
    file_hash = get_file_hashes(file_path)
    if file_hash in virus_signatures:
        return True
    else:
        return False

def update_virus_definitions():
    try:
        response = requests.get(VIRUS_DEFINITIONS_URL)
        if response.status_code == 200:
            virus_definitions = response.text.split('\n')
            print("Virus definitions updated successfully.")
            return virus_definitions
        else:
            print("Failed to update virus definitions. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error updating virus definitions: {e}")

def scan_file(file_path, virus_signatures):
    file_type = identify_file_type(file_path)
    print(f"Scanning file: {file_path} ({file_type})")
    if check_for_virus_signatures(file_path, virus_signatures):
        print(f"Virus detected in {file_path}!")
    else:
        print(f"{file_path} is clean.")

def main():
    display_banner()
    virus_signatures = update_virus_definitions()
    if virus_signatures:
        while True:
            file_path = input("Enter the file path to scan (or 'q' to quit): ")
            if file_path.lower() == 'q':
                break
            if os.path.isfile(file_path):
                scan_file(file_path, virus_signatures)
            else:
                print(f"Invalid file path: {file_path}")

if __name__ == "__main__":
    main()



import json
import argparse
import requests

# Set up the argument parser
parser = argparse.ArgumentParser(description='Extract domains from a JSON file and output to a TXT file.')
parser.add_argument('-L', '--local', type=str, help='Local file path to read the data from.')

# Parse the arguments
args = parser.parse_args()

# Define the output TXT file path
output_txt_file_path = 'domains.txt'

# Function to get data from GitHub
def get_data_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # will raise an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()

# Function to read local JSON file
def get_data_from_local_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Determine the source of the data
if args.local:
    data = get_data_from_local_file(args.local)
else:
    github_url = 'https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json'
    data = get_data_from_github(github_url)

# Extract domains from the data
domains = [domain for entry in data for domain in entry['domains']]

# Write the extracted domains to a TXT file
with open(output_txt_file_path, 'w') as file:
    for domain in domains:
        file.write(domain + '\n')

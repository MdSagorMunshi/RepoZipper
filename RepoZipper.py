import os
import zipfile
import requests
from tqdm import tqdm
import shutil
import subprocess
import re

def extract_username(profile_url):
    match = re.match(r'https://github.com/([a-zA-Z0-9_-]+)', profile_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid GitHub profile URL")

def get_username_from_input(input_string):
    if re.match(r'https://github.com/([a-zA-Z0-9_-]+)', input_string):
        return extract_username(input_string)
    else:
        return input_string

def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos?sort=created'
    repos = []
    while url:
        response = requests.get(url)
        response.raise_for_status()
        repos.extend(response.json())
        url = response.links.get('next', {}).get('url')
    return repos

def clone_repos(repos, temp_dir):
    for repo in tqdm(repos, desc="Cloning Repositories", unit="repo", leave=False):
        repo_url = repo['clone_url']
        repo_name = repo['name']
        repo_dir = os.path.join(temp_dir, repo_name)
        print(f"Cloning {repo_name}...")
        subprocess.run(['git', 'clone', repo_url, repo_dir], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def zip_repos(temp_dir, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_dir))

def main():
    user_input = input("Enter GitHub profile URL or username: ").strip()
    username = get_username_from_input(user_input)
    temp_dir = 'temp_repo_dir'
    zip_filename = f'{username}_repos.zip'

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    try:
        repos = get_repos(username)
        print(f"Found {len(repos)} repositories.")
        
        clone_repos(repos, temp_dir)
        
        zip_repos(temp_dir, zip_filename)
        print(f"Created zip file: {zip_filename}")
        print(f"Total Repositories Cloned: {len(repos)}")
        if repos:
            print(f"Date of creation: {repos[0]['created_at']}")

    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()

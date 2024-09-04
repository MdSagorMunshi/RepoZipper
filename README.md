
# RepoZipper

RepoZipper is a Python script that allows you to clone all repositories from a specified GitHub user and package them into a single ZIP file. It supports both GitHub profile URLs and usernames as input, making it easy to use in various scenarios.

## Features

- **Input Flexibility:** Accepts both GitHub profile URLs and usernames.
- **Automatic Username Extraction:** If a URL is provided, the script extracts the username automatically.
- **Repository Cloning:** Clones all repositories belonging to the specified user.
- **Zipping:** Compresses all cloned repositories into a single ZIP file.
- **Progress Tracking:** Utilizes a progress bar to show the cloning process.

## **Upcoming Features**

**In the next update, we plan to add support for multiple download options, allowing you to choose different formats or methods for downloading repositories.**


## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests` library: `pip install requests`
- `tqdm` library: `pip install tqdm`

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/MdSagorMunshi/RepoZipper.git
    cd RepoZipper
    ```

2. **Run the Script:**
    Execute the script by providing either a GitHub profile URL or a username when prompted:
    ```bash
    python RepoZipper.py
    ```

3. **Input:**
   - You can enter a GitHub profile URL (e.g., `https://github.com/MdSagorMunshi`) or just the username (e.g., `MdSagorMunshi`).
   - The script will then clone all repositories associated with the provided username.

4. **Output:**
    - The script creates a ZIP file containing all cloned repositories.
    - The ZIP file will be named based on the username (e.g., `MdSagorMunshi_repos.zip`).

5. **Clean-up:**
    - The temporary directory used for cloning repositories is automatically deleted after the ZIP file is created.

## Example

```bash
$ python clone_and_zip.py
Enter GitHub profile URL or username: https://github.com/MdSagorMunshi
Found 8 repositories.
Cloning Repositories: 100%|██████████████████████████████| 8/8 [00:30<00:00, 3.75s/repo]
Created zip file: MdSagorMunshi_repos.zip
Total Repositories Cloned: 8
Date of creation: 2024-08-26T19:01:12Z
```

## Error Handling

- The script will raise an error if the provided GitHub URL is invalid.
- If a network issue occurs during the cloning process, the script will stop and display an error message.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request.

## Acknowledgments

- [tqdm](https://github.com/tqdm/tqdm) for the progress bar.
- [requests](https://github.com/psf/requests) for handling HTTP requests.



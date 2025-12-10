# ginit - GitHub Repository Initialization CLI

A clean, simple command-line tool to automate the entire workflow of initializing a Git repository, creating a GitHub repository, and pushing your code.

## Installation

### Option 1: Install as CLI tool (Recommended)

```powershell
pip install -e .
```

After installation, you can use `ginit` from anywhere:

```powershell
ginit "C:\path\to\your\project"
```

### Option 2: Run directly with Python

```powershell
python ginit.py "C:\path\to\your\project"
```

## Features

- ✓ Clean, minimal CLI output
- ✓ Automatic git initialization
- ✓ Auto-generates `.gitignore`
- ✓ Creates GitHub repository
- ✓ License selection (MIT, Apache, GPL, BSD, ISC, Unlicense)
- ✓ Pushes to main branch
- ✓ Public/private repository option

## 📦 Project Structure

```
ginit/
├── ginit.py             # CLI entry point
├── main.py              # Main workflow orchestration
├── git_operations.py    # Git commands
├── github_api.py        # GitHub API interactions
├── config.py            # Configuration & user input
├── licenses.py          # License templates
├── setup.py             # Package installation
└── requirements.txt     # Dependencies
```

## Setup

### 1. Create a GitHub Token

1. Go to https://github.com/settings/tokens
2. Generate a new token (classic) with `repo` scope
3. Copy the token

**Option A: Using .env file (Recommended)**

Create a `.env` file in this directory:
```
GITHUB_TOKEN=your_token_here
```

**Option B: Using environment variable**

```powershell
# PowerShell
$env:GITHUB_TOKEN='your_token_here'
```

## Usage

### Basic usage

```powershell
ginit /path/to/project
```

### With custom repository name

```powershell
ginit /path/to/project my-repo-name
```

### Interactive mode

Just run `ginit` and follow the prompts:

```powershell
ginit
```

## Example Output

```
Enter the folder path to automate: C:\MyProject

Enter custom repository name (or press Enter to use folder name): 

Enter repository description (optional): My awesome project

Make repository private? (y/N): n

Select a license for your repository:
1. MIT License
2. Apache License 2.0
3. GNU General Public License v3.0
4. BSD 3-Clause License
5. BSD 2-Clause License
6. ISC License
7. The Unlicense
8. No License

Enter choice (1-8) or press Enter to skip: 1

Enter author/copyright holder name: John Doe

✓ Initialized git repository
✓ Created LICENSE (MIT License)
✓ Created initial commit
✓ Created repository: MyProject
✓ Pushed to GitHub

✓ Repository created: https://github.com/username/MyProject
```

## Uninstall

```powershell
pip uninstall ginit-cli
```

## License

MIT License

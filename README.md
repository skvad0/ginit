# ginit - GitHub Repository Initialization CLI

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

- Clean, minimal CLI output
- Automatic git initialization
- Auto-generates `.gitignore`
- Creates GitHub repository
- License selection (MIT, Apache, GPL, BSD, ISC, Unlicense)
- Pushes to main branch
- Public/private repository option

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

## Uninstall

```powershell
pip uninstall ginit-cli
```

## License

MIT License

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

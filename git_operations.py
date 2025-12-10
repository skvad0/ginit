"""
Git Operations Module
Handles all local Git operations including init, add, commit, and push.
"""

import subprocess
from pathlib import Path


class GitOperations:
    """Handles all Git-related operations."""
    
    @staticmethod
    def run_command(command, cwd=None):
        """
        Run a shell command and return the output.
        
        Args:
            command: Command to run as a list
            cwd: Working directory for the command
            
        Returns:
            tuple: (success: bool, output: str)
        """
        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                check=True
            )
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            return False, e.stderr
    
    @staticmethod
    def check_git_installed():
        """
        Check if git is installed on the system.
        
        Raises:
            RuntimeError: If git is not installed
        """
        success, _ = GitOperations.run_command(['git', '--version'])
        if not success:
            raise RuntimeError("Git is not installed. Please install Git first.")
        return True
    
    @staticmethod
    def is_git_repo(folder_path):
        """
        Check if the folder is already a git repository.
        
        Args:
            folder_path: Path to check
            
        Returns:
            bool: True if folder is a git repo
        """
        git_dir = Path(folder_path) / '.git'
        return git_dir.exists()
    
    @staticmethod
    def init_repo(folder_path):
        """
        Initialize a git repository in the specified folder.
        
        Args:
            folder_path: Path to the folder to initialize
            
        Returns:
            bool: True if successful
        """
        success, output = GitOperations.run_command(['git', 'init'], cwd=folder_path)
        
        if not success:
            print(f"Failed to initialize git: {output}")
            return False
        
        print("Initialized git repository")
        return True
    
    @staticmethod
    def create_gitignore(folder_path):
        """
        Create a basic .gitignore file if it doesn't exist.
        
        Args:
            folder_path: Path to the folder
        """
        gitignore_path = Path(folder_path) / '.gitignore'
        
        if not gitignore_path.exists():
            default_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
"""
            gitignore_path.write_text(default_content)
    
    @staticmethod
    def add_all_files(folder_path):
        """
        Add all files to git staging area.
        
        Args:
            folder_path: Path to the repository folder
            
        Returns:
            bool: True if successful
        """
        success, output = GitOperations.run_command(['git', 'add', '.'], cwd=folder_path)
        
        if not success:
            print(f"Failed to add files: {output}")
            return False
        
        return True
    
    @staticmethod
    def commit(folder_path, commit_message="Initial commit"):
        """
        Create a commit with the specified message.
        
        Args:
            folder_path: Path to the repository folder
            commit_message: Commit message
            
        Returns:
            bool: True if successful
        """
        success, output = GitOperations.run_command(
            ['git', 'commit', '-m', commit_message],
            cwd=folder_path
        )
        
        if not success:
            if "nothing to commit" in output:
                return True
            print(f"Failed to commit: {output}")
            return False
        
        print("Created initial commit")
        return True
    
    @staticmethod
    def add_remote(folder_path, repo_url):
        """
        Add remote origin to the repository.
        
        Args:
            folder_path: Path to the local repository
            repo_url: URL of the remote repository
            
        Returns:
            bool: True if successful
        """
        # Remove existing remote if it exists
        GitOperations.run_command(['git', 'remote', 'remove', 'origin'], cwd=folder_path)
        
        success, output = GitOperations.run_command(
            ['git', 'remote', 'add', 'origin', repo_url],
            cwd=folder_path
        )
        
        if not success:
            print(f"Failed to add remote: {output}")
            return False
        
        return True
    
    @staticmethod
    def rename_branch(folder_path, branch='main'):
        """
        Rename the current branch.
        
        Args:
            folder_path: Path to the local repository
            branch: New branch name
            
        Returns:
            bool: True if successful
        """
        success, output = GitOperations.run_command(
            ['git', 'branch', '-M', branch],
            cwd=folder_path
        )
        
        if not success:
            print(f"Failed to rename branch: {output}")
            return False
        
        return True
    
    @staticmethod
    def push(folder_path, branch='main'):
        """
        Push commits to remote repository.
        
        Args:
            folder_path: Path to the local repository
            branch: Branch to push
            
        Returns:
            bool: True if successful
        """
        print("Pushing to GitHub...", end='', flush=True)
        success, output = GitOperations.run_command(
            ['git', 'push', '-u', 'origin', branch],
            cwd=folder_path
        )
        
        if not success:
            print(f"\rFailed to push: {output}")
            return False
        
        print("\rPushed to GitHub     ")
        return True

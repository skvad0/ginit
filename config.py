"""
Configuration Module
Handles configuration, validation, and user input.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv


class Config:
    """Handles configuration and validation."""
    
    @staticmethod
    def get_github_token():
        """
        Get GitHub token from environment variable or .env file.
        
        Returns:
            str: GitHub token or None if not set
        """
        # Load .env file if it exists
        load_dotenv()
        return os.getenv('GITHUB_TOKEN')
    
    @staticmethod
    def validate_github_token():
        """
        Validate that GitHub token is set and provide setup instructions.
        
        Returns:
            str: GitHub token
            
        Raises:
            SystemExit: If token is not set
        """
        github_token = Config.get_github_token()
        
        if not github_token:
            print("\nError: GITHUB_TOKEN not found.")
            print("\nTo set up, choose one of these options:")
            print("\nOption 1 - Create a .env file (Recommended):")
            print("1. Go to https://github.com/settings/tokens")
            print("2. Generate a new token with 'repo' scope")
            print("3. Create a file named '.env' in this directory")
            print("4. Add this line: GITHUB_TOKEN=your_token_here")
            print("\nOption 2 - Set environment variable:")
            print("   Windows PowerShell: $env:GITHUB_TOKEN='your_token_here'")
            print("   Windows CMD: set GITHUB_TOKEN=your_token_here")
            print("   Linux/Mac: export GITHUB_TOKEN='your_token_here'")
            sys.exit(1)
        
        return github_token
    
    @staticmethod
    def validate_folder_path(folder_path):
        """
        Validate that folder path exists and is a directory.
        
        Args:
            folder_path: Path to validate
            
        Returns:
            Path: Resolved absolute path
            
        Raises:
            ValueError: If path is invalid
        """
        folder_path = Path(folder_path).resolve()
        
        if not folder_path.exists():
            raise ValueError(f"Folder '{folder_path}' does not exist.")
        
        if not folder_path.is_dir():
            raise ValueError(f"'{folder_path}' is not a directory.")
        
        return folder_path
    
    @staticmethod
    def get_folder_path_from_args():
        """
        Get folder path from command line arguments or prompt user.
        
        Returns:
            str: Folder path
            
        Raises:
            SystemExit: If no folder path provided
        """
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            folder_path = input("\nEnter the folder path to automate: ").strip()
            if not folder_path:
                print("Error: No folder path provided.")
                sys.exit(1)
            return folder_path
    
    @staticmethod
    def get_repo_name_from_args(folder_path):
        """
        Get repository name from command line or prompt user.
        
        Args:
            folder_path: Path object of the folder
            
        Returns:
            str: Repository name (defaults to folder name)
        """
        if len(sys.argv) > 2:
            return sys.argv[2]
        else:
            custom_name = input(f"\nEnter custom repository name (or press Enter to use folder name): ").strip()
            return custom_name if custom_name else folder_path.name
    
    @staticmethod
    def get_repository_description():
        """
        Prompt user for repository description.
        
        Returns:
            str: Repository description
        """
        return input("\nEnter repository description (optional): ").strip()
    
    @staticmethod
    def get_private_repo_preference():
        """
        Prompt user if repository should be private.
        
        Returns:
            bool: True if private, False if public
        """
        private_input = input("\nMake repository private? (y/N): ").strip().lower()
        return private_input == 'y'
    
    @staticmethod
    def get_license_preference():
        """
        Prompt user to select a license.
        
        Returns:
            tuple: (license_key: str, author_name: str or None)
        """
        from licenses import LicenseTemplates
        
        print("\nSelect a license for your repository:")
        licenses = LicenseTemplates.get_license_list()
        
        # Display options
        license_keys = list(licenses.keys())
        for idx, (key, name) in enumerate(licenses.items(), 1):
            print(f"{idx}. {name}")
        
        # Get user selection
        while True:
            choice = input(f"\nEnter choice (1-{len(licenses)}) or press Enter to skip: ").strip()
            
            if not choice:
                return 'None', None
            
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(license_keys):
                    license_key = license_keys[choice_idx]
                    
                    # Get author name if license requires it
                    if license_key != 'None':
                        author_name = input("\nEnter author/copyright holder name: ").strip()
                        if not author_name:
                            author_name = None
                        return license_key, author_name
                    else:
                        return 'None', None
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(licenses)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @staticmethod
    def print_header():
        """Print application header."""
        print("GitHub Repository Automation Tool")
        print("=" * 60)
    
    @staticmethod
    def print_workflow_start(folder_path, repo_name):
        """
        Print workflow start message.
        
        Args:
            folder_path: Path to the folder
            repo_name: Repository name
        """
        print(f"\n{'='*60}")
        print(f"Starting GitHub automation for: {folder_path}")
        print(f"Repository name: {repo_name}")
        print(f"{'='*60}\n")
    
    @staticmethod
    def print_workflow_complete(repo_url):
        """
        Print workflow completion message.
        
        Args:
            repo_url: URL of the created repository
        """
        print(f"\n{'='*60}")
        print("Automation completed successfully!")
        print(f"Repository URL: {repo_url}")
        print(f"{'='*60}\n")

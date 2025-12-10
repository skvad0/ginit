"""
GitHub Automation Script
Automates git init, commit, and push to a newly created GitHub repository.
"""

import sys
import traceback

from config import Config
from git_operations import GitOperations
from github_api import GitHubAPI
from licenses import LicenseTemplates


class GitHubAutomation:
    """Main automation orchestrator."""
    
    def __init__(self, github_token):
        """
        Initialize GitHub automation with a personal access token.
        
        Args:
            github_token: GitHub personal access token with repo scope
        """
        self.github_api = GitHubAPI(github_token)
        self.git_ops = GitOperations()
    
    def automate_full_workflow(self, folder_path, repo_name=None, description="", 
                               private=False, license_key=None, license_author=None,
                               commit_message="Initial commit"):
        """
        Complete automation: init, commit, create repo, and push.
        
        Args:
            folder_path: Path to the folder to automate
            repo_name: Name for the GitHub repo (defaults to folder name)
            description: Repository description
            private: Whether the repo should be private
            license_key: License key (e.g., 'MIT', 'Apache-2.0')
            license_author: Author name for the license
            commit_message: Initial commit message
            
        Returns:
            bool: True if all steps successful
        """
        # Validate folder path
        try:
            folder_path = Config.validate_folder_path(folder_path)
        except ValueError as e:
            print(f"Error: {e}")
            return False
        
        # Use folder name as repo name if not specified
        if repo_name is None:
            repo_name = folder_path.name
        
        # Check if git is installed
        self.git_ops.check_git_installed()
        
        # Check if already a git repo
        if not self.git_ops.is_git_repo(folder_path):
            if not self.git_ops.init_repo(folder_path):
                return False
        
        # Create .gitignore
        self.git_ops.create_gitignore(folder_path)
        
        # Create LICENSE file if specified
        if license_key and license_key != 'None':
            LicenseTemplates.create_license_file(folder_path, license_key, license_author)
        
        # Add and commit
        if not self.git_ops.add_all_files(folder_path):
            return False
        
        if not self.git_ops.commit(folder_path, commit_message):
            return False
        
        # Create GitHub repository
        repo = self.github_api.create_repository(repo_name, description, private, license_key)
        if repo is None:
            return False
        
        # Add remote and push
        repo_url = self.github_api.get_authenticated_repo_url(repo)
        
        if not self.git_ops.add_remote(folder_path, repo_url):
            return False
        
        if not self.git_ops.rename_branch(folder_path, 'main'):
            return False
        
        if not self.git_ops.push(folder_path, 'main'):
            return False
        
        print(f"\nRepository created: {repo.html_url}")
        
        return True


def main():
    """Main entry point for the CLI."""
    # Get and validate GitHub token
    github_token = Config.validate_github_token()
    
    # Get folder path from command line or prompt
    folder_path_str = Config.get_folder_path_from_args()
    
    # Validate folder path first to get the Path object
    try:
        folder_path = Config.validate_folder_path(folder_path_str)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Get repository name
    repo_name = Config.get_repo_name_from_args(folder_path)
    
    # Get description
    description = Config.get_repository_description()
    
    # Get privacy preference
    private = Config.get_private_repo_preference()
    
    # Get license preference
    license_key, license_author = Config.get_license_preference()
    
    try:
        # Create automation instance and run
        automation = GitHubAutomation(github_token)
        success = automation.automate_full_workflow(
            folder_path=folder_path,
            repo_name=repo_name,
            description=description,
            private=private,
            license_key=license_key,
            license_author=license_author
        )
        
        sys.exit(0 if success else 1)
            
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

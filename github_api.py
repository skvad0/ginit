"""
GitHub API Module
Handles all GitHub API operations including repository creation.
"""

from github import Github, GithubException


class GitHubAPI:
    """Handles all GitHub API operations."""
    
    def __init__(self, github_token):
        """
        Initialize GitHub API client with a personal access token.
        
        Args:
            github_token: GitHub personal access token with repo scope
        """
        self.github_token = github_token
        self.github_client = Github(github_token)
        self.user = self.github_client.get_user()
    
    def get_username(self):
        """
        Get the authenticated user's username.
        
        Returns:
            str: GitHub username
        """
        return self.user.login
    
    def create_repository(self, repo_name, description="", private=False, license_key=None):
        """
        Create a new GitHub repository.
        
        Args:
            repo_name: Name of the repository
            description: Repository description
            private: Whether the repo should be private
            license_key: License template key (e.g., 'MIT', 'Apache-2.0')
            
        Returns:
            Repository object or None if failed
        """
        try:
            print("Creating GitHub repository...", end='', flush=True)
            
            # Map license keys to GitHub's license templates
            github_license_map = {
                'MIT': 'mit',
                'Apache-2.0': 'apache-2.0',
                'GPL-3.0': 'gpl-3.0',
                'BSD-3-Clause': 'bsd-3-clause',
                'BSD-2-Clause': 'bsd-2-clause',
                'ISC': 'isc',
                'Unlicense': 'unlicense'
            }
            
            license_template = github_license_map.get(license_key) if license_key and license_key != 'None' else None
            
            repo = self.user.create_repo(
                name=repo_name,
                description=description,
                private=private,
                auto_init=False,
                license_template=license_template
            )
            print(f"\rCreated repository: {repo_name}")
            return repo
        except GithubException as e:
            if e.status == 422:
                print(f"\rRepository '{repo_name}' already exists")
            else:
                print(f"\rFailed to create repository: {e.data.get('message', str(e))}")
            return None
    
    def get_authenticated_repo_url(self, repo):
        """
        Get repository clone URL with authentication token embedded.
        
        Args:
            repo: Repository object
            
        Returns:
            str: Authenticated clone URL
        """
        return repo.clone_url.replace('https://', f'https://{self.github_token}@')
    
    def repository_exists(self, repo_name):
        """
        Check if a repository already exists for the authenticated user.
        
        Args:
            repo_name: Name of the repository to check
            
        Returns:
            bool: True if repository exists
        """
        try:
            self.user.get_repo(repo_name)
            return True
        except GithubException:
            return False

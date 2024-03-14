# filename: furl_issues.py
from github import Github

# Ask the user for the repository name
repo_name = input("Enter the name of the GitHub repository: ")

# Authenticate with GitHub using a personal access token
token = input("Enter your GitHub personal access token: ")
g = Github(token)

# Get the repository
repo = g.get_repo(repo_name)

# Fetch all issues from the repository
issues = repo.get_issues(state='all')

# Serialize the issues into a markdown document
markdown_content = ""
for issue in issues:
    markdown_content += f"# Issue #{issue.number}: [{issue.title}]({issue.html_url})\n"
    markdown_content += f"- Labels: {' '.join([label.name for label in issue.labels])}\n"
    markdown_content += f"- Created At: {issue.created_at}\n"
    markdown_content += "- Status: " + ("Open" if issue.state == 'open' else "Closed") + "\n\n"
    markdown_content += f"{issue.body}\n\n"

# Save the markdown content to a file
with open("furled_issues.md", "w") as file:
    file.write(markdown_content)

print("Issues have been furled and saved to furled_issues.md")
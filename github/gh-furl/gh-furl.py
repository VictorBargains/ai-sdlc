# gh-furl.py
## placeholder version only works on public repos and only naively summarizes issue headers

from github import Github

# First create a Github instance:

# TODO: find access token in environment variable or other configuration management
g = Github("<access_token>")


# TODO: find local repo name via package.json or other file scanning (can glob do the equivalent of closest in the DOM? -- starting at current directory, find the first package.json file in current or parent, recurseively)
# could also check git remote -v and parse the output to find the repo name
repo = g.get_repo("<repo_full_name>")

issues = repo.get_issues(state='open')
for issue in issues:
  print(f"# [{issue.title} #{issue.number}]({issue.html_url})")
  print(f"- Labels: {', '.join([label.name for label in issue.labels])}")
  print(f"- Created At: {issue.created_at}")
  print(f"- Status: {'Closed' if issue.closed_at else 'Open'}")
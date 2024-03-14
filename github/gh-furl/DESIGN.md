# DESIGN.md for Issues-Furler Tool

## Overview

The `issues-furler` tool is a proof of concept designed to authenticate with a GitHub repository and serialize all of its issues into a single markdown document. This tool leverages PyGithub for authentication and issue retrieval, focusing on simplifying issue management and overview.

## Goals

- Authenticate with GitHub and identify the associated repository, defaulting to the repository defined in the closest `package.json` file or other repository identification methods within the filesystem.
- Fetch all issues from the specified repository using PyGithub.
- Serialize the issues into a markdown document, following a structured format for readability and consistency.

## Design Requirements

1. **Authentication**: Implement secure GitHub authentication, supporting both personal access tokens and OAuth tokens where applicable.
   
2. **Repository Identification**: Automatically detect the repository's details from the project's directory, with fallback options for manual specification.

3. **Issue Serialization**: Format each GitHub issue into a markdown section, including metadata such as title, labels, and issue URL.

## Markdown Format for Issues

Each issue will be represented as a heading in the markdown document, followed by optional metadata lines. The format for a "furled issue heading" will closely resemble:

```
# [Issue Title #issue_id](issue_url)
- Labels: `label1`, `label2`
- Created At: YYYY-MM-DD
- Status: Open/Closed
```

This format ensures that each issue is easily identifiable and that critical information is immediately accessible.

## Implementation Suggestions

- **PyGithub**: Utilize the PyGithub library for all interactions with the GitHub Issues API, including authentication and data retrieval.
- **Filesystem Scanning**: Implement logic to search for `package.json` or other indicators of repository information within the project directory.
- **Markdown Generation**: Develop a module to convert issue data into the specified markdown format, ensuring consistency and readability.

This reduced design focuses on establishing a foundational tool for issue management within GitHub repositories, prioritizing simplicity and functionality for the proof of concept.
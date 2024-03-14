# DESIGN.md for GH-Furling System

## Overview

The GH-Furling system is designed to bridge the gap between GitHub's project management capabilities and local development workflows, allowing users to interact with GitHub projects, issues, and milestones through a markdown-based interface. It consists of two primary components: `gh-furl` for pulling data from GitHub into a markdown document, and `gh-unfurl` for parsing markdown documents to apply updates to GitHub.

## Design Requirements

1. **Programmatic GitHub API Access**: The system must have a programmatic way to access both the GitHub Issues API and the GitHub Projects API. The Issues API is accessible via REST, and the Projects API is available through GitHub's CLI and GraphQL.
   
2. **Modular Architecture**: The system should be designed with a modular approach, allowing for separate handling of authentication, project management, and issue management functionalities.

3. **Markdown Compatibility**: It must support generating and parsing markdown documents to facilitate the translation between GitHub project/issue data and a readable or editable markdown format.

4. **Natural Language Processing**: Capability to parse natural language instructions within markdown for translating into GitHub actions, enabling intuitive project management interactions.

## Implementation Suggestions

- **PyGithub Utilization**: For REST API interactions, particularly with issues, consider leveraging the PyGithub library, which already provides comprehensive support for GitHub's REST API.
  
- **GraphQL for Projects API**: Explore direct GraphQL queries or extending PyGithub to handle project management tasks, as current official support via REST API is limited.

- **Markdown Specification**: Develop a detailed specification for the markdown format that includes explicit sections and metadata for projects, issues, and tasks, ensuring clarity and ease of parsing.

- **NLP Library Integration**: Incorporate existing NLP libraries to interpret and process natural language commands within the markdown documents.

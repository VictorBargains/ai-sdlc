# PLANNING.md for GHMD-Furling System

## Overview

This document outlines the development plan and milestones for the GHMD-Furling system, which aims to integrate GitHub's project and issue management with a markdown-based documentation system.

## Development Plan

The development plan adopts a progressive enhancement approach, focusing on establishing a minimum viable product (MVP) that handles GitHub issues first before expanding to include project integration.

### Phase 1: MVP for GitHub Issues

**Objective**: Demonstrate the ability to authenticate with GitHub, connect to a specified repository, and dump all relevant issue data into a markdown file.

#### Milestones

1. **GitHub Authentication Module Development**: Implement the `gh-auth` module to handle secure OAuth authentication with GitHub.

2. **GitHub Issues Module Development**: Develop the `gh-issues` module using PyGithub to fetch and process issue data from the GitHub REST API.

3. **Markdown Generation for Issues**: Create functionality within `gh-issues` to format fetched issue data into a structured markdown document.

4. **Prototype Testing**: Test the MVP with a real GitHub repository to ensure accurate fetching, processing, and markdown generation of issue data.

### Phase 2: Project Integration

**Objective**: Extend the system to include GitHub project data, incorporating project boards, milestones, and labels into the markdown documentation.

#### Milestones

1. **Feasibility Study**: Research and decide whether to extend PyGithub with GraphQL capabilities or develop a separate module for interacting with the GitHub Projects API.

2. **GitHub Projects Module Development**: Based on the feasibility study, develop `gh-projects` to handle project data fetching and processing.

3. **Markdown Enhancement for Projects**: Update the markdown generation logic to include project data alongside issue information.

4. **Integration and Testing**: Integrate project management features with the existing issue management functionality and test with real-world data.

### Progressive Enhancement

After establishing the MVP and integrating project management features, the system will be iteratively enhanced with additional functionalities such as:

- Natural language processing for updating GitHub issues and projects via markdown documents.
- User confirmation workflows for applying changes to GitHub.
- Advanced markdown formatting options for better documentation customization.

## Development Tools and Technologies

- **Python**: Primary programming language for module development.
- **PyGithub**: Leveraged for GitHub REST API interactions.
- **GraphQL**: For accessing GitHub's Projects API, if extending PyGithub or developing a new module.
- **NLP Libraries**: For parsing and executing natural language instructions within markdown documents.

This plan lays the foundation for the GHMD-Furling system, ensuring a structured approach to development and the achievement of key objectives through well-defined milestones.
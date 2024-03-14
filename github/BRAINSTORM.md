# MD-SDLC Github Tools Brainstorming

User
Okay. Now I would like to design a related tool which can connect to a GitHub account, interact with the projects and issues APIs, and then create a "furled version" of the project management artifacts and issues.

Issues deal with core task information such as which repository, user, milestone, and labels a particular issue is attached to. The project management system adds task status, kanban boards, and iterations (AKA sprints).

Once again there will be a pair of tools: one which pulls data from GitHub to generate a furled summary of a project and its issues; and one which can take natural language instructions about project, design, and task updtaes, and translate them into a set of discrete mutations to the GitHub project/issues (with confirmation from a human that the changes are correct before they are applied).

GPT
Designing a toolset to interface with GitHub's project and issues APIs, and manage project management artifacts in a "furled" markdown format, involves creating two distinct tools: one for pulling data from GitHub to generate summaries, and another for interpreting natural language instructions into GitHub actions. Here's a proposed design for these tools:

GitHub Furler (GitHub-to-MD): This tool authenticates with a user's GitHub account, accesses specified repositories, and pulls project management artifacts such as issues, milestones, labels, kanban boards, and sprint data. It then generates a furled markdown document summarizing this information. The document would include sections for each project aspect, utilizing metadata headers for organization and clarity.

GitHub Unfurler (MD-to-GitHub): This tool takes a markdown document containing project updates, task descriptions, or modifications in a structured format and parses it to identify actionable items. Using natural language processing, it translates these items into discrete mutations (create, update, close issues; update project boards, etc.) for a GitHub project. Before applying any changes, it would generate a summary of proposed mutations for user review and confirmation.

Key Features and Considerations:
Authentication and Security: Both tools must securely authenticate with GitHub, likely using OAuth tokens, to access and modify user data.
API Rate Limiting: Handle GitHub API rate limits gracefully, possibly by queuing actions or notifying the user of delays.
Error Handling: Robust error handling for API failures or conflicts (e.g., trying to update a closed issue).
Confirmation Workflow: For the Unfurler, a clear and concise summary of proposed changes should be presented to the user for confirmation, preventing unintended actions.
Documentation and Help: Include detailed documentation within the markdown on how to structure updates or tasks for the Unfurler, aiding both human and AI in creating compatible documents.
These tools would offer a novel way to bridge detailed project management activities on GitHub with a more narrative, human-readable format, potentially improving collaboration and project oversight.

User
Okay. let's go with ghmd-furl and ghmd-unfurl as names for now.  This makes it clear it mediates between github and markdown. Let's also identify core components which can be shared across both, such as an abstraction around the github auth and api layers. The issues system has a REST API but as far as I know, the only way to interact with the Projects system on GitHub is through their `gh` CLI tool using a graphql query.

https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects

https://docs.github.com/en/rest/issues?apiVersion=2022-11-28

I don't know if the sum total of all issues endpoints are exposed through their REST API, or if some operations would require using the CLI for an issue and not just for a project. Similarly, I do not know whether there are future plans to provide a Projects API -- Projects is a much newer system, so the focus on CLI+GraphQL instead of REST might be an intentional choice about modernizing tech, or it might just be that Projects are too young for them to have prioritized the REST API yet.

Given these unknowns, and the complexity of access for these online integrations, it seems we should be aiming for maximum decoupling. Under the project of "ghmd-furling" we may have multiple sub modules -- not only the furl and unfurl tools which the end user would interact with, but many sub tools composed together into those tools:
- a configuration management module covering program options and github auth + integration info
- a module which can authenticate with and issue commands to and report output from the GitHub CLI (for now, only for project-level data)
- A similar module which can interact with GitHub REST APIs (for now, only for issue-level data)
- a module which can turn natural language instructions into a set of commands that might be routed to any of the other github modules, which may be implemented as something like autogen which uses a series of agents with tools.

Can you think of any other module boundaries we might want to draw here? Let's summarize the modules we think we will need, and the technologies they could use.
GPT
For the ghmd-furling system, considering the various interactions with GitHub's APIs and the need for modularity, here are some proposed module boundaries along with the technologies they could use:

GitHub Authentication Module: Handles OAuth authentication and token management with GitHub. Could use Python's requests library for HTTP requests and a secure storage mechanism for tokens.

GitHub CLI Interaction Module: For interacting with GitHub's GraphQL API via the gh CLI, especially for project management features not available in the REST API. This could rely on Python's subprocess module to execute CLI commands and parse their output.

GitHub REST API Module: Interfaces with GitHub's REST API for issues, comments, labels, and more. This could use the requests library for making HTTP requests to the GitHub API.

Natural Language Processing Module: Translates natural language instructions into actions that can be performed via the GitHub API or CLI. This might leverage machine learning libraries like transformers for understanding and parsing natural language inputs.

Configuration Management Module: Manages user settings, GitHub integration details, and application preferences. Could be built with Python's configparser or similar libraries for managing configuration files.

Markdown Processing Module: For generating and parsing markdown documents that represent the GitHub project management artifacts. This module might use libraries like markdown2 or Mistune for markdown processing.

Command Routing Module: Determines which actions to take based on natural language instructions or markdown document structure, routing commands to the appropriate GitHub interaction modules. This could be implemented with a custom Python dispatcher or command pattern implementation.

User Interaction and Confirmation Module: Manages user interactions for confirming proposed changes before applying them to GitHub. This could include simple CLI interfaces or more complex GUIs using libraries like Tkinter (for standalone applications) or web frameworks like Flask (for web-based interfaces).

These modules, together, form a comprehensive system that is flexible, extendable, and capable of handling the complexities of interacting with GitHub's project and issue management features while also being user-friendly and accessible.

User
There does seem to be a pygithub module but it only claims to interact with the REST API. https://github.com/PyGithub/PyGithub
We probably still need to access the `gh` CLI for project management tasks, but perhaps it could be done through a GraphQL connection without the CLI. If PyGithub is open source, it may be wise to create a branch or fork of pygithub which can also perform GraphQL operations in addition to REST. This could then be contributed back to the community as a pull request.
GPT
Creating a branch or fork of PyGithub to add GraphQL capabilities for project management tasks, in addition to its existing REST API functionalities, is an excellent idea. This enhancement would significantly improve the tool's utility for developers needing comprehensive GitHub automation, including those features only accessible via GraphQL. Contributing such extensions back to the community as a pull request aligns well with open-source principles, fostering collaboration and expanding the tool's usefulness. This approach would also streamline ghmd-furling system development by consolidating GitHub interactions within a single Python library.


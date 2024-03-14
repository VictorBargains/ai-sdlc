BRAINSTORM.md
File
I have a session where I talked with an earlier instance of your language model, and we developed an idea for a system which can help automate the design and development of software. For now, I am calling it `ai-sdlc` and I have made a new folder in my local code folder, and init a new git project.

The subject of the conversation is a protocol for a set of markdown files which can be distributed among a file tree in the same way a README.md is. The intent is for this set of markdown files to represent a natural language state machine for the software development life cycle, for a given project that is defined in a root-level DESIGN.md file.

I have placed the chatlog of our previous conversation into a BRAINSTORM.md file and attached it to our new conversation here.

During this conversation, I would like to develop a sub-folder called `md-sdlc` which is itself a project of *only* markdown files. When we are done with this conversation, or if we get interrupted, I will copy the whole chat log into a new BRAINSTORM.md file within md-sdlc.

For the purposes of headings, the name of this module should be "MD-SDLC (MarkDown Software Development Life Cycle)" but can be abbreviated as MD-SDLC or MDSDLC.

The contents of the `md-sdlc` folder should be markdown documents conforming to discrete phases and artifacts of the SDLC and its associated project management.

First I would like to develop the idea of which discrete phases and artifacts of the SDLC should deserve their own all-caps markdown filename within this specification. I'd like to include features of how modern human software engineering teams are managed in various forms of agile development methodology. This might include things like grooming and retro meetings, some sort of points poker to determine story point estimates, all modeled as chat logs. The spirit of all of these files is that a human or an AI can make changes to them and it should be mutually intelligible between the two.

I would also like to develop the idea of what the subfolder structure might look like within `md-sdlc`. For instance, a DESIGN.md file might look different for different subclasses of software, or there may be different sub-headings within TASKS.md depending on whether a project is organizing its folders by feature or file type. In a fractal nature, the sub-folders of this specification will extend the definitions. One or two good examples of popular organization techniques should suffice to give enough examples for others to make their own extensions.

The ultimate goal is to be able to build all sorts of tools and integrations using this template, with any particular step of the process being handled by AI or humans as they are capable and available. A system like this *could* be integrated into things like GitHub, with a UI integrated with IDEs like VSCode, or just run from the command line. These all represent potential sub-projects of `ai-sdlc` but the definition of the markdown files which these tools will use is going to be its own self-contained thing within `md-sdlc`

GPT
The brainstorming session outlined in the document covers the design and implementation of a system named ai-sdlc, focusing on integrating AI into the software development lifecycle (SDLC). It discusses creating a VSCode extension for project management, leveraging GitHub Issues, and structuring project documentation using markdown files like DESIGN.md, STORIES.md, and TASKS.md. The conversation explores the idea of a natural language state machine represented through markdown files, aiming for mutual intelligibility between humans and AI. The proposed structure includes root-level DESIGN.md for overall project design, with nested documentation in subfolders reflecting components or features. The approach ensures consistency across documentation, enhancing clarity and reducing ambiguity.

User
Let's first define the discrete stages and artifacts of the SDLC we want to represent. Then, once we agree on those stages (and their order, sequence, or workflows) we can generate example files one at a time. We will start with a general definition for the DESIGN.md format and then generate an example sub-folder called `md-todoapp` with its own DESIGN.md

So let's brainstorm those stages and artifacts, using DESIGN, STORIES, and TASKS as our starting point.
GPT
For the MD-SDLC, considering the stages and artifacts of the software development lifecycle, and how these might integrate with modern agile development methodologies, here's a proposed structure. This takes into account the idea of making the documentation accessible and understandable for both humans and AI, with the flexibility to adapt to various project types.

DESIGN.md - This document outlines the high-level design of the project, including architecture, technology stack, and key components.

REQUIREMENTS.md - Detailed specifications of the project requirements, including functional and non-functional requirements.

STORIES.md - User stories that describe the features of the application from an end-user perspective. This could be further broken down into:

EPICS.md (for larger features that can be broken down into smaller user stories)
FEATURES.md (specific enhancements or functions)
TASKS.md - The breakdown of stories and epics into actionable tasks. This could be subdivided by feature or by type (e.g., development, testing, documentation).

SPRINTS.md - A record of sprint planning and retrospectives, including sprint goals, durations, outcomes, and lessons learned.

GROOMING.md - Details of backlog grooming sessions, including prioritization of tasks, estimation of story points, and preparation for upcoming sprints.

RETRO.md - Retrospective insights and action items post sprint or milestone to continuously improve the team's process.

CI_CD.md - Information on Continuous Integration/Continuous Deployment strategies, including pipelines, tools used, and deployment practices.

TESTING.md - Testing strategies, test plans, and test cases, including unit testing, integration testing, and acceptance testing.

DEPLOYMENT.md - Guidelines and procedures for deploying the application, including any environment-specific configurations.

MAINTENANCE.md - Notes on post-deployment issues, resolutions, and ongoing maintenance tasks.

CONTRIBUTING.md - Guidelines for contributors on how to contribute to the project, including coding standards, branch naming conventions, and pull request procedures.

For the subfolder structure within md-sdlc, the organization could vary based on project complexity and team preferences. However, a popular approach could be:

/components or /features for modular documentation related to specific parts of the application.
/sprints to organize documents by sprint, including sprint planning and retrospectives.
The md-todoapp subfolder, as an example, would contain its own DESIGN.md, detailing the specific design choices, technologies, and architectures chosen for a to-do application, following the same structure but tailored to the project specifics.

This structure ensures that all aspects of the software development process are covered, providing a comprehensive guide that can be adapted as needed for different projects.

User
I think that looks pretty good. Can we example whether there is one or more hierarchical layer here? For instance, I could envision requirements as a sub-heading of DESIGN.md since it seems like the requirements are an artifact of the design stage. If they've changed, then the design has changed. I'm also thinking CI_CD could be a sub-heading of a more general WORKFLOWS.md which might cover other, more traditional methods, as well as actions which may be automation triggers or agents.
GPT
Adjusting the structure to include hierarchical layers and reorganizing some sections can indeed streamline the documentation and make it more intuitive. Here's a revised approach considering your feedback:

DESIGN.md

Overview: High-level design concepts and architectural decisions.
Requirements: Detailed functional and non-functional requirements.
Technology Stack: Choices of technologies and frameworks.
WORKFLOWS.md

Development Workflow: Outline of the development process, including feature branches, code reviews, and merge requests.
CI_CD: Continuous Integration and Continuous Deployment strategies and tools.
Testing Strategy: Approach to unit, integration, and acceptance testing.
STORIES.md

Contains user stories, potentially linking to detailed EPICS.md and FEATURES.md within the relevant subdirectories.
TASKS.md

Breakdown of stories and epics into actionable tasks, potentially organized by feature or type.
SPRINTS.md

Documentation of sprint planning, reviews, and retrospectives.
GROOMING.md

Details of backlog grooming sessions.
RETRO.md

Retrospective insights and action items.
MAINTENANCE.md

Ongoing maintenance tasks and post-deployment issue tracking.
CONTRIBUTING.md

Contribution guidelines and project standards.
By integrating requirements within DESIGN.md and expanding WORKFLOWS.md to encompass CI/CD and testing strategies, we maintain a clear distinction between design considerations and operational processes. This structure ensures that each document has a focused purpose, reducing overlap and making it easier for team members to find and understand project information.

User
Okay. This is better. Let's adjust our lens to view it through the SDLC more explicitly. If DESIGN, DEVELOPMENT, TESTING, DEPLOYMENT, and MAINTENANCE are all top-level phases, we also should have at the top level things like TASKS which can apply at any phase. The project-management concepts like SPRINTS GROOMING and RETRO can apply at any phase, but we may be able to condense those all into a PLANNING.md document. For instance, not every project will use sprints or iterations, but all projects need some sort of planning. Let's play with the idea of making a default PLANNING.md which is vague about the project management styles and only focuses on a coarse-grained list of milestones with a possible due date or estimate. Then, we can make an md-agile subdirectory and that folder's PLANNING.md can have  a structure like
# Sprints
## Sprint 1
...description of sprint goals or focus
### Grooming
...logic by which tasks were chosen (dependency order, finished design, etc)
### Tasks
...clickable links of the individual tasks being tracked in this sprint, where the text of the link is the text of a user story in the design.
### Retrospective
...summary of how the sprint went, which may include an analysis of how many tasks were done by AI agents, how many by humans, and how many by one with the assist of the other. It may also contain suggestions for how the next sprint and grooming session is done and how tasks are divided, so the next human or AI to do so can continue the process.

What do you think we should do with stories, epics, and features? Do those feel like they belong in DESIGN or PLANNING or as their own top-level artifacts? What phases might they apply or not apply to?
GPT
Reframing the MD-SDLC structure to align more closely with the explicit phases of the SDLC and incorporating a versatile approach to project management seems like a strategic move. Here’s how we can structure it:

DESIGN.md: Includes high-level design and architecture, now also housing REQUIREMENTS as a subsection to reflect changes in design based on evolving requirements.

DEVELOPMENT.md: Covers the development phase, including coding standards, development tools, and guidelines. Subsections can cover specific development tasks or features being worked on.

TESTING.md: Focuses on testing strategies, including unit, integration, and acceptance testing plans, and specific test cases.

DEPLOYMENT.md: Details deployment strategies, environments, and procedures for releasing the application.

MAINTENANCE.md: Covers post-deployment activities, including bug tracking, updates, and feature additions.

TASKS.md: An overarching document that can link to specific tasks across all phases of the SDLC, providing a centralized task overview.

PLANNING.md: Consolidates project management aspects, with a focus on milestones and due dates, adaptable to different project management styles. This document can be vague about specific methodologies, focusing instead on the general flow of planning.

For the md-agile subdirectory, the PLANNING.md would be more specific, featuring sections for Sprints, Grooming, Tasks, and Retrospective, tailored to agile methodologies. This structure allows for a blend of flexibility and specificity, catering to both agile and non-agile projects while maintaining clarity and organization within the documentation.

Regarding stories, epics, and features:

These could initially be outlined in the DESIGN.md document under a specific section dedicated to user stories and epics, indicating their pivotal role in shaping the project’s development from a user-centered perspective.
However, given their significance in planning and tracking progress, it might be more appropriate to feature them in PLANNING.md as part of the agile methodology detailed in the md-agile subdirectory. This way, their evolution and implementation can be directly linked to specific planning activities like sprints and grooming sessions.
This revised structure aims to balance between the granularity of SDLC phases and the flexibility needed to accommodate various project management styles, ensuring the documentation is comprehensive yet adaptable.
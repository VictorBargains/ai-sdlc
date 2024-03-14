# PyGithub Research

We would ultimately want to use PyGithub for project-level concerns (which require GraphQL access) and not just issues-level (which PyGithub exposes through the GitHub REST API). It will probably be necessary to extend pygithub to achieve this, but the work may not be too far off.

There is an existing issue on their github which asks for a certian graphql feature, and now a comment has been posted to say there is now a branch with a GraphQL call.

Issue comment: https://github.com/PyGithub/PyGithub/issues/2567#issuecomment-1842963772
Diff of commit adding graphql mutation: https://github.com/PyGithub/PyGithub/commit/232df79a2947dc96363bdc6f51a6f446ff2b241f#diff-90017b18548bd848900b7cffd7fe86a610dc20e5d228663dfb429a47cdf65a20R767-R772
PR which was merged: https://github.com/PyGithub/PyGithub/pull/2816

By examining that PR and the Pygithub codebase, it should be possible to make the additions we need to access project data.

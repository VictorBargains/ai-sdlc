# AI-SDLC (Artificial Intelligence Software Development Life Cycle)

This repository contains the designs and code for an AI Capabilities Research Project ocodenamed `ai-sdlc`. This project is a work-in-progress and is currently in its very early stages. As such, it may not function as expected and any effectiveness at its intended tasks should not be assumed.

AI-SDLC is being developed in a hierarchical, fractal, modular pattern. Since this project is centered around Large Language Models, much of the "code" will actually be in natural language. Markdown is being chosen as the format of choice due to its innate ability to be parsed by humans and LLMs in equal measure.

Especially in the early stages, most of this repository will consist of design documents, and attempts to capture the development process in a similar format.

### BRAINSTORM.md

This file represents a raw chat log between (usually) a human and a large language model. It can be given as context to either type of agent when starting any particular task about solidifying the design.

Here are the links to the `BRAINSTORM.md` documents in each of the project's current layers:

- [Root AI-SDLC Brainstorming](./BRAINSTORM.md)

- [GitHub Access](./github/BRAINSTORM.md)
  - [GitHub Project Management with Autogen](./autogen/gh-proj-mgmt/BRAINSTORM.md)

- [SDLC Markdown Specifications](./md-sdlc/BRAINSTORM.md)
  - [File Furling](./furling/BRAINSTORM.md)

### DESIGN.md

This file should be the end result of the brainstorming process, or something that uses the BRAINSTORM.md as input and engages with the user to develop the final design. It should be iterated on to define the full feature set before planning the development.

Here are the links to the `DESIGN.md` documents in each of the project's current layers:

- [Furling](./furling/DESIGN.md)
- [GitHub Access](./github/DESIGN.md)
  - [GitHub Issues Furling](./github/gh-furl/DESIGN.md)


### Bootstrapping via Markdown

This pattern of naming documents after the various stages of the software development lifecycle is the general pattern that this repo will follow for now.

This project will heavily rely on AI bootstrapping so the LLMs will be generating their own design documents and their own development plans, etc.

## Autogen

This project makes use of [Autogen](https://microsoft.github.io/autogen/), a multi-agent LLM framework from Microsoft.

## License

Given that Autogen is licensed under the MIT License, this project will also use the MIT License for consistency and to ensure compatibility.

## Disclaimer

This project is a research project and is not guaranteed to function as expected. It is in its early stages and any effectiveness at its intended tasks should not be assumed. Use at your own risk.

## MIT License

```
MIT License

Copyright (c) 2024 Victor B Andersen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# DESIGN.md for MD-Furling System

## Overview

The `md-furling` system comprises two primary tools: `md-furl` and `md-unfurl`. These tools are designed to serialize and deserialize file structures into a markdown format (`md`), facilitating a smooth transition between nested file structures and a single, human-readable document. This system aims to make it easy for both humans and machines to parse and reconstruct file hierarchies.

## Goals

- **Lossless Transfer**: Ensure a lossless transition of file information between the serialized markdown format and the original file structure.
- **Human and Machine Parseability**: Create a format that is easily understandable by both humans and machines, enabling processing by NLP or traditional pattern matching.
- **Flexibility**: Support various levels of nesting within the file structures without losing information or readability.


## Design Requirements
-
- A "furled document" consists of one or more files represented as a series of file heading and content pairs, with an optional header section of its own.
- The process of furling means to serialize one or more files into this "furled" document format.
- The process of unfurling means to deserialize a furled document back into its component files with maximum fidelity.

### Document Metadata
- The start of a furled document, before the first file heading, can contain arbitrary metadata in markdown format.
- The heading of a furled document is encouraged to contain a summary of these furling and unfurling specifications which were used in the construction of the furled document.
- The metadata at the top of a furled document should serve as instructions to either a language model or a human on how to unfurl the files.
- As this standard evolves, it may be prudent to record a specification version number used, or itemize the explicit axioms of the protocol at the top.
- Additional metadata may include a root path to use when 

### File Headings
- A "furled file heading" is a multiline pattern which starts with one or more `#` (markdown heading) characters indicating its depth level, is then followed by a space and a markdown link whose URL ends with the label name, and which terminates in two newlines.
- The first line of the file heading contains a link to the path or subpath at which the file should be unfurled to.
- In order to qualify as a furled file heading, and not just a normal markdown heading, the contents of the heading should just be a link, and that link's URL should end with the link label.
- For files whose names are unique within a set of furled files (like FooBarView.js), only the file name will be shown in the label of the link.
- For files whose names are not unique within a set of furled files (like /src/components/foo/views/index.js and /src/components/bar/views/index.js) then the shortest unique subpath should be used as the link label rather than just the filename (in this case those subpaths would be foo/views/index.js and bar/views/index.js).

### File Metadata
- File headings can optionally include additional lines before the double newline to add file metadata to be set when unfurling.
- File metadata is optional, and any fields not set will use filesystem defaults.
- Since many filesystems may use different names or values for metadata, this part of the system is not guaranteed to be lossless.
- If metadata is set for a furled file, the system should try to set as much of that metadata when the file is unfurled.
- As a general rule, a list of metadata should be in a `Key: value` format similar to email headers, but they may be annotated with markdown bullet points or subheadings to taste.
- Boolean properties like Read-Only or Executable can be fully specified with both a key and a value, but can also be specified as just their key to imply true.
- The absence of one of those boolean properties does not mean that it should be set to false; Instead it should be ignored completely when unfurling, leaving it to the local filesystem default value.
- Some metadata might have more than one level of specificity, such as unix file permissions where the executable bit can be set at 3 different levels. In a case like this, "Executable" without being more specific could mean executable by all levels, where as "User Executable" or "Group Executable" could result in a more specific permission set.

### Nesting Headings and Depth Rewriting
- Files being furled into one document will be scanned to see if they contain existing furled file headers, and if so all those headers will be increased by one depth level.
- When being unfurled from a document, before being saved into their own files, their content will be scanned and all furled file headers will be decreaed by one depth level.
- Precision pattern matching should be used to ensure that *only* those markdown headings which match the furled file heading pattern should have a `#` added or removed from them during this depth adjustment process.
- The process of furling or unfurling will happen only one level at a time, and when unfurling a document only the topmost level headings will be unfurled into files.
- A document being unfurled should be split at file headings only if they have the same heading depth as the topmost heading (presumably level 1 `#`), but all other heading levels should be scanned for decrease.


## Examples

### Metadata Headers

- Each file section starts with a metadata header, using a key-value format for attributes like creation date, modification date, and file permissions.
- Example of a file metadata header:
  ```md
  # [path/to/example/Example.py](Example.py)
  * Created: 2022-05-17
  * Last Modified: 2023-03-02
  * Executable
  * Read-Only
  ```

### Natural Language Header

- Include a natural language header in furled documents, explaining the document's structure and providing enough information for an LLM to unfurl it correctly.
- Example of a natural language header:
  ```
  This document is a serialized representation of a file structure, using markdown for readability and parseability. Each section represents a file or folder, indicated by markdown headings. A file heading consists of a normal markdown `#` heading that contains a filename as a link, with the URL being the full (absolute or relative) path to the file, as it was before it was furled, or as it should be after it is unfurled. Optional metadata for each file is provided as additional key-value pairs or boolean flags following the file heading immediately on the next line. Two newlines separate the contents of each file from the headers before and after it. Text before the first file header is metadata about the entire set of furled files and the furling process itself. When a document is unfurled, only the top level of file headings will be processed. As each file is unfurled, any headings at a depth greater than 1 will be reduced by 1 depth level (one less `#` at the start of its line). The inverse will be true of furling files that already contain furled file headers -- their depth number will be increased by 1 (one more `#` at the start of its line). Ensuring this process is done properly will prevent the need for additional escaping or nesting logic.
  ```

## Use Cases

- **Collaborative Editing**: Simplify the process of sharing complex file structures for collaborative editing or review.
- **Version Control**: Provide a human-readable format for tracking changes in file structures over time.
- **AI Processing**: Enable AI tools to parse and manipulate file structures using natural language processing techniques.

## Challenges and Solutions

- **Handling Deep Nesting**: Use dynamic depth rewriting to ensure readability without losing the hierarchical structure.
- **Escaping Mechanism**: Avoid the need for escaping by leveraging markdown syntax and careful design of the serialization format.

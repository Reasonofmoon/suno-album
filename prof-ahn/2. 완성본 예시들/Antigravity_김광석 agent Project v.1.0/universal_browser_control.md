---
description: Universal protocols for invoking the Antigravity Browser Control for various agentic tasks.
---

# Universal Browser Control Protocols

This document establishes the standard "Universal" interface for invoking the `browser_subagent` across different agentic domains. Any specialized agent (Search, Academic, Shopping, etc.) should follow these patterns to ensure consistent, reliable browser automation.

## Core Principle: Unconditional Invocation
When a task requires real-time information, verification, or interaction with web content, the agent **MUST** invoke the `browser_subagent`. Do not rely solely on internal knowledge for dynamic data.

---

## 🔍 Protocol A: The "Intelligence Scout" (General Search)
**Use Case**: Breaking news, current events, fact-checking, general knowledge gathering.

### Standard Invocation
**TaskName**: `Fetching External Intelligence: [Topic]`
**Task Payload**:
```text
1. Navigate to 'https://www.google.com'.
2. Search for '[User Query]'.
3. Analyze the top 5 search results.
4. Extract key facts, dates, and summaries related to '[Specific Focus]'.
5. Return a synthesized summary of the findings, citing sources where possible.
```

---

## 🎓 Protocol B: The "Scholar" (Academic Research)
**Use Case**: Finding papers, citations, technical specifications, or deep research.

### Standard Invocation
**TaskName**: `Academic Literature Search: [Topic]`
**Task Payload**:
```text
1. Navigate to 'https://scholar.google.com' (or 'https://arxiv.org').
2. Search for '[Keywords]'.
3. For the top 5 relevant papers:
    - Extract Title, Authors, Publication Year.
    - Extract the Abstract or Summary.
    - Look for PDF links.
4. (Optional) If full text is accessible, extract the 'Methodology' or 'Conclusion' section.
5. Return a structured list of these papers.
```

---

## 🧩 Protocol C: The "Query Splitter" (Complex Multi-Step Search)
**Use Case**: Answering complex questions that require multiple distinct searches (e.g., "Compare the GDP of X and Y in 2024").

### Workflow Strategy
1.  **Decompose**: Break the user's request into atomic questions.
2.  **Iterate**: Execute a `browser_subagent` call for *each* atomic question.

### Standard Invocation (Per Sub-Query)
**TaskName**: `Sub-Query Search: [Atomic Question]`
**Task Payload**:
```text
1. Navigate to 'https://www.google.com'.
2. Search for '[Atomic Question]'.
3. extract specific data point: [Target Data].
4. Return the specific answer for this sub-query.
```

---

## 🛠 Protocol D: The "Debugger" (Documentation Lookup)
**Use Case**: Looking up API docs, error codes, or library usage.

### Standard Invocation
**TaskName**: `Documentation Lookup: [Library/Error]`
**Task Payload**:
```text
1. Navigate to Google.
2. Search for '[Language/Library] [Error Message or Function Name] docs'.
3. Locate the official documentation or a high-quality StackOverflow thread.
4. Extract the code example or usage explanation.
5. Return the solution or usage pattern.
```

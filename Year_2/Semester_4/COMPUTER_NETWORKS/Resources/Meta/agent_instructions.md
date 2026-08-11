# Agent Instructions: Computer Networks Study Material Generation

Your objective is to read the `Resources/Meta/mindmap.md` file and generate comprehensive, high-quality study notes for each **main topic** (top-level bullet point) in the mindmap. You are strongly encouraged to use your web search capabilities to gather additional information, clarify complex theoretical concepts, or find insightful real-world analogies and examples.

## Output Structure

For each top-level entry in the mindmap, you must produce **exactly one Markdown file**. Each top-level bullet becomes a self-contained, standalone study document covering all of its subtopics in depth.

1. **Target Directory**: All files must be saved inside the `Lectures/` directory. Create the directory if it does not exist.
2. **One File per Main Topic**: Do not split subtopics into separate files. Every sub-bullet and nested sub-bullet must be covered as sections and subsections within the single parent file.
3. **File Naming**: Use the format `topic_<n>_<concept_name>.md` where `<n>` is the topic number (1-indexed) and `<concept_name>` is a concise English transliteration or translation of the topic title. Use underscores for spaces, all lowercase.

**Naming Examples from `mindmap.md`:**

| Mindmap Entry | Output File |
|---|---|
| Network at the Edge | `Lectures/topic_1_network_edge.md` |
| The Internet | `Lectures/topic_2_the_internet.md` |
| Network Structure | `Lectures/topic_3_network_structure.md` |
| Access Technologies | `Lectures/topic_4_access_technologies.md` |
| Physical Media | `Lectures/topic_5_physical_media.md` |
| Data Switching | `Lectures/topic_6_data_switching.md` |
| Basic Issues | `Lectures/topic_7_basic_issues.md` |

## File Internal Structure

Every generated file must follow this internal structure, strictly in this order:

### 1. Title
Use the topic name as the `# H1` heading, followed immediately by a subtitle in italics.

```
# Network at the Edge
*The Network at a Glance*
```

### 2. Table of Contents
A linked Markdown table of contents mapping to each subtopic section within the file.

### 3. Introduction
A paragraph (3-5 sentences) that frames the topic within the broader context of computer networks. Explain *why* this topic matters, what problem it addresses, and how it relates to the other main topics in the course.

### 4. Subtopic Sections
For each sub-bullet in the mindmap, create an `## H2` section. For each nested sub-sub-bullet, create an `### H3` subsection. Every section must contain:

- A clear conceptual explanation (what it is, how it works, why it exists).
- A real-world analogy where applicable to ground abstract concepts.
- Key terminology in **bold** with an inline definition on first use.
- ASCII diagrams or structured text diagrams where a visual would aid understanding (e.g., client-server flow, packet-switching hop, protocol stack layers).
- Comparative tables where two or more related concepts are being contrasted (e.g., packet switching vs. circuit switching, DSL vs. HFC vs. FTTH).

### 5. Summary Table
A Markdown table at the end of the file that consolidates the key concepts, their one-line definitions, and any critical distinguishing characteristics.

| Concept | Definition | Key Characteristic |
|---|---|---|
| ... | ... | ... |

### 6. Key Takeaways
A short bulleted list (5-10 bullets) of the most important facts, distinctions, and exam-relevant points from the entire topic.

---

## Content and Formatting Guidelines

### 1. Markdown Styling
- Use standard, clean Markdown: headings (`#`, `##`, `###`), bold, italics, bullet lists, numbered lists, and tables.
- Use LaTeX only when presenting quantitative formulas (e.g., throughput, propagation delay, bandwidth-delay product):
  - **Inline math:** Single dollar signs `$ equation $`.
  - **Block math:** Double dollar signs `$$ equation $$` on their own line.
- Use fenced code blocks (` ``` `) for ASCII diagrams, protocol exchange sequences, and configuration snippets.

### 2. Clarity and Flow
- Write for a university student encountering these concepts for the first time, using standard technical terms (e.g., "router", "TCP/IP", "packet", "bandwidth").
- Follow a top-down progression: start with the big picture, then drill into specifics.
- Do not leave out important edge cases, protocol details, or distinctions — e.g., the difference between symmetric and asymmetric DSL, or why LEO satellites have lower latency than geostationary ones.
- Highlight exam-critical distinctions explicitly using a **bold label** such as **"Exam Note:"** or **"Key Distinction:"**.

### 3. Theoretical Depth and Web Search
- Do not skip theory. Before giving an analogy or example, provide the technical definition.
- For quantitative concepts (e.g., propagation delay, packet transmission time, store-and-forward delay), state the relevant formula and walk through a concrete numerical example.
- **Use web search** to verify facts, check current standards (e.g., 5G frequencies, fiber speeds), or find well-known analogies used in networking textbooks.
- Where relevant, cross-reference to the OSI model or TCP/IP stack layers, clearly stating which layer a concept belongs to.

### 4. Diagrams and Examples
- For every architectural concept (client-server, peer-to-peer, network edge vs. core), include an ASCII diagram showing the relationship between components.
- For every data-transfer mechanism (packet switching, circuit switching, routing), include a step-by-step trace of what happens to a unit of data from source to destination.
- For every access technology (DSL, HFC, FTTH, Wi-Fi, 5G), include a comparison of upload/download speeds, typical use cases, and physical medium used.
- Examples must be concrete and specific: use real company names, real protocol names, realistic numbers.

**Example of an ASCII diagram (client-server):**
```
  [Client A]          [Server]
      |                   |
      |--- HTTP Request -->|
      |                   |
      |<-- HTTP Response --|
      |                   |
```

**Example of a comparative table (packet vs. circuit switching):**
| Property | Packet Switching | Circuit Switching |
|---|---|---|
| Resource reservation | No (statistical multiplexing) | Yes (dedicated path) |
| Bandwidth efficiency | High (shared) | Low (idle capacity wasted) |
| Suitable for | Internet traffic (bursty) | Voice calls (constant rate) |
| Example | Internet (IP) | Traditional PSTN |

### 5. Networking-Specific Requirements
The following requirements apply specifically to this subject and override the general example count guidance:

- **No minimum solved-problem count is required.** This subject is primarily conceptual and architectural, not computational.
- **Do include at least one worked numerical example per file** where a quantitative formula is presented (e.g., calculate end-to-end delay for a 3-hop packet-switched path, or calculate throughput given link capacity and RTT).
- **Do include at least one protocol interaction sequence** per file where a protocol is discussed (e.g., a DNS query-response sequence, a TCP three-way handshake sketch).
- **Subtopic headers are required.** Use the exact names from `mindmap.md` as your `## H2` section headings to maintain alignment with lecture materials.

---

## General Rules
- Emojis are not allowed and may not be used in any way.
- If you spot any emojis, ask whether they are needed; if the answer is no, remove them.
- Do not fabricate protocol specifications or RFC numbers. If uncertain, use web search to verify or explicitly mark the information as approximate.
- All file content must be in English for prose explanations, technical terms, protocol names, standards, and code/diagram blocks.
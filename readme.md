# Auto-LeetCode-Notes

Auto-LeetCode-Notes is a Python-based automation tool designed to streamline the process of creating detailed, high-quality study notes for LeetCode problems. It fetches problem details from LeetCode, combines them with your Python solution, and leverages a GPT model to generate in-depth analysis and comparative notes in Markdown format.

This tool helps you focus on solving problems while it handles the note-taking, ensuring you build a structured and professional personal knowledge base.

## Features

- **Automated Note Generation**: Automatically creates detailed Markdown notes from your solution files.
- **Batch Processing**: Process multiple solutions at once based on a simple `todo.yml` configuration file.
- **GPT-Powered Analysis**: Uses AI to identify your approach, suggest alternative solutions, and provide a comprehensive analysis of time/space complexity.
- **Customizable Prompts**: Easily tailor the GPT prompts to fit your specific learning style or requirements.
- **Organized by Category**: Automatically organizes notes into subdirectories based on problem categories (e.g., `Two Pointers`, `Binary Tree`).

## Quick Start

Follow these steps to get the tool up and running.

### 1. Installation

First, clone the repository and install the required Python packages.

```bash
git clone <your-repository-url>
cd Auto-LeetCode-Notes
pip install -r requirements.txt
```

### 2. Configuration

The tool requires an OpenAI API key to function.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your OpenAI API key to the `.env` file as shown below. You can also specify a custom base URL if you are using a proxy.

    ```env
    OPENAI_API_KEY="sk-your-key-here"
    # Optional: If you use a proxy or a different API endpoint
    # OPENAI_BASE_URL="https://api.example.com/v1"
    ```

## Usage

The tool offers two primary modes of operation: processing a single solution or batch processing an entire category of solutions.

### Processing a Single Solution

To generate a note for a single LeetCode problem, use the `process_single.py` script. You need to provide the path to your solution file and optionally a category name.

The script infers the LeetCode problem "slug" from the filename (e.g., `15-3sum.py` becomes `3sum`).

```bash
python scripts/process_single.py solutions/15.py --category "Two Pointers"
```

### Batch Processing Solutions

For batch processing, first define your problem lists in `todo.yml`. The keys represent categories (which will become folder names), and the values are lists of LeetCode problem IDs.

**Example `todo.yml`:**

```yaml
Two Pointers-Two Sum:
  - 15
  - 2824

Binary Tree-BFS:
  - 107
  - 116
  - 117
```

Once `todo.yml` is configured, run `process_batch.py` with the desired category name.

```bash
python scripts/process_batch.py "Two Pointers-Two Sum"
```

The script will find all corresponding solution files in the `solutions/` directory (e.g., `15.py`, `2824.py`) and generate notes for them, skipping any that already exist.

## Customization

### How to Modify the GPT Prompt

The core of the AI-generated analysis lies in the prompt. You can customize it to change the structure, tone, or content of the output.

1.  **Locate the Prompt File**: The prompt is constructed in the `create_prompt` function within `src/lc_automator/gpt.py`.

2.  **Edit the Prompt**: Open the file and modify the `prompt` string variable. You can change any part of the template, such as:
    *   The introductory instructions for the AI.
    *   The sections to be generated (e.g., adding a new "Pitfalls" section).
    *   The format of the test cases or complexity analysis tables.

**Example**: To change the tone to be more concise, you could modify the initial instruction from "You are a world-class algorithm expert..." to "Generate a brief technical summary...".

### File and Directory Structure

- **`solutions/`**: Place your raw Python solution files here. The filename should ideally be the problem ID (e.g., `2824.py`).
- **`notes/`**: The generated Markdown notes are stored here. The tool creates subdirectories inside `notes/` based on the categories you provide.
- **`src/lc_automator/`**: Contains the core logic for fetching data (`fetcher.py`) and interacting with GPT (`gpt.py`).
- **`scripts/`**: Contains the executable scripts for single and batch processing.
- **`todo.yml`**: The control file for batch processing.
- **`.env`**: Your local environment configuration (API keys, etc.). Not version controlled.

By following this structure, you can easily manage your solutions and generated notes.
# 🤖 LeetCode Auto-Note Generator

![Workflow Status](https://img.shields.io/badge/status-active-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

An automated pipeline to supercharge your LeetCode learning process. This tool fetches problem details, uses GPT-4o to generate in-depth, multi-solution analysis notes based on your code, and organizes everything neatly into category-based folders. It's designed to let you focus on what matters: **solving problems**.

The final generated notes are structured, professional, and follow a consistent template—perfect for knowledge consolidation and interview preparation.

---

## ✨ Features

- **🧠 Intelligent Note Generation**: Provide just your solution code, and the tool uses GPT-4o to fill in all other analytical sections (Clarifying Questions, Complexity, Test Cases, Follow-ups, etc.).
- **🚀 Multi-Solution Analysis**: Automatically generates analysis and code for alternative approaches (e.g., provides in-order and post-order solutions when you submit a pre-order one).
- **📚 Category-Based Organization**: Manages your study plan through a simple `todo.yml` file. Notes are automatically saved into structured folders based on categories like `二叉树-BFS`.
- **⚙️ Fully Automated Workflow**:
    1. **Plan**: Edit a single `todo.yml` file to manage your to-do list.
    2. **Code**: Write your solution in a simple `[problem_id].py` file.
    3. **Generate**: Run a single command to batch-process all new solutions for a category.
    4. **Commit**: Use a shell script to automatically commit and push your progress to GitHub.
- **🌐 Smart Problem Fetching**: Automatically looks up problem details (like title, description) using just the problem ID, so you don't have to name your files with long slugs.
- **💨 Efficient Caching**: Problem ID-to-slug mappings are cached locally to minimize API calls and speed up subsequent runs.
- **🖥️ Optional UI**: Includes a simple web interface built with Streamlit for interactive, single-file processing.

---

## 🛠️ Installation & Setup

1. **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2. **Install Dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    pip install -r requirements.txt
    ```
    *(You may need to create a `requirements.txt` file with `openai`, `python-dotenv`, `requests`, `pyyaml`, `streamlit`)*

3. **Set Up Environment Variables:**
    Create a file named `.env` in the root of the project and add your OpenAI API key:
    ```
    # .env
    OPENAI_API_KEY=sk-YourSecretApiKeyHere
    # Optional: If you use a proxy or a different base URL
    # OPENAI_BASE_URL=https://your.proxy.url/v1
    ```

4. **Make Commit Script Executable:**
    This step is required to run the automated commit script.
    ```bash
    chmod +x commit.sh
    ```

---

## 🚀 My Workflow

This project is designed for a highly efficient daily workflow.

### Step 1: Plan & Code

1. **Update `todo.yml`:** Open the `todo.yml` file and add the LeetCode problem IDs you plan to solve under the appropriate category.
    ```yaml
    二叉树-BFS:
      - 102
      - 103
      - 107 # Just finished this one
    ```
2. **Write Your Solution:** Create a new Python file in the `solutions/` directory named after the problem ID (e.g., `solutions/107.py`). Write your code inside.

### Step 2: Generate Notes

Run the batch processing script, specifying the category you worked on. The script will automatically find your new solution files, fetch problem data, generate notes, and skip any problems that are already done.

```bash
python batch_process.py "二叉树-BFS"
```

The new Markdown notes will appear in the `notes/[category_name]/` directory.

### Step 3: Commit and Push

Once you're happy with the generated notes, run the commit script to save everything to your GitHub repository.

```bash
./commit.sh
```

The script automatically creates a commit message with the current date and pushes all new files.

---

## 🕹️ Alternative Usage

### Single File Processing
If you want to process just one file without using the todo.yml system, you can call `main_script.py` directly. The script will infer the problem slug from the filename.

```bash
# Filename must contain the slug, e.g., 102-binary-tree-level-order-traversal.py
python main_script.py solutions/102-binary-tree-level-order-traversal.py --category "二叉树-BFS"
```

### Interactive UI (with Streamlit)
For a user-friendly web interface, run the Streamlit app:

```bash
streamlit run app.py
```

This will open a local web server where you can upload a solution file, specify a category, and generate a note with the click of a button.

---

## 🔮 Future Improvements
- **Error Handling:** Add more robust error handling for API failures and network issues.
- **Custom Templates:** Allow users to select different note templates via a config file.
- **Language Support:** Add a flag to generate notes in different languages (e.g., `--lang zh`).
- **Dashboard:** Create a simple dashboard using the UI to visualize progress (e.g., problems solved per category).
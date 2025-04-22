# LoCoBot - Local Coding chat Bot

LoCoBot is a simple CLI chat bot that runs 100% locally. Given the directory of a software project on your machine, it can be a useful coding assistant. This is basically a LLama3.2 wrapper (although the model can be easily changed in the `src/locobot.py` file). This was mainly made to learn more about running contextualized LLMs locally, and to have a coding chat bot which I know for certain won't send my information to some big Tech company.

## Setup

**Ollama**

Start by installing ollama: https://ollama.com/download


Then, pull llama3.2, and the embedding model mxbai-embed-large.

```sh
ollama pull llama3.2
ollama pull mxbai-embed-large
```

**Python virtual environment**


Note: python >= 3.10 is required.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
source .venv/bin/activate
```

If, while trying to run LoCoBot, you encounter some error related to sqlite3, try running:

```sh
python -m pip install pysqlite3-binary
```

## Run and Config

To run LoCoBot, simply use

```sh
python src/main.py config.json
```

You must pass a config json which specifies the directory of a software project on your machine, and the files/paths to include and exclude. See [example.json](config/example.json) for reference.


There is a set of specific prompts that LoCoBot interprets a as commands. These include commands to save the conversation to a markdown file, listing the files LoCoBot is using for context, etc. Use the prompt `help` to get a comprehensive list of these commands.

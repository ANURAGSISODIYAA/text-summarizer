# Text Summarizer CLI

A command-line tool for summarizing text using the Ollama API and the Qwen2 0.5B model. This tool can take either a text file or direct text input and return a concise summary.

## Features

- Summarizes text from a file.
- Summarizes direct text input.
- Utilizes the Qwen2 0.5B model from Ollama for generating summaries.

## Requirements

- Python 3.11 or higher
- Ollama API
- Click library

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. Install the required dependencies:

```bash
pip install ollama click
````
3. Ensure the Qwen2 model is pulled from Ollama:
```bash
ollama pull qwen2:0.5b
```
## Usage

Summarize a Text File
To summarize a text file, run the following command:
```bash
python summarizer.py -f book.txt
````
Summarize Direct Text Input
To summarize direct text input, run the command like this:
```
python summarizer.py "The quick brown fox jumped over the lazy dog."


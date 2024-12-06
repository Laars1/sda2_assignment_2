# SDA2 Assignment 2

This repository implements a microkernel architecture with plugins for various tasks. The core system manages plugins for tasks like logging, word counting, and summarization, which process input files and generate output.

## Features
- Core system with plugin management
- Execute individual or all plugins
- File operations (read, process, save)

### Plugins
Following plugins are provided and executable:
- **TopKeyWords**: A plugin that processes text files and identifies the top keywords based on frequency.
- **WordCounter**: A plugin that counts the number of words in an input text file.
- **Summary**: A plugin that generates a summary of the input text using a machine learning model.
- **CaseConverterToUpper**: A plugin that processes text files and returns the text in capital letters
- **CaseConverterToLower**: A plugin that processes text files and returns the text in lower letters

## Requirements
- Python 3.0.x-3.12x,
- Pytorch (can be installed with pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118)
- Rust (required to run tensorflow) 
- tensorflow (pip install tensorflow)
- transformers package installiert (pip install transformers)

## Installation
Clone the repository:
```bash
git clone https://github.com/Laars1/sda2_assignment_2.git
```

## Input and Output

By default, the program uses a news article provided in the `input.txt` file. Each plugin processes the input, and the results are appended to the `output.txt` file. You can modify the input and output files as needed, but the default behavior assumes these file names for ease of use.

Ensure that the provided content is compatible with `UTF-8`.

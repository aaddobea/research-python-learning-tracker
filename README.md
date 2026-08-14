# Research Python Learning Tracker

A lightweight desktop learning tracker designed for a research workflow that progresses from Python fundamentals to data science, machine learning, PyTorch, VeReMi Extension, and a proposed CNN-BiLSTM model.

## Learning roadmap

1. **Python Fundamentals** — Python Crash Course
2. **Data Science** — Python for Data Analysis
3. **Machine Learning** — Hands-On Machine Learning
4. **PyTorch & Deep Learning** — Official PyTorch Tutorials
5. **VeReMi Extension** — Dataset understanding and preprocessing
6. **Proposed CNN-BiLSTM** — Model implementation and evaluation

## Features

- Topic-by-topic learning checklist
- Stage progress and overall progress
- Study timer
- Research notes
- Optional study reminders
- Automatic local progress saving
- No third-party Python packages required to run the source application

## Requirements

- Python 3.11+ recommended
- Tkinter (normally included with the standard Windows Python installation)

## Run from source

```bash
python research_python_learning_tracker.py
```

## Build a Windows executable

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build:

```bash
python -m PyInstaller --onefile --windowed --name "Research Python Learning Tracker" research_python_learning_tracker.py
```

The executable will be created in:

```text
dist/Research Python Learning Tracker.exe
```

Copy the executable to your Windows Desktop and launch it by double-clicking.

## Data storage

Progress and notes are stored locally in:

```text
C:\\Users\\YOUR_USERNAME\\.research_python_learning_tracker.json
```

The application does not upload learning data to a server.

## Project structure

```text
research-python-learning-tracker/
├── research_python_learning_tracker.py
├── README.md
├── LICENSE
└── .gitignore
```

## Roadmap

Planned future improvements include Windows toast notifications, daily study targets, chapter-level tracking, weekly analytics, exportable progress reports, and a more detailed VeReMi research milestone dashboard.

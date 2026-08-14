import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from datetime import datetime
import json

APP_NAME = "Research Python Learning Tracker"
DATA_FILE = Path.home() / ".research_python_learning_tracker.json"

STAGES = [
    ("1. Python Fundamentals", "Python Crash Course", [
        "Variables and simple data types",
        "Lists and tuples",
        "if / elif / else",
        "for and while loops",
        "Dictionaries",
        "Functions",
        "Classes and basic OOP",
        "Files and exceptions",
        "Basic testing",
    ]),
    ("2. Data Science", "Python for Data Analysis", [
        "JSON and nested data",
        "NumPy arrays",
        "Pandas Series and DataFrames",
        "Reading and writing data",
        "Data cleaning",
        "Missing values",
        "Filtering and grouping",
        "Feature transformation",
        "Matplotlib visualisation",
        "Exploratory data analysis",
    ]),
    ("3. Machine Learning", "Hands-On Machine Learning", [
        "Train / validation / test split",
        "Feature scaling",
        "Label encoding",
        "Classification",
        "Overfitting and underfitting",
        "Confusion matrix",
        "Precision, recall and F1",
        "ROC / AUC",
        "Hyperparameter tuning",
    ]),
    ("4. PyTorch & Deep Learning", "Official PyTorch Tutorials", [
        "Tensors",
        "Dataset and DataLoader",
        "nn.Module",
        "Training loops",
        "Loss functions",
        "Optimizers",
        "Backpropagation",
        "CNN fundamentals",
        "LSTM fundamentals",
        "BiLSTM fundamentals",
        "GPU / CUDA basics",
    ]),
    ("5. VeReMi Extension", "VeReMi Extension Documentation", [
        "Understand dataset structure",
        "Identify selected attack scenarios",
        "Read JSON records",
        "Extract relevant features",
        "Construct attack labels",
        "Clean and validate records",
        "Inspect class distribution",
        "Create leakage-safe data splits",
        "Create temporal sequences",
    ]),
    ("6. Proposed CNN-BiLSTM", "Your Research Implementation", [
        "Implement CNN baseline",
        "Implement BiLSTM baseline",
        "Implement proposed CNN-BiLSTM",
        "Select sequence length",
        "Tune hyperparameters",
        "Train and validate",
        "Evaluate held-out test set",
        "Confusion matrix and class-wise metrics",
        "Precision / Recall / F1 / AUC",
        "False-positive rate and detection latency",
        "Reproducible experiment configuration",
    ]),
]

DEFAULT_STATE = {
    "completed": {},
    "notes": "",
    "reminder_minutes": 60,
    "reminders_enabled": True,
    "study_seconds": 0,
    "last_saved": ""
}

def load_state():
    state = DEFAULT_STATE.copy()
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                state.update(json.load(f))
    except Exception:
        pass
    return state

state = load_state()

root = tk.Tk()
root.title(APP_NAME)
root.geometry("1180x760")
root.minsize(1000, 680)

style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass

header = ttk.Frame(root, padding=(22, 18))
header.pack(fill="x")

ttk.Label(header, text=APP_NAME, font=("Segoe UI", 22, "bold")).pack(anchor="w")
ttk.Label(
    header,
    text="A structured path from Python fundamentals to your VeReMi + CNN-BiLSTM research",
    font=("Segoe UI", 10)
).pack(anchor="w", pady=(3, 0))

main = ttk.Panedwindow(root, orient="horizontal")
main.pack(fill="both", expand=True, padx=18, pady=(0, 12))

left = ttk.Frame(main, padding=10)
right = ttk.Frame(main, padding=12)
main.add(left, weight=1)
main.add(right, weight=3)

ttk.Label(left, text="Research Roadmap", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 8))

stage_list = tk.Listbox(left, font=("Segoe UI", 10), activestyle="none", exportselection=False, height=12)
stage_list.pack(fill="both", expand=True)

for stage, _, _ in STAGES:
    stage_list.insert("end", stage)

ttk.Label(
    left,
    text="\nRecommended order:\nPython → Data Science → ML → PyTorch → VeReMi → CNN-BiLSTM",
    wraplength=240,
    justify="left"
).pack(anchor="w", pady=(12, 0))

stage_title = ttk.Label(right, text="", font=("Segoe UI", 16, "bold"))
stage_title.pack(anchor="w")

book_label = ttk.Label(right, text="", font=("Segoe UI", 10))
book_label.pack(anchor="w", pady=(3, 12))

progress_label = ttk.Label(right, text="", font=("Segoe UI", 10, "bold"))
progress_label.pack(anchor="w")

progress_bar = ttk.Progressbar(right, mode="determinate", maximum=100)
progress_bar.pack(fill="x", pady=(5, 12))

topic_canvas_frame = ttk.Frame(right)
topic_canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(topic_canvas_frame, highlightthickness=0)
scroll = ttk.Scrollbar(topic_canvas_frame, orient="vertical", command=canvas.yview)
topic_frame = ttk.Frame(canvas)

topic_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=topic_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

bottom = ttk.Frame(root, padding=(18, 0, 18, 18))
bottom.pack(fill="x")

overall_label = ttk.Label(bottom, text="", font=("Segoe UI", 10, "bold"))
overall_label.pack(anchor="w", pady=(0, 8))

dashboard = ttk.Frame(bottom)
dashboard.pack(fill="x")

timer_box = ttk.LabelFrame(dashboard, text="Study Timer", padding=10)
timer_box.pack(side="left", fill="y", padx=(0, 10))

timer_label = ttk.Label(timer_box, text="00:00:00", font=("Consolas", 18, "bold"))
timer_label.pack()

timer_running = False

def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def tick():
    if timer_running:
        state["study_seconds"] += 1
        timer_label.config(text=format_time(state["study_seconds"]))
        root.after(1000, tick)

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        tick()

def pause_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global timer_running
    timer_running = False
    state["study_seconds"] = 0
    timer_label.config(text="00:00:00")
    save_state()

for text, command in [("Start", start_timer), ("Pause", pause_timer), ("Reset", reset_timer)]:
    ttk.Button(timer_box, text=text, command=command).pack(side="left", padx=2, pady=(7, 0))

notes_box = ttk.LabelFrame(dashboard, text="Research Notes", padding=8)
notes_box.pack(side="left", fill="both", expand=True, padx=(0, 10))

notes = tk.Text(notes_box, height=6, width=55, wrap="word", font=("Segoe UI", 9))
notes.pack(fill="both", expand=True)
notes.insert("1.0", state.get("notes", ""))

reminder_box = ttk.LabelFrame(dashboard, text="Reminder", padding=10)
reminder_box.pack(side="right", fill="y")

reminder_enabled = tk.BooleanVar(value=state.get("reminders_enabled", True))
reminder_minutes = tk.StringVar(value=str(state.get("reminder_minutes", 60)))

def save_state():
    state["notes"] = notes.get("1.0", "end-1c")
    state["reminders_enabled"] = reminder_enabled.get()
    try:
        state["reminder_minutes"] = max(5, int(reminder_minutes.get()))
    except ValueError:
        state["reminder_minutes"] = 60
    state["last_saved"] = datetime.now().isoformat(timespec="seconds")
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        save_status.config(text="Progress saved")
    except Exception as exc:
        save_status.config(text=f"Save error: {exc}")

ttk.Checkbutton(reminder_box, text="Enable", variable=reminder_enabled, command=save_state).pack(anchor="w")
ttk.Label(reminder_box, text="Minutes:").pack(anchor="w", pady=(7, 2))
ttk.Entry(reminder_box, textvariable=reminder_minutes, width=8).pack(anchor="w")

def key_for(stage_idx, topic_idx):
    return f"{stage_idx}:{topic_idx}"

def total_progress():
    total = sum(len(topics) for _, _, topics in STAGES)
    done = sum(1 for value in state["completed"].values() if value)
    pct = done / total * 100 if total else 0
    return done, total, pct

def refresh_overall():
    done, total, pct = total_progress()
    overall_label.config(text=f"Overall research learning progress: {done}/{total} ({pct:.0f}%)")

def show_stage(index):
    stage, book, topics = STAGES[index]
    stage_title.config(text=stage)
    book_label.config(text=f"Primary resource: {book}")

    for widget in topic_frame.winfo_children():
        widget.destroy()

    completed = 0
    for i, topic in enumerate(topics):
        var = tk.BooleanVar(value=bool(state["completed"].get(key_for(index, i), False)))
        if var.get():
            completed += 1
        ttk.Checkbutton(
            topic_frame,
            text=topic,
            variable=var,
            command=lambda i=i, v=var: topic_changed(index, i, v)
        ).pack(anchor="w", fill="x", padx=8, pady=5)

    pct = completed / len(topics) * 100 if topics else 0
    progress_bar["value"] = pct
    progress_label.config(text=f"Stage progress: {completed}/{len(topics)} topics ({pct:.0f}%)")
    refresh_overall()

def topic_changed(stage_idx, topic_idx, var):
    state["completed"][key_for(stage_idx, topic_idx)] = bool(var.get())
    save_state()
    show_stage(stage_idx)

def on_stage_select(event=None):
    selection = stage_list.curselection()
    if selection:
        show_stage(selection[0])

stage_list.bind("<<ListboxSelect>>", on_stage_select)

save_status = ttk.Label(bottom, text="Ready")
save_status.pack(anchor="e", pady=(4, 0))

def reminder_check():
    if reminder_enabled.get():
        try:
            minutes = max(5, int(reminder_minutes.get()))
        except ValueError:
            minutes = 60

        last = state.get("last_reminder", "")
        now = datetime.now()
        remind = True
        if last:
            try:
                elapsed = (now - datetime.fromisoformat(last)).total_seconds() / 60
                remind = elapsed >= minutes
            except Exception:
                pass

        if remind:
            state["last_reminder"] = now.isoformat(timespec="seconds")
            save_state()
            messagebox.showinfo(
                "Research Study Reminder",
                "Time for a focused study session.\n\n"
                "1. Finish your current Python topic.\n"
                "2. Practise with a small example.\n"
                "3. Apply the concept to VeReMi when appropriate.\n\n"
                "Build the data pipeline before moving to the CNN-BiLSTM."
            )
    root.after(60000, reminder_check)

stage_list.selection_set(0)
stage_list.activate(0)
show_stage(0)
timer_label.config(text=format_time(state.get("study_seconds", 0)))
root.after(60000, reminder_check)


def close_app():
    save_state()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()

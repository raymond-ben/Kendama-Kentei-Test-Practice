# Kendama Kentei Trainer

A lightweight desktop application for practicing official Kendama Kentei tests.

Users can select a level and class, load the corresponding five tricks, and track their attempts in a simple intuitive interface. 

For more information about the official Kendama Kentei program, rules, and certification process, please visit the [official Kendama Kentei website](https://kendamakentei.com/en/).

NOTE: This application is only current for the 2026 tricklists.

## Why I Built This

As a kendama player, I wanted a lightweight tool for practicing official
Kendama Kentei tests without needing printed sheets or manually tracking
attempts. This project was also an opportunity to learn desktop application
development with Python and Flet.

---

## Features

- All official Kentei levels are available
- Select any class within a level
- Displays the official 2026 tricks for each level
- Track up to five attempts for each trick
- Live progress bar showing completed tricks

---

## Screenshot

[![Screenshot-2026-07-22-at-3-07-44-PM.png](https://i.postimg.cc/28ZdqHcN/Screenshot-2026-07-22-at-3-07-44-PM.png)](https://postimg.cc/XpnBmg6s)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/kentei-practice.git
cd kentei-practice
```

Create and activate a virtual environment:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the application

```bash
python src/main.py
```

---

## Built With

- Python
- Flet
- Pandas
- OpenPyXL

---

## Project Structure

```
src/
    main.py
    ui.py
    trick_card.py
    data_loader.py

data/
    tricks.xlsx
```

---

## Data Source

The trick list is based on the official Kendama Kentei curriculum.
# Snake

**Snake** game written in Python.
Play using the **arrow keys**, including **diagonal movement** by pressing two arrow keys at the same time.

---

## Features
- **Arrow-key controls** + **diagonals** (press two arrows simultaneously)
- Multiple apple types spawn with different behavior:
  - **Red apple**: +1 point
  - **Gold apple**: +5 points 
  - **Toxic apples**: **chase you** and can **kill** you

---

## Project Structure
```bash
SNAKE/
├─ config/
│ ├─ init.py
│ └─ config.py # directions
├─ core/
│ ├─ init.py
│ ├─ apple.py # Apple classes + spawn logic (red/gold/toxic)
│ ├─ game.py # Game state + board building
│ └─ snake.py # Snake logic 
├─ utils/
│ ├─ init.py
│ └─ utils.py # helper functions 
├─ main.py # entry point
└─ README.md
```
---

## Quick start
```bash
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

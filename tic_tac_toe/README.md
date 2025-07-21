# Tic Tac Toe (OOP Python Backend)

This is a backend-only implementation of Tic Tac Toe using Object-Oriented Programming in Python.

## 💾 Installation

```bash
pip install flask  # Only for REST API
```

## 🚀 Run (Standard Input)

```bash
python main.py
```

## 🌐 Run (REST API)

```bash
python rest_api.py
```

## 🧱 Structure

- `match.py` → Controls the game loop, turns, and win/draw checks.
- `table.py` → Manages the 3x3 board.
- `option.py` → Represents a player's symbol (`X` or `O`).
- `main.py` → CLI entry point.
- `rest_api.py` → (Optional) Flask-based REST interface.

## 👨‍🏫 OOP Principles Used

- **Encapsulation**: Board state is kept inside `Table`.
- **Abstraction**: Each class hides internal logic behind simple interfaces.
- **Inheritance/Polymorphism**: Can be extended to subclasses of `Option` for AI or animations.
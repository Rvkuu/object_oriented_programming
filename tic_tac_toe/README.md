# Object-Oriented Programming (OOP) Principles in Tic Tac Toe Game

This document explains how the four core principles of OOP are applied in the Tic Tac Toe game implementation. The code is structured across multiple files and classes: `table.py`, `player.py`, `match.py`, and `main.py`.

---

## 1. Encapsulation

**Definition**: The bundling of data and methods that operate on that data within one unit, restricting direct access from outside.

**Examples:**

* **`Table` class** encapsulates the board state using a private `grid` and provides controlled methods like `update()`, `is_empty()`, and `get_winner()` to manipulate and inspect it.
* **`Player` class** encapsulates player-specific data like `name` and `symbol`. Subclasses use this internally for decision-making.
* **`Match` class** encapsulates the flow of the game, managing turns, winner checking, and board updates internally.

**Benefit:** Users of these classes don’t need to interact directly with the data; they just use the provided interfaces.

---

## 2. Abstraction

**Definition**: Hiding complex implementation details and exposing only what is necessary.

**Examples:**

* `get_winner()` in `Table` hides the internal logic of checking rows, columns, and diagonals.
* `make_move()` in `Player` subclasses abstracts how the move is chosen (user input or random AI).
* `play()` in `Match` abstracts the full game loop, hiding logic such as switching turns, displaying messages, and processing inputs.

**Benefit:** Simplifies interaction and isolates complexity, making the code easier to maintain and extend.

---

## 3. Inheritance

**Definition**: A mechanism to create a new class using properties and behavior of an existing class.

**Examples:**

* `HumanPlayer` and `RandomAIPlayer` inherit from the abstract `Player` class.
* The base `Player` class defines common attributes (`name`, `symbol`) and a required method `make_move()` using `@abstractmethod`.

**Benefit:** Promotes code reuse and specialization, allowing multiple types of players without duplicating code.

---

## 4. Polymorphism

**Definition**: The ability to treat different types of objects through the same interface.

**Examples:**

* `make_move()` method is defined in the abstract `Player` class but implemented differently in `HumanPlayer` and `RandomAIPlayer`.
* The `Match` class uses:

  ```python
  row, col = current_player.make_move(self.table)
  ```

  This line works for both human and AI players due to polymorphism.

**Benefit:** Enables flexible and extensible code; you can add new player types (e.g., smarter AI) without modifying the game engine.

---

## Summary Table

| OOP Principle | Where It's Applied                                | Functionality & Role                                 |
| ------------- | ------------------------------------------------- | ---------------------------------------------------- |
| Encapsulation | `Table.grid`, `Player.name`, `Match.current_turn` | Protects internal data from external interference    |
| Abstraction   | `get_winner()`, `make_move()`, `play()`           | Hides complexity behind clear interfaces             |
| Inheritance   | `HumanPlayer`, `RandomAIPlayer` → `Player`        | Promotes code reuse and behavioral extensions        |
| Polymorphism  | `current_player.make_move()`                      | Allows interchangeable use of different player types |

---

## Code Structure Overview

* **table.py**: Handles all board-related logic and display.
* **player.py**: Defines the abstract `Player` class and concrete subclasses for human and AI players.
* **match.py**: Controls game flow, switching turns, checking game status, and invoking player moves.
* **main.py**: Entry point of the program. Prompts user for game mode and starts a match accordingly.

---

This design reflects clean separation of concerns and demonstrates all four core principles of object-oriented programming in practice.


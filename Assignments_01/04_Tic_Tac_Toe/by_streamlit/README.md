# Professional Tic Tac Toe with AI

A sleek and interactive Tic Tac Toe game built using Python and Streamlit. This game allows you to play against an AI that uses the Minimax algorithm, complete with score tracking and custom styling.

---

## 🚀 Live Demo
Experience the game live: [Play Now]("")

## Features

- **Two-player mode (You vs. AI):**  
  Play against an AI opponent that makes optimal moves using the Minimax algorithm.

- **Customizable Game Board:**  
  Enjoy a stylish game board with hover effects and responsive design.

- **Score Tracking:**  
  Your wins, the AI wins, and the high score are saved and displayed on a custom score board.

- **Game Reset Options:**  
  Easily restart the current round or reset all scores.

---

## Prerequisites

- Python 3.x
- Required Python packages:
  - streamlit
  - json (standard library)
  - os (standard library)
  
Install Streamlit (and any additional dependencies) using pip:

```bash
pip install streamlit
```

## Installation & Setup

### Clone or Download the Repository:
- Save the code into a file named, for example, `app.py`.

### Ensure that scores.json Exists:
- The game uses a JSON file to save and load scores. If it does not exist, it will be created upon the first score update.

### Run the Application:
- Open your terminal or command prompt, navigate to the directory where `app.py` is located, and run:

  ```bash
  streamlit run app.py
  ```

## How to Play

### Starting the Game:
- **When the app loads:**  
  You'll see the title and the current score board. The game board will display empty cells represented by buttons.

### Your Move:
- **Player Action:**  
  Click any empty cell to place your **X**.
- **AI Response:**  
  The AI will automatically respond by placing an **O**.

### Winning Conditions:
- **Criteria:**  
  The game checks for three in a row horizontally, vertically, or diagonally.
- **Tie:**  
  If neither wins and the board is full, the game declares a tie.

### Game Options:
- **Restart Game:**  
  Resets the board to start a new round while keeping the current scores.
- **Reset Everything:**  
  Clears the board and resets all the scores to start from scratch.

### Score Tracking:
- **Display:**  
  Your score, the AI’s score, and the highest score are shown on a custom score board at the top.

## Code Structure

### Board Initialization:
- **Function:** `initialize_board()`  
  Creates a new 3x3 game board with empty cells.

### Winner Check:
- **Function:** `check_winner(board)`  
  Examines rows, columns, and diagonals to determine if there is a winner, a tie, or if the game should continue.

### Minimax Algorithm:
- **Function:** `minimax(board, depth, is_maximizing)`  
  Recursively evaluates possible moves to let the AI choose the best move.

### AI Move Selection:
- **Function:** `ai_move(board)`  
  Determines the optimal move for the AI by comparing scores from the Minimax function.

### Display and Styling:
- **Function:** `display_board(board)`  
  Uses HTML and CSS to render a stylish game board and score board in Streamlit.

### User Move Handling:
- **Function:** `handle_click(i, j)`  
  Registers your move, updates the board, and triggers the AI move.

### Score Management:
- **Functions:** `save_scores()` and `load_scores()`  
  Handle saving and loading game scores from a JSON file.

### Game Reset Options:
- **Function:** `restart_game()`  
  Resets the board for a new round.
- **Function:** `reset_everything()`  
  Clears all scores.

### Main Application:
- **Function:** `main()`  
  Sets up the game interface, initializes session state, and displays game rules and instructions.


---
Developed with ❤️ by **Areeba Zafar**
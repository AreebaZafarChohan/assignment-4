import streamlit as st
import json
import os

# Initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Check if there's a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    # Check for tie
    if all(cell != ' ' for row in board for cell in row):
        return 'Tie'
    
    return None

# Minimax algorithm for AI moves
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Tie':
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# AI makes a move
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Custom styling for the board
def display_board(board):
    st.markdown("""
    <style>
        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-gap: 10px;
            margin: 30px auto;
            justify-content: center;
            background-color: purlpe;
        }
        .cell {
            width: 50px;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: transparent;
            border: 2px solid #4a4a4a;
            border-radius: 8px;
            font-size: 32px;
            font-weight: bold;
            color: #333333;
            transition: all 0.3s ease;
        }
        .cell:hover {
            background-color: #f5f5f5;
            transform: scale(1.05);
        }
        .x-cell {
            color: #ff4b4b;
        }
        .o-cell {
            color: #4b8df8;
        }
        .score-board {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
            padding: 15px;
            background-color: #f0f2f6;
            border-radius: 10px;
            color: black;
        }
        .score-item {
            text-align: center;
            color: black;
        }
        
    </style>
    """, unsafe_allow_html=True)

    # Score board
    st.markdown(f"""
    <div class="score-board">
        <div class="score-item">
            <div style="font-size: 14px; color: #666;">Your Score</div>
            <div style="font-size: 24px; font-weight: bold;">{st.session_state.player_score}</div>
        </div>
        <div class="score-item">
            <div style="font-size: 14px; color: #666;">AI Score</div>
            <div style="font-size: 24px; font-weight: bold;">{st.session_state.ai_score}</div>
        </div>
        <div class="score-item">
            <div style="font-size: 14px; color: #666;">High Score</div>
            <div style="font-size: 24px; font-weight: bold;">{st.session_state.high_score}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Game board
    st.markdown('<div class="board">', unsafe_allow_html=True)
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if board[i][j] != ' ':
                    cell_class = "x-cell" if board[i][j] == 'X' else "o-cell"
                    st.markdown(f'<div class="cell {cell_class}">{board[i][j]}</div>', unsafe_allow_html=True)
                else:
                    if st.button(' ', key=f'{i}-{j}', 
                               on_click=handle_click, args=(i,j),
                               disabled=st.session_state.game_over):
                        pass
    st.markdown('</div>', unsafe_allow_html=True)


# Handle player click
def handle_click(i, j):
    if st.session_state.board[i][j] == ' ' and not st.session_state.game_over:
        st.session_state.board[i][j] = 'X'
        winner = check_winner(st.session_state.board)
        
        if not winner:
            ai_move(st.session_state.board)
            winner = check_winner(st.session_state.board)
        
        if winner:
            st.session_state.game_over = True
            if winner == 'X':
                st.session_state.message = "🎉 You won!"
                st.session_state.player_score += 1
                save_scores()
            elif winner == 'O':
                st.session_state.message = "🤖 AI won!"
                st.session_state.ai_score += 1
                save_scores()
            else:
                st.session_state.message = "🤝 It's a tie!"

# Save scores to file
def save_scores():
    scores = {
        "player_score": st.session_state.player_score,
        "ai_score": st.session_state.ai_score,
        "high_score": max(st.session_state.player_score, st.session_state.high_score)
    }
    with open("scores.json", "w") as f:
        json.dump(scores, f)

# Load scores from file
def load_scores():
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as f:
            scores = json.load(f)
            return scores.get("player_score", 0), scores.get("ai_score", 0), scores.get("high_score", 0)
    return 0, 0, 0

# Reset the game (without resetting scores)
def restart_game():
    st.session_state.board = initialize_board()
    st.session_state.game_over = False
    st.session_state.message = "Your turn (X)"

# Reset everything including scores
def reset_everything():
    st.session_state.board = initialize_board()
    st.session_state.game_over = False
    st.session_state.message = "Your turn (X)"
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.high_score = 0
    save_scores()

# Main app
def main():
    st.title("🎯 Professional Tic Tac Toe")
    st.subheader("(Play with AI 🤖🚀)")
    
    # Initialize session state
    if 'board' not in st.session_state:
        st.session_state.player_score, st.session_state.ai_score, st.session_state.high_score = load_scores()
        restart_game()
    
    # Display game status
    st.subheader(st.session_state.message)
    
    # Display the board
    display_board(st.session_state.board)
    
    # Add actual button functionality
    if st.button("Restart Game"):
        restart_game()
    if st.button("Reset Everything"):
        reset_everything()
    
    # Instructions
    st.markdown("### Game Rules")
    st.write("1. Click any empty cell to place your X")
    st.write("2. The AI will automatically place its O")
    st.write("3. First to get 3 in a row (horizontally, vertically or diagonally) wins")
    st.write("4. Click 'Restart Game' for a new round or 'Reset Everything' to clear all scores")

if __name__ == "__main__":
    main()
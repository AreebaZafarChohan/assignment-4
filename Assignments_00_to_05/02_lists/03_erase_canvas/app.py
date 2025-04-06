# erase_canvas

"""
Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

"""

import tkinter as tk  # Importing the Tkinter library for GUI

# Constants
GRID_SIZE = 10   # Grid size (10x10 grid)
CELL_SIZE = 40   # Size of each cell in pixels
ERASER_SIZE = 50 # Size of the eraser in pixels

def create_grid(canvas, rows, cols, cell_size):
    """ Creates a grid of blue-colored cells """
    for row in range(rows):  # Loop through each row
        for col in range(cols):  # Loop through each column
            x1, y1 = col * cell_size, row * cell_size  # Top-left corner of the cell
            x2, y2 = x1 + cell_size, y1 + cell_size  # Bottom-right corner of the cell
            
            # Create a blue rectangle (cell) with a black outline
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black", tags="cell")

def create_eraser(canvas, size):
    """ Creates a gray-colored eraser rectangle """
    return canvas.create_rectangle(0, 0, size, size, fill="gray", outline="black")

def move_eraser(event, canvas, eraser, eraser_size):
    """ Moves the eraser based on mouse movement """
    x1, y1 = event.x - eraser_size // 2, event.y - eraser_size // 2  # Calculate new position
    x2, y2 = x1 + eraser_size, y1 + eraser_size  # Bottom-right corner
    
    # Move the eraser to the new position
    canvas.coords(eraser, x1, y1, x2, y2)

def erase_cells(event, canvas, eraser_size):
    """ Erases (changes to white) the cells that the eraser touches """
    
    # Find all items that overlap with the eraser
    overlapping_items = canvas.find_overlapping(
        event.x - eraser_size // 2, event.y - eraser_size // 2,
        event.x + eraser_size // 2, event.y + eraser_size // 2
    )
    
    # Loop through each overlapping item
    for item in overlapping_items:
        if "cell" in canvas.gettags(item):  # Check if the item is a grid cell
            canvas.itemconfig(item, fill="white")  # Change the cell color to white

def main():
    """ Main function to initialize the GUI application """
    root = tk.Tk()  # Create the main application window
    root.title("Eraser on Canvas")  # Set the window title

    # Create a canvas for drawing the grid and eraser
    canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
    canvas.pack()  # Add the canvas to the window

    # Create the grid and eraser
    create_grid(canvas, GRID_SIZE, GRID_SIZE, CELL_SIZE)
    eraser = create_eraser(canvas, ERASER_SIZE)

    # Bind mouse drag event to move eraser and erase cells
    canvas.bind("<B1-Motion>", lambda event: (move_eraser(event, canvas, eraser, ERASER_SIZE), erase_cells(event, canvas, ERASER_SIZE)))

    root.mainloop()  # Start the Tkinter event loop


# This line ensures that the main() function runs when the script is executed
if __name__ == "__main__":
    main()    

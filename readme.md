# **Tic-Tac-Toe**
This is the first step in my journey to develop my skills as a programmer. I have embarked on other projects as seen on 
GitHub. [Abhishek Repo](https://github.com/Milkshake10401)
The objectives of this project is to understand and remember the libraries I can use from python.
The goals for this project is to have a working model that works... maybe to have a better user interface in the future.

### Observe the following steps below:

1. **Understand the Rules:**\
Ensure you have a clear understanding of the Tic Tac Toe game rules. This includes the grid layout, winnin


2. **Board Representation:**\
The game board is represented using a 2D list, where each element corresponds to a cell on the board:
```python
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
```


3. **Displaying the Board:**\
Use the following function to display the current state of the board:
```python
def display_board(board):
    for row in board:
        print('|'.join(row))
```


4. **Player Input Handling:**\
Implement a function to take player input and update the board. Ensure the input is valid:

```python
def get_player_input():
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    return row, col
```


5. **Checking for a Winner:**\
Develop a function to check if there is a winner after each move, considering rows, columns, and diagonals:

```python
def check_winner(board):
    # Check rows, columns, and diagonals
    # Return 'X' if Player X wins, 'O' if Player O wins, or None if no winner yet
```

6. **Main Game Loop:**\
Create a loop to alternate turns between two players, taking input and updating the board until there's a winner or a draw.


7. **Handling Edge Cases:**\
Consider scenarios like a draw, invalid input, or attempting to play in an already occupied cell. Ensure the program gracefully handles these cases.


8. **Testing Your Game:**\
Play through the game multiple times to ensure it works as expected. Test different scenarios to catch any bugs.


9. **Refining and Optimizing:**\
Once the basic functionality is working, refine your code, optimize algorithms, and consider adding additional features if desired.


10. **Documentation:**\
Add comments to explain your code and document any important decisions or logic.


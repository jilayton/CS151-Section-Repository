# File: Prob1.py

"""
This program draws a Tic-Tac-Toe board in the center of the
graphics window.
"""

from pgl import GWindow, GLine

# Constants

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
BOARD_SIZE = 240
center_point_x = GWINDOW_WIDTH/6
center_point_y = GWINDOW_HEIGHT/2

# Main program

def tic_tac_toe_board():
    """
    Draws a Tic-Tac-Toe board.  The program centers the board
    on the window and computes the coordinates of the lines
    from the constant BOARD_SIZE.
    """
    gw = GWindow(GWINDOW_HEIGHT, GWINDOW_WIDTH)
#    gw.add(GLine(0,0,500,300))
## Vert Lines
    gw.add(GLine((GWINDOW_WIDTH-BOARD_SIZE)/2, GWINDOW_HEIGHT,
                 (GWINDOW_WIDTH-BOARD_SIZE)/2, GWINDOW_HEIGHT/6))
    gw.add(GLine(GWINDOW_WIDTH/6, GWINDOW_HEIGHT,
                 GWINDOW_WIDTH/6, GWINDOW_HEIGHT/6))   
    
## Horiz Lines
    gw.add(GLine(GWINDOW_WIDTH, GWINDOW_HEIGHT/2,
                 GWINDOW_WIDTH/48, GWINDOW_HEIGHT/2))  
    gw.add(GLine(GWINDOW_WIDTH, 3*GWINDOW_HEIGHT/4,
                 GWINDOW_WIDTH/48, 3*GWINDOW_HEIGHT/4))
    

    











if __name__ == "__main__":
    tic_tac_toe_board()

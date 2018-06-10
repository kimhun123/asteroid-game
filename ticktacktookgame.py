import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 340 # size of window's width in pixels
WINDOWHEIGHT = 340 # size of windows' height in pixels
BOXSIZE = 100 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 3 # number of columns of icons
BOARDHEIGHT = 3 # number of rows of icons

# Colorset
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

BGCOLOR = WHITE
BOXCOLOR = BLACK
HIGHLIGHTCOLOR = GRAY
LINECOLOR = WHITE

O = 'O'
X = 'X'

def main():
 global FPSCLOCK, DISPLAYSURF
 pygame.init()
 FPSCLOCK = pygame.time.Clock()
 DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

 mousex = 0 # used to store x coordinate of mouse event
 mousey = 0 # used to store y coordinate of mouse event
 pygame.display.set_caption('TicTacToe - harang97')

 mainBoard = [[None,None,None],[None,None,None],[None,None,None]]
 playerTurn = 'X'

 firstSelection = None # stores the (x, y) of the first box clicked.

 DISPLAYSURF.fill(BGCOLOR)
 drawBoard(mainBoard)

 while True: # main game loop
  mouseClicked = False

  DISPLAYSURF.fill(BGCOLOR)
  drawBoard(mainBoard)

  for event in pygame.event.get():
   if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
    pygame.quit()
    sys.exit()
   elif event.type == MOUSEMOTION:
    mousex, mousey = event.pos
   elif event.type == MOUSEBUTTONUP:
    mousex, mousey = event.pos
    mouseClicked = True

  boxx, boxy = getBoxAtPixel(mousex, mousey)
  if boxx != None and boxy != None:
   # the mouse is currently over a box.
   if mainBoard[boxx][boxy] == None:
    drawHighlightBox(boxx, boxy)
   if mainBoard[boxx][boxy] == None and mouseClicked:
    mainBoard[boxx][boxy] = playerTurn # set the box as "filled"
    drawXO(playerTurn, boxx, boxy)
    if playerTurn == 'X':
     playerTurn = 'O'
    else: playerTurn = 'X'

    # Algorithm that check the game is over
    if hasWon(mainBoard):
     pass
    if hasDraw(mainBoard):
     pass
    # -----------------------------
  # Redraw the screen and wait a clock tick.
  pygame.display.update()
  FPSCLOCK.tick(FPS)


def getBoxAtPixel(x, y):
 # Draw Box on display surface
 for boxx in range(BOARDWIDTH):
  for boxy in range(BOARDHEIGHT):
   left, top = leftTopCoordsOfBox(boxx, boxy)
   boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
   if boxRect.collidepoint(x, y):
    return (boxx, boxy)
 return (None, None)


def drawBoard(board):
 # Draws all of the boxes in their covered or revealed state.
 for boxx in range(BOARDWIDTH):
  for boxy in range(BOARDHEIGHT):
   left, top = leftTopCoordsOfBox(boxx, boxy)
   if board[boxx][boxy] == None:
    pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
   else:
    pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
    drawXO(board[boxx][boxy], boxx, boxy)


def leftTopCoordsOfBox(boxx, boxy):
 # Convert board coordinates to pixel coordinates
 left = boxx* (BOXSIZE + GAPSIZE) + GAPSIZE
 top = boxy * (BOXSIZE + GAPSIZE)  + GAPSIZE
 return (left, top)


def drawHighlightBox(boxx, boxy):
 left, top = leftTopCoordsOfBox(boxx, boxy)
 pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left , top , BOXSIZE , BOXSIZE))

def drawXO(playerTurn, boxx, boxy):
 left, top = leftTopCoordsOfBox(boxx, boxy)
 if playerTurn == 'X':
  pygame.draw.line(DISPLAYSURF, LINECOLOR, (left + 3, top + 3), (left + BOXSIZE - 3, top + BOXSIZE - 3), 4)
  pygame.draw.line(DISPLAYSURF, LINECOLOR, (left + BOXSIZE - 3, top + 3), (left + 3, top + BOXSIZE - 3), 4)
 else:
  HALF = int(BOXSIZE / 2)
  pygame.draw.circle(DISPLAYSURF, LINECOLOR, (left + HALF, top + HALF), HALF - 3, 4)

def hasWon(board):
 # Returns True if player 1 or 2 wins
 return True


def hasDraw(board):
 # Returns True if all the boxes have been filled
 for i in board:
  if None in i:
   return False
 return True

if __name__ == '__main__':
 main()

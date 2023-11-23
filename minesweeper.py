from cmu_graphics import *
import math
from PIL import Image
import os, pathlib


class User:
    def __init__(self, row, col):
        self.row = row
        self.col = col
class Mine:
    def __init__(self, row, col):
        self.minerow = row
        self.minecol = col
        self.image = 'mine.jpg'
        

def onAppStart(app):
    app.character =  'character new.png'
    app.user = User(0, 0)
    app.rows = 6
    app.cols = 6
    app.boardLeft = 75
    app.boardTop = 100
    app.boardWidth = 300
    app.boardHeight = 300
    app.cellBorderWidth = 2
    app.selection = None
    app.board = [(['green'] * app.cols) for rwo in range(app.rows)]
    app.score = 0
    app.time = 0
    app.ischeck = [(app.user.row, app.user.col)]
    app.gameover = False
    app.stepsPerSecond = 1

def onMousePress(app, mouseX, mouseY):
    selectedCell = getCell(app, mouseX, mouseY)
    if selectedCell != None:
      if selectedCell == app.selection:
          app.selection = None
      else:
          app.selection = selectedCell

def redrawAll(app):
    drawLabel(f'score: {app.score}', (app.boardWidth + app.boardLeft)//2, 50, size = 15)
    drawLabel(f'time: {app.time}', (app.boardWidth + app.boardLeft)//2, app.boardHeight + app.boardTop + 50, size = 15)
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    for i in range(app.rows):
        drawLabel(f'{i}', app.boardLeft + cellWidth*i + cellWidth//2, app.boardTop - 30, font = 'arial', size = 15)
    for j in range(app.cols):
        drawLabel(f'{j}', app.boardLeft - 30, app.boardTop + cellHeight*j + cellHeight//2, font = 'arial', size = 15)
    drawBoard(app)
    drawBoardBorder(app)
    drawImage(app.character, app.boardLeft + cellWidth*app.user.col + cellWidth//2, app.boardTop + cellHeight*app.user.row + cellHeight//2, width=30,height=30, align = 'center')
    
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col, app.board[row][col])

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):
    if (row, col) in app.ischeck:
        color = 'white'
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
      return (row, col)
    else:
      return None

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def onKeyPress(app, key):
    if key == 'right':
        if app.user.col + 1 < app.cols:
            app.user.col += 1
            app.ischeck.append((app.user.row, app.user.col))
    elif key == 'left':
        if app.user.col > 0:
            app.user.col -= 1
            app.ischeck.append((app.user.row, app.user.col))
    elif key == 'down':
        if app.user.row + 1< app.rows:
            app.user.row += 1
            app.ischeck.append((app.user.row, app.user.col))
    elif key == 'up':
        if app.user.row > 0:
            app.user.row -= 1
            app.ischeck.append((app.user.row, app.user.col))
    
def onStep(app):
    if app.gameover == False:
        app.time += 1
                           
        
def main():
    runApp(width = 600, height = 600)

main()
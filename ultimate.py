import pygame
from pygame.locals import *

class BigGrid():

    def __init__(self, listy=[[None,None,None], \
                              [None,None,None], \
                              [None,None,None]],
                              xo='X', winner = None, counter = 0):
        #self.background = background
        self.listy = listy
        self.xo = xo
        self.winner = winner
        self.counter = counter

    def make_board(self,board_size,board):
        background = pygame.Surface(board_size.get_size())
        background = background.convert()
        #background.fill(255,255,255)
        #vert
        pygame.draw.line(board, (0,0,0),(300,0),(300,900), 5)
        pygame.draw.line(board, (0,0,0),(600,0),(600,900), 5)
        #horiz
        pygame.draw.line(board, (0,0,0),(0,300),(900,300), 5)
        pygame.draw.line(board, (0,0,0),(0,600),(900,600), 5)
        pygame.display.update()

        return background

    def status(self,board):
        if self.winner == None:
            message = self.xo + "'s turn"
        else:
            message = self.winner + " wins YEET"
        font = pygame.font.Font(None, 24)
        text = font.render(message, 1, (10,10,10))

        board.fill ((250,250,250), (0,900,900,25))
        board.blit(text, (10,900))

    def showBoard(self,board_size,board):
        self.status(board)
        board_size.blit(board, (0,0))
        pygame.display.flip()

    def position(self, mX, mY):
        if mY < 300:
            row = 0
        elif mY < 600:
            row = 1
        else:
            row = 2
        if mX < 300:
            column = 0
        elif mX < 600:
            column = 1
        else:
            column = 2
        return (row,column)

    def moveDraw(self,board, bRow, bColumn, player_piece):
        xCenter = ((bColumn)*300)+150
        yCenter = ((bRow)*300)+150
        if (player_piece == 'O'):
            pygame.draw.circle(board, (0,0,250),(xCenter,yCenter),90,12)
        else:
            pygame.draw.line(board,(255,215,0),(xCenter-66,yCenter-66), \
                                   (xCenter+66,yCenter+66),12)
            pygame.draw.line(board,(255,215,0),(xCenter-66,yCenter+66), \
                                   (xCenter+66,yCenter-66),12)
        self.listy[bRow][bColumn] = player_piece

    def clickedy(self,board):
        (mX,mY) = pygame.mouse.get_pos()
        (row,column) = self.position(mX,mY)
        if self.listy[row][column] == 'X' or self.listy[row][column] == 'O':
            return
        self.moveDraw(board,row,column,self.xo)

        if self.xo == 'X':
            self.xo = 'O'
        else:
            self.xo = 'X'

    def winnerwinnerchickendinner(self,board):
        for row in range(0,3):
            if self.listy[row][0] == self.listy[row][1] == self.listy[row][2] \
               and self.listy[row][0] != None and self.counter == 0:
               self.winner = self.listy[row][0]
               self.counter += 1
               pygame.draw.line (board, (250,0,0), (0,3*((row+1)*100 -50)), (900,3*((row+1)*100 - 50)),6)
               break
        for column in range(0,3):
            if self.listy[0][column] == self.listy[1][column] == self.listy[2][column] \
               and self.listy[0][column] != None and self.counter == 0:
               self.winner = self.listy[0][column]
               self.counter += 1
               pygame.draw.line (board, (250,0,0), (3*((column+1)*100 -50), 0), (3*((column+1)*100 - 50), 900),6)
               break
        if self.listy[0][0] == self.listy[1][1] == self.listy[2][2] and \
           self.listy[0][0] != None and self.counter == 0:
            # diagonal left to right
            self.winner = self.listy[0][0]
            self.counter += 1
            pygame.draw.line (board, (250,0,0), (0, 0), (900, 900), 6)

        if self.listy[0][2] == self.listy[1][1] == self.listy[2][0] and \
           self.listy[0][2] != None and self.counter == 0:
            # diagonal right to left
            self.winner = self.listy[0][2]
            self.counter += 1
            pygame.draw.line (board, (250,0,0), (900, 0), (0, 900), 6)

class lilGrid():

    def __init__(self, listy=[[None,None,None], \
                              [None,None,None], \
                              [None,None,None]],
                              xo='X', winner = None, counter = 0):
        #self.background = background
        self.listy = listy
        self.xo = xo
        self.winner = winner
        self.counter = counter

    def make_board(self,board_size,board,startx,starty):
        background = pygame.Surface(board_size.get_size())
        background = background.convert()
        addx = (startx-1)*300
        addy = (starty-1)*300
        #background.fill(255,255,255)
        #vert
        pygame.draw.line(board, (0,0,0),(addx+100,addy+15),((addx+100),(addy+285)), 5)
        pygame.draw.line(board, (0,0,0),(addx+200,addy+15),((addx+200),(addy+285)), 5)
        #horiz
        pygame.draw.line(board, (0,0,0),(addx+15,addy+100),((addx+285),(addy+100)), 5)
        pygame.draw.line(board, (0,0,0),(addx+15,addy+200),((addx+285),(addy+200)), 5)
        pygame.display.update()

        return background

    def status(self,board):
        if self.winner == None:
            message = self.xo + "'s turn"
        else:
            message = self.winner + " wins YEET"
        font = pygame.font.Font(None, 24)
        text = font.render(message, 1, (10,10,10))

        board.fill ((250,250,250), (0,300,300,25))
        board.blit(text, (10,300))

    def showBoard(self,board_size,board):
        self.status(board)
        board_size.blit(board, (0,0))
        pygame.display.flip()

    def position(self, mX, mY):
        if mY < 100:
            row = 0
        elif mY < 200:
            row = 1
        else:
            row = 2
        if mX < 100:
            column = 0
        elif mX < 200:
            column = 1
        else:
            column = 2
        return (row,column)

    def moveDraw(self,board, bRow, bColumn, player_piece):
        xCenter = ((bColumn)*100)+50
        yCenter = ((bRow)*100)+50
        if (player_piece == 'O'):
            pygame.draw.circle(board, (0,0,250),(xCenter,yCenter),30,12)
        else:
            pygame.draw.line(board,(255,215,0),(xCenter-22,yCenter-22), \
                                   (xCenter+22,yCenter+22),12)
            pygame.draw.line(board,(255,215,0),(xCenter-22,yCenter+22), \
                                   (xCenter+22,yCenter-22),12)
        self.listy[bRow][bColumn] = player_piece

    def clickedy(self,board):
        (mX,mY) = pygame.mouse.get_pos()
        (row,column) = self.position(mX,mY)
        if self.listy[row][column] == 'X' or self.listy[row][column] == 'O':
            return
        self.moveDraw(board,row,column,self.xo)

        if self.xo == 'X':
            self.xo = 'O'
        else:
            self.xo = 'X'

    def winnerwinnerchickendinner(self,board):
        for row in range(0,3):
            if self.listy[row][0] == self.listy[row][1] == self.listy[row][2] \
               and self.listy[row][0] != None and self.counter == 0:
               self.winner = self.listy[row][0]
               self.counter += 1
               pygame.draw.line (board, (250,0,0), (0,(row+1)*100 -50), (300,(row+1)*100 - 50),6)
               break
        for column in range(0,3):
            if self.listy[0][column] == self.listy[1][column] == self.listy[2][column] \
               and self.listy[0][column] != None and self.counter == 0:
               self.winner = self.listy[0][column]
               self.counter += 1
               pygame.draw.line (board, (250,0,0), ((column+1)*100 -50, 0), ((column+1)*100 - 50, 300),6)
               break
        if self.listy[0][0] == self.listy[1][1] == self.listy[2][2] and \
           self.listy[0][0] != None and self.counter == 0:
            # diagonal left to right
            self.winner = self.listy[0][0]
            self.counter += 1
            pygame.draw.line (board, (250,0,0), (0, 0), (300, 300), 6)

        if self.listy[0][2] == self.listy[1][1] == self.listy[2][0] and \
           self.listy[0][2] != None and self.counter == 0:
            # diagonal right to left
            self.winner = self.listy[0][2]
            self.counter += 1
            pygame.draw.line (board, (250,0,0), (300, 0), (0, 300), 6)

#yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
lil1 = lilGrid()
lil2 = lilGrid()
lil3 = lilGrid()
lil4 = lilGrid()
lil5 = lilGrid()
lil6 = lilGrid()
lil7 = lilGrid()
lil8 = lilGrid()
lil9 = lilGrid()

BigBoi = BigGrid(listy=[[lil1,lil2,lil3], \
                          [lil4,lil5,lil6], \
                          [lil7,lil8,lil9]],
                          xo='X', winner = None, counter = 0)
"""Make BigBoi a grid with lil grids inside"""
pygame.init()
board_size = pygame.display.set_mode ((900, 925))
# create the game board
board = board_size


BigBoi.make_board(board_size, board)
lil1.make_board(board_size, board, 1, 1)
lil2.make_board(board_size, board, 1, 2)
lil3.make_board(board_size, board, 1, 3)
lil4.make_board(board_size, board, 2, 1)
lil5.make_board(board_size, board, 2, 2)
lil6.make_board(board_size, board, 2, 3)
lil7.make_board(board_size, board, 3, 1)
lil8.make_board(board_size, board, 3, 2)
lil9.make_board(board_size, board, 3, 3)

pygame.display.update()
BigBoi.showBoard(board_size, board_size)
lil1.showBoard(board_size, board_size)
lil2.showBoard(board_size, board_size)
lil3.showBoard(board_size, board_size)
lil4.showBoard(board_size, board_size)
lil5.showBoard(board_size, board_size)
lil6.showBoard(board_size, board_size)
lil7.showBoard(board_size, board_size)
lil8.showBoard(board_size, board_size)
lil9.showBoard(board_size, board_size)
pygame.display.update()
#white = (255,255,255)
board_size.fill([255, 255, 255])
pygame.display.set_caption ('Tic Tac Toe')
pygame.display.flip()

# main event loop
running = 1

while (running == 1):
    BigBoi.make_board(board_size, board)
    lil1.make_board(board_size, board, 1, 1)
    lil2.make_board(board_size, board, 1, 2)
    lil3.make_board(board_size, board, 1, 3)
    lil4.make_board(board_size, board, 2, 1)
    lil5.make_board(board_size, board, 2, 2)
    lil6.make_board(board_size, board, 2, 3)
    lil7.make_board(board_size, board, 3, 1)
    lil8.make_board(board_size, board, 3, 2)
    lil9.make_board(board_size, board, 3, 3)
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            BigBoi.clickedy(board)
            lil1.clickedy(board)
            lil2.clickedy(board)
            lil3.clickedy(board)
            lil4.clickedy(board)
            lil5.clickedy(board)
            lil6.clickedy(board)
            lil7.clickedy(board)
            lil8.clickedy(board)
            lil9.clickedy(board)
        # check for a winner
        BigBoi.winnerwinnerchickendinner(board)
        lil1.winnerwinnerchickendinner(board)
        lil2.winnerwinnerchickendinner(board)
        lil3.winnerwinnerchickendinner(board)
        lil4.winnerwinnerchickendinner(board)
        lil5.winnerwinnerchickendinner(board)
        lil6.winnerwinnerchickendinner(board)
        lil7.winnerwinnerchickendinner(board)
        lil8.winnerwinnerchickendinner(board)
        lil9.winnerwinnerchickendinner(board)
        # update the display
        BigBoi.showBoard(board_size, board)
        lil1.showBoard(board_size, board)
        lil2.showBoard(board_size, board)
        lil3.showBoard(board_size, board)
        lil4.showBoard(board_size, board)
        lil5.showBoard(board_size, board)
        lil6.showBoard(board_size, board)
        lil7.showBoard(board_size, board)
        lil8.showBoard(board_size, board)
        lil9.showBoard(board_size, board)
        pygame.display.update()
pygame.quit

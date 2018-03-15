import pygame
from pygame.locals import *

class BigGrid():

    def __init__(self, listy=[[None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None], \
                              [None,None,None], [None,None,None], [None,None,None]], \
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

        #lil grids
        for x in range(4):
            for y in range(4):
                addx = (x-1)*300
                addy = (y-1)*300
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

        board.fill ((250,250,250), (0,900,900,25))
        board.blit(text, (10,900))

    def showBoard(self,board_size,board):
        self.status(board)
        board_size.blit(board, (0,0))
        pygame.display.flip()

    def position(self, mX, mY):
        if mY < 100:
            row = 0
        elif mY < 200:
            row = 1
        elif mY < 300:
            row = 2
        elif mY < 400:
            row = 3
        elif mY < 500:
            row = 4
        elif mY < 600:
            row = 5
        elif mY < 700:
            row = 6
        elif mY < 800:
            row = 7
        else:
            row = 8
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

#yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
simple = BigGrid()

pygame.init()
board_size = pygame.display.set_mode ((900, 925))
# create the game board
board = board_size
# simple.make_board(board_size, board)
pygame.display.update()
simple.showBoard(board_size, board_size)
pygame.display.update()
#white = (255,255,255)
board_size.fill([255, 255, 255])
pygame.display.set_caption ('Tic Tac Toe')
pygame.display.flip()

# main event loop
running = 1

while (running == 1):
    simple.make_board(board_size, board)
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            simple.clickedy(board)

        # check for a winner
        simple.winnerwinnerchickendinner(board)

        # update the display
        simple.showBoard(board_size, board)
        pygame.display.update()
pygame.quit

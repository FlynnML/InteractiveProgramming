import pygame
from pygame.locals import *

class Grid():

    def __init__(self, listy=[[None,None,None], \
                              [None,None,None], \
                              [None,None,None]],
                              xo='X', winner = None):
        #self.background = background
        self.listy = listy
        self.xo = xo
        self.winner = winner

    def make_board(self,board_size):
        background = pygame.Surface(board_size.get_size())
        background = background.convert()
        background.fill(255,255,255)
        #vert
        pygame.draw.line (background, (0,0,0),(100,0),(100,300), 2)
        pygame.draw.line (background, (0,0,0),(200,0),(200,300), 2)
        #horiz
        pygame.draw.line (background, (0,0,0),(0,100),(300,100), 2)
        pygame.draw.line (background, (0,0,0),(0,200),(300,200), 2)

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

    def showBoard(self,board_size, board):
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
            pygame.draw.circle(board, (0,0,0),(xCenter,yCenter),44,2)
        else:
            pygame.draw.line(board,(0,0,0),(xCenter-22,yCenter-22), \
                                   (xCenter+22,yCenter+22),2)
            pygame.draw.line(board,(0,0,0),(xCenter+22,yCenter+22), \
                                   (xCenter-22,yCenter-22),2)
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
               and self.listy[row][0] != None:
               self.winner = self.listy[row][0]
               pygame.draw.line (board, (250,0,0), (0,(row+1)*100 -50), (300,(row+1)*100 - 50),2)
               break
        for column in range(0,3):
            if self.listy[0][column] == self.listy[1][column] == self.listy[2][column] \
               and self.listy[0][column] != None:
               self.winner = self.listy[0][column]
               pygame.draw.line (board, (250,0,0), ((column+1)*100 -50, 0), ((column+1)*100 - 50, 300),2)
               break
        if self.listy[0][0] == self.listy[1][1] == self.listy[2][2] and \
           self.listy[0][0] != None:
            # diagonal left to right
            self.winner = self.listy[0][0]
            pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)

        if self.listy[0][2] == self.listy[1][1] == self.listy[2][0] and \
           self.listy[0][2] != None:
            # diagonal right to left
            self.winner = self.listy[0][2]
            pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)

#yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
simple = Grid()

pygame.init()
board_size = pygame.display.set_mode ((300, 325))
#simple.make_board(board_size)
#white = (255,255,255)
board_size.fill([255, 255, 255])
pygame.display.set_caption ('Tic Tac Toe')
pygame.display.flip()
# create the game board
board = board_size

# main event loop
running = 1

while (running == 1):
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


#though hath been yote

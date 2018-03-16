import pygame
from pygame.locals import *

class BigGrid():

    def __init__(self, listy=[[None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None], \
                              [None,None,None,None,None,None,None,None,None]], \
                              xo='X', winner = None, winsquare = [[0,0,0], \
                                                                  [0,0,0], \
                                                                  [0,0,0]]):
        #self.background = background
        self.listy = listy
        self.xo = xo
        self.winner = winner
        self.winsquare = winsquare

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

        if mX < 100:
            column = 0
        elif mX < 200:
            column = 1
        elif mX < 300:
            column = 2
        elif mX < 400:
            column = 3
        elif mX < 500:
            column = 4
        elif mX < 600:
            column = 5
        elif mX < 700:
            column = 6
        elif mX < 800:
            column = 7
        else:
            column = 8
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
        #print(mX,mY)
        (row,column) = self.position(mX,mY)
        if self.listy[row][column] == 'X' or self.listy[row][column] == 'O':
            return
        self.moveDraw(board,row,column,self.xo)

        if self.xo == 'X':
            self.xo = 'O'
        else:
            self.xo = 'X'

    def winnerwinnerchickendinner(self,board):
        #horiz lil wins
        for h in range(9):
            for j in range(3):
                if self.listy[h][3*j]=='X' and self.listy[h][3*j+1]=='X' and self.listy[h][3*j+2]=='X' and self.winsquare[h//3][j] == 0:

                    self.winsquare[h//3][j] += 1
                    pygame.draw.line (board, (250,0,0), (15+(300*j),50+(100*h)), (285+(300*j),50+(100*h)), 15)
                    xCenter = 150 + 300*j
                    yCenter = 150 + 300*(h//3)
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter-100), \
                                           (xCenter+100,yCenter+100),7)
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter+100), \
                                           (xCenter+100,yCenter-100),7)
                elif self.listy[h][3*j]=='O' and self.listy[h][3*j+1]=='O' and self.listy[h][3*j+2]=='O' and self.winsquare[h//3][j] == 0:

                    self.winsquare[h//3][j] += 2
                    pygame.draw.line (board, (250,0,0), (15+(300*j),50+(100*h)), (285+(300*j),50+(100*h)), 15)
                    xCenter = 150 + 300*j
                    yCenter = 150 + 300*(h//3)
                    pygame.draw.circle(board, (145,255,187),(xCenter,yCenter),120,7)
        #vert lil wins
        for h in range(9):
            for j in range(3):
                if self.listy[3*j][h]=='X' and self.listy[3*j+1][h]=='X' and self.listy[3*j+2][h]=='X' and self.winsquare[j][h//3] == 0:

                    self.winsquare[j][h//3] += 1
                    pygame.draw.line (board, (250,0,0), (50+(100*h),15+(300*j)), (50+(100*h),285+(300*j)), 15)
                    xCenter = 150 + 300*(h//3)
                    yCenter = 150 + 300*j
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter-100), \
                                           (xCenter+100,yCenter+100),7)
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter+100), \
                                           (xCenter+100,yCenter-100),7)
                elif self.listy[3*j][h]=='O' and self.listy[3*j+1][h]=='O' and self.listy[3*j+2][h]=='O' and self.winsquare[j][h//3] == 0:

                    self.winsquare[j][h//3] += 2
                    pygame.draw.line (board, (250,0,0), (50+(100*h),15+(300*j)), (50+(100*h),285+(300*j)), 15)
                    xCenter = 150 + 300*(h//3)
                    yCenter = 150 + 300*j
                    pygame.draw.circle(board, (145,255,187),(xCenter,yCenter),120,7)
        #l to r diag wins
        for h in range(3):
            for j in range(3):
                if self.listy[3*h][3*j]=='X' and self.listy[3*h+1][3*j+1]=='X' and self.listy[3*h+2][3*j+2]=='X' and self.winsquare[h][j] == 0:

                    pygame.draw.line (board, (250,0,0), (15+(300*j),15+(300*h)), (285+(300*j),285+(300*h)), 15)
                    self.winsquare[h][j] += 1
                    xCenter = 150 + 300*(j)
                    yCenter = 150 + 300*h
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter-100), \
                                           (xCenter+100,yCenter+100),7)
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter+100), \
                                           (xCenter+100,yCenter-100),7)


                elif self.listy[3*h][3*j]=='O' and self.listy[3*h+1][3*j+1]=='O' and self.listy[3*h+2][3*j+2]=='O' and self.winsquare[h][j] == 0:

                    pygame.draw.line (board, (250,0,0), (15+(300*j),15+(300*h)), (285+(300*j),285+(300*h)), 15)
                    self.winsquare[h][j] += 2
                    xCenter = 150 + 300*(j)
                    yCenter = 150 + 300*h
                    pygame.draw.circle(board, (145,255,187),(xCenter,yCenter),120,7)

        #r to l diag wins
        for h in range(3):
            for j in range(3):
                if self.listy[3*h+2][3*j]=='X' and self.listy[3*h+1][3*j+1]=='X' and self.listy[3*h][3*j+2]=='X' and self.winsquare[h][j] == 0:

                    pygame.draw.line (board, (250,0,0), (285+(300*j),15+(300*h)), (15+(300*j),285+(300*h)), 15)
                    self.winsquare[h][j] += 1
                    xCenter = 150 + 300*(h)
                    yCenter = 150 + 300*j
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter-100), \
                                           (xCenter+100,yCenter+100),7)
                    pygame.draw.line(board,(232,132,255),(xCenter-100,yCenter+100), \
                                           (xCenter+100,yCenter-100),7)

                elif self.listy[3*h+2][3*j]=='O' and self.listy[3*h+1][3*j+1]=='O' and self.listy[3*h][3*j+2]=='O' and self.winsquare[h][j] == 0:

                    pygame.draw.line (board, (250,0,0), (285+(300*j),15+(300*h)), (15+(300*j),285+(300*h)), 15)
                    self.winsquare[h][j] += 2
                    xCenter = 150 + 300*(h)
                    yCenter = 150 + 300*j
                    pygame.draw.circle(board, (145,255,187),(xCenter,yCenter),120,7)

        #BIG ROW WIN
        for i in range(3):
            if self.winsquare[0][i] == 1 and self.winsquare[1][i] == 1 and self.winsquare[2][i] == 1 and self.winner == None:
                self.winner = 'X'
                pygame.draw.line (board, (255,136,0), (150+(i*300),0), (150+(i*300),900),20)
            elif self.winsquare[0][i] == 2 and self.winsquare[1][i] == 2 and self.winsquare[2][i] == 2 and self.winner == None:
                self.winner = 'O'
                pygame.draw.line (board, (255,136,0), (150+(i*300),0), (150+(i*300),900),20)
        #BIG COL WIN
        for i in range(3):
            if self.winsquare[i][0] == 1 and self.winsquare[i][1] == 1 and self.winsquare[i][2] == 1 and self.winner == None:
                self.winner = 'X'
                pygame.draw.line (board, (255,136,0), (0,150+(i*300)), (900,150+(i*300)),20)
            elif self.winsquare[i][0] == 2 and self.winsquare[i][1] == 2 and self.winsquare[i][2] == 2 and self.winner == None:
                self.winner = 'O'
                pygame.draw.line (board, (255,136,0), (0,150+(i*300)), (900,150+(i*300)),20)

        #BIG L TO R DIAG WIN
        if self.winsquare[0][0] == 1 and self.winsquare[1][1] == 1 and self.winsquare[2][2] == 1 and self.winner == None:
            self.winner = 'X'
            pygame.draw.line (board, (255,136,0), (0, 0), (900, 900), 20)
        elif self.winsquare[0][0] == 2 and self.winsquare[1][1] == 2 and self.winsquare[2][2] == 2 and self.winner == None:
            self.winner = 'O'
            pygame.draw.line (board, (255,136,0), (0, 0), (900, 900), 20)



        #BIG R TO L DIAG WIN
        if self.winsquare[0][2] == 1 and self.winsquare[1][1] == 1 and self.winsquare[2][0] == 1 and self.winner == None:
            self.winner = 'X'
            pygame.draw.line (board, (255,136,0), (900, 0), (0, 900), 20)
        elif self.winsquare[0][2] == 2 and self.winsquare[1][1] == 2 and self.winsquare[2][0] == 2 and self.winner == None:
            self.winner = 'O'
            pygame.draw.line (board, (255,136,0), (900, 0), (0, 900), 20)




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

#Blake Kim kimx5227

#I understand that this is a graded, individual examination that may not be
#discussed with anyone. I also understand that obtaining solutions or
#partial solutions from outside sources, or discussing
#any aspect of the examination with anyone will result in failing the course.
#I further certify that this program represents my own work and that none of
#it was obtained from any source other than material presented as part of the
#course.
import turtle
import random

#Initializes and sets up the turtle board and grid
def initiate(turtle_object):
    turtle.tracer(0)
    turtle.setworldcoordinates(0,0,100,100)
    turtle.penup()
    turtle.speed(0)
    turtle.color('green')
    turtle.shape('square')
    turtle.turtlesize(3,3,1)

#Prints the numbers on the side of the board
def printboard(turtle_object):
    countrow=15
    countcolumn=15
    rownum=82.5
    columnnum=14
    value=0
    while countrow<=85:
        while countcolumn<=85:
            turtle.goto(countrow,countcolumn)
            turtle.shape('square')
            turtle.stamp()
            countcolumn+=9.84
        countcolumn=15
        countrow+=9.84
    turtle.hideturtle()
    while rownum>10:
        turtle.goto(5,rownum)
        turtle.write(value,False,font=("Arial",20,"normal"))
        value+=1
        rownum-=9.84
    value=0
    while columnnum<87.5:
        turtle.goto(columnnum,90)
        turtle.write(value,False,font=("Arial",20,"normal"))
        value+=1
        columnnum+=9.84

def boardmatrix():
    matrix=[]
    for i in range(8):
        row=[]
        for j in range(8):
            row.append('0')
        matrix.append(row)
    matrix[3][3]="1"
    matrix[4][4]="1"
    matrix[3][4]="2"
    matrix[4][3]="2"
    return matrix

#creates and stamps the initial pieces on the board
def showMatrix(turtle_object, board):
    indexrow=0
    indexcolumn=0
    while indexrow<len(board):
        rowcoordinate=83.88-indexrow*9.84
        while indexcolumn<len(board):
            columncoordinate=15+indexcolumn*9.84
            turtle.goto(rowcoordinate,columncoordinate)
            if board[indexrow][indexcolumn]=="1":
                turtle.color('white')
                turtle.stamp()
            elif board[indexrow][indexcolumn]=="2":
                turtle.color('black')
                turtle.stamp()
            indexcolumn+=1
        indexcolumn=0
        indexrow+=1

#checks each row,column, and diagonal manuelly and returns a list of valid moves
def getValidMoves(board,color):
    validmoves=[]
    eliminatedrepeats=[]
    humanpieces=[]
    rowcount=0
    columncount=0
    if color=='2':
        flipped='1'
    else:
        flipped='2'
    while rowcount<len(board):
        while columncount<len(board):
            if board[rowcount][columncount]==color:
                pieces=(rowcount,columncount)
                humanpieces.append(pieces)
            columncount+=1
        columncount=0
        rowcount+=1
    for movetuple in humanpieces:
        storedrow=int(movetuple[0])
        storedcolumn=int(movetuple[1])
        row=storedrow
        column=storedcolumn
        again=True
        if row==0:
            if column==0:
                row+=1
                if board[row][column]==flipped:
                    while board[row][column]!="0" and row<7 and board[row][column]!=color:
                        row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0" and board[row-1][column]!=color:
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column<7 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0" and board[row][column-1]!=color:
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                column+=1
                row+=1
                if row<7 and column<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row<7 and column<7 and board[row][column]!=color:
                            column+=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column<=7 and board[row-1][column-1]!="0" and board[row-1][column-1]!=color:
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            elif column==7:
                row+=1
                if board[row][column]==flipped:
                    while board[row][column]!="0" and row<7 and board[row][column]!=color:
                        row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0" and board[row-1][column]!=color:
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column>0 and board[row][column]!=color:
                        column-=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0" and board[row][column+1]!=color:
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                column-=1
                row+=1
                if column>0 and row<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row<7 and column>0 and board[row][column]!=color:
                            column-=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column>=0 and board[row-1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            else:
                row+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row<7 and board[row][column]!=color:
                        row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column>0 and board[row][column]!=color:
                        column-=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                column+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column<7 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row+=1
                column-=1
                if row<7 and column>0:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row<7 and column>0 and board[row][column]!=color:
                            column-=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column>=0 and board[row-1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                row+=1
                column+=1
                if row<7 and column<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row<7 and column<7 and board[row][column]!=color:
                            column+=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column<=7 and board[row-1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
        elif row==7:
            if column==0:
                row-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row>0 and board[row][column]!=color:
                        row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column<7 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row-=1
                column+=1
                if row>0 and column<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row>0 and column<7 and board[row][column]!=color:
                            column+=1
                            row-=1
                        if board[row][column]=='0' and row>=0 and column<=7 and board[row+1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            elif column==7:
                column-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column>0 and board[row][column]!=color:
                        column-=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row>0 and board[row][column]!=color:
                        row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row=storedrow
                column-=1
                row-=1
                if row>0 and column>0:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row>0 and column>0 and board[row][column]!=color:
                            column-=1
                            row-=1
                        if board[row][column]=='0' and row>=0 and column>=0 and board[row+1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            else:
                row-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row>0 and board[row][column]!=color:
                        row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column<7 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                column-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column>0 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row-=1
                column+=1
                if row>0 and column<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row>0 and column<7 and board[row][column]!=color:
                            column+=1
                            row-=1
                        if board[row][column]=='0' and row>=0 and column<=7 and board[row+1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                column=storedcolumn
                row=storedrow
                row+=1
                column-=1
                if row<7 and column>0:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and column>0 and row<7 and board[row][column]!=color:
                            column-=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column>=0 and board[row-1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
        else:
            if column==0:
                column+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column<7 and board[row][column]!=color:
                        column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row<7 and board[row][column]!=color:
                        row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                row-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row>0 and board[row][column]!=color:
                        row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column+=1
                row+=1
                if row<7 and column<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and column<7 and row<7 and board[row][column]!=color:
                                column+=1
                                row+=1
                        if board[row][column]=='0' and column<=7 and row<=7 and board[row-1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                column+=1
                row-=1
                if column<7 and row>0:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and column<7 and row>0 and board[row][column]!=color:
                            column+=1
                            row-=1
                        if board[row][column]=='0' and column<=7 and row>=0 and board[row+1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            elif column==7:
                column-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and column>0 and board[row][column]!=color:
                        column-=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                column=storedcolumn
                row+=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row<7 and board[row][column]!=color:
                        row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                row-=1
                if board[row][column]==flipped:
                    while board[row][column]!='0' and row>0 and board[row][column]!=color:
                        row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column-=1
                row+=1
                if column>0 and row<7:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and row<7 and column>0 and board[row][column]!=color:
                            column-=1
                            row+=1
                        if board[row][column]=='0' and row<=7 and column>=0 and board[row-1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                column-=1
                row-=1
                if column>0 and row>0:
                    if board[row][column]==flipped:
                        while board[row][column]!='0' and column>0 and row>0 and board[row][column]!=color:
                            column-=1
                            row-=1
                        if board[row][column]=='0' and column>=0 and row>=0 and board[row+1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
            else:
                row+=1
                if board[row][column]==flipped:
                    while row<7 and again:
                        if board[row][column]=='0' and board[row-1][column]!=color:
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                            again=False
                        elif board[row][column]=='0' and board[row-1][column]==color:
                            again=False
                        elif board[row][column]==color:
                            again=False
                        else:
                            row+=1
                    if board[row][column]=='0' and row<=7 and board[row-1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                again=True
                column+=1
                if board[row][column]==flipped:
                    while column<7 and again:
                        if board[row][column]=='0' and board[row][column-1]!=color:
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                            again=False
                        elif board[row][column]=='0' and board[row][column-1]==color:
                            again=False
                        elif board[row][column]==color:
                            again=False
                        else:
                            column+=1
                    if board[row][column]=='0' and column<=7 and board[row][column-1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                again=True
                column+=1
                row+=1
                if row<7 and column<7:
                    if board[row][column]==flipped:
                        while row<7 and column<7 and again:
                            if board[row][column]=='0' and board[row-1][column-1]!=color:
                                posstuple=(row,column)
                                validmoves.append(posstuple)
                                again=False
                            elif board[row][column]=='0' and board[row-1][column-1]==color:
                                again=False
                            elif board[row][column]==color:
                                again=False
                            else:
                                column+=1
                                row+=1
                        if board[row][column]=='0' and row<=7 and column<=7 and board[row-1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                again=True
                column-=1
                row-=1
                if row>0 and column>0:
                    if board[row][column]==flipped:
                        while row>0 and column>0 and again:
                            if board[row][column]=='0' and board[row+1][column+1]!=color:
                                posstuple=(row,column)
                                validmoves.append(posstuple)
                                again=False
                            elif board[row][column]=='0' and board[row+1][column+1]==color:
                                again=False
                            elif board[row][column]==color:
                                again=False
                            else:
                                column-=1
                                row-=1
                        if board[row][column]=='0' and row>=0 and column>=0 and board[row+1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                again=True
                column+=1
                row-=1
                if column<7 and row>0:
                    if board[row][column]==flipped:
                        while row>0 and column<7 and again:
                            if board[row][column]=='0' and board[row+1][column-1]!=color:
                                posstuple=(row,column)
                                validmoves.append(posstuple)
                                again=False
                            elif board[row][column]=='0' and board[row+1][column-1]==color:
                                again=False
                            elif board[row][column]==color:
                                again=False
                            else:
                                column+=1
                                row-=1
                        if board[row][column]=='0' and row>=0 and column<=7 and board[row+1][column-1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                again=True
                row=storedrow
                column=storedcolumn
                column-=1
                row+=1
                if column>0 and row<7:
                    if board[row][column]==flipped:
                        while row<7 and column>0 and again:
                            if board[row][column]=='0' and board[row-1][column+1]!=color:
                                posstuple=(row,column)
                                validmoves.append(posstuple)
                                again=False
                            elif board[row][column]=='0' and board[row-1][column+1]==color:
                                again=False
                            elif board[row][column]==color:
                                again=False
                            else:
                                column-=1
                                row+=1
                        if board[row][column]=='0' and row<=7 and column>=0 and board[row-1][column+1]!="0":
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                column=storedcolumn
                row=storedrow
                row-=1
                again=True
                if board[row][column]==flipped:
                    while row>0 and again:
                        if board[row][column]=='0' and board[row+1][column]!=color:
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                            again=False
                        elif board[row][column]=='0' and board[row+1][column]==color:
                            again=False
                        elif board[row][column]==color:
                            again=False
                        else:
                            row-=1
                    if board[row][column]=='0' and row>=0 and board[row+1][column]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
                row=storedrow
                column=storedcolumn
                column-=1
                again=True
                if board[row][column]==flipped:
                    while column>0 and again:
                        if board[row][column]=='0' and board[row][column+1]!=color:
                            posstuple=(row,column)
                            validmoves.append(posstuple)
                            again=False
                        elif board[row][column]=='0' and board[row][column+1]==color:
                            again=False
                        elif board[row][column]==color:
                            again=False
                        else:
                            column-=1
                    if board[row][column]=='0' and column>=0 and board[row][column+1]!="0":
                        posstuple=(row,column)
                        validmoves.append(posstuple)
    for movetuple in validmoves:
        if movetuple not in eliminatedrepeats:
            eliminatedrepeats.append(movetuple)
    return eliminatedrepeats

#randomly selects the next move
def selectNextPlay(board):
    white='1'
    validmoves=getValidMoves(board,white)
    nummoves=len(validmoves)
    if nummoves==1:
        turn=validmoves[0]
    else:
        choice=random.randint(0,nummoves-1)
        turn=validmoves[choice]
    return turn

#creates list of pieces that need to be appended
def append(flip):
    newflip=[]
    for piece in flip:
        row=piece[0]
        column=piece[1]
        piecetuple=(row,column)
        newflip.append(piecetuple)
    return newflip

#checks valid moves compared to inputted moves
def isValidMove(board,row,col,color):
    validmoves=getValidMoves(board,color)
    if row.isdigit()==False or col.isdigit()==False:
        return False
    move=(int(row),int(col))
    if move in validmoves:
        return True
    else:
        return False

#updates the board by stamping the new columns
def update(board,turn,color,turtle_object):
    if color=="2":
        storedrow=int(turn[0])
        storedcolumn=int(turn[2])
    else:
        storedrow=int(turn[0])
        storedcolumn=int(turn[1])
    row=storedrow
    column=storedcolumn
    flip=[]
    newflip=[]
    newboard=board
    fliptuple=(storedrow,storedcolumn)
    newflip.append(fliptuple)
    repeat=True
    if color=="2":
        opposite="1"
    else:
        opposite="2"
    if row==0:
        if column==0:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            repeat=True
            column=storedcolumn
            row+=1
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            repeat=True
            row+=1
            column+=1
            while column<len(board) and row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) and row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        elif column==len(board)-1:
            column-=1
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            repeat=True
            row+=1
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            repeat=True
            column-=1
            row-=1
            while row>=0 and column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        else:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            column-=1
            repeat=True
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            row+=1
            repeat=True
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            row+=1
            column+=1
            repeat=True
            while column<len(board) and row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            row+=1
            column-=1
            repeat=True
            while column>=0 and row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board) or column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
    elif row==len(board)-1:
        if column==0:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            row-=1
            repeat=True
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column+=1
            row-=1
            repeat=True
            while column<len(board) and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) and row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        elif column==len(board)-1:
            column-=1
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            row-=1
            repeat=True
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column-=1
            row-=1
            repeat=True
            while column>=0 and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        else:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            column-=1
            repeat=True
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            row-=1
            repeat=True
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            row=storedrow
            row-=1
            column+=1
            repeat=True
            if row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            while column<len(board) and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            repeat=True
            row-=1
            column-=1
            while column>=0 and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
    else:
        if column==0:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            repeat=True
            column=storedcolumn
            row+=1
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            repeat=True
            row-=1
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            repeat=True
            column+=1
            row-=1
            while column<len(board) and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            repeat=True
            column+=1
            row+=1
            while column<len(board) and row<len(board)and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        elif column==len(board)-1:
            column-=1
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            repeat=True
            row+=1
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            row-=1
            repeat=True
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            row-=1
            column-=1
            repeat=True
            while column>=0 and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            row+=1
            column-=1
            repeat=True
            while row<len(board) and column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
        else:
            column+=1
            while column<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            repeat=True
            column-=1
            while column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            column=storedcolumn
            repeat=True
            row+=1
            while row<len(board) and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            row-=1
            repeat=True
            while row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            row-=1
            column-=1
            repeat=True
            while column>=0 and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==0 or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            row+=1
            column-=1
            repeat=True
            while row<len(board) and column>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column-=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if row==len(board) or column==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            repeat=True
            column+=1
            row-=1
            while column<len(board) and row>=0 and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row-=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==0:
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
            row=storedrow
            column=storedcolumn
            repeat=True
            column+=1
            row+=1
            while column<len(board) and row<len(board)and repeat:
                if board[row][column]==opposite:
                    fliptuple=(row,column)
                    flip.append(fliptuple)
                    column+=1
                    row+=1
                elif board[row][column]=="0":
                    flip=[]
                    repeat=False
                else:
                    repeat=False
            if column==len(board) or row==len(board):
                flip=[]
            else:
                newflip+=append(flip)
                flip=[]
    if color=="2":
        turtle.color('black')
    if color=='1':
        turtle.color('white')
    for piece in newflip:
        row=piece[0]
        column=piece[1]
        newboard[row][column]=color
        columncoordinate=83.88-row*9.84
        rowcoordinate=15+column*9.84
        turtle.goto(rowcoordinate,columncoordinate)
        turtle.stamp()
    return newboard

#checks input to make sure that it is correctly formatted
def stripinput(string):
    newinput=""
    count=0
    index=0
    while count<1:
        while index<len(string) and count<1:
            char=string[index]
            if char.isdigit():
                count+=1
                newinput+=char
            index+=1
        count+=1
    newinput+=","
    while count<=2:
        while index<len(string):
            char=string[index]
            if char.isdigit():
                count+=1
                newinput+=char
            index+=1
        count+=1
    return newinput

#wait function that delays computer's move
def wait():
    wait=0
    return wait

#counts pieces for each board color
def total(board):
    total=[]
    humantotal=0
    computertotal=0
    for row in board:
        for column in row:
            if column=="1":
                computertotal+=1
            elif column=="2":
                humantotal+=1
    total.append(computertotal)
    total.append(humantotal)
    return total

def main():
    turtle_object=turtle.Turtle()
    turtle_object.getscreen()
    initiate(turtle_object)
    printboard(turtle_object)
    board=boardmatrix()
    turtle.shape("circle")
    showMatrix(turtle_object, board)
    gameover=False
    while gameover==False:
        black='2'
        white='1'
        blackmoves=getValidMoves(board,black)
        whitemoves=getValidMoves(board,white)
        print(blackmoves,"blackmoves")
        print(whitemoves,"whitemoves")
        loop=0
        repeat=False
        moreinput=True
        event=False
        if len(blackmoves)>0:
            blackpossible=True
        else:
            blackpossible=False
        if len(whitemoves)>0:
            whitepossible=True
        else:
            whitepossible=False
        while moreinput and blackpossible:
            if repeat and loop>0:
                humanturn=turtle.textinput("Invalid option",humanturn +" isn't a valid input. Please renter the row and column")
                correctedturn=stripinput(humanturn)
            else:
                humanturn=turtle.textinput("Your turn","Enter a row and column in the form(row,column): ")
                correctedturn=stripinput(humanturn)
            if humanturn=="":
                moreinput=False
                gameover=True
                humanturn="endgame"
            elif len(humanturn)==3 and humanturn==correctedturn:
                row=humanturn[0]
                col=humanturn[2]
                if isValidMove(board,row,col,black):
                    board=update(board,humanturn,black,turtle_object)
                    turtle.update()
                    moreinput=False
                else:
                    repeat=True
                    loop+=1
            else:
                repeat=True
                loop+=1
        moreinput=True
        if whitepossible and humanturn!="":
            turn=selectNextPlay(board)
            board=update(board,turn,white,turtle_object)
            turtle.ontimer(wait(),500)
            turtle.update()
        completeboard=total(board)
        computertotal=completeboard[0]
        humantotal=completeboard[1]
        if completeboard[0]+completeboard[1]==64:
            gameover=True
        elif whitepossible==False and blackpossible==False:
            gameover=True
        if humanturn=="":
            print("You have ended the game early. Thanks for playing!")
            gameover=True
        elif computertotal>humantotal and gameover:
            print("You lost. The score was Computer:",computertotal, "You:",humantotal)
        elif humantotal>computertotal and gameover:
            print("You Won! The score was You:",humantotal,"Computer:",computertotal)
        elif humantotal+computertotal!=64 and gameover:
            print("Both sides don't have any moves: The score was You:", humantotal,"Computer:",computertotal)
if __name__ == '__main__':
    main()

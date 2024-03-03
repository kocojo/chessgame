class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
class info:
    def __init__(self):
        self.board = [
             ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
             ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
             ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['--', '--', '--', '--', '--', '--', '--', '--'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.moveLog = Stack()
        self.Wking_postion = (7,4)
        self.Bking_postion = (0,4)
        self.Woo = True
        self.Boo = True
        self.Wo0o = True
        self.Bo0o = True
    def check_r(self,pos1,pos2):
        check = True
        if pos1 != pos2:
            if pos1[0] == pos2[0]:
                if pos1[1]>pos2[1]:
                    a = pos1[1]
                    b = pos2[1]+1
                else:
                    a = pos2[1]
                    b = pos1[1]+1
                for i in range(b,a):
                    if self.board[pos1[0]][i]!="--":
                        k= self.board[pos1[0]][i]
                        check = False
                        break
                if self.board[pos2[0]][pos2[1]][0] == self.board[pos1[0]][pos1[1]][0]:
                    check = False
            elif pos1[1] == pos2[1]:
                if pos1[0] > pos2[0]:
                    a = pos1[0]
                    b = pos2[0]+1
                else:
                    a = pos2[0]
                    b = pos1[0]+1
                for i in range(b,a):
                    if self.board[i][pos1[1]] != "--":
                        check = False
                        break
                if self.board[pos2[0]][pos2[1]][0] == self.board[pos1[0]][pos1[1]][0]:
                    check = False
            else:
                check = False
            return check
        else:
            return False
    def rook(self,pos1):
        result =[]
        a = [True,True,True,True]
        for i in range(1,8):
           if a[0] == True:
               if (pos1[0]+i)<8 and self.board[pos1[0]+i][pos1[1]] =="--":
                   result.append((pos1[0]+i,pos1[1]))
               elif (pos1[0]+i)<8 and self.board[pos1[0]+i][pos1[1]][0] != self.board[pos1[0]][pos1[1]][0]:
                   result.append((pos1[0]+i,pos1[1]))
                   a[0] = False
               else:
                    a[0] = False
           if a[1] == True:
               if (pos1[0]-i)>=0 and self.board[pos1[0]-i][pos1[1]] =="--":
                   result.append((pos1[0]-i,pos1[1]))
               elif (pos1[0]-i)>=0 and self.board[pos1[0]-i][pos1[1]][0] != self.board[pos1[0]][pos1[1]][0]:
                   result.append((pos1[0]-i,pos1[1]))
                   a[1] = False
               else:
                    a[1] = False
           if a[2] == True:
               if (pos1[1]-i)>=0 and self.board[pos1[0]][pos1[1]-i] =="--":
                   result.append((pos1[0],pos1[1]-i))
               elif (pos1[1]-i)>=0 and self.board[pos1[0]][pos1[1]-i][0] != self.board[pos1[0]][pos1[1]][0]:
                   result.append((pos1[0],pos1[1]-i))
                   a[2] = False
               else:
                    a[2] = False
           if a[3] == True:
               if (pos1[1]+i)<8 and self.board[pos1[0]][pos1[1]+i] =="--":
                   result.append((pos1[0],pos1[1]+i))
               elif (pos1[1]+i)<8 and self.board[pos1[0]][pos1[1]+i][0] != self.board[pos1[0]][pos1[1]][0]:
                   result.append((pos1[0],pos1[1]+i))
                   a[3] = False
               else:
                    a[3] = False
        return result
    def check_b(self,pos1):
        result = []
        a =[True,True,True,True]
        for i in range(8):
            for i in range(1, 8):
                if a[0] == True:
                    if (pos1[1] + i) < 8 and (pos1[0] + i) < 8 and self.board[pos1[0] + i][pos1[1] + i] == "--":
                        result.append((pos1[0] + i, pos1[1] + i))
                    elif (pos1[1] + i)<8 and  (pos1[0] + i) < 8 and self.board[pos1[0] + i][pos1[1] + i][0] != self.board[pos1[0]][pos1[1]][0]:
                        result.append((pos1[0] + i, pos1[1] + i))
                        a[0] = False
                    else:
                        a[0] = False
                if a[1] == True:
                    if (pos1[1]+i) <8 and (pos1[0] - i) >= 0 and self.board[pos1[0] - i][pos1[1] + i] == "--":
                        result.append((pos1[0] - i, pos1[1] + i ))
                    elif (pos1[1]+i) <8 and (pos1[0] - i) >= 0 and self.board[pos1[0] - i][pos1[1] + i][0] != self.board[pos1[0]][pos1[1]][0]:
                        result.append((pos1[0] - i, pos1[1] + i ))
                        a[1] = False
                    else:
                        a[1] = False
                if a[2] == True:
                    if (pos1[0] + i)< 8 and (pos1[1] - i) >= 0 and self.board[pos1[0] + i][pos1[1] - i] == "--":
                        result.append((pos1[0] + i, pos1[1] - i))
                    elif (pos1[0] + i)< 8 and (pos1[1] - i) >= 0 and self.board[pos1[0]+i][pos1[1] - i][0] != self.board[pos1[0]][pos1[1]][0]:
                        result.append((pos1[0] + i, pos1[1] - i))
                        a[2] = False
                    else:
                        a[2] = False
                if a[3] == True:
                    if (pos1[0] - i)>= 0 and (pos1[1] - i) >=0 and self.board[pos1[0] - i][pos1[1] - i] == "--":
                        result.append((pos1[0] -i , pos1[1] - i))
                    elif (pos1[0] - i)>= 0 and (pos1[1] - i) >=0 and self.board[pos1[0] - i][pos1[1] - i][0] != self.board[pos1[0]][pos1[1]][0]:
                        result.append((pos1[0]-i, pos1[1] - i))
                        a[3] = False
                    else:
                        a[3] = False
        return result
    def check_K(self,pos1):
        pos = [(pos1[0]+1,pos1[1]+1),(pos1[0]-1,pos1[1]-1),(pos1[0]+1,pos1[1]-1),(pos1[0]-1,pos1[1]+1),(pos1[0]+1,pos1[1]),(pos1[0]-1,pos1[1]),(pos1[0],pos1[1]+1),(pos1[0],pos1[1]-1)]
        result = []
        for pos2 in pos:
            if pos2[0] < 8 and pos2[0] >= 0 and pos2[1] < 8 and pos2[1] >= 0:
                if self.board[pos2[0]][pos2[1]][0] != self.board[pos1[0]][pos1[1]][0]:
                    result.append(pos2)
        oo = True
        o0o = True
        if not ((pos1==(0,4) and self.board[pos1[0]][pos1[1]][0]=='b' and self.check_r((0,7),(0,5))) or (pos1==(7,4) and self.board[pos1[0]][pos1[1]][0]=='w' and self.check_r((7,7),(7,5)))):
            oo = False
        if not ((pos1 == (0, 4) and self.board[pos1[0]][pos1[1]][0] == 'b' and self.check_r((0, 0), (0, 3))) or (pos1 == (7, 4) and self.board[pos1[0]][pos1[1]][0] == 'w' and self.check_r((7, 0), (7, 3)))):
            o0o = False
        if oo or o0o:
            for i in self.moveLog.items:
                if i[0]==pos1 or (i == (pos1,"oo") or i == (pos1,"o0o")):
                    oo=False
                    o0o=False
                if i[0] == (pos1[0],pos1[1]+3) or i[1] == (pos1[0],pos1[1]+3):
                    oo = False
                if i[0]==(pos1[0],pos1[1]-4) or i[1] == (pos1[0],pos1[1]-4):
                    o0o=False
                if not (oo or o0o):
                    break
        if oo:
            result.append('oo')
        if o0o:
            result.append('o0o')
        return result
    def check_Q(self,pos1):
        return self.check_b(pos1)+self.rook(pos1)
    def check_p(self,pos1):
        result = []
        try:
            if (self.board[pos1[0]][pos1[1]][0] != self.board[pos1[0]+1][pos1[1]+1][0]) and (self.board[pos1[0]+1][pos1[1]+1][0] == "w"):
                result.append((pos1[0]+1,pos1[1]+1))
        except:
            pass
        try:
            if (self.board[pos1[0]][pos1[1]][0] != self.board[pos1[0]+1][pos1[1]-1][0]) and (self.board[pos1[0]+1][pos1[1]-1][0] == "w") and pos1[1]>0:
                result.append((pos1[0]+1,pos1[1]-1))
        except:
            pass
        try:
            if (self.board[pos1[0]][pos1[1]][0] != self.board[pos1[0]-1][pos1[1]-1][0]) and (self.board[pos1[0]-1][pos1[1]-1][0] == "b") and pos1[1]>0:
                result.append((pos1[0]-1,pos1[1]-1))
        except:
            pass
        try:
            if (self.board[pos1[0]][pos1[1]][0] != self.board[pos1[0]-1][pos1[1]+1][0]) and (self.board[pos1[0]-1][pos1[1]+1][0] == "b"):
                result.append((pos1[0]-1,pos1[1]+1))
        except:
            pass
        if (pos1[0]==1 and self.board[pos1[0]][pos1[1]]=="bp") or (pos1[0]==6 and self.board[pos1[0]][pos1[1]]=="wp"):
            if  self.board[pos1[0]][pos1[1]][0]=="b" and self.board[pos1[0]+1][pos1[1]]=="--" and pos1[0]==1:
                result.append((pos1[0]+1,pos1[1]))
                if self.board[pos1[0]+2][pos1[1]]=="--":
                    result.append((pos1[0] + 2, pos1[1]))
            if  self.board[pos1[0]][pos1[1]][0]=="w" and self.board[pos1[0]-1][pos1[1]]=="--" and pos1[0]==6:
                result.append((pos1[0]-1,pos1[1]))
                if self.board[pos1[0]-2][pos1[1]]=="--":
                    result.append((pos1[0] - 2, pos1[1]))
        else:
            try:
                if self.board[pos1[0]][pos1[1]][0] == "b" and self.board[pos1[0] + 1][pos1[1]] == "--":
                    result.append((pos1[0] + 1, pos1[1]))
            except:
                pass
            try:
                if  self.board[pos1[0]][pos1[1]][0]=="w" and self.board[pos1[0]-1][pos1[1]]=="--":
                    result.append((pos1[0]-1,pos1[1]))
            except:
                pass
        if self.moveLog.items != []:
            if self.board[pos1[0]][pos1[1]][0] == "b":
                if self.moveLog.items[-1] == ((pos1[0] + 2, pos1[1] + 1), (pos1[0], pos1[1] + 1),"--") and \
                        self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]][1] == "p":
                    result.append((pos1[0] + 1, pos1[1] + 1, "bp"))
                elif self.moveLog.items[-1] == ((pos1[0] + 2, pos1[1] - 1), (pos1[0], pos1[1] - 1),"--") and \
                        self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]][1] == "p":
                    result.append((pos1[0] + 1, pos1[1] - 1, "bp"))
            elif self.board[pos1[0]][pos1[1]][0] == "w":
                if self.moveLog.items[-1] == ((pos1[0] - 2, pos1[1] + 1), (pos1[0], pos1[1] + 1),"--") and \
                        self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]][1] == "p":
                    result.append((pos1[0] - 1, pos1[1] + 1, "wp"))
                elif self.moveLog.items[-1] == ((pos1[0] - 2, pos1[1] - 1), (pos1[0], pos1[1] - 1),"--") and \
                        self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]][1] == "p":
                    result.append((pos1[0] - 1, pos1[1] - 1, "wp"))
        new =[]
        for i in range(len(result)):
            if result[i][0] == 7:
                new = new + [(result[i][0],result[i][1],"bQ"),(result[i][0],result[i][1],"bN"),(result[i][0],result[i][1],"bR")]
            if result[i][0] == 0:
                new =  new + [(result[i][0],result[i][1],"wQ"),(result[i][0],result[i][1],"wN"),(result[i][0],result[i][1],"wB"),(result[i][0],result[i][1],"wR")]
        if new != []:
            return new
        else:
            return result
    def check_N(self,pos1):
        pos=[(pos1[0]-2,pos1[1]+1),(pos1[0]-1,pos1[1]-2),(pos1[0]-2,pos1[1]-1),(pos1[0]-1,pos1[1]+2),(pos1[0]+1,pos1[1]+2),(pos1[0]+2,pos1[1]+1),(pos1[0]+2,pos1[1]-1),(pos1[0]+1,pos1[1]-2),]
        result=[]
        for pos2 in pos:
            if pos2[0] < 8 and pos2[0] >= 0 and pos2[1] < 8 and pos2[1] >= 0:
                if self.board[pos2[0]][pos2[1]][0] != self.board[pos1[0]][pos1[1]][0]:
                    result.append(pos2)
        return result
    def check_move(self,pos1):
        a = self.board[pos1[0]][pos1[1]]
        if ((a[0]=="b") and (not self.whiteToMove)) or ((a[0]=="w") and (self.whiteToMove)):
            if a[1]=="R":
                return self.rook(pos1)
            if a[1]=="N":
                return self.check_N(pos1)
            if a[1]=="B":
                return self.check_b(pos1)
            if a[1]=="Q":
                return self.check_Q(pos1)
            if a[1]=="K":
                return self.check_K(pos1)
            if a[1]=="p":
                return self.check_p(pos1)
        else:
            return []
    def save_move_log(self,pos1,pos2):
        self.moveLog.push((pos1,pos2,self.board[pos2[0]][pos2[1]]))
    def undo(self):
        if not self.moveLog.is_empty():
            try:
                if len(self.moveLog.items[-1][1]) == 2:
                    self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]]
                    self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]] = self.moveLog.items[-1][2]
                    if self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] == "wK":
                        self.Wking_postion = (self.moveLog.items[-1][0][0],self.moveLog.items[-1][0][1])
                    elif self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] == "bK":
                        self.Bking_postion = (self.moveLog.items[-1][0][0], self.moveLog.items[-1][0][1])
                    self.whiteToMove = not self.whiteToMove
                    self.moveLog.pop()
                else:
                    if self.moveLog.items[-1][1][2][1]!="p":
                        if self.whiteToMove:
                            self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = "bp"
                            self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]] = self.moveLog.items[-1][2]
                            self.moveLog.pop()
                            self.whiteToMove = not self.whiteToMove
                        else:
                            self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = "wp"
                            self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]] = self.moveLog.items[-1][2]
                            self.moveLog.pop()
                            self.whiteToMove = not self.whiteToMove
                    else:
                        self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]]
                        self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][1][1]] = self.moveLog.items[-1][2]
                        self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]] = "--"
                        self.whiteToMove = not self.whiteToMove
                        self.moveLog.pop()
            except:
                if self.moveLog.items[-1][1]=='oo' and self.whiteToMove:
                    self.board[0][4]='bK'
                    self.board[0][6]='--'
                    self.board[0][5]='--'
                    self.board[0][7]='bR'
                    self.moveLog.pop()
                    self.Bking_postion = (0,4)
                    self.whiteToMove = not self.whiteToMove
                elif self.moveLog.items[-1][1]=='o0o' and self.whiteToMove:
                    self.board[0][4]='bK'
                    self.board[0][2]='--'
                    self.board[0][3]='--'
                    self.board[0][0]='bR'
                    self.moveLog.pop()
                    self.Wking_postion = (7,4)
                    self.whiteToMove = not self.whiteToMove
                elif self.moveLog.items[-1][1]=='o0o' and (not self.whiteToMove):
                    self.board[7][4]='wK'
                    self.board[7][2]='--'
                    self.board[7][3]='--'
                    self.board[7][0]='wR'
                    self.moveLog.pop()
                    self.Bking_postion = (0, 4)
                    self.whiteToMove = not self.whiteToMove
                elif self.moveLog.items[-1][1] == 'oo' and not self.whiteToMove:
                    self.board[7][4] = 'wK'
                    self.board[7][6] = '--'
                    self.board[7][5] = '--'
                    self.board[7][7] = 'wR'
                    self.moveLog.pop()
                    self.Wking_postion = (7, 4)
                    self.whiteToMove = not self.whiteToMove
                elif self.moveLog.items[-1][1][2][1] !="p":
                    if self.whiteToMove:
                        self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = "bp"
                        self.board[self.moveLog.items[-1][1][0][0]][self.moveLog.items[-1][1][0][1]] = self.moveLog.items[-1][2]
                        self.whiteToMove = not self.whiteToMove
                        self.moveLog.pop()
                    else:
                        self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = "wp"
                        self.board[self.moveLog.items[-1][1][0][0]][self.moveLog.items[-1][1][0][1]] = self.moveLog.items[-1][2]
                        self.whiteToMove = not self.whiteToMove
                        self.moveLog.pop()
                else:
                    self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][0][1]] = self.board[self.moveLog.items[-1][1][0]][self.moveLog.items[-1][1][1]]
                    self.board[self.moveLog.items[-1][0][0]][self.moveLog.items[-1][1][1]] = self.moveLog.items[-1][2]
                    self.whiteToMove = not self.whiteToMove
                    self.moveLog.pop()
    def change_Pieces(self,move):
        pos1 = move[0]
        pos2 = move[1]
        if len(pos2)!=3 and pos2[1]!="o":
            self.save_move_log(pos1, pos2)
            self.board[pos2[0]][pos2[1]] = self.board[pos1[0]][pos1[1]]
            self.board[pos1[0]][pos1[1]] = "--"
            if self.board[pos2[0]][pos2[1]] == "bK":
                self.Bking_postion = pos2
            elif self.board[pos2[0]][pos2[1]] == "wK":
                self.Wking_postion = pos2
            self.whiteToMove = not self.whiteToMove
        elif self.board[pos1[0]][pos1[1]][1] == "K" and pos2 == "oo":
            if self.board[pos1[0]][pos1[1]] == "bK":
                self.Bking_postion = (pos1[0],pos1[1]+2)
            elif self.board[pos1[0]][pos1[1]] == "wK":
                self.Wking_postion = (pos1[0],pos1[1]+2)
            self.board[pos1[0]][pos1[1]+2] = self.board[pos1[0]][pos1[1]]
            self.board[pos1[0]][pos1[1]] = "--"
            self.board[pos1[0]][pos1[1] + 1] = self.board[pos1[0]][pos1[1] + 3]
            self.board[pos1[0]][pos1[1] + 3] = "--"
            self.whiteToMove = not self.whiteToMove
            self.moveLog.push((pos1,"oo"))
        elif self.board[pos1[0]][pos1[1]][1] == "K" and pos2 == "o0o":
            if self.board[pos1[0]][pos1[1]] == "bK":
                self.Bking_postion = (pos1[0], pos1[1] - 2)
            elif self.board[pos1[0]][pos1[1]] == "wK":
                self.Wking_postion = (pos1[0], pos1[1] - 2)
            self.board[pos1[0]][pos1[1]-2] = self.board[pos1[0]][pos1[1]]
            self.board[pos1[0]][pos1[1]] = "--"
            self.board[pos1[0]][pos1[1] - 1] = self.board[pos1[0]][pos1[1] - 4]
            self.board[pos1[0]][pos1[1] - 4] = "--"
            self.whiteToMove = not self.whiteToMove
            self.moveLog.push((pos1,"o0o"))
        elif len(pos2) ==3 and pos2[2]!="o":
            if pos2[2][1]!="p":
                self.moveLog.push((pos1, pos2, self.board[pos2[0]][pos2[1]]))
                self.board[pos1[0]][pos1[1]] = "--"
                self.board[pos2[0]][pos2[1]] = pos2[2]
                self.whiteToMove = not self.whiteToMove
            else:
                self.moveLog.push((pos1,(pos2[0],pos2[1],self.board[pos1[0]][pos1[1]]), self.board[pos1[0]][pos2[1]]))
                self.board[pos2[0]][pos2[1]] = self.board[pos1[0]][pos1[1]]
                self.board[pos1[0]][pos1[1]] = "--"
                self.board[pos1[0]][pos2[1]] = "--"
                self.whiteToMove = not self.whiteToMove
    def get_all_move(self):
        result = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j][0] == "w" and self.whiteToMove:
                    a = self.check_move((i,j))
                    for k in a:
                        result.append(((i,j),k))
                if self.board[i][j][0] == "b" and not self.whiteToMove:
                    a = self.check_move((i,j))
                    for k in a:
                        result.append(((i,j),k))
        return result
    def incheck(self):
        test = False
        self.whiteToMove = not self.whiteToMove
        a = self.get_all_move()
        for i in a:
            if self.whiteToMove and i[1][0] == self.Bking_postion[0] and i[1][1] == self.Bking_postion[1]:
                test =True
                break
            elif not self.whiteToMove and i[1][0] == self.Wking_postion[0] and i[1][1] == self.Wking_postion[1]:
                test = True
                break
        self.whiteToMove = not self.whiteToMove
        return test
    def get_all_posible_move(self):
        a = self.get_all_move()
        result = []
        for i in a:
            self.change_Pieces(i)
            self.whiteToMove = not self.whiteToMove
            if not self.incheck():
                result.append(i)
            self.whiteToMove = not self.whiteToMove
            self.undo()
        return result
    def is_stalemate(self):
        if self.get_all_posible_move() ==[] and not self.incheck():
            return True
        else:
            if len(self.moveLog.items)>8 and (self.moveLog.items[-9],self.moveLog.items[-8],self.moveLog.items[-7],self.moveLog.items[-6]) == (self.moveLog.items[-5],self.moveLog.items[-4],self.moveLog.items[-3],self.moveLog.items[-2]) and self.moveLog.items[-1] == self.moveLog.items[-9]:
                return True
            else:
                a = {"bp":False,"bR":False,"bN":False,"bB":False,"bQ":False,"bK":False,"--":False}
                b = {"wR":False,"wp":False,"wB":False,"wN":False,"wQ":False,"wK":False,"--":False}

                for i in range(8):
                    for j in range(8):
                        a[self.board[i][j]] = True
                        b[self.board[i][j]] = True
                a1=0
                b1=0
                for i in a.keys():
                    if a[i] ==True:
                        a1+=1
                        b1+=1
                if a1<2 and b1<2 and b["wQ"]==False and b["wR"] == False and not b["wp"] and a["bQ"] == False and a["bR"] ==False and not a["bp"]:
                    return True
                else:
                    return False
    def is_checkmate(self):
        return True if self.get_all_posible_move() == []  and self.incheck() else False
a = info()
a.change_Pieces(((6, 3), (4, 3)))
a.change_Pieces(((1, 2), (2, 2)))
a.undo()
a.change_Pieces(((0,0),(0,3)))
print(a.board)
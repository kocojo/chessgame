import chess_engine
class note:
    def __init__(self,data,next,board:chess_engine.info):
        self.data = data
        self.next = next
        self.board = board
        self.point = -999
        self.parent =None
class tree:
    def __init__(self):
        self.goc =None
    def addgoc(self, data,next,board):
        self.goc = note(data, next,board)
    def duyet(self, note):
        a = []
        if note.next != []:
            for i in note.next:
                a = a + self.duyet(i)
            a.append(note.data)
            return a
        else:
            return [note.data]
    def add(self, cha, data,turn,board):
            cha.next.append(note(data, [],board))
    def leaf(self,node:note):
        result = []
        if node.next ==[]:
            return [node]
        else:
            for i in node.next:
                result = result+self.leaf(i)
        return result
    def change_root(self,data):
        for i in self.goc.next:
            if i.data == data:
                self.goc = i
                break



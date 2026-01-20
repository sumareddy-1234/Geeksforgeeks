class Solution:
    def __init__(self):
        self.arr=[]
        self.redo_arr=[]
    def append(self, x):
        # append x into document
        self.arr.append(x)
        self.redo_arr.clear()

    def undo(self):
        # undo last change
        if self.arr:
            self.redo_arr.append(self.arr.pop())

    def redo(self):
        # redo changes
        if self.redo_arr:
            self.arr.append(self.redo_arr.pop())

    def read(self):
        # read the document
        return "".join(self.arr)
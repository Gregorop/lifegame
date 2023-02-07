from cell import Cell

class Field:
    def __init__(self,x,y, win, cell_size,w,h):
        self.win = win
        self.x, self.y = x,y

        self.cells = []
        self.create_cells(cell_size,w,h)

    def create_cells(self,cell_size,w,h):
        rows = []
        
        for xn in range(w//cell_size):
            rows.append([])
            for yn in range(h//cell_size):
                rows[xn].append(Cell(self.x+xn*cell_size,self.y+yn*cell_size,cell_size,self.win))
        
        #проставляем связи
        for xn in range(len(rows)):
            for yn in range(len(rows[xn])):
                if xn != 0:
                    if yn != 0:
                        rows[xn][yn].nebgs["lu"] = rows[xn-1][yn-1]
                    if yn != len(rows)-1:
                        rows[xn][yn].nebgs["ld"] = rows[xn-1][yn+1]
                    rows[xn][yn].nebgs["lm"] = rows[xn-1][yn]
                if xn != len(rows)-1:
                    if yn != 0:
                        rows[xn][yn].nebgs["ru"] = rows[xn+1][yn-1]
                    if yn != len(rows)-1:
                        rows[xn][yn].nebgs["rd"] = rows[xn+1][yn+1]
                    rows[xn][yn].nebgs["rm"] = rows[xn+1][yn]
                if yn != 0: rows[xn][yn].nebgs["mu"] = rows[xn][yn-1]
                if yn != len(rows)-1: rows[xn][yn].nebgs["md"] = rows[xn][yn+1]
            
                self.cells.append(rows[xn][yn])

    def draw(self):
        for cell in self.cells:
            cell.draw()
                
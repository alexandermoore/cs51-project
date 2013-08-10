class IntersectSolver :

    self.inter_stack = []
    
    def __init(self,maze) :
        return
        
    def __add_intersect_to_stack(self,maze,pos,last_pos) :
        r = pos[0]
        c = pos[1]
        from_dir = (last_pos[0] - pos[0], last_pos[1] - pos[1])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        inter_lst = []
        for dir in dirs
            if (maze.board[r + dir[0]][c + dir[1]] == True) and (dir != from_dir) :
                inter_lst.append((dir[0], dir[1], False))
        inter_lst.append(from_dir[0],from_dir[1],True)
        
        inter_stack.append((r, c, inter_lst))
        return

        
        
    def __solve(self,maze) :
        return
    
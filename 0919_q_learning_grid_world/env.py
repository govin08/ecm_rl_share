class GridWorld:
    def __init__(self, traps:list, size:int=5):
        self.size = size
        self.start = (0, 0)
        self.goal = (self.size-1, self.size-1)
        self.traps = traps
        self.reset()
        
    def reset(self):
        self.pos = list(self.start)
        return tuple(self.pos)
    
    def step(self, action):
        # 행동: 0=up, 1=down, 2=left, 3=right
        moves = [(-1,0), (1,0), (0,-1), (0,1)]  # UP, DOWN, LEFT, RIGHT
        dx, dy = moves[action]
        
        # 경계 체크 후 이동
        new_x = self.pos[0] + dx
        new_y = self.pos[1] + dy
        new_x = max(0, min(self.size-1, new_x))
        new_y = max(0, min(self.size-1, new_y))
        self.pos = [new_x, new_y]
        
        # 보상 및 종료 여부
        current_pos = tuple(self.pos)
        
        if current_pos == self.goal:
            return current_pos, 10, True  # 목표 도달
        elif current_pos in self.traps:
            return current_pos, -5, True  # 함정에 빠짐 (큰 패널티)
        else:
            return current_pos, -0.1, False  # 일반 이동 비용
    

    def render(self):
        """Grid 시각화"""
        grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        
        # 함정 표시
        for trap in self.traps:
            grid[trap[0]][trap[1]] = 'T'
        
        # 목표 표시
        grid[self.goal[0]][self.goal[1]] = 'G'
        
        # 에이전트 표시
        grid[self.pos[0]][self.pos[1]] = 'A'
        
        print("\nGrid World:")
        print("A: Agent, G: Goal, T: Trap, .: Empty")
        for row in grid:
            print(' '.join(row))
        print()
class GridWorld:
    def __init__(self):
        self.rows = 3
        self.cols = 4
        self.actions = ['U', 'D', 'L', 'R']  # Up, Down, Left, Right
        
        # (row, col) 형식 (0-based indexing)
        self.start = (0, 0)
        self.wall = (1, 1)
        self.terminals = {(1, 3): -1, (2, 3): 1}  # state: reward
        self.step_reward = -0.1
        self.gamma = 0.9
        
    def get_states(self):
        """벽과 터미널을 제외한 모든 상태"""
        states = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) != self.wall:
                    states.append((r, c))
        return states
    
    def is_terminal(self, state):
        return state in self.terminals
    
    def get_next_state(self, state, action):
        """행동에 따른 다음 상태 반환"""
        if self.is_terminal(state):
            return state
        
        r, c = state
        if action == 'U':
            r += 1  # 위로 (row 감소)
        elif action == 'D':
            r -= 1  # 아래로 (row 증가)
        elif action == 'L':
            c -= 1
        elif action == 'R':
            c += 1
        
        # 경계 체크
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return state  # 벽에 부딪히면 제자리
        # 벽 체크
        if (r, c) == self.wall:
            return state
        
        return (r, c)
    
    def get_reward(self, state, action):
        """보상 반환"""
        next_state = self.get_next_state(state, action)
        
        if next_state in self.terminals:
            return self.terminals[next_state]
        
        return self.step_reward

import random
import numpy as np

class TD:
    def __init__(self, actions=4, lr=0.1, gamma=0.9, epsilon=0.1):
        self.actions = actions
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}
        # numpy array 추가 (25x4 형태: 상태x행동)
        self.q_array = np.zeros((25, 4))
        
    def state_to_index(self, state):
        """(x,y) 상태를 0~24 인덱스로 변환"""
        x, y = state
        return x * 5 + y

    def get_q(self, state, action):
        return round(self.q_table.get((state, action), 0.0), 2)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.actions-1)
        else:
            q_values = [self.get_q(state, a) for a in range(self.actions)]
            return q_values.index(max(q_values))
        
def q_learning_update(agent, state, action, reward, next_state):
    old_q = agent.get_q(state, action)
    next_max = max([agent.get_q(next_state, a) for a in range(agent.actions)])
    new_q = old_q + agent.lr * (reward + agent.gamma * next_max - old_q)
    agent.q_table[(state, action)] = new_q
    state_idx = agent.state_to_index(state)
    agent.q_array[state_idx, action] = round(new_q, 2)

def sarsa_update(agent, state, action, reward, next_state, next_action):
    old_q = agent.get_q(state, action)
    next_q = agent.get_q(next_state, next_action)
    new_q = old_q + agent.lr * (reward + agent.gamma * next_q - old_q)
    agent.q_table[(state, action)] = new_q
    state_idx = agent.state_to_index(state)
    agent.q_array[state_idx, action] = round(new_q, 2)

class Agent:
    def __init__(self, env):
        self.env = env
        self.V = {s: 0.0 for s in env.get_states()}  # Value function
        self.policy = {s: 'R' for s in env.get_states()}  # Initial policy
    
    def policy_evaluation_async(self, threshold=0.001):
        """Asynchronous Policy Evaluation"""
        while True:
            delta = 0
            for state in self.env.get_states():
                if self.env.is_terminal(state):
                    continue
                
                v = self.V[state]
                action = self.policy[state]
                
                # Bellman equation for policy evaluation
                next_state = self.env.get_next_state(state, action)
                reward = self.env.get_reward(state, action)
                self.V[state] = reward + self.env.gamma * self.V[next_state]
                
                delta = max(delta, abs(v - self.V[state]))
            
            if delta < threshold:
                break
    
    def policy_improvement(self):
        """Policy Improvement"""
        policy_stable = True
        
        for state in self.env.get_states():
            if self.env.is_terminal(state):
                continue
            
            old_action = self.policy[state]
            
            # 모든 행동에 대해 Q값 계산
            action_values = {}
            for action in self.env.actions:
                next_state = self.env.get_next_state(state, action)
                reward = self.env.get_reward(state, action)
                action_values[action] = reward + self.env.gamma * self.V[next_state]
            
            # 최선의 행동 선택
            self.policy[state] = max(action_values, key=action_values.get)
            
            if old_action != self.policy[state]:
                policy_stable = False
        
        return policy_stable
    
    def policy_iteration(self):
        """Asynchronous Policy Iteration"""
        iteration = 0
        while True:
            iteration += 1
            print(f"\n{'='*50}")
            print(f"Iteration {iteration}")
            print(f"{'='*50}")
            
            # Policy Evaluation
            self.policy_evaluation_async()
            
            # Policy Improvement
            policy_stable = self.policy_improvement()
            
            self.print_results()
            
            if policy_stable:
                print(f"\n✅ Policy converged after {iteration} iterations!")
                break
    
    def print_results(self):
        """결과 출력"""
        print("\nValue Function:")
        for r in range(self.env.rows):
            row_values = []
            for c in range(self.env.cols):
                if (r, c) == self.env.wall:
                    row_values.append("  WALL ")
                else:
                    row_values.append(f"{self.V[(r,c)]:6.2f}")
            print("  ".join(row_values))
        
        print("\nOptimal Policy:")
        for r in range(self.env.rows):
            row_policy = []
            for c in range(self.env.cols):
                if (r, c) == self.env.wall:
                    row_policy.append(" W ")
                elif self.env.is_terminal((r, c)):
                    row_policy.append(" T ")
                else:
                    row_policy.append(f" {self.policy[(r,c)]} ")
            print("  ".join(row_policy))

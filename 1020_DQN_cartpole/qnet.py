import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """
    Q-Network: 상태를 입력받아 각 행동의 Q-value를 출력
    """
    def __init__(self, state_dim=4, action_dim=2, hidden_dim=128):
        """
        Args:
            state_dim (int): 상태 공간의 차원 (CartPole: 4)
            action_dim (int): 행동 공간의 차원 (CartPole: 2)
            hidden_dims (list): 은닉층의 크기 리스트
        """
        super(QNetwork, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim)
        )
        
    def forward(self, state):
        """
        Args:
            state (torch.Tensor): 상태 (batch_size, state_dim)
        
        Returns:
            torch.Tensor: Q-values (batch_size, action_dim)
        """
        return self.network(state)
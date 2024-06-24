from torch import nn, torch

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,x):
        return torch.softmax(x, dim=0)
class MyStableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,x):
        max_value = torch.max(x)
        return torch.softmax(x - max_value, dim=0)
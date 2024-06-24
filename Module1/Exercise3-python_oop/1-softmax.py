import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        result = torch.zeros_like(data)
        sum_exp = torch.sum(torch.exp(data))

        for i in range(data.size(0)):
            result[i] = torch.exp(data[i]) / sum_exp

        return result


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        result = torch.zeros_like(data)
        c = torch.max(data)
        sum_exp = torch.sum(torch.exp(data - c))

        for i in range(data.size(0)):
            result[i] = torch.exp(data[i] - c) / sum_exp

        return result

if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    print(softmax(data))

    softmax_stable = softmax_stable()
    print(softmax_stable(data))

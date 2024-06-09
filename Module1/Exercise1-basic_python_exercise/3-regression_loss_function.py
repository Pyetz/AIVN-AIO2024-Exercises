import math
import random as r

# mean absolute error
def MAE(targets, predicts, num_samples):
    total_loss = 0
    for i in range(num_samples):
        loss = abs(targets[i] - predicts[i])
        total_loss += loss
        print(f"loss name: MAE, sample: {i}, pred: {predicts[i]}, target: {targets[i]}, loss: {loss}")
    final_loss = total_loss / num_samples
    print(f"final MAE: {final_loss}")

# mean squared error
def MSE(targets, predicts, num_samples):
    total_loss = 0
    for i in range(num_samples):
        loss = (targets[i] - predicts[i]) ** 2
        total_loss += loss
        print(f"loss name: MSE, sample: {i}, pred: {predicts[i]}, target: {targets[i]}, loss: {loss}")
    final_loss = total_loss / num_samples
    print(f"final MSE: {final_loss}")

#root mean squared error
def RMSE(targets, predicts, num_samples):
    total_loss = 0
    for i in range(num_samples):
        loss = (targets[i] - predicts[i]) ** 2
        total_loss += loss
        print(f"loss name: RMSE, sample: {i}, pred: {predicts[i]}, target: {targets[i]}, loss: {loss}")
    final_loss = math.sqrt(total_loss / num_samples)
    print(f"final RMSE: {final_loss}")

if __name__ == '__main__':
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if num_samples.isnumeric():
        num_samples = int(num_samples)
        loss_name = input('Input loss name: ')
        targets = []
        predicts = []
        for i in range(num_samples):
            target = r.uniform(0, 10)
            predict = r.uniform(0, 10)
            targets.append(target)
            predicts.append(predict)

        if loss_name == 'MAE':
            MAE(targets, predicts, num_samples)
        elif loss_name == 'MSE':
            MSE(targets, predicts, num_samples)
        else:
            RMSE(targets, predicts, num_samples)
    else:
        print('number of samples must be an integer number')
    
import numpy as np
import pandas as pd

# from function import generate_data

rg = np.random.default_rng()
bias = 0.5
l_rate = 0.1
epochs = 50
epoch_loss = []


def generate_data(n_features, n_values):
    features = rg.random((n_features, n_values))
    weights = rg.random((1, n_values))[
        0
    ]  # Extra parenthesis to make weight matrix one dimensional
    targets = np.random.choice([0, 1], n_features)
    data = pd.DataFrame(features, columns=["x0", "x1", "x2"])
    data["targets"] = targets
    return data, weights


# print(data)
# print(targets)


def get_weighted_sum(n_features, weight, b):
    return np.dot(n_features, weight) + b


def sigmoid(w_sum):
    return 1 / (1 + np.exp(-w_sum))


def cross_entropy(target, prediction):
    return -(target * np.log10(prediction) + (1 - target) * np.log10(1 - prediction))


def update_weights(weights, l_rate, target, prediction, features):
    new_weights = []
    for x, w in zip(features, weights):
        new_w = w + l_rate * (target - prediction) * x
        new_weights.append(new_w)
    return new_weights


def update_bias(bias, l_rate, target, prediction):
    return bias + l_rate * (target - prediction)


# Function to create a Neural Network
data, weights = generate_data(50, 3)


def train_model(data, weights, bias, l_rate, epochs):
    for e in range(epochs):
        individual_loss = []
        for i in range(len(data)):
            features = data.loc[i][:-1]
            target = data.loc[i][-1]
            w_sum = get_weighted_sum(features, weights, bias)
            prediction = sigmoid(w_sum)
            # print(prediction)
            loss = cross_entropy(target, prediction)
            individual_loss.append(loss)
            # print(loss)
            # Gradient Descent
            # print(f"Old Values,\n weights= {weights} \n bias= {bias}")
            weights = update_weights(weights, l_rate, target, prediction, features)
            bias = update_bias(bias, l_rate, target, prediction)
            # print(f"New Values,\n weights= {weights} \n bias= {bias}")
        average_loss = sum(individual_loss) / len(individual_loss)
        epoch_loss.append(average_loss)
        print("*********************************")
        print("Epoch = ", e + 1)
        print(f"Average Loss = {average_loss}")


train_model(data, weights, bias, l_rate, epochs)

# Plot the average loss
df = pd.DataFrame(epoch_loss)
df_plot = df.plot(kind="line", grid=True).get_figure()
df_plot.savefig("Training_Loss.pdf")

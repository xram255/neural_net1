weight = 0.1
alpha = 0.01

def neural_net(inp, wght):
    pred = inp * wght
    return pred

num_of_toes = [8.5, 9.5, 10, 9]
input  = num_of_toes[0]

prediction = neural_net(input, weight)

print(prediction)
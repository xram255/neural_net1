import numpy as np

weights = np.array([.7, .2, -.5])
alpha = .1

streetlights = np.array([[0, 0, 1],
                         [0, 1, 1],
                         [0, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1],
                         [1, 0, 1]])

walk_vs_stop = np.array([0, 1, 0, 1, 1, 0])

'''
input = streetlights[2]
print(weights)
print(input.dot(weights))
'''

for iteration in range (40):
    error_for_all_lights = 0
    for row_index in range (len(walk_vs_stop)):
        input = streetlights[row_index]
        goal_prediction = walk_vs_stop[row_index]
        print(error_for_all_lights)
        prediction = input.dot(weights)
        error = (prediction -goal_prediction) ** 2 #square error
        error_for_all_lights += error
        print("in", error_for_all_lights)
        delta = prediction - goal_prediction #difference between actual to prediction
        weights = weights -(alpha * input * delta) #weights update

        #print("prediction: ", prediction)

    print("weights: ", weights)
    print("Error: ", error)

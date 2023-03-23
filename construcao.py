# Aluno: Rafael Coelho Monte Alto
# Professor: Gladston Juliano Prates Moreira 

# BCC 405 - Otimizacao Nao Linear 

# Metodos de construcao de uma solucao para o problema knapsack 

import numpy as np
import random 

from fo import calcula_fo

def construcao_aleatoria(n, capacity, objects):
    s = np.zeros(n)
    weight = 0
    while (weight < capacity):
        # choose random object 
        random_index = random.randint(0, len(objects) - 1)
        # if object is already part of the solution 
        if (s[random_index] == 1): 
            continue
        # check for capacity constraint 
        elif (weight + objects[random_index][1] > capacity):
            break 
        # add it to solution  
        else:
            s[random_index] = 1
            weight += objects[random_index][1]
    return s

def construcao_inicial(n, capacity, objects):
    s = np.zeros(n)
    while True:
        random_index = random.randint(0, len(objects) - 1)
        if (objects[random_index][1] > capacity):
            None
        else: 
            s[random_index] = 1
            break
    return s

def guloso(n, capacity, objects):
    s = np.zeros(n)
    # cost benefit 
    cb = np.zeros(n) 
    for i in range(len(cb)):
        cb[i] = objects[i][0] / objects[i][1]
    # print("cost benefit:", cb)
    # current weight of bag 
    weight = 0
    k = 0
    while (k < n): 
        k += 1
        # select highest cost benefit 
        high = cb.argmax(axis=0) 
        # if best object has weight that will surpass capacity, discard 
        if (weight + objects[high][1] > capacity):
            cb[high] = 0
        # if object can be added to the bag, do it 
        else:
            s[high] = 1 
            weight += objects[high][1] 
            cb[high] = 0 
    return s
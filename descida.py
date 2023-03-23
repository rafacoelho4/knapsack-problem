# Aluno: Rafael Coelho Monte Alto
# Professor: Gladston Juliano Prates Moreira 

# BCC 405 - Otimizacao Nao Linear 

from construcao import construcao_aleatoria, guloso
from fo import calcula_fo

import numpy as np 
import random

def vizinho_aleatorio(s, objects, capacity):
    # calculating weight of current solution 
    weight = 0
    for i in range(len(s)):
        weight += s[i] * objects[i][1]

    s_viz = np.copy(s)

    while True:
        # choosing random index os solution 
        random_index = random.randint(0, len(objects) - 1)
        # if object is part of the solution, remove 
        if(s_viz[random_index] == 1):
            s_viz[random_index] = 0
            break
        # if chosen object is not part of the current solution, try to include 
        elif(s_viz[random_index] == 0):
            # print("object is NOT part of solution")
            if(weight + objects[random_index][1] > capacity):
                # print("adding _ to _ doesnt work:", objects[random_index][1], weight)
                continue
            else:
                s_viz[random_index] = 1
                break

    return s_viz

def descida_aleatoria(s, objects, capacity, max_it):
    fo = calcula_fo(s, objects)
    k = 0
    while (k < max_it):
        # print(k)
        s_viz = vizinho_aleatorio(s, objects, capacity) 
        fo_viz = calcula_fo(s_viz, objects)
        if (fo_viz > fo): 
            print(s_viz)
            print("houve melhora de _ para _ :", fo, fo_viz)
            s = s_viz
            fo = fo_viz
            k = 1
        else:
            k += 1
    return s

def primeira_melhora(s, objects, capacity):
    fo = calcula_fo(s, objects)
    # random order of neighbors
    arr = np.arange(len(s))
    np.random.shuffle(arr)
    print(arr)
    k = 0
    while (k < len(s)):
        s_viz = reverse_bit(s, objects, capacity, arr[k])
        fo_viz = calcula_fo(s_viz, objects)
        if (fo_viz > fo): 
            print("houve melhora de _ para _ :", fo, fo_viz)
            print(s_viz)
            s = s_viz
            break
        else: 
            k += 1
    return s

def reverse_bit(s, objects, capacity, b):
    # calculating weight of current solution 
    weight = 0
    for i in range(len(s)):
        weight += s[i] * objects[i][1]
    # copy of solution 
    s_viz = np.copy(s) 
    # taking item out 
    if(s_viz[b] == 1): 
        s_viz[b] = 0
    else: 
        # trying to include new object 
        if(weight + objects[b][1] > capacity):
            return s_viz
        else: 
            s_viz[b] = 1
    return s_viz

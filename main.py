# Aluno: Rafael Coelho Monte Alto
# Professor: Gladston Juliano Prates Moreira 

# BCC 405 - Otimizacao Nao Linear 

from construcao import construcao_aleatoria, construcao_inicial, guloso
from descida import descida_aleatoria, primeira_melhora
from fo import calcula_fo

# (profit, weight)
# (x, y)

def main():
    # test case 0
    # n = 5 
    # c = 10 
    # o = [(2, 1), (4, 6), (8, 4), (1, 1), (6, 1)]
    # test case 1
    n = 20
    c = 994 
    o = [(403,94), (886,506), (814,416), (1151,992), (983,649), (629,237), (848,457),
        (1074,815), (839,446), (819,422), (1062,791), (762,359), (994,667),
        (950,598), (111,7), (914,544), (737,334), (1049,766), (1152,994), (1110,893)]
    z = 2291
    # s = guloso(n=n, capacity=c, objects=o)
    s = construcao_aleatoria(n=n, capacity=c, objects=o) 
    # s = construcao_inicial(n=n, capacity=c, objects=o) 
    print("solucao inicial:", s)
    print("fo inicial:", calcula_fo(s, objects=o))
    # s = descida_aleatoria(s, objects=o, capacity=c, max_it=2000) 
    s = primeira_melhora(s, objects=o, capacity=c) 
    print("solucao final:", s)
    fo = calcula_fo(s, objects=o)
    print("fo final:", fo)
    print("distance to optimal solution:", z - fo)

if __name__ == "__main__":
    main()
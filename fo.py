# Aluno: Rafael Coelho Monte Alto
# Professor: Gladston Juliano Prates Moreira 

# BCC 405 - Otimizacao Nao Linear 

def calcula_fo(s, objects):
    fo = 0
    for i in range(len(s)):
        fo += s[i] * objects[i][0]
    return fo
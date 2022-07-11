import pickle

def exibir_alunos(lista):
    for i in lista:
        nome,nota1,nota2,nota3,nota4, total, tempo = i
        print(nome,total)

def bonus_pontos(lista):
    contador = 0
    formulario = []
    for i in lista:
        nome,nota1,nota2,nota3,nota4, total, tempo = i
        if contador < 5 :
            tupla = (nome,nota1,nota2,nota3,nota4, total + 2, tempo)
            formulario.append(tupla)
        else:
            if total == formulario[(contador -1)][5] - 2 and tempo == formulario[(contador - 1)][6]:
                tupla = (nome,nota1,nota2,nota3,nota4, total + 2, tempo)
                formulario.append(tupla)
            else:
                tupla = (nome,nota1,nota2,nota3,nota4, total, tempo)
                formulario.append(tupla)
        contador += 1
    return formulario

def anterior(x,y):
    nome_x,nota1_x,nota2_x,nota3_x,nota4_x,total_x,tempo_x = x
    nome_y, nota1_y, nota2_y, nota3_y, nota4_y, total_y, tempo_y = y
    if total_x > total_y: return True
    if total_x < total_y: return False
    if nota2_x > nota2_y: return True
    if nota2_x < nota2_y: return False
    if tempo_x < tempo_y: return True
    if tempo_x > tempo_y: return False

def particao(lista,inferior,superior):
    pivo = lista[inferior]
    i = inferior + 1
    j = superior - 1
    while i <= j:
        while i <= j and anterior(lista[i],pivo):
            i += 1
        while j >= i and not(anterior(lista[j],pivo)):
            j -= 1
        if i < j :
            lista[i],lista[j] = lista[j],lista[i]
    lista[inferior],lista[j] = lista[j], lista[inferior]
    return j

def quicksort(lista,inferior,superior):
    if inferior < superior:
        posicao = particao(lista,inferior,superior)
        quicksort(lista,inferior,(posicao - 1))
        quicksort(lista,(posicao + 1),superior)
    return lista

def Cria_lista_alunos(alunos,notas): #cria uma lista de tuplas com o nome do aluno seguido de suas notas, o total por fim tempo do codigo
    lista = []
    for i in notas:
        if i[0] in alunos:
            tupla = (alunos[i[0]],i[1],i[2],i[3],i[4],(i[1]+ i[2] + i[3] + i[4]),i[5])
            lista.append(tupla)
    return lista

def main():
    with open("entrada.bin","rb") as arq:
        alunos = pickle.load(arq) #dicionario onde as chaves sao um numero crescente comecando em 1 e o value eh o nome do aluno
        notas = pickle.load(arq) #lista de tuplas onde o primeiro elem eh a chave que corresponde ao aluno, o 2 ao 5 elem sao as notas do mesmo e o ultimo eh o tempo do codigo
    lista_notas =  Cria_lista_alunos(alunos,notas)
    inferior = 0
    superior = len(lista_notas)
    ordena_ai = quicksort(lista_notas,inferior,superior)
    ordena_ai[0], ordena_ai[1] = ordena_ai[1], ordena_ai[0]
    bonificacao = bonus_pontos(ordena_ai)
    ordem = exibir_alunos(bonificacao)
main()

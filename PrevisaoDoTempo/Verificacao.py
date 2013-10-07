import cPickle as pickle
import neurolab as nl
import csv
import numpy as np


def __lerarquivo__():
    with open('leituras_para_verificacao.csv') as verificacaos:
        lista = []
        for linha in csv.reader(verificacaos, delimiter=','):
            lista.append(linha)
        return lista

def verificar(variavel):
    with open('A702_normalizado.pickle', 'r') as arquivo:
        arquivoinput = pickle.load(arquivo)

    inputNorm = nl.tool.Norm(arquivoinput)
    entradas = []
    verificacaosfile = __lerarquivo__()
    for i, linha in enumerate(verificacaosfile):
        if i < 2:
            continue
        entrada = []
        entrada.append(float(verificacaosfile[i][19]))
        entrada.append(float(verificacaosfile[i][2]))
        entrada.append(float(verificacaosfile[i-1][3]))
        entrada.append(float(verificacaosfile[i][3]))
        if float(verificacaosfile[i-1][18]) < 0:
            entrada.append(0.0)
        else:
            entrada.append(float(verificacaosfile[i-1][18]))
        if float(verificacaosfile[i][18]) < 0:
            entrada.append(0.0)
        else:
            entrada.append(float(verificacaosfile[i-1][18]))
        entrada.append(float(verificacaosfile[i-1][9]))
        entrada.append(float(verificacaosfile[i][9]))
        entradas.append(entrada)
    saidas = []
    for i, linha in enumerate(verificacaosfile):
        if i < 2 or (i + 6) >= len(verificacaosfile):
            continue
        saida = []
        #for count in range(1, 7):
            #saida.append(float(verificacaosfile[i + count][3]))
        saida.append(float(verificacaosfile[i + 1][3]))
        saidas.append(saida)
    with open('A702_'+variavel+'.pickle', 'r') as arquivo:
        target = pickle.load(arquivo)
    target = target[0: len(arquivoinput)]
    outputNorm = nl.tool.Norm(target)
    net = nl.load(variavel+'.net')
    saidasprevistas = []
    for entrada in entradas:
        inputNormTarget = inputNorm(entrada)
        out = net.sim(inputNormTarget)
        saidasprevistas.append(outputNorm.renorm(out)[0])
    diffs = []
    for i, medido in enumerate(saidas):
        diff = []
        for j, medido2 in enumerate(medido):
            diff.append(abs(saidas[i][j] - saidasprevistas[i][j]))
        diffs.append(diff)
    diffs = np.array(diffs)
    for i in range(0, len(diffs[0])):
        print('%s' % variavel)
        print('avg: %.2f' % np.average(diffs[:, i]))
        print('std: %.2f' % np.std(diffs[:, i]))

    pass


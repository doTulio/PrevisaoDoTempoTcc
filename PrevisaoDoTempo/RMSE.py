# coding=utf-8
import json
from math import tanh, sqrt
from Weight import Weight
from string import join
"""
vou precisar ler os arquivos binários com as previsões
depois ler o arquivo com os pesos
para todas as entradas, criar previsões com os pesos
depois comparar o primeiro arquivo com as previsões calculadas a partir do peso
"""


def __frombinarylisttoint__(binarylist):
    resultstr = binarylist
    for i, item in enumerate(resultstr):
        resultstr[i] = str(item)
    binarylist = join(resultstr, sep="")
    return int(binarylist, 2)


def __sigmoid__(x):
    return tanh(x)


def __showWeights__(inputs, wi, wo, no, nh):
    ni = len(inputs) + 1
    ai = inputs + [1.0]
    ah = []
    ao = []

    if len(inputs) != ni - 1:
        raise ValueError('wrong number of inputs')

    # hidden activations
    for j in range(nh):
        sum = 0.0
        for i in range(ni):
            sum += ai[i] * wi[i][j]
        ah.append(__sigmoid__(sum))

    # output activations
    for k in range(no):
        sum = 0.0
        for j in range(nh):
            sum += ah[j] * wo[j][k]
        ao.append(__sigmoid__(sum))
    return ao[:]


def __mostrar__(input, wi, wo, outputsize, nh):
    result = __showWeights__(input, wi, wo, outputsize, nh)
    for i, item in enumerate(result):
        if item >= 0.5:
            result[i] = 1
        else:
            result[i] = 0
    resultint = __frombinarylisttoint__(result)
    return resultint


def __lerarquivo__(nomearquivo):
    with open(nomearquivo) as f:
        arquivo = f.read()
    arquivo = json.loads(arquivo)
    return arquivo


def __pesos__(nomearquivo):
    nomearquivo = "weights_" + nomearquivo
    with open(nomearquivo) as f:
        pesos = f.read()
    pesos = json.loads(pesos)
    return Weight(pesos['wi'], pesos['wo'])


def __rmse__(medido, previsao):
    sum = 0
    all = []
    for i in range(len(medido)):
        dif = abs(medido[i] - previsao[i])
        all.append(dif)
        dif **= 2
        sum += dif
    print("Max error: %d" % max(all))
    print("RMSE: %f" % sqrt(sum/len(medido)))


def rodar(nomearquivo):
    outputsize = 6
    nh = 3
    medido = []
    previsao = []
    arquivo = __lerarquivo__(nomearquivo)
    pesos = __pesos__(nomearquivo)

    for linha in arquivo:
        medido.append(__frombinarylisttoint__(linha[1]))

    for linha in arquivo:
        previsao.append(__mostrar__(linha[0], pesos.wi, pesos.wo, outputsize, nh))

    __rmse__(medido, previsao)
    pass


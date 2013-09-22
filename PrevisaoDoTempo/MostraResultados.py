# coding=utf-8
import math
from Weight import Weight


def __sigmoid__(x):
    return math.tanh(x)


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
    resultstr = result
    for i, item in enumerate(resultstr):
        resultstr[i] = str(item)
    import string
    resultstr = string.join(resultstr, "")
    resultstr = int(resultstr, 2)
    #print(input, result, resultstr)
    return resultstr


def __strtolist__(str):
    lista = []
    for char in str:
        lista.append(int(char))
    return lista


__getBin__ = lambda x, n: str(bin(int(round(float(x)))))[2:].zfill(n)


def __tobinary__(str, valor):
    # t = 6
    # r = 12
    # p = 8
    # hora = 5
    bin = 0
    if str == 't':
        bin = 6
    elif str == 'r':
        bin = 12
    elif str == 'p':
        bin = 8
    elif str == 'h':
        bin = 5
    return __getBin__(valor, bin)


def prever(params, nomearquivo):
    t = __strtolist__(__tobinary__('t', params['t']))
    radiacao = __strtolist__(__tobinary__('r', params['r']))
    chuva = __strtolist__(__tobinary__('p', params['p']))
    data = __strtolist__(__tobinary__('h', params['h']))

    input = t + radiacao + chuva + data
    import json
    with open(nomearquivo, 'r') as f:
        weights = json.loads(f.read())
    weights = Weight(weights['wi'], weights['wo'])
    return __mostrar__(input, weights.wi, weights.wo, 6, 3)


def temperaturas(params):
    temperaturas = [int(params['t'])]
    for i in range(1, 7):
        nomearquivo = 'weights_A702_t_+' + str(i) + '.json'
        temperaturas.append(prever(params, nomearquivo))
    return temperaturas


def precipitacao(params):
    precipitacao = [int(params['p'])]
    for i in range(1, 7):
        nomearquivo = 'weights_A702_chuva_+' + str(i) + '.json'
        precipitacao.append(prever(params, nomearquivo))
    return precipitacao
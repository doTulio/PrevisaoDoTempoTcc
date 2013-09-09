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
    print(input, result, resultstr)


def __strtolist__(str):
    lista = []
    for char in str:
        lista.append(int(char))
    return lista


def prever():
    chuva = __strtolist__('00000000')
    data = __strtolist__('01111')
    t = __strtolist__('011101')
    radiacao = __strtolist__('110011100000')
    input = chuva + data + t + radiacao
    import json
    with open('weights_A702_t_+6.json', 'r') as f:
        weights = json.loads(f.read())
    weights = Weight(weights['wi'], weights['wo'])
    print(weights.__dict__)
    __mostrar__(input, weights.wi, weights.wo, 6, 4)
# coding=utf-8
import cPickle as pickle
from dateutil.parser import parse
from neurolab.tool import Norm

def __lerarquivo__():
    with open('A702.pickle', 'r') as arquivo:
        return pickle.load(arquivo)


def __salvararquivo__(normalizado, i, variavel):
    with open('A702_' + variavel + '+' +str(i) + '.pickle', 'wb') as arquivo:
        pickle.dump(normalizado, arquivo)


def __parserDataEmHora__(dataStr):
    return parse(dataStr).hour


def __normaliza__(arquivo, hora, variavel):
    output = []
    size = len(arquivo)
    for i, hour in enumerate(arquivo):
        prox = i + hora
        if prox == size:
            break
        saida = []
        saida.append(float(arquivo[prox][variavel]))
        output.append(saida)
    #normf = Norm(output)
    #norm_target = normf(output)
    return output


def main():
    arquivo = __lerarquivo__()
    variaveis = ['t', 'chuva', 'radiacao']
    for i in range(1, 7):
        for variavel in variaveis:
            normalizado = __normaliza__(arquivo, i, variavel)
            __salvararquivo__(normalizado, i, variavel)
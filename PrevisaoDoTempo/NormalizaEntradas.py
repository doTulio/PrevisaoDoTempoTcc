# coding=utf-8
import cPickle as pickle
from dateutil.parser import parse


def __lerarquivo__():
    with open('A702.pickle', 'r') as arquivo:
        return pickle.load(arquivo)


def __salvararquivo__(normalizado):
    with open('A702_normalizado.pickle', 'wb') as arquivo:
        pickle.dump(normalizado, arquivo)


def __parserDataEmHora__(dataStr):
    return parse(dataStr).hour


def __normaliza__(arquivo):
    input = []
    for i, hora in enumerate(arquivo):
        if i == 0:
            continue
        entrada = []
        entrada.append(float(arquivo[i]['chuva']))
        entrada.append(float(__parserDataEmHora__(arquivo[i]['data'])))
        entrada.append(float(arquivo[i - 1]['t']))
        entrada.append(float(arquivo[i]['t']))
        entrada.append(float(arquivo[i - 1]['radiacao']))
        entrada.append(float(arquivo[i]['radiacao']))
        entrada.append(float(arquivo[i - 1]['po']))
        entrada.append(float(arquivo[i]['po']))
        input.append(entrada)
    return input[0:-6]


def main():
    arquivo = __lerarquivo__()
    normalizado = __normaliza__(arquivo)
    __salvararquivo__(normalizado)
    pass
# coding=utf-8
import json


def __lerjson__():
    with open('A702_binary.json', 'r') as f:
        arquivojson = f.read().replace('\n', '')
    return json.loads(arquivojson)


def __salvaarquivo__(entradas, variavel, horaahead):
    filename = 'A702_' + variavel + '_+' + str(horaahead) + '.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(entradas, indent=4))


def __defineentradas__(arquivo, variavel, horaahead):
    todos = []
    for i, item in enumerate(arquivo):
        if i + horaahead >= len(arquivo):
            break
        entradas = []
        saidas = []
        entradaesaidas = []
        for word in item.iteritems():
            for char in word[1]:
                entradas.append(int(char))
        for char in arquivo[i + horaahead][variavel]:
            saidas.append(int(char))
        entradaesaidas.append(entradas)
        entradaesaidas.append(saidas)
        todos.append(entradaesaidas)
    __salvaarquivo__(todos, variavel, horaahead)


def main():
    arquivo = __lerjson__()
    saidas = ['t', 'chuva', 'radiacao']
    for hora in range(1, 7):
        for saida in saidas:
            __defineentradas__(arquivo, saida, hora)
    pass
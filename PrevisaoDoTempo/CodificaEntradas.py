# coding=utf-8
def __lerjson__(json):
    with open('A702.json', 'r') as f:
        arquivojson = f.read().replace('\n', '')
    return json.loads(arquivojson)


def __tratadata__(data):
    from dateutil import parser
    return parser.parse(data).hour


__getBin__ = lambda x, n: str(bin(int(round(float(x)))))[2:].zfill(n)


def __tobinary__(json):
    for item in json:
        for word in item.iteritems():
            if word[0] == 'velocidade':
                bin = 4
            elif word[0] == 'p':
                bin = 10
            elif word[0] == 't':
                bin = 6
            elif word[0] == 'radiacao':
                bin = 12
            elif word[0] == 'chuva':
                bin = 8
            elif word[0] == 'data':
                hora = __tratadata__(word[1])
                item[word[0]] = __getBin__(hora, 5)
                bin = 5
            elif word[0] == 'po':
                bin = 6
            if word[0] != 'data':
                valor = float(word[1])
                # se for menor que 0, substitui por 0
                if valor < 0:
                    valor = 0
                item[word[0]] = __getBin__(valor, bin)
                if not item[word[0]].isdigit():
                    raise Exception(u'negativo não tratado')
                bin = ''.rjust(bin, '1')
                bin = int(bin, 2)
                if bin <= float(word[1]):
                    print 'bin: ' + str(bin)
                    print 'word[0]: ' + str(word[0])
                    print 'word[1]: ' + str(word[1])
                    raise Exception(u'valor maior que máximo da codificação binária')


def __salvajson__(dados, json):
    dados = json.dumps(dados, indent=4)
    with open('A702_binary.json', 'w') as f:
        f.write(dados)


def main():
    from os import chdir
    import json
    chdir('/home/en/TCC/CSV')
    arquivojson = __lerjson__(json)
    __tobinary__(arquivojson)
    __salvajson__(arquivojson, json)

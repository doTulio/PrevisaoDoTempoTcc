def __getmonth__(month):
    return {
        'JAN': 1,
        'FEV': 2,
        'MAR': 3,
        'ABR': 4,
        'MAI': 5,
        'JUN': 6,
        'JUL': 7,
        'AGO': 8,
        'SET': 9,
        'OUT': 10,
        'NOV': 11,
        'DEZ': 12
    }[month]


def __data__(data):
    from datetime import datetime as dt
    dia = int(data[0])
    mes = int(__getmonth__(data[1]))
    ano = int(data[2])
    hora = int(data[3])
    data = dt(ano,mes,dia, hora, 0)
    return data.isoformat()


def __processacsv__(arquivoum, arquivodois):
    objeto = []
    arquivodoislist = []
    for i in arquivodois:
        arquivodoislist.append(i)
    for ir, row in enumerate(arquivoum):
        if ir < 2:
            continue
        row2 = arquivodoislist[ir]
        for hora in range(24):
            data = row[0].split('-')
            data.append(hora)
            radiacao = 'NULL'
            if 9 <= hora <= 22:
                radiacao = row2[hora - 9 + 98]
            if radiacao == 'NULL':
                radiacao = 0
            objeto.append(
                {
                    'chuva': row2[hora + 1],
                    'data': __data__(data),
                    'p': row2[hora + 25],
                    't': row[hora + 1],
                    'po': row[hora + 25],
                    'velocidade': row2[hora + 135],
                    'radiacao': radiacao
                }
            )
    return objeto


def __tratanulos__(dados):
    for i, item in enumerate(dados):
        for tup in item.iteritems():
            if tup[1] == 'NULL':
                dados[i][tup[0]] = dados[i - 1][tup[0]]


def __lerarquivo__(nome):
    import csv

    arquivo = open(nome,'rb')
    return csv.reader(arquivo, delimiter=',')


def main():
    import json
    from os import chdir
    chdir("/home/en/TCC/CSV")
    arquivoum = __lerarquivo__("A702_I.csv")
    arquivodois = __lerarquivo__("A702_II.csv")
    dados = __processacsv__(arquivoum, arquivodois)
    __tratanulos__(dados)
    dados = json.dumps(dados, indent=4)
    f = open('A702.json', 'r+')
    f.write(dados)
    f.close()
    return
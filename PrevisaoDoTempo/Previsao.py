# coding=utf-8
import neurolab as nl
import cPickle as pickle


def prevertemperatura(params):
    inputs = []
    inputs.append(params['chuva'])
    inputs.append(params['hora'])
    inputs.append(params['tanterior'])
    inputs.append(params['tatual'])
    inputs.append(params['ranterior'])
    inputs.append(params['ratual'])

    temperaturas = []
    temperaturas.append(float(params['tatual']))

    with open('A702_normalizado.pickle', 'r') as arquivo:
        arquivoinput = pickle.load(arquivo)

    inputNorm = nl.tool.Norm(arquivoinput)
    inputNormTarget = inputNorm(inputs)

    for i in range(1, 7):
        with open('A702_t+' + str(i) + '.pickle', 'r') as arquivo:
            output = pickle.load(arquivo)
            net = nl.load('t+' + str(i) + '.net')
            out = net.sim(inputNormTarget)
            outputNorm = nl.tool.Norm(output)
            temperaturas.append(outputNorm.renorm(out)[0][0])
    return temperaturas


def preverprecipitacao(params):
    inputs = []
    inputs.append(params['chuva'])
    inputs.append(params['hora'])
    inputs.append(params['tanterior'])
    inputs.append(params['tatual'])
    inputs.append(params['ranterior'])
    inputs.append(params['ratual'])

    precipitacaos = []
    precipitacaos.append(float(params['chuva']))

    with open('A702_normalizado.pickle', 'r') as arquivo:
        arquivoinput = pickle.load(arquivo)

    inputNorm = nl.tool.Norm(arquivoinput)
    inputNormTarget = inputNorm(inputs)

    for i in range(1, 7):
        with open('A702_chuva+' + str(i) + '.pickle', 'r') as arquivo:
            output = pickle.load(arquivo)
            net = nl.load('chuva+' + str(i) + '.net')
            out = net.sim(inputNormTarget)
            outputNorm = nl.tool.Norm(output)
            saida = outputNorm.renorm(out)[0][0]
            if saida < 1:
                saida = 0
            precipitacaos.append(saida)
    return precipitacaos

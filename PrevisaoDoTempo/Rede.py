# coding=utf-8
import neurolab as nl
import cPickle as pickle


def train(previsao):
    with open('A702_normalizado.pickle', 'r') as arquivo:
        inputs = pickle.load(arquivo)
    with open('A702_' + previsao + '.pickle', 'r') as arquivo:
        target = pickle.load(arquivo)

    target = target[0: len(inputs)]

    inputNorm = nl.tool.Norm(inputs)
    inputNormTarget = inputNorm(inputs)

    outputNorm = nl.tool.Norm(target)
    outputNormTarget = outputNorm(target)

    net = nl.net.newff([[0, 1]] * len(inputNormTarget[0]), [50, 1])
    net.trainf = nl.train.train_bfgs
    error = net.train(inputNormTarget, outputNormTarget, epochs=100, show=1)
    net.save(previsao + '.net')
    #net = nl.load('t_+1.net')
    #teste = [24.2, 25.4, 0, 0]
    #testeNorm = inputNorm(teste)
    #out = net.sim(testeNorm)
    #outDenorm = outputNorm.renorm(out)
    #print outDenorm
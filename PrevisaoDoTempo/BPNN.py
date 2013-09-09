# coding=utf-8
# Back-Propagation Neural Networks
# 
# Written in Python.  See http://www.python.org/
# Placed in the public domain.
# Neil Schemenauer <nas@arctrix.com>

import math
import random

random.seed(0)

class Weight:
    def __init__(self, wi, wo):
        self.wi = wi
        self.wo = wo


# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b - a) * random.random() + a


# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y ** 2


class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0] * self.ni
        self.ah = [1.0] * self.nh
        self.ao = [1.0] * self.no

        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni - 1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni - 1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum += self.ai[i] * self.wi[i][j]
            #self.ah[j] = sigmoid(sum)
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum += self.ah[j] * self.wo[j][k]
            #self.ao[k] = sigmoid(sum)
            self.ao[k] = sigmoid(sum)

        return self.ao[:]

    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k] - self.ao[k]
            #output_deltas[k] = dsigmoid(self.ao[k]) * error
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k] * self.wo[j][k]
            #hidden_deltas[j] = dsigmoid(self.ah[j]) * error
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N * change + M * self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N * change + M * self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5 * (targets[k] - self.ao[k]) ** 2
        return error

    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])
            #self.ao[k] = sigmoid(sum)

    def train(self, patterns, iterations=1000, N=2, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 10 == 0:
                print('error %-.5f' % error)
                print('percent: %f\n' % ((float(i) / iterations) * 100))


def showWeights(inputs, wi, wo, no, nh):
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
        ah.append(sigmoid(sum))

    # output activations
    for k in range(no):
        sum = 0.0
        for j in range(nh):
            sum += ah[j] * wo[j][k]
        ao.append(sigmoid(sum))
    return ao[:]


def treinamento(nomearquivo):
    from datetime import datetime
    import json

    antes = datetime.today()
    with open(nomearquivo) as f:
        arquivo = f.read().replace('\n', '')
        arquivo = json.loads(arquivo)
    novoarquivo = []
    for item in arquivo:
        if rand(0, 1000) < 500:
            novoarquivo.append(item)
    print("len(novoarquivo): ", len(novoarquivo))
    for i, linha in enumerate(novoarquivo):
        for j, saida in enumerate(linha[1]):
            if saida == 0:
                novoarquivo[i][1][j] = -1

    inputsize = len(novoarquivo[0][0])
    outputsize = len(novoarquivo[0][1])
    n = NN(inputsize, 10, outputsize)
    n.train(novoarquivo, iterations=1000, N=0.5, M=0)
    dif = datetime.today() - antes
    print('secs: ', dif.seconds)
    #n.test(novoarquivo)

    n.weights()
    weights = Weight(n.wi, n.wo)
    path = "weights_" + nomearquivo
    with open(path, 'w+') as f:
        jsondumps = json.dumps(weights.__dict__)
        f.write(jsondumps)
    pass
# coding=utf-8
import XML2Json
import NormalizaEntradas
import NormalizaSaidas
import Rede
import os
import cPickle as pickle
import app


def main():
    os.chdir("../CSV")
    # converte de CSV para JSON
    #XML2Json.main()
    #NormalizaEntradas.main()
    #NormalizaSaidas.main()
    #Rede.train('t+6')
    '''for i in range(1, 7):
        Rede.train('radiacao+'+str(i))'''
    '''vars = ['t', 'chuva']
    for i in range(1, 7):
        for var in vars:
            Rede.train(var + '+' + str(i))'''
    app.main()


if __name__ == "__main__":
    main()

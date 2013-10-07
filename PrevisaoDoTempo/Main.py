# coding=utf-8
import XML2Json
import NormalizaEntradas
import NormalizaSaidas
import Rede
import os
import cPickle as pickle
import app
import Verificacao


def main():
    os.chdir("../CSV")
    # converte de CSV para JSON
    #XML2Json.main()
    #NormalizaEntradas.main()
    #NormalizaSaidas.main()
    #Rede.train('t+6')
    #Rede.train('t+1')
    #Rede.train('t_Proximas6Horas')
    '''vars = ['t', 'chuva', 'radiacao']
    for i in range(1, 7):
        for var in vars:
            Rede.train(var + '+' + str(i))'''
    '''for i in range(1, 7):
        Verificacao.verificar('t+%d' % i)'''
    #Verificacao.verificar('t_Proximas6Horas')
    #Verificacao.verificar('t+6')
    #Verificacao.verificar('t+1')
    app.main()


if __name__ == "__main__":
    main()

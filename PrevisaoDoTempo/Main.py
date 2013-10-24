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
    #Rede.train('radiacao+3')
    '''Rede.train('radiacao+3')
    Rede.train('radiacao+4')
    Rede.train('radiacao+5')
    Rede.train('radiacao+6')'''
    #Rede.train('t+6')
    #Rede.train('t+1')
    #Rede.train('t_Proximas6Horas')
    '''vars = ['t', 'chuva', 'radiacao']
    for i in range(1, 7):
        for var in vars:
            Rede.train(var + '+' + str(i))'''
    #for i in range(1, 7):
    #    Rede.train('radiacao+%d' % i)
    #for i in range(1, 7):
    #    Verificacao.verificar('chuva+%d' % i)
    #Verificacao.verificar('t_Proximas6Horas')
    #Verificacao.verificar('t+6')
    #for i in range(1, 7):
        #Verificacao.verificar('radiacao+%d' % i)

    #Verificacao.verificar('radiacao+3')
    app.main()


if __name__ == "__main__":
    main()

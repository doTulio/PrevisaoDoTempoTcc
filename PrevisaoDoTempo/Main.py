# coding=utf-8
import XML2Json
import CodificaEntradas
import EntradasESaidas
import BPNN
import BPNN2
import MostraResultados
import RMSE
import os
import Xbpnn

def main():
    os.chdir("../CSV")
    #XML2Json.main()
    #CodificaEntradas.main()
    #EntradasESaidas.main()
    BPNN.treinamento("A702_t_+1.json")
    #Xbpnn.treinamento("A702_t_+1.json")
    #BPNN.treinamento("A702_t_+2.json")
    #BPNN.treinamento("A702_t_+3.json")
    #BPNN.treinamento("A702_t_+4.json")
    #BPNN.treinamento("A702_t_+5.json")
    #BPNN.treinamento("A702_t_+6.json")
    #MostraResultados.prever()
    #RMSE.rodar("A702_t_+1.json")
    pass


if __name__ == "__main__":
    main()

# coding=utf-8
import XML2Json
import CodificaEntradas
import EntradasESaidas
import BPNN
import MostraResultados
import RMSE
import os
import View


def main():
    os.chdir("../CSV")
    #XML2Json.main()
    #CodificaEntradas.main()
    #EntradasESaidas.main()
    '''BPNN.treinamento("A702_t_+1.json")
    BPNN.treinamento("A702_t_+2.json")
    BPNN.treinamento("A702_t_+3.json")
    BPNN.treinamento("A702_t_+4.json")
    BPNN.treinamento("A702_t_+5.json")
    BPNN.treinamento("A702_t_+6.json")
    BPNN.treinamento("A702_chuva_+1.json")
    BPNN.treinamento("A702_chuva_+2.json")
    BPNN.treinamento("A702_chuva_+3.json")
    BPNN.treinamento("A702_chuva_+4.json")
    BPNN.treinamento("A702_chuva_+5.json")
    BPNN.treinamento("A702_chuva_+6.json")'''
    #MostraResultados.prever()
    #RMSE.rodar("A702_chuva_+6.json")
    View.app.main()


if __name__ == "__main__":
    main()

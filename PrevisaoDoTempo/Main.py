# coding=utf-8
import XML2Json
import NormalizaEntradas
import os
import app


def main():
    os.chdir("../CSV")
    # converte de CSV para JSON
    #XML2Json.main()
    NormalizaEntradas.main()
    #app.app.main()


if __name__ == "__main__":
    main()

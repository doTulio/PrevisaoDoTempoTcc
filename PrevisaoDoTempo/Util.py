class Util:
    @staticmethod
    def frombinarylisttoint(binarylist):
        from string import join
        resultstr = binarylist
        for i, item in enumerate(resultstr):
            resultstr[i] = str(item)
        binarylist = join(resultstr, sep="")
        return int(binarylist, 2)


class NormalizaEntradaESaida:
    def __init__(self, minprev, maxprev, minorig, maxorig):
        self.A = maxprev
        self.B = minprev
        self.a = minorig
        self.b = maxorig

    def normaliza(self, x):
        if self.B-self.A is 0:
            return 0
        return self.a + float((x - self.A)*(self.b-self.a))/(self.B-self.A)

# -*- coding: utf-8 -*-
from gunstar.http import RequestHandler
import Previsao


class IndexHandler(RequestHandler):
    def get(self):
        params = {
            'chuva': self.request.GET.get('chuva', 0),
            'hora': self.request.GET.get('hora', 11),
            'tanterior': self.request.GET.get('tanterior', 7.4),
            'tatual': self.request.GET.get('tatual', 8),
            'ranterior': self.request.GET.get('ranterior', 0),
            'ratual': self.request.GET.get('ratual', 134.8),
            'poanterior': self.request.GET.get('poanterior', 15.0),
            'poatual': self.request.GET.get('poatual', 15.0)
        }
        obj = {
            'temperaturas': Previsao.prevertemperatura(params),
            'precipitacao': Previsao.preverprecipitacao(params),
            'radiacao': Previsao.preverradiacao(params)
        }
        self.render_template('index.html', obj=obj, params=params)
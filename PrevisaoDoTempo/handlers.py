# -*- coding: utf-8 -*-
from gunstar.http import RequestHandler
import Previsao


class IndexHandler(RequestHandler):
    def get(self):
        params = {
            'chuva': self.request.GET.get('chuva', 0),
            'hora': self.request.GET.get('hora', 13),
            'tanterior': self.request.GET.get('tanterior', 29.6),
            'tatual': self.request.GET.get('tatual', 31.5),
            'ranterior': self.request.GET.get('ranterior', 1376.0),
            'ratual': self.request.GET.get('ratual', 2057.0)
        }
        obj = {
            'temperaturas': Previsao.prevertemperatura(params),
            'precipitacao': Previsao.preverprecipitacao(params)
        }
        self.render_template('index.html', obj=obj, params=params)
# -*- coding: utf-8 -*-
from gunstar.http import RequestHandler
import MostraResultados

class IndexHandler(RequestHandler):
    def get(self):
        params = {
            't': self.request.GET.get('t', 30),
            'h': self.request.GET.get('h', 12),
            'p': self.request.GET.get('p', 0),
            'r': self.request.GET.get('r', 3000)
        }
        obj = {
            'temperaturas': MostraResultados.temperaturas(params),
            'precipitacao': MostraResultados.precipitacao(params)
        }
        self.render_template('index.html', obj=obj, params=params)
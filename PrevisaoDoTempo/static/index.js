(function ($) {
    $(document).ready(function() {
        $('#container').highcharts({
            chart: {
                backgroundColor: '#EEEEEE',
                type: 'line'
            },
           title: {
               text: 'Previsão do Tempo'
           },
           xAxis: {
               categories: ['Atual', '+1 h', '+2 h', '+3 h', '+4 h', '+5 h', '+6 h']
           },
           yAxis: [{
               labels: {
                   formatter: function() { return this.value + '°C'; },
                   aling: 'left',
                   x: 0,
                   y: -2
               },
               showFirstLabel: true,
               title: {
                   text: 'Temperatura'
               }
           },{
               labels: {
                   align: 'right',
                   x: 0,
                   y: -2,
                   formatter: function() { return this.value + ' kJ/m²'; }
               },
               title: {
                   text: 'Radiação',
                   style: {
                       color: '#DDDF0D'
                   }
               },
               showFirstLabel: true,
               opposite: false
           }, {
               labels: {
                   align: 'right',
                   x: 0,
                   y: -2,
                   formatter: function() { return this.value + ' mm'; }
               },
               title: {
                   text: 'Precipitação'
               },
               showFirstLabel: false,
               opposite: true
           }
           ],
           series: [{
               type: 'spline',
               name: 'Temperatura',
               shadow: true,
               yAxis: 0,
               data: temperaturas
           }, {
               type: 'spline',
               yAxis: 1,
               borderWidth: 0,
               color: '#DDDF0D',
               name: 'Radiação',
               shadow: true,
               data: radiacao
           }, {
               type: 'column',
               yAxis: 2,
               borderWidth: 0,
               name: 'Precipitação',
               shadow: true,
               data: precipitacao
           }]
        });

        $("#visualizar").on('click', function() {
            $("#leitura").toggle();
        });
        $("#leitura #fechar").on('click', function() {
            $(this).parents("#leitura").hide();
        });
    });
})(jQuery);
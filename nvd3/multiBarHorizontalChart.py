#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python-nvd3 is a Python wrapper for NVD3 graph library.
NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.

Project location : https://github.com/areski/python-nvd3
"""

from NVD3Chart import NVD3Chart


class multiBarHorizontalChart(NVD3Chart):
    """
    usage ::

        chart = nvd3.multiBarHorizontalChart(name='multiBarHorizontalChart', height=400, width=400)
        xdata = [-14, -7, 7, 14]
        ydata = [-6, 5, -1, 9]
        y2data = [-23, -6, -32, 9]
        chart.add_serie(y=ydata, x=xdata)
        chart.add_serie(y=y2data, x=xdata)
        chart.buildhtml()

    js-code ::

        data_lineChart = [ { "key" : "Serie 1",
            "values" : [ { "x" : 0,
                  "y" : -2
                },
                { "x" : 1,
                  "y" : 4
                },
                { "x" : 2,
                  "y" : -7
                },
              ],
            "yAxis" : "1"
          },
          { "key" : "Serie 2",
            "values" : [ { "x" : 0,
                  "y" : -4
                },
                { "x" : 1,
                  "y" : 8
                },
                { "x" : 2,
                  "y" : -14
                },
              ],
            "yAxis" : "1"
          }
        ]

        nv.addGraph(function() {
                var chart = nv.models.multiBarHorizontalChart();
                chart.xAxis
                    .tickFormat(d3.format(',.2f'))
                chart.yAxis
                    .tickFormat(d3.format(',.2f'))
                d3.select('#multiBarHorizontalChart svg')
                    .datum(data_multiBarHorizontalChart)
                    .transition().duration(500)
                    .attr('height', 350)
                    .call(chart);

            return chart;
        });
    """
    def __init__(self, height=450, width=None, **kwargs):
        NVD3Chart.__init__(self, **kwargs)
        self.create_x_axis('xAxis', format=".2f")
        self.create_y_axis('yAxis', format=".2f")
        # must have a specified height, otherwise it superimposes both chars
        if height:
            self.set_graph_height(height)
        if width:
            self.set_graph_width(width)
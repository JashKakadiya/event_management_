from django.shortcuts import render
from django.http import HttpResponse
from .scripts.fusioncharts import FusionCharts

from ..models import *

def chart(request):
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Total Sales of each Event",
            "subCaption": "",
            "xAxisName": "Event",
            "yAxisName": "Count",
            "numberPrefix": "Ps.",
            "theme": "fusion"
        }

    dataSource['data'] = []
    for key in Event.objects.all():
      data = {}
      data['label'] = key.name
      data['value'] = key.total_count
      dataSource['data'].append(data)

    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    return render(request, 'index.html', {'output': column2D.render()})
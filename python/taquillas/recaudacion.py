#!/usr/bin/python
import cairo
import pycha.bar

width, height = (500, 400)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

dataSet = (
	('dataSet 1', ((0, 1), (1, 3), (2, 2.5))),
	('dataSet 2', ((0, 2), (1, 4), (2, 3))),
	('dataSet 5', ((0, 5), (1, 1), (2, 0.5))),     
)

options = {
       'legend': {'hide': False},
       'background': {'color': '#ffffff'},
	   'stroke': {'shadow': False},
}

chart = pycha.bar.VerticalBarChart(surface,options)
chart.addDataset(dataSet)
chart.render()

surface.write_to_png('output.png')

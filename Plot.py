from numpy import *
import Gnuplot

Original=genfromtxt('Plot.dat')
Random=genfromtxt('random_data.dat')
Random2=genfromtxt('random_data2.dat')

plot1=Gnuplot.PlotItems.Data(Original, with_="lp", title="Original")

plot2=Gnuplot.PlotItems.Data(Random, with_="lp", title="Random with B")

plot3=Gnuplot.PlotItems.Data(Random2, with_="lp", title="Random with B/2")

gp=Gnuplot.Gnuplot(persist = 1)

gp('set xlabel "AGENTS SELECTED" ')
gp('set ylabel "BUDGET UTILIZED" ')
gp('set xrange [0:15]')
gp('set yrange [0:120]')
gp('set grid')

gp.plot(plot1,plot2,plot3)

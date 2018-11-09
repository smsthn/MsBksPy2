import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class MsCharts:
    @staticmethod
    def makePie(window,data,legends):
        fig = matplotlib.figure.Figure(figsize=(4,4))
        ax = fig.add_subplot(111)
        ax.pie(data,labels=legends, autopct='%1.1f%%',)
        
        #fig.legend(legends)
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        #ax.add_artist(circle)
        return FigureCanvasTkAgg(fig, master=window)



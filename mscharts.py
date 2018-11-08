import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class MsCharts:
    @staticmethod
    def makePie(window,data,legends):
        fig = matplotlib.figure.Figure(figsize=(5,5))
        ax = fig.add_subplot(111)
        ax.pie(data)
        ax.legend(legends)
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        ax.add_artist(circle)
        return FigureCanvasTkAgg(fig, master=window)



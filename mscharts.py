import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.ttk import *
from books import *
import tkinter as tk





class MsCharts(Toplevel):
    def __init__(self,main,mainwindow,title, catagoriesdata, catagorieslegends, readingstatusdata, readingstatuslegends):
        Toplevel.__init__(self,main)
        self.main = mainwindow

        self.minsize(1200 , 800)
        self.title(title)
        self.config(bg='white')

        self.ctgglabel = Label(self,text='CatagoriesGraph',font=("Courier", 16,'bold'),background='white')
        self.ctgglabel.grid(row=0, column=0, padx=10, pady=10)
        self.ctgg = self.makePie(catagoriesdata,catagorieslegends)
        self.ctgg._master = self
        self.ctgg.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)
        self.ctgg.draw()
        self.ctgdlb = tk.Listbox(self, exportselection=False)
        self.ctgdlb.grid(row=2, column=0, padx=10, pady=10,sticky="sw")
        ttk.Separator(self,orient=VERTICAL).grid(row=1,column=0,rowspan=3,sticky="nse")
        self.rdsttsglabel = Label(self,text='ReadingStatusGraph',font=("Courier", 16,'bold'),background='white')
        self.rdsttsglabel.grid(row=0, column=1, padx=10, pady=10)
        self.rdsttsg = self.makePie(readingstatusdata, readingstatuslegends)
        self.rdsttsg._master = self
        self.rdsttsg.get_tk_widget().grid(row=1, column=1, padx=10, pady=10)
        self.rdsttsg.draw()
        self.rdsttsdlb = tk.Listbox(self, exportselection=False)
        self.rdsttsdlb.grid(row=2, column=1, padx=10, pady=10,sticky="se")

        for i in range(0,len(catagoriesdata)):
            self.ctgdlb.insert(tk.END,str(catagorieslegends[i])+' : ' +str(catagoriesdata[i]))
        for i in range(0,len(readingstatusdata)):
            self.rdsttsdlb.insert(tk.END,str(readingstatuslegends[i])+' : ' +str(readingstatusdata[i]))




    
    def makePie(self,data,legends):
        fig = matplotlib.figure.Figure(figsize=(6,6))
        ax = fig.add_subplot(111)
        ax.pie(data,labels=legends, autopct='%1.1f%%',)
        
        fig.legend(legends)
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        #ax.add_artist(circle)
        return FigureCanvasTkAgg(fig, master = self)



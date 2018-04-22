# class to control the main framework for graphing

from Tkinter import *
from singlePlaneEngine import SinglePlaneEngine
from threePlaneEngine import ThreePlaneEngine

class Controller:

    #graphing_mode 1 means 3d, graphing_mode 0 emans 2d
    def __init__(self,graphing_mode,window_width,window_height):
        self.window_width = window_width
        self.window_height = window_height
        if(graphing_mode == 0):
            self.engine = SinglePlaneEngine(self.window_width,self.window_height)
        elif(graphing_mode == 1):
            self.engine = ThreePlaneEngine(self.window_width,self.window_height)

    def run(self):

        #vec = self.engine.create_vector(0,0,2,2)
        #vec = self.engine.create_vector(0,0,0,2,5,3)

        root = Tk()
        canvas = Canvas(root,width=self.window_width,height=self.window_height)
        canvas.pack()

        canvas.create_line(vec.scale(200),fill="black")

        root.canvas = canvas.canvas = canvas
        canvas.data = { }
        self.engine.initCanvas(canvas)
        root.mainloop()

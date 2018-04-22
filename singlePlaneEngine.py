# engine for 2d rendering

from td.vector import Vector

class SinglePlaneEngine:

    def __init__(self,window_width,window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.originX = window_width/2
        self.originY = window_height/2

    def initCanvas(self,canvas):
        canvas.create_line(self.originX,0,self.originX,self.window_height, fill="red")
        canvas.create_line(0,self.originY,self.window_width,self.originY, fill="blue")

    def create_vector(self,x,y,xm,ym):
        x,y = self.parse_coords(x,y)
        return Vector(x,y,xm,(-1) * ym)

    def parse_coords(self,x,y):
        return (self.originX + x),(self.originY - y)

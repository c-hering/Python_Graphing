# engine for 3d rendering

from thrd.vector import Vector

class ThreePlaneEngine:

    def __init__(self,window_width,window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.originX = window_width/2
        self.originY = window_height/2

    def initCanvas(self,canvas):
        canvas.create_line(self.originX,0,self.originX,self.window_height, fill="red")
        canvas.create_line(0,self.originY,self.window_width,self.originY, fill="blue")
        canvas.create_line(0,self.window_height,self.window_width,0, fill="green")

    def create_vector(self,x,y,z,xm,ym,zm):
        x,y = self.parse_coords(x,y,z)
        return Vector(x,y,xm,(-1) * ym,zm)

    def parse_coords(self,x,y,z):
        x = x-z
        y = y-z
        return (self.originX + x),(self.originY - y)

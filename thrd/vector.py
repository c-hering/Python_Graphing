class Vector:

    def __init__(self,x,y,xm,ym,zm):
        self.starting_x = x
        self.starting_y = y
        self.slope_x = xm
        self.slope_y = ym
        self.slope_z = zm

    def scale(self, scalar):
        return self.starting_x,self.starting_y,self.starting_x + (scalar * self.slope_x) + (scalar * self.slope_z),self.starting_y + (scalar * self.slope_y) + (scalar * self.slope_x)

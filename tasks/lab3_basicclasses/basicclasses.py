class GeometricObject:
    def __init__(self, color: str, isFilled: bool):
        self.color = color
        self.isFilled = isFilled

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color},{self.isFilled})"

class Triangle(GeometricObject):
    def __init__(self, SideLen: float, color: str, isFilled: bool):
        super().__init__(color, isFilled)
        self.SideLen = SideLen
    

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color},{self.isFilled},{self.SideLen})"

class Cirle(GeometricObject):
    def __init__(self, radius: float, color: str, isFilled: bool):
        super().__init__(color, isFilled)
        self.radius = radius
        self.area = (self.radius**2)*3.14

    def __area__(self):
        return self.area

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color},{self.isFilled},{self.radius})"

class Rectangle(GeometricObject):
    def __init__(self, width: float, height: float, color: str, isFilled: bool):
        super().__init__(color, isFilled)
        self.width = width
        self.height = height
        self.area = self.width*self.height

    def __area__(self):
        return self.area 

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color},{self.isFilled},{self.width},{self.height})"

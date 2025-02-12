import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, area: {self.area():.2f}"
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __gt__(self, other):
        return self.radius > other.radius  # גדול יותר

    def __lt__(self, other):
        return self.radius < other.radius  # קטן יותר

    def __eq__(self, other):
        return self.radius == other.radius  # שווים
circles = [Circle(5), Circle(2), Circle(7), Circle(3)]
circles.sort()  # ממיין לפי רדיוס
for c in circles:
    print(c)  # ידפיס את כל העיגולים מהקטן לגדול




import turtle

def draw_circle(circle):
    turtle.penup()
    turtle.goto(0, -circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)

turtle.speed(1)
for c in circles:
    draw_circle(c)

# turtle.done()




#בזה נעזרתי ב
#chat gpt
#כדי ללמוד איך לצייר עיגול יותר גדול (הוא לימד אותי שזה אפשרי בכלל) לא הבנתי הכל אבל את הרוב כן
import turtle

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y - self.radius)  # הזזה כלפי מטה כך שהעיגול לא יצא מהמסך
        turtle.pendown()
        turtle.circle(self.radius)  # מצייר עיגול

# יצירת עיגולים גדולים יותר
big_circles = [Circle(100), Circle(150), Circle(200)]

# ציור העיגולים עם מרווח ביניהם
turtle.speed(2)
x_position = -200  # קביעת מיקום התחלתי

for c in big_circles:
    c.draw(x_position, 0)
    x_position += 250  # להזיז את כל עיגול ימינה כדי שלא יכסה את הקודם

turtle.done()


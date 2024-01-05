# 版权https://github.com/royalneverwin/beating-heart

from tkinter import * # Python 实现GUI界面的包
from math import sin, cos, pi, log
import random
import time

CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE = 11


def scatter_inside(x, y, beta=0.15): # log scatter & scatter inside
    ratiox = - beta * log(random.random()) #*** can modify ***#
    ratioy = - beta * log(random.random())
    dx = ratiox * (x - CANVAS_CENTER_X)
    dy = ratioy * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def heart_function(t, enlarge_ratio: float = IMAGE_ENLARGE):
    # heart function
    x = 16 * (sin(t)**3)
    y = -(13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))

    # enlarge
    x *= enlarge_ratio
    y *= enlarge_ratio

    # shift to the center of canvas
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)

def shrink(x, y, ratio):
    sk_range = -1 / ((x-CANVAS_CENTER_X) ** 2 + (y-CANVAS_CENTER_Y) ** 2)
    dx = ratio * sk_range * (x-CANVAS_CENTER_X)
    dy = ratio * sk_range * (y-CANVAS_CENTER_Y)
    return x - dx, y - dy


class Heart:
    def __init__(self, frame):
        self.points = set()
        self.edge_points = set()
        self.inside_points = set()
        self.all_points = {}
        self.build(2000) #*** can modify ***#
        self.frame = frame
        for f in range(frame):  # pre calculate
            self.calc(f)

        # for halo
        self.random_halo = 1000



    def build(self, number):
        # randomly find 'number' points on the heart curve
        for _ in range(number):
            t = random.uniform(0, 2 * pi) # t = angle
            x, y = heart_function(t)
            x, y = shrink(x, y, -1000)
            self.points.add((int(x), int(y)))

        # randomly find points on the edge
        for px, py in self.points:
            for _ in range(3): #*** can modify ***#
                x, y = scatter_inside(px, py, 0.05) #*** can modify ***#
                self.edge_points.add((x, y))

        # randomly find points inside the heart
        pt_ls = list(self.points)
        for _ in range(4000): #*** can modify ***#
            x, y = random.choice(pt_ls) # choice need idx, and set has no idx, only list has
            x, y = scatter_inside(x, y) #*** can modify ***#
            self.inside_points.add((x, y))


    def cal_position(self, x, y, ratio): # calculate the position of points when beating
        # attention: the closer to the center, the bigger beating range point has
        bt_range = 1 / ((x-CANVAS_CENTER_X) ** 2 + (y-CANVAS_CENTER_Y) ** 2)
        dx = ratio * bt_range * (x-CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * bt_range * (y-CANVAS_CENTER_Y) + random.randint(-1, 1)
        return x - dx, y - dy


    def calc(self, frame): # calculate points' position for different frame
        ratio = 800 * sin(frame / 10 * pi) #*** can modify ***# this is 30 fps
        all_pts = []

        # for halo
        halo_radius = int(4 + 6 * (1 + sin(self.frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(sin(self.frame / 10 * pi) ** 2))
        heart_halo_point = set()
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t, enlarge_ratio=11.6)
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                # 处理新的点
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_pts.append((x, y, size))

        # on the curve
        for x, y in self.points:
            x, y = self.cal_position(x, y, ratio)
            size = random.randint(1, 3) #*** can modify ***#
            all_pts.append((x, y, size))

        # on the edge
        for x, y in self.edge_points:
            x, y = self.cal_position(x, y, ratio)
            size = random.randint(1, 2) #*** can modify ***#
            all_pts.append((x, y, size))

        # inside
        for x, y in self.inside_points:
            x, y = self.cal_position(x, y, ratio)
            size = random.randint(1, 2) #*** can modify ***#
            all_pts.append((x, y, size))

        self.all_points[frame] = all_pts


    def render(self, canvas, frame): # draw points
        for x, y, size in self.all_points[frame % self.frame]: # set operation
            canvas.create_rectangle(x, y, x+size, y+size, width=0, fill='#ff7171')


def draw(root: Tk, canvas: Canvas, heart: Heart, frame=0):
    canvas.delete('all')
    heart.render(canvas, frame)
    root.after(30, draw, root, canvas, heart, frame+1)


if __name__ == '__main__':
    root = Tk()
    root.title('漂亮宝贝一周年快乐')
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()
    heart = Heart(20)
    draw(root, canvas, heart)
    root.mainloop()
__author__ = 'Troy'
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class FBD:

    def __init__(self,xlen,ylen):
        self.figure = plt.figure()
        self.xBase, self.yBase = -(xlen/2.0), -(ylen/2.0)
        self.xLen, self.yLen = xlen, ylen
        self.body = plt.Rectangle((self.xBase, self.yBase), xlen, ylen, fc='r')
        self.forces = {}

    // DRAWING FUNCTIONS

    def calc_axes(self):
    #
        xPad, yPad = 2, 2
        xmin = self.xBase - xPad
        xmax = self.xBase + self.xLen + xPad
        ymin = self.yBase - yPad
        ymax = self.yBase + self.yLen + yPad
        return (xmin,xmax,ymin,ymax)

    def direction_base(self, direction):
        directions = {
            "TOP": [self.xBase + self.xLen / 2.0, self.yBase + self.yLen],
            "BOTTOM": [self.xBase, self.yBase + self.yLen],
            "LEFT": [self.xBase, self.yBase + self.yLen / 2.0],
            "RIGHT": [self.xBase + self.xLen, self.yBase + self.yLen / 2.0],
        }
        return directions[direction]

    def force_arrows(self):
        arrows = []
        for i in self.forces:
            force = self.forces[i]
            baseX, baseY = force["base"]
            arrow = plt.arrow(baseX, baseY, force["x"], force["y"], head_width=.1, head_length=.3, fc='k', ec='k')
            arrows.append(arrow)
        return arrows

    def draw(self):
        plt.gca().add_patch(self.body)
        plt.axis(self.calc_axes())
        for arrow in self.force_arrows():
            plt.gca().add_patch(arrow)
        return self.figure.show()

    # GENERAL FUNCTIONS

    def add_force(self, vector, name="", direction="NONE", base=[0,0],text=""):
        fid = len(self.forces) + 1
        if name == "":
            name = fid
        fmagnitude = np.sqrt(sum([i**2 for i in vector]))
        fdir = np.rad2deg(np.arctan2(vector[1], vector[0]))
        if direction != "NONE":
            base = self.direction_base(direction)

        self.forces[name] = {
            "id": fid,
            "mag": fmagnitude,
            "dir": fdir,
            "vector": vector,
            "x": vector[0],
            "y": vector[1],
            "base": base,
            "stem": direction,
            "text": text,
        }


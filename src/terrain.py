import numpy as np


class Terrain(object):
    def __init__(self, power, roughness, mu, sigma):
        self.edgesize = 2 ** power + 1
        self.maxheight = self.edgesize - 1
        self.map = np.full((self.edgesize, self.edgesize), self.maxheight / 2)
        self.roughness = roughness
        self.mu = mu
        self.sigma = sigma

        self.setcorners()
        self.divide(self.edgesize - 1)

    def setcorners(self):
        """
        setcorners()

        Set initial values for points in the corners of the map.
        Initial value is equal to half of the max value.
        """
        self.map[0, 0] = self.maxheight / 2
        self.map[0, self.edgesize - 1] = self.maxheight / 2
        self.map[self.edgesize - 1, 0] = self.maxheight / 2
        self.map[self.edgesize - 1, self.edgesize - 1] = self.maxheight / 2

    def divide(self, size):
        half = size / 2
        scale = self.roughness * size

        if half < 1:
            return

        for y in np.arange(half, self.edgesize - 1, size):
            for x in np.arange(half, self.edgesize - 1, size):
                self.square(
                    x, y, half,
                    np.random.normal(self.mu, self.sigma) * scale * 2 - scale)

        for y in np.arange(0, self.edgesize, half):
            for x in np.arange(np.mod(y + half, size), self.edgesize, size):
                self.diamond(
                    x, y, half,
                    np.random.normal(self.mu, self.sigma) * scale * 2 - scale)

        self.divide(size / 2)

    def square(self, x, y, size, offset):
        average = np.mean([
            self.map[int(x - size), int(y - size)],
            self.map[int(x + size), int(y - size)],
            self.map[int(x + size), int(y + size)],
            self.map[int(x - size), int(y + size)]
        ])

        self.map[int(x), int(y)] = average + offset

    def diamond(self, x, y, size, offset):
        points = []

        try:
            points.append(self.map[int(x), int(y - size)])
        except IndexError as ie:
            pass
        try:
            points.append(self.map[int(x + size), int(y)])
        except IndexError as ie:
            pass
        try:
            points.append(self.map[int(x), int(y + size)])
        except IndexError as ie:
            pass
        try:
            points.append(self.map[int(x - size), int(y)])
        except IndexError as ie:
            pass

        average = np.mean(points)

        self.map[int(x), int(y)] = average + offset

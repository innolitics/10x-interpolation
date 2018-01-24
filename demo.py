from math import pi

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


def sweep_image(x, y):
    frequency = 0.1 + 0.1*x/100
    img = np.sin(2*pi*x*frequency)
    return img


def compare_images(a, b):
    figure, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.imshow(a)
    ax1.set_title('A')
    ax2.imshow(b)
    ax2.set_title('B')
    ax3.imshow(a - b)
    ax3.set_title('A - B')
    return figure


if __name__ == '__main__':
    nx, ny = (101, 101)

    xv = np.linspace(0, 100, nx)
    yv = np.linspace(0, 100, ny)
    x1, y1 = np.meshgrid(xv, yv)
    x2, y2 = np.meshgrid(xv + 0.5, yv + 0.5)

    image = sweep_image(x1, y1)
    shifted_image = sweep_image(x2, y2)

    known_points = np.hstack((x1.flatten(), y1.flatten()))
    known_values = image.flatten()

    # TODO: get this line to work (I think it is bc I am using meshgrid instead
    # of megrid; see http://louistiao.me/posts/numpy-mgrid-vs-meshgrid/
    shifted_image_nearest = griddata(
            known_points, known_values, (x1, y1), method='nearest')

    compare_images(shifted_image, shifted_image_nearest)
    plt.show()

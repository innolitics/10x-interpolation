from math import pi

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    '''
    Our band-limited signal.
    '''
    return np.sin(2*pi*x*0.1) + 4.3*np.sin(2*pi*x*0.04) - 3*np.sin(2*pi*x*0.01)


def sinc_interp(x, xp, yp):
    '''
    x - locations where you want to interpolate
    xp - locations of samples; is assumed to be equidistant and increasing
    yp - values of samples
    '''
    assert len(xp) == len(yp)
    assert len(xp) > 2
    T = xp[1] - xp[0]
    y = np.zeros_like(x)
    for i in range(len(xp)):
        y += yp[i]*np.sinc((x - xp[i])/T)
    return y


if __name__ == '__main__':
    nx = 101

    x0 = np.arange(0, nx + 1, dtype=np.float64)
    f0 = f(x0)

    x0_5 = x0 + 0.5
    f0_5 = f(x0_5)

    f0_linear = np.interp(x0, x0_5, f0_5)
    f0_sinc = sinc_interp(x0, x0_5, f0_5)

    fig1, ax1 = plt.subplots()
    ax1.plot(x0, f0, 'k-', label='f sampled at 0, 1, ...')
    ax1.plot(x0_5, f0_5, 'r-', label='f sampled at 0.5, 1.5, ...')
    ax1.plot(x0, f0_linear, 'b-', label='f linearly interpolated at 0, 1, ... from samples at 0.5, 1.5, ...')
    ax1.plot(x0, f0_sinc, 'g:', label='f sinc interpolated at 0, 1, ... from samples at 0.5, 1.5, ...')
    ax1.set_title("Demonstration of how linear interpolation acts as a low pass filter, but sinc interp doesn't")
    ax1.legend()

    plt.show()

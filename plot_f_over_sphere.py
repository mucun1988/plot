from mayavi import mlab
import numpy as np
from scipy.special import sph_harm


def f(x, y, z):
    return x * y * z


def quadratic(x, y, z):
    v = np.array([x, y, z])
    return Q.dot(v).dot(v) + b.dot(v)


def plot_f_over_sphere(f, n=1001):
    # Create a sphere
    r = 1
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0:pi:n * 1j, 0:2 * pi:n * 1j]

    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)

    s = np.zeros_like(x)

    for i in range(n):
        for j in range(n):
            s[i, j] = f(x[i, j], y[i, j], z[i, j])

    mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 400))
    mlab.clf()

    mlab.mesh(x, y, z, scalars=s, colormap='jet')
    mlab.colorbar(orientation='vertical')
    mlab.outline()
    mlab.axes()
    mlab.view(distance=10)
    mlab.show()


Q = np.random.randn(3, 3)
Q = Q / 2 + Q.T / 2
b = np.array([-1, 1, -1])

plot_f_over_sphere(f=quadratic)

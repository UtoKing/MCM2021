from Fungi import Fungi1, Fungi2, Fungi3, Environment
import sys
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    environment = Environment(0.61, 26, 100)
    fungi1 = Fungi1(4.71, environment)
    fungi2 = Fungi2(4.11, environment)
    fungi3 = Fungi3(3.77, environment)
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    t = 0
    for i in range(sys.maxsize ** 10):
        fungi1.set_dr(environment)
        fungi1.set_number(0.001)
        fungi2.set_dr(environment)
        fungi2.set_number(0.001)
        fungi3.set_dr(environment)
        fungi3.set_number(0.001)
        environment.set_fungi_density(fungi1, fungi2, fungi3)
        environment.set_wood_number(fungi1, fungi2, fungi3, 0.001)
        if environment.wood_number <= 1:
            break
        t = t + 1
        a.append(fungi1.dr)
        b.append(environment.fungi1_density)
        c.append(fungi2.dr)
        d.append(environment.fungi2_density)
        e.append(fungi3.dr)
        f.append(environment.fungi3_density)
        g.append(environment.wood_number)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(t)
    x = np.arange(0, t * 0.01-0.005, 0.01)
    plt.subplot(2, 1, 1)
    plt.plot(x, a)
    plt.plot(x, c)
    plt.plot(x, e)
    plt.ylabel('Decomposition rate')
    plt.title('Fungi')
    plt.legend(['Fungi1', 'Fungi2', 'Fungi3'])
    plt.subplot(2, 1, 2)
    plt.plot(x, b)
    plt.plot(x, d)
    plt.plot(x, f)
    plt.xlabel('time')
    plt.ylabel('Fungi-density')
    plt.legend(['Fungi1', 'Fungi2', 'Fungi3'])
    plt.show()

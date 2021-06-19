import numpy as np

def gradient_descent(x,y):
    m_current = b_current = 0
    iteration = 1000
    n = len(x)
    learning_rate = 0.001

    for i in range(iteration):
        y_prdicted = m_current * x + b_current
        cost = (1/n) * sum([val**2 for val in (y-y_prdicted)])
        md = -(2/n)*sum(x*(y-y_prdicted))
        bd = -(2/n)*sum(y-y_prdicted)
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print("m {}, b{}, cost {}, iteration {}".format(m_current , b_current , cost , i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,2,10,15])

gradient_descent(x,y)
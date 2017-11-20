import numpy as np
import pylab as plb

def lcg(numbers, a, m, x_0):
    numbers_out = [x_0]
    i = 0
    for x in range(numbers):
        numbers_out.append(((a*numbers_out[i])%m)/m)
        i += 1
    return np.array(numbers_out)

if __name__ == "__main__":
    first = lcg(10000, 2, 3, 1)
    second = lcg(10000, 2**31, 2**16+3, 1)
    third = lcg(10000, 7**5, 2**31-1, 1)
    print("Standard deviation first:", np.sqrt(np.mean(first**2)-np.mean(first)**2))
    print("Standard deviation second:", np.sqrt(np.mean(second ** 2) - np.mean(second)**2))
    print("Standard deviation third:", np.sqrt(np.mean(third ** 2) - np.mean(third)**2))
    plb.figure()
    bins = np.linspace(0, 1, 10)
    plb.hist(first, bins=np.linspace(min(first), max(first), 10), label="first")
    plb.figure()
    plb.hist(second, bins=bins, label="second")
    plb.figure()
    plb.hist(third, bins=np.linspace(min(third), max(third), 10), label="third")

    '''
    The parameters are only in the second case suitable. In the first and third example the values are too close to zero.
    '''
    y_second = np.append(second[1:], lcg(0, 2**31, 2**16+3, second[-1]))
    y_third = np.append(third[1:],lcg(0, 2**31, 2**16+3, third[-1]))
    plb.figure()
    plb.scatter(second, y_second, marker=".")
    plb.title("scatter plot of second")
    plb.xlabel("x_i of second")
    plb.ylabel("x_i+1 of second")
    plb.figure()
    plb.scatter(third, y_third, marker=".")
    plb.xlabel("x_i of third")
    plb.ylabel("x_i+1 of third")
    plb.title("scatter plot of third")
    plb.show()
    '''Second is still better'''

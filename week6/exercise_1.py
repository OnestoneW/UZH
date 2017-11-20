import scipy.stats as sp
import numpy as np
import pylab as plb

'''
Question 1:
The expected values for the standard deviation and the expected value are the sums of all variables.
So the expected value of the new (gaussian) distribution is the sum of all expected values. Same with the std. deviation.

'''

def generate_arrays(how_many, size_of_array):
    '''Generates a number of arrays with exponentional distributed numbers.
        returns a list of arrays'''
    arrays = []
    for i in range(how_many):
        arrays.append(sp.expon.rvs(loc=0, scale=1, size=size_of_array))

    return arrays

if __name__ == "__main__":
    test = generate_arrays(1000, 100)
    sum_of_numbers = sum(test)
    mean_of_sum = np.mean(sum_of_numbers)

    mean_calculated = 0
    for arr in test:
        mean_calculated += np.mean(arr)

    deviation_calculated = 0
    for arr in test:
        deviation_calculated += np.sqrt(np.mean(arr**2)-np.mean(arr)**2)


    deviation_observed = np.sqrt(np.mean(sum_of_numbers**2)-np.mean(sum_of_numbers)**2)

    print("Calculated mean value:", mean_calculated)
    print("Observed mean value:", mean_of_sum)
    print("Calculated std deviation:", deviation_calculated)
    print("Observed std devaition:", deviation_observed)

    #normalize the gaussian:
    x = np.linspace(min(sum_of_numbers), max(sum_of_numbers), len(sum_of_numbers))
    gaussian = sp.norm.pdf(x, loc=mean_calculated, scale=deviation_observed
                           )
    plb.figure()
    plb.hist(sum_of_numbers, bins=x, normed=True)
    plb.xlabel("summed up distribution")
    plb.ylabel("propability")
    plb.plot(x, gaussian, 'r')
    plb.show()
import numpy as np
import pylab as plb
import scipy.stats as sp

def create_expon_randoms(lamda, n):
    return -np.log(plb.rand(n)) / lamda

def mean_t(times):
    return 1/len(times) * sum(times)

if __name__ == "__main__":
    expon_1 = create_expon_randoms(1, 500)
    expon_2 = create_expon_randoms(1, 500)
    expon_3 = create_expon_randoms(1, 500)
    expon_4 = create_expon_randoms(1, 500)
    expon_5 = create_expon_randoms(1, 500)
    mean_t_1 = mean_t(expon_1)
    mean_t_2 = mean_t(expon_2)
    mean_t_3 = mean_t(expon_3)
    mean_t_4 = mean_t(expon_4)
    mean_t_5 = mean_t(expon_5)
    print("calculated means for the samples:")
    print(mean_t_1, mean_t_2, mean_t_3, mean_t_4, mean_t_5)

    #(2):
    new_dist = []
    new_std_dev = []
    for i in range(1000):
        expon = create_expon_randoms(1, 500)
        mean = np.mean(expon)
        std_deviation = np.sqrt(np.mean(expon**2) - np.mean(expon)**2)
        new_dist.append(mean)
        new_std_dev.append(std_deviation)

    plb.figure()
    bins = np.linspace(min(new_dist), max(new_dist), 50)
    plb.hist(new_dist, bins=bins)
    plb.xlabel("estimated mean life")
    plb.ylabel("count")
    plb.show()
    #yes, the mean value of the distribution agrees with my expectation. Since I summed up all mean values, the mean should exactly be my mean.

    #(6)
    for i in range(5):
        values = create_expon_randoms(1, 500)
        estimation = len(values) / sum(values)
        print("esitmation number", i, ":", estimation)

    #(7)
    dist_of_lamda = []
    std_deviation_lamda = []
    for i in range(1000):
        values = create_expon_randoms(1, 500)
        estimation = len(values) / sum(values)
        dev = np.sqrt(np.mean(values**2) - np.mean(values)**2)
        dist_of_lamda.append(estimation)
        std_deviation_lamda.append(dev)
    x_values = np.linspace(min(dist_of_lamda), max(dist_of_lamda), 50)
    plb.figure()
    plb.hist(dist_of_lamda, bins=x_values)
    plb.xlabel("lambda estimations")
    plb.ylabel("counts")
    plb.show()
    #also this one statisfies my expectations.
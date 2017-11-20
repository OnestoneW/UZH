import pylab as plb
import numpy as np

def calc_mean(data_set):
    mean_value = np.mean(data_set)
    return round(mean_value, 2)

def calc_uncert_mean(data_set):
    mean_value = np.mean(data_set)
    uncertainity = 0
    variance = 0

    for value in data_set:
        variance += (value - mean_value)**2

    variance = (1/len(data_set))*variance
    variance = np.sqrt(variance)/np.sqrt(len(data_set))
    return round(variance, 2)

def calc_variance(data_set):
    mean_value = np.mean(data_set)
    variance = 0
    for value in data_set:
        variance += (value - mean_value)**2
    variance = variance/len(data_set)
    return round(variance, 2)

def calc_std_deviation(data_set):
    mean_value = np.mean(data_set)
    deviation = 0
    for value in data_set:
        deviation += (value - mean_value) ** 2
    deviation = np.sqrt(deviation / len(data_set))
    return round(deviation, 2)

def calc_deviation_hist(n, bins):
    bin_length = bins[1] - bins[0]
    centers = bins + bin_length/2
    centers = centers[:-1]

    variance = sum(n*(centers**2))/sum(n) - (sum(n*centers)/sum(n))**2

    deviation = np.sqrt(variance)
    return variance, deviation

def calc_covariance(set_1, set_2):
    cov = np.mean(set_1*set_2) - np.mean(set_1)*np.mean(set_2)
    return cov

def calc_corellation(set_1, set_2):
    cov = calc_covariance(set_1, set_2)
    cor = cov / (calc_std_deviation(set_1)*calc_std_deviation(set_2))
    return cor

if __name__ == "__main__":
    data = plb.loadtxt("ironman.dat")
    total_rank = data[:, 0]
    year_of_birth = data[:, 1]
    age = 2010 - year_of_birth
    total_time = data[:, 2]
    swimming_time = data[:, 3]
    swimming_rank = data[:, 4]
    cycling_time = data[:, 5]
    cycling_rank = data[:, 6]
    running_time = data[:, 7]
    running_rank = data[:, 8]
    number_of_bins = 100
    n_age, bins_age, patches_age = plb.hist(age, number_of_bins)
    n_time, bins_time, patches_time = plb.hist(total_time, number_of_bins)

    print("mean value on ages",calc_mean(age))
    print("uncertainity on mean:", calc_uncert_mean(age))
    print("mean value on total_time:", calc_mean(total_time))
    print("uncertainity on mean:", calc_uncert_mean(total_time))
    print("variance on age:", calc_variance(age))
    print("variance on time:", calc_variance(total_time))
    print("standard deviation on age:", calc_std_deviation(age))
    print("standard deviation on time:", calc_std_deviation(total_time))

    variance_age, deviation_age = calc_deviation_hist(n_age, bins_age)
    variance_time, deviation_time = calc_deviation_hist(n_time, bins_time)
    print("variance on time:", variance_age)
    print("variance on time:", variance_time)
    print("standard deviation on age:", deviation_age)
    print("standard deviation on time:", deviation_time)

    #It is clearly to see that if the bin width gets smaller (more bins), hist-data get`s closer to the calculated value.
    print("Differences variance ", str(variance_time-calc_variance(total_time)))
    print("Differences deviation", str(deviation_time - calc_std_deviation(total_time)))

    print("cov tot_rank to tot_time:", calc_covariance(total_rank, total_time))
    print("cor tot_rank to tot_time:", calc_corellation(total_rank, total_time))
    print("cov year_of_birth", calc_covariance(year_of_birth, total_time))
    print("cor year_of_birth and tot_time:", calc_corellation(year_of_birth, total_time))
    print("cov tot_time and swim_time", calc_covariance(total_time, swimming_time))
    print("cor tot_time and swim_time", calc_corellation(total_time, swimming_time))
    print("cov cycl_time and runn_time", calc_covariance(cycling_time, running_time))
    print("cor cycl_time and runn_time", calc_corellation(cycling_time, running_time))
    #The calculated values harmony with my observations from the scatter plot last week

    total_time_seconds = total_time*60
    print("cov year_of_birth", calc_covariance(year_of_birth, total_time_seconds))
    print("cor year_of_birth and tot_time:", calc_corellation(year_of_birth, total_time_seconds))
    #the correlation stays the same.

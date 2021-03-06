# Draw 10,000 samples out of Poisson distribution: n_nohitters
season_mean = 251/115
n_nohitters = np.random.poisson(season_mean, size=10000)

# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)

# Compute probability of getting seven or more: p_large
p_large = n_large / len(n_nohitters)

# Print the result
print('Probability of seven or more no-hitters:', p_large)

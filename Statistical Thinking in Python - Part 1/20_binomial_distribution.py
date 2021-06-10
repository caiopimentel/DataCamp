# Take 10,000 samples out of the binomial distribution: n_defaults
n = 100
p = 0.05
n_defaults = np.random.binomial(n, p, size=10000)

# Compute CDF: x, y
x, y = ecdf(n_defaults)

# Plot the CDF with axis labels
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('n_defaults')
_ = plt.ylabel('ECDF')

# Show the plot
plt.show()

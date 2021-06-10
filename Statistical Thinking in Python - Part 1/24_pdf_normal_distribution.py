# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
mean = 20
samples_std1 = np.random.normal(mean, 1, size=100000)
samples_std3 = np.random.normal(mean, 3, size=100000)
samples_std10 = np.random.normal(mean, 10, size=100000)

# Make histograms
_ = plt.hist(samples_std1, normed=True, histtype='step', bins=100)
_ = plt.hist(samples_std3, normed=True, histtype='step', bins=100)
_ = plt.hist(samples_std10, normed=True, histtype='step', bins=100)

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()

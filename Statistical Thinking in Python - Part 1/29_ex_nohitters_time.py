# Draw samples of waiting times: waiting_times
nohitter_mean = 764 
hitingcycle_mean = 715 
waiting_times = successive_poisson(nohitter_mean, hitingcycle_mean, 100000)

# Make the histogram
_ = plt.hist(waiting_times, bins=100, normed=True, histtype='step')


# Label axes
_ = plt.xlabel('Probability')
_ = plt.ylabel('Waiting time')

# Show the plot
plt.show()

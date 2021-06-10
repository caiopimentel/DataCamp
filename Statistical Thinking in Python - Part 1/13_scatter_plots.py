# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel('versicolor_petal_length (cm)')
_ = plt.ylabel('versicolor_petal_width (cm)')

# Show the result
plt.show()
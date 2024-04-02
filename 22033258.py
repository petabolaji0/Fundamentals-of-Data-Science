# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Import .csv file
data = np.genfromtxt("data8-1.csv", delimiter=' ')
print(data)

# Divide data into bins and plot histogram to visualize distribution
# Create histogram
hist, bins = np.histogram(data, bins=35)

# Calculate mid points of bins and width
bin_mid = 0.5*(bins[:-1] + bins[1:])
bin_width = bins[1:]-bins[:-1]

# Convert histogram frequencies to get probability density function
probd_fn = hist/np.sum(hist)

# Create plot of densities over the bin midpoints
plt.figure(figsize=(10, 6))
plt.bar(bin_mid, probd_fn, 0.8*bin_width)
plt.xlim(0, 140000)

# Add x-label, y-label, and title
plt.xlabel('Salaries, €', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
plt.title('Probability Density Function', fontsize=20)

# Calculate the Mean Annual Salary (W)
W = np.sum(bin_mid * probd_fn).round(2)
print('\n Mean Annual Salary(W) = €', W)

# Show Mean Annual Salary on the plot
plt.plot([W, W], [0.0, max(probd_fn)], color='red', linestyle='--',\
         label='Mean Annual salary (W) = €34,136.72')
plt.text(W, max(probd_fn), s='W', fontsize=13, color='red')

# Calculate the Standard Deviation (X)
variance = np.sum((bin_mid - W)**2 * probd_fn)
X = np.sqrt(variance).round(2)
print('\n Standard Deviation(X) = €', X)

# Show Standard Deviation on the plot
plt.plot([X, X], [0.0, max(probd_fn)], color='black', linestyle='--',\
         label='Standard Deviation (X) = €23,454.97')
plt.text(X, max(probd_fn), s='X', fontsize=13, color='black')

# Add legend
plt.legend()

# Save the figure as an image file
plt.savefig("probability_density_plot.png", dpi=300)

# Show plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Function to plot histograms and KDE
def plot_distribution(sample, dist_name, ax, sample_size):
    # Plot histogram
    ax.hist(sample, bins = 30, density = True, alpha=0.5, color='b')

    # Plot KDE
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    if dist_name == 'Normal':
        p = stats.norm.pdf(x)
    elif dist_name == 'Cauchy':
        p = stats.cauchy.pdf(x)
    elif dist_name == 'Student':
        p = stats.t.pdf(x, df=3)
    elif dist_name == 'Poisson':
        # For Poisson, we increase the range to cover all possible values
        x = np.arange(0, max(sample) + 1)
        p = stats.poisson.pmf(x, mu=10)
    elif dist_name == 'Uniform':
        p = stats.uniform.pdf(x, loc=-np.sqrt(3), scale=2 * np.sqrt(3))

    ax.plot(x, p, 'k', linewidth=2)
    title = f"{dist_name} distribution, n={sample_size}"
    ax.set_title(title)


# Sample sizes
sample_sizes = [10, 50, 1000]

# Distributions
distributions = {
    'Normal': lambda size: np.random.normal(0, 1, size),
    'Cauchy': lambda size: np.random.standard_cauchy(size),
    'Student': lambda size: np.random.standard_t(3, size),
    'Poisson': lambda size: np.random.poisson(10, size),
    'Uniform': lambda size: np.random.uniform(-np.sqrt(3), np.sqrt(3), size)
}

# Plotting
fig, axes = plt.subplots(len(distributions), len(sample_sizes), figsize=(18, 15))

for i, (dist_name, dist_func) in enumerate(distributions.items()):
    for j, size in enumerate(sample_sizes):
        sample = dist_func(size)
        plot_distribution(sample, dist_name, axes[i][j], size)
        if dist_name == "Cauchy":
            plt.xlim(-50, 50)

plt.tight_layout()
plt.show()

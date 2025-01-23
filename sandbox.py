from pycounts_524_2024.pycounts import count_words
count_words("zen.txt")

from pycounts_524_2024.plotting import plot_words

counts = count_words("zen.txt")
fig = plot_words(counts, 10)
plt.show()

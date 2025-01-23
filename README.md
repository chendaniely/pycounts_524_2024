# pycounts_524_2024

Calculate word counts in a text file!

SemVer update needs special commit message starting text.

## Installation

```bash
$ pip install pycounts_524_2024
```

## Usage

`pycounts_524_2024` can be used to count words in a text file and plot results
as follows:

```python
from pycounts_524_2024.pycounts import count_words
from pycounts_524_2024.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_524_2024` was created by Daniel Chen. It is licensed under the terms of the MIT license.

## Credits

`pycounts_524_2024` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

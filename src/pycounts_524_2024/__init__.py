# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_524_2024")

from pycounts_524_2024.pycounts import count_words

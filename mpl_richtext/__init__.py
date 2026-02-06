"""
mpl-richtext: Rich text rendering for Matplotlib
"""

from .core import richtext
from .version import __version__
from .utils import format_nepali_number, convert_to_nepali

__all__ = ['richtext', '__version__', 'format_nepali_number', 'convert_to_nepali']

__author__ = 'Rabin Katel'
__email__ = 'kattelrabinraja13@gmail.com'
__license__ = 'MIT'
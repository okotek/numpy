"""SciPy Core

You can support the development of SciPy by purchasing documentation at

http://www.trelgol.com

It is being distributed for a fee for a limited time to try and raise money for
development.

Documentation is also available in the docstrings.
"""

try:
    from __core_config__ import show as show_core_config
except ImportError:
    show_core_config = None

if show_core_config is None:
    print 'Running from scipy core source directory.'
else:
    from scipy.base import *
    import scipy.basic as basic
    from scipy.basic.fft import fft, ifft
    from scipy.basic.random import rand, randn
    import scipy.basic.fft as fftpack
    import scipy.basic.linalg as linalg
    import scipy.basic.random as random
    from core_version import version as __core_version__
    from scipy.test.testing import ScipyTest
    test = ScipyTest('scipy').test

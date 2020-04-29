# coding: utf8

import os
__version__ = '0.0.1'

VERSION = __version__

GLO_PATH = os.path.dirname(os.path.abspath(__file__))

def get_version():
	return __version__
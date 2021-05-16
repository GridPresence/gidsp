import math
import numpy as np
import scipy as sp

class Signal:

    def __init__(self, sampfreq=None, sigin=None, generator=None):
        if sampfreq is Not None:
            self._sampf = (float)sampfreq
            self._sampt = 1.0/self._sampf
        if sigin is not None:
            
            

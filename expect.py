import ConfigParser
import sys

import importlib


import networkx

import random
import re

import time

from scipy.stats import geom
from scipy.stats import lognorm
from scipy.stats import uniform
from scipy.stats import zipf

config = ConfigParser.RawConfigParser()
class ConstDistribution():
    def __init__(self, value):
        self.value = value
    def rvs(self, value):
        return value
    def next():
        return self.value

class GetDistribution():
    def __init__(self, name):
        distribution = config.get(name, 'distribution')
        if distribution == 'const':
            self.func = ConstDistribution(config.getfloat(name, 'param1'))
        else:
            self.func = getattr(importlib.import_module('scipy.stats'), distribution)
    def expectation(self):
        return self.func.expect(self.func,2.245,1.133)



a = GetDistribution('InterSessionTime')
b= a.expectation()
print b
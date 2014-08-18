#access to current and super-level modules
import sys
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

from csv_reader import readcsv
from mysql import database

input = readcsv('/Users/Zhe/Desktop/grammer/csvtrial.csv')


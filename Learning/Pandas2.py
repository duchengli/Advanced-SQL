import pandas as pd
import numpy as np
from pandas import DataFrame,Series


frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(frame.ix[:,'d':'e'])
print(frame.loc[:,'d':'e'])

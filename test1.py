import math
import random
from scipy.stats import norm, zscore
population=eval(input("有幾個同學: "))
data = range(1,population+1)
print("請回答: ",random.sample(data,1))
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 07:05:22 2019

@author: Rudrajit
"""

import matplotlib.pyplot as plt
from random import randint
from statistics import mean,median
Estimates=[randint(1,1000) for x in range (75)]
Estimates.sort()
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:len(Estimates)-tv]
y=[5 for x in range (len(Estimates))]
plt.plot(Estimates,y,'r--')
plt.plot([500],[5],'g^')#actual value (let)
plt.plot([mean(Estimates)],[5],'ro')#mean
plt.plot([median(Estimates)],[5],'bs')#median
plt.show()

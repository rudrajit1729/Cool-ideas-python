from random import randint
from statistics import mean
from scipy import stats
Estimates=[randint(1,1000) for x in range (75)]
print(Estimates)
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
#trimmed value
##tv=int(0.1*len(Estimates))
##Estimates=Estimates[tv:len(Estimates)-tv]
##print(Estimates)
##print(mean(Estimates))
print(m)

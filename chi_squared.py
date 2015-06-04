from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# clean data by dropping null rows
loansData.dropna(inplace=True)

# use collections to determine occurrences of each quantity of open credit lines
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print freq
print "\n"

# determine frequency of each quantity of open credit lines
count_sum = sum(freq.values())

for k,v in freq.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)
print "\n"

print "...graphing data..."

# graph frequency as bar graph
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

print "DONE!" + "\n"

# perform chi-squared test
chi, p = stats.chisquare(freq.values())
print "chi-square is " + str(chi)
print "\n"
print "p-value is " + str(p)
# chi
# > 2408.433146517214
# p
# > 0.0

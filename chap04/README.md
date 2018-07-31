# Cumulative Distribution Functions

### 4.1 The limits of PMFs 
PMFs  work  well  if  the  number  of  values  is  small.   But  as  the  number  of values increases, the probability
associated with each value gets smaller and the effect of random noise increases.
These problems can be mitigated by **binning** the data; that is, dividing the range of values into non-overlapping
intervals and counting the number of values in each bin.  Binning can be useful, but it is tricky to get the size
of the bins right.  If they are big enough to smooth out noise, they might also smooth out useful information.
An alternative that avoids these problems is the **cumulative distribution function (CDF).**

### 4.2 Percentiles
In this context, the percentile rank is the fraction of people who scored lower than you (or the same). So
if you are “in the 90th percentile,” you did as well as or better than 90% of the people who took the exam.

Calculating percentile :
```
def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank
```
As an example, if the scores in the sequence were 55, 66, 77, 88 and 99, and you got the 88,  then your percentile
rank would be 100 * 4 / 5 which is 80.
If you are given a percentile rank and you want to find the corresponding value, one option is to sort the values and
search for the one you want:
```
def Percentile(scores, percentile_rank):
    """The result of this calculation is a percentile."""
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
    return score
```
This implementation of Percentile is not efficient. A better approach is to use the percentile rank to compute the
index of the corresponding percentile:
```
def Percentile2(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) // 100
    return scores[index]
```
 To  summarize, PercentileRank takes a value and computes its percentile rank in a set of values; Percentile
takes a percentile rank and computes the corresponding value.

### 4.3 CDFs
The CDF is the function that maps from a value to its percentile rank. To evaluate CDF(x) for a particular value of x
, we compute the fraction of values in the distribution less than or equal to x.
```
def EvalCdf(sample, x):
    count = 0.0
    for value in sample:
        if value <= x:
            count += 1
    prob = count / len(sample)
    return prob
```
if x is greter than largest val in sample then CDF(x) = 1, now think about CDF(x) if x<smallest val in sample.

### 4.4 Representing CDFs
thinkstats2 provides a class named Cdf that represents CDFs. The fundamental methods Cdf provides are:
1. Prob(x) : Given a value x, computes the probability **p = CDF(x)**.
2. Value(p): Given a probability p, computes the corresponding value, x.
```
live, firsts, others = first.MakeFrames()
cdf = thinkstats2.Cdf(live.prglngth, label='prglngth')
```
thinkplot provides a function named Cdf that plots Cdfs as lines. It takes some time to get used to CDFs, but once
you do, I think you will find that they show more information, more clearly, than PMFs.
```
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='weeks', ylabel='CDF')
```

### 4.5 Comparing CDFs
CDFs are especially useful for comparing distributions. 
```
first_cdf = thinkstats2.Cdf(firsts.totalwgt_lb, label='first')
other_cdf = thinkstats2.Cdf(others.totalwgt_lb, label='other')
thinkplot.PrePlot(2)
thinkplot.Cdfs([first_cdf, other_cdf])
thinkplot.Show(xlabel='weight (pounds)', ylabel='CDF')
```
We can see that first babies are slightly lighter throughout the distribution,
with a larger discrepancy above the mean.

### 4.6 Percentile Based statistics
Once you have computed a CDF, it is easy to compute percentiles and percentile ranks.  The Cdf class provides these
two methods:
1. PercentileRank(x): Given  a  value x, computes  its  percentile  rank,100*CDF(x).
2. Percentile(p): Given a percentile rank p, computes the corresponding value,x. Equivalent to Value(p/100).

**Median : ** the 50th percentile is the value that divides the distribution in half, also known as the
median. It also has center tendency. More generally, percentiles are often used to summarize the shape of a distri-
bution.  Statistics  like  these  that  rep-
resent equally-spaced points in a CDF are called [quantiles](https://en.wikipedia.org/wiki/Quantile)

### 4.7 Random Numbers
Sample is a random sample of 100 birth weights, chosen with replacement; that is, the same value could be chosen
more than once.Ranks is a list of percentile ranks.
```
weights = live.totalwgt_lb
cdf = thinkstats2.Cdf(weights, label='totalwgt_lb')
sample = np.random.choice(weights, 100, replace=True)
ranks = [cdf.PercentileRank(x) for x in sample]
rank_cdf = thinkstats2.Cdf(ranks)
thinkplot.Cdf(rank_cdf)
thinkplot.Show(xlabel='percentile rank', ylabel='CDF')
```
This figure shows is that 10% of the sample is below the 10th percentile, 20% is below the 20th percentile, and so on,
exactly as we should expect. So, regardless of the shape of the CDF, the distribution of percentile ranks
is uniform.  This property is useful, because it is the basis of a simple and efficient algorithm for generating
random numbers with a given CDF.

### Comparing Percentile Length
Percentile  ranks  are  useful  for  comparing  measurements  across  different
groups.  For example, people who compete in foot races are usually grouped
by  age  and  gender.   To  compare  people  in  different  age  groups,  you  can
convert race times to percentile ranks.
```
def PositionToPercentile(position, field_size):
beat = field_size - position + 1
percentile = 100.0 * beat / field_size
return percentile ;

def PercentileToPosition(percentile, field_size):
beat = percentile * field_size / 100.0
position = field_size - beat + 1
return position ;
```
In my age group, denoted M4049 for “male between 40 and 49 years of age”,
I came in 26th out of 256.  So my percentile rank in my age group was 90%.
If I am still running in 10 years , I will be in the M5059
division.  Assuming that my percentile rank in my division is the same, how
much slower should I expect to be?
There were 171 people in M5059, so I would have to come in between 17th
and 18th place to have the same percentile rank.  The finishing time of the
17th runner in M5059 was 46:05,  so that’s the time I will have to beat to
maintain my percentile rank.
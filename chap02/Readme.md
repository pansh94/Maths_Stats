# Distribution
In Python, an efficient way to compute frequencies is with a dictionary. Given
a sequence of values,t :
```
hist = {}
for x in t:
    hist[x] = hist.get(x, 0) + 1
```

### 2.2 Representing Hist
The Hist constructor can take a sequence, dictionary, pandas Series, or another Hist.  You can instantiate a Hist object
like this:
```
import thinkstat2;
hist = thinkstat2.Hist([1,2,2,3,5]);
print(hist) #Hist({1: 1, 2: 2, 3: 1, 5: 1})
```
Hist objects provide Freq, which takes a value and returns its frequency:
`hist.Freq(2) or hist[2] #2 `

Values returns an unsorted list of the values in the Hist:
`hist.Values() #[1,5,3,2]`

To loop through the values in order, you can use the built-in function sorted:
```
for val in sorted(hist.Values()):
    print(val, hist.Freq(val))
```
### 2.3 Plotting Histogram
thinkplot.py that provides functions for plotting Hists and other objects defined in thinkstats2.py
```
import thinkplot
thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')
```

### 2.4 NSFG Variables
The most common value in data, called the *mode*.

### 2.5 Outliers
Rare Values are not always visible in histogram. There it's always good to check for extreme
values that might be errors in measurement and recording, or might be accurate reports of rare events, known as 
*Outliers*.
Hist provides methods Largest and Smallest, which take an integer *n* and return the n largest or smallest  
values from the histogram:
```
for weeks, freq in hist.Smallest(10):
    print(weeks, freq) #[0, 4, 9, 13, 17, 18, 19, 20, 21, 22]
```
Before 10 week preganancy data and above 30 weeks data are outliers and are possible error. Between 10 and 30
may be premature birth or error data.The best way to handle outliers depends on “domain knowledge”.

### 2.6 First Babies
```
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
first_hist = thinkstats2.Hist(firsts.prglngth)
other_hist = thinkstats2.Hist(others.prglngth)
width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Show(xlabel='weeks', ylabel='frequency',xlim=[27, 46])
```
*thinkplot.PrePlot* takes the number of histograms we are planning to plot; it uses this information to 
choose an appropriate collection of colors. With *width=0.45* , the total width of the two bars is 0.9,
leaving some space between each pair. Finally, I adjust the axis to show only data between 27 and 46 weeks because
this is most valid age for baby pregnancy.
Histograms are useful because they make the most frequent values immediately apparent.  But they are not the best
choice for comparing two distributions.

### 2.7 Summarizing distribution
A histogram is a complete description of the distribution of a sample. But often we want to summarize the distribution
with a few descriptive statistics. Some of the character are :
1. **Central tendency** : Do values tend to cluster around a certain value ?
2. **Modes** : Is there more than one cluster?
3. **Spread** :  How much variability is there in the values?
4. **Tails** : How quickly do the probabilities drop off as we move away from the modes?
5. **Outliers**  Are there extreme values far from the modes?
Statistics designed to answer these questions are called **summary statistics**. Most common one is mean.
**Mean** : It is tend to describe central tendency. f you have a sample of
n values, xi , the mean, ̄x, is the sum of the values divided by the number of values; in other words
`mean = 1(x1+x2+x3....+xn)/n`
Sometimes the mean is a good description of a set of values.  For example, apples are all pretty much
the same size (at least the ones sold in supermarkets). So if I buy 6 apples and the total weight is 3
pounds, it would be a reasonable summary to say they are about a half pound each.
But pumpkins are more diverse.  Suppose I grow several varieties in my garden, and one day I harvest three
decorative pumpkins that are 1 pound each, two pie pumpkins that are 3 pounds each, and one Atlantic Giant
pumpkin that weighs 591 pounds.  The mean of this sample is 100 pounds,  but if I told you “The average pumpkin
in my garden is 100 pounds,” that would be misleading.  In this example, there is no meaningful average because
there is no typical pumpkin.

### 2.8 Variance
Variance and mean can solve the pumpkin problem. Variance describe *spread* summary distribution.
`S^2 = (x1-mean)^2+(x2-mean)^2+(x3-mean)^2...+(xn-mean)^2/n`
The term xi− mean is called the “deviation from the mean,” so variance is the
mean squared deviation. The square root of variance, S , is the **standard deviation**. 
Pandas  data  structures  provides  methods  to  compute  mean,  variance  and
standard deviation:
```
mean = live.prglngth.mean()
var = live.prglngth.var()
std = live.prglngth.std()
```
For all live births,  the mean pregnancy length is 38.6 weeks,  the standard
deviation is 2.7 weeks, which means we should expect deviations of 2-3 weeks
to be common. Variance  of  pregnancy  length  is  7.3,  which  is  hard  to  interpret,  especially
since  the  units  are  weeks^2,  or  “square  weeks.”  Variance  is  useful  in  some
calculations, but it is not a good summary statistic.

### 2.9 Effective
An *effect size* is a summary statistic intended to describe (wait for it) the size of an effect.  For 
example, to describe the difference between two groups, one obvious choice is the difference in the means.

Mean pregnancy length for first babies is 38.601; for other babies it is 38.523.The difference is 0.078 weeks,
which works out to 13 hours.  As a fraction of the typical pregnancy length, this difference is about 0.2%.

Another  way  to  convey  the  size  of  the  effect  is  to  compare  the  difference between  groups  to  the
variability  within  groups. **Cohen’s d** is  a  statistic intended to do that; it is defined as
d = { mean(x1) - mean(x2) }/s 
x1 and x2 are gp and s is pooled standard deviation.
Here’s the Python code that computes Cohen’s d:
```
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
```
In this example, the difference in means is 0.029 standard deviations, which is small. To put that in perspective,
the difference in height between men and women is about 1.7 standard deviations.
Links :
1. [see Effect Size](https://en.wikipedia.org/wiki/Effect_size)
2. [see Mode](https://en.wikipedia.org/wiki/Mode_(statistics))




# Probability Mass Function 
### Pmfs
Another way to represent a distribution is probability mass function. it maps from each value to its probability.
A **probability** is a frequency expressed as a fraction of the sample size, n. To get from frequencies to probabilities,
we divide through by n, which is called **normalization**.

Given  a  Hist,  we  can  make  a  dictionary  that  maps  from  each  value  to  its probability:
```
n =  hist.Total() ;
d = {} ;
for x,v in hist.Items() :
    d[x] = v/n ;
```
Or we can use the Pmf class provided by **thinkstats2**. Like Hist, the Pmf constructor can take a list, pandas Series,
dictionary, Hist, or another Pmf object. Here’s an example with a simple list:
```
import thinkstats2 ;
pmf = thinkstats2.Pmf([1,2,2,3,4]) ;
pmf >> {1:0.2, 2: 0.4, 3: 0.2, 5: 0.2}
```
To look probability associated with value :
```
pmf.Prob(2) >>> 0.4
pmf[2] >>> 0.4
pmf.Incr(2,0.2) 
pmf.Prob(2) >>> 0.6
pmf.Mult(2,0.5)
pmf[2] >>> 0.3
```
If you modify a Pmf, the result may not be normalized; that is, the probabilities may no longer add up to 1.
To check, you can call Total, which returns the sum of the probabilities:
`pmf.Total()  == 0.9`
To renormalize, call Normalize:
```
>>> pmf.Normalize()
>>> pmf.Total()
1.0
```

### 3.2 Plotting PMFs
thinkplot provides two ways to plot Pmfs:

1. To plot a Pmf as a bar graph, you can use **thinkplot.Hist** .Bar graphs are most useful if the number of values
 in the Pmf is small.
2. To plot a Pmf as a step function, you can use **thinkplot.Pmf** .This option is most useful if there are a large
 number of values and the Pmf is smooth.  This function also works with Hist objects.

Note :  Based on this figure(**plot_bar_step**), first babies seem to be less likely than others to arrive on time
(week 39) and more likely to be a late (weeks 41 and 42).

### 3.3 Other Visualization
Histograms and PMFs are useful while you are exploring data and trying to identify patterns and relationships. Once
you have an idea what is going on, a  good  next  step  is  to  design  a  visualization  that  makes  the  patterns
you have identified as clear as possible.
Lets focus on distribution near the mode.
```
weeks = range(35, 46)
diffs = []
for week in weeks:
    p1 = first_pmf.Prob(week)
    p2 = other_pmf.Prob(week)
    diff = 100 * (p1 - p2)
    diffs.append(diff)
```

### 3.4 Class Size Paradox
If you ask the Dean for the average class size, he would construct a PMF, compute the mean, and report that the
average class size is 23.7.  Here’s the code:
```
d = { 7: 8, 12: 8, 17: 14, 22: 4,27: 6, 32: 12, 37: 8, 42: 3, 47: 2 }
pmf = thinkstats2.Pmf(d, label='actual')
print('mean', pmf.Mean())
```
But if you survey a group of students, ask them how many students are in their classes, and compute the mean, you
would think the average class was bigger.  Let’s see how much bigger.
```
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x) #For each class size,x, we multiply the probability by x,the number of students
        #who  observe  that  class  size.   The  result  is  a  new  Pmf  that  represents  the biased distribution.
    new_pmf.Normalize()
    return new_pmf
    
def UnbiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, 1.0/x)
    new_pmf.Normalize()
    return new_pmf
#It’s similar to BiasPmf ,the only difference is that it divides each probability by x instead of multiplying.
```

### 3.5 DataFrame Indexing
```
import numpy as np
import pandas
array = np.random.randn(4, 2) #create 2d array of 4 rows.
df = pandas.DataFrame(array)
#OR
index = ['a', 'b', 'c', 'd']
columns = ['A', 'B']
df = pandas.DataFrame(array, columns=columns, index = index) #To assign column names and index to each row.
```
**Note :**
If you are given a PMF, you can still compute the mean, but the process is slightly different:
 ̄x =Summation of (pi * xi) for all 0<=i<=n
where the
xi are the unique values in the PMF and pi = PMF(xi). Similarly, you can compute variance like this:
S^2=Summation of pi(xi−̄x)^2 for all i


# Maths_Stats
Mathematical analysis of dataset. [Think Stat Book for Data Scientist](http://greenteapress.com/thinkstats2/thinkstats2.pdf)
[Documentation of think plot](http://greenteapress.com/thinkstats2/thinkplot.html)
## DataSet Information
Since  1973  the  U.S.  Centers  for  Disease  Control  and  Prevention  (CDC)
have  conducted  the  National  Survey  of  Family  Growth  (NSFG),  which  is
intended to gather “information on family life, marriage and divorce, preg-
nancy, infertility, use of contraception, and men’s and women’s health.  The
survey results are used ...  to plan health services and health education pro-
grams,  and  to  do  statistical  studies  of  families,  fertility,  and  health.”[See](
http://cdc.gov/nchs/nsfg.htm)

The  NSFG  has  been  conducted  seven  times;  each  deployment  is  called  a 
cycle. We will use data from Cycle 6, which was conducted from January 2002 to March 2003.

1. **2002FemPreg.dat.gz** :  Pregnancy data from Cycle 6 of the NSFG is in a file called
2002FemPreg.dat.gz ; it is a gzip-compressed data file in plain text(ASCII), with fixed
width columns.  Each line in the file is a record that contains data about one pregnancy.

2. **2002FemPreg.dct** : is a Stata dictionary file.  Stata is a statistical software system; a “dictionary” in this
context is a list of variable names, types, and indices that identify where in
each line to find each variable.

### 2.Variable in dataframe :
1. *caseid* is the integer ID of the respondent.
2. *prglngth* is the integer duration of the pregnancy in weeks
3. *outcome* is an integer code for the outcome of the pregnancy. The code 1 indicates a live birth.
4. *pregordr* is  a  pregnancy  serial  number;  for  example,  the  code  for  a respondent’s first pregnancy is 1, for the second       pregnancy is 2, and so on.
5. *birthord* is a serial number for live births; the code for a respondent’s first child is 1, and so on.  For outcomes other than live birth, this field is blank.
6. *birthwgt_lb* and *birthwgt_oz* contain the pounds and ounces parts of the birth weight of the baby.
7. *agepreg* is the mother’s age at the end of the pregnancy.
8. *finalwgt* is the statistical weight associated with the respondent. It is a floating-point value that indicates the number of people in the U.S. population this respondent represents.

### 3.Plotting Histogram(2.2) :
Module called thinkplot.py provides functions for plotting Hists and other objects defined in thinkstats2.py. It is based on pyplot which  is  part  of  the matplotlib package. 
```
import thinkplot
thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')
```

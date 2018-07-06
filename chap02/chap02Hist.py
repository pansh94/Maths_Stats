import nsfg ;
import thinkstats2;
import thinkplot ;
import math ;

def MakeDataframes():
    preg = nsfg.ReadFemPreg();
    live = preg[preg.outcome == 1];
    first = live[live.birthord == 1] ;
    other = live[live.birthord != 1] ;
    return (live,first,other) ;

def drawHist(ser,lab,xLab,yLab):
    hist = thinkstats2.Hist(ser, label = lab);
    thinkplot.Hist(hist);
    thinkplot.Show(xlabel = xLab, ylabel= yLab);

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

def firstBabies(first,others):
    first_hist = thinkstats2.Hist(first.prglngth)
    others_hist = thinkstats2.Hist(others.prglngth)
    width = 0.45 ;
    #thinkplot.preplot(2) ;
    #thinkplot.Hist(first_hist, align='right', width=width)
    #thinkplot.Hist(others_hist, align='left', width=width)
    #thinkplot.Show(xlabel='weeks', ylabel='frequency', xlim=[27, 46])
    first_mean = first.prglngth.mean() ;
    other_mean = others.prglngth.mean() ;
    print("Mean of Pregnancy length of first born :",first_mean ) ;
    print("Mean of Pregnancy length of other than first born :", other_mean);
    pct_mean = (abs(first_mean - other_mean)*100)/other_mean ;
    print("% change between first and other born : ",pct_mean) ;

def ex_que2_3(hist):
    max_fre = 0;
    max_key = -1 ;
    #method1
    for week,fre in hist.Largest(len(hist)) :
        if(fre > max_fre) :
            max_fre = fre ;
            max_key = week ;
    #method2
    p, x = max([(p, x) for x, p in hist.Items()])
    print('Mode of series = ',max_key," And ",x) ;

def AllMode(hist):
    print(sorted(hist.Items(), key=itemgetter(1), reverse=True));


def que2_4(first,other):
    print("Cohen effect value for weight of first baby and other : ",CohenEffectSize(first.totalwgt_lb,other.totalwgt_lb));

def main():

    live,first,other = MakeDataframes() ;

    #plot  the histogram of birthwgt_lb for live births.
    #drawHist(live.birthwgt_oz,'birthwgt_oz','Ounce','Frequency') ;
    #drawHist(live.agepreg, 'agepreg','Pregnancy Age','Frequency');
    #drawHist(live.prglngth,'prglngth','Pregnancy Length','Frequency')
    firstBabies(first,other) ;
    print("Mean for Live birth : ",live.prglngth.mean()) ;
    print("Variance for Live birth : ",live.prglngth.var());
    print("Standard Deviation for Live birth : ",live.prglngth.std());
    cohen_d = CohenEffectSize(first.prglngth,other.prglngth) ;
    print("Diff in mean per standard deviation : ", cohen_d) ;

    #exercise 2.3
    hist = thinkstats2.Hist(live.prglngth) ;
    ex_que2_3(hist)
    que2_4(first,other) ;


if __name__ == '__main__' :
    main();
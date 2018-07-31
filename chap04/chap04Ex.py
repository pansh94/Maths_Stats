import numpy as np ;
import nsfg ;
import first ;
import thinkstats2 ;
import thinkplot ;

def MakeDataFrames():
    preg = nsfg.ReadFemPreg();
    live = preg[preg.outcome == 1];
    first = live[live.birthord == 1];
    other = live[live.birthord != 1];
    return (live, first, other);

def PercentileRank(group,value):
    count = 0 ;
    for val in group:
        if val <= value :
            count+= 1 ;
    return(100*(count/len(group))) ;

def Percentile(group,percentile_rank):
    group.sort();
    index =  percentile_rank * (len(scores)-1) // 100 ;
    return(group[index]) ;

def CalCDF(group,value):
    count = 0 ;
    for val in group :
        if val <= value :
            count+=1 ;

    return(count/len(group)) ;

def LiveCDFAnalysis(live):
    live_prglng_cdf = thinkstats2.Cdf(live.prglngth) ;
    thinkplot.Cdf(live_prglng_cdf) ;
    thinkplot.Show(xlabel='Pregnancy length (weeks)', ylabel='CDF', loc='upper left') ;

def WeightDiffInFirstOther(first,other):
    first_cdf = thinkstats2.Cdf(first.totalwgt_lb,label = 'First') ;
    other_cdf = thinkstats2.Cdf(other.totalwgt_lb,label = 'Other') ;
    thinkplot.PrePlot(2);
    thinkplot.Cdfs([first_cdf,other_cdf]);
    thinkplot.Show(xlabel='Weight (pounds)', ylabel='CDF') ;

def RandomLiveWeightAnalysis(live):
    weight = live.totalwgt_lb ;
    live_cdf = thinkstats2.Cdf(weight,label = "live") ;
    random_sample = np.random.choice(weight,100,replace=True) ;
    ranks = [live_cdf.PercentileRank(x) for x in random_sample ] ;
    rank_cdf = thinkstats2.Cdf(ranks) ;
    thinkplot.Cdf(rank_cdf);
    thinkplot.Show(xlabel = "Percentile Rank",ylabel = "CDF") ;

def main():
    live,first,other= MakeDataFrames() ;
    LiveCDFAnalysis(live) ;
    WeightDiffInFirstOther(first,other) ;
    RandomLiveWeightAnalysis(live) ;

if __name__ == '__main__' :
    main();


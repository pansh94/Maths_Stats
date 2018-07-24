import thinkstats2 ;
import nsfg ;
import thinkplot ;
from collections import defaultdict ;
import numpy as np ;
import math ;

def MakeDataFrames():
    preg = nsfg.ReadFemPreg();
    live = preg[preg.outcome == 1];
    first = live[live.birthord == 1];
    other = live[live.birthord != 1];
    return (live, first, other,preg);

def MakePregMap(df):
    d = defaultdict(list);
    for index,caseid in  df.caseid.iteritems():
        d[caseid].append(index);
    return d ;

def ProbilityMassFunction(group):
    hist = thinkstats2.Hist(group) ;
    n = hist.Total() ;
    map_prob = {} ;
    for x,v in hist.Items():
        map_prob[x] = v/n ;
    #OR
    pmf = thinkstats2.Pmf(group) ;
    #print(type(map_prob) ," AND ", type(pmf));
    return  pmf ;

def plot_bar_step(first_pmf,other_pmf):
    """PrePlot takes optional parameters rows and cols to make a grid of figures for bar grapg"""
    width = 0.5 ;
    thinkplot.PrePlot(2,cols=2) ;
    thinkplot.Hist(first_pmf , align = "left",width = width ) ;
    thinkplot.Hist(other_pmf, align="right", width=width) ;
    thinkplot.Config(xlabel = "weeks", ylabel = "probability" , axis= [27,46,0,0.6]) ;
    #for step graph
    thinkplot.PrePlot(2) ;
    thinkplot.SubPlot(2) ;
    thinkplot.Pmfs([first_pmf,other_pmf]);
    thinkplot.Show(xlabel = "weeks", axis= [27,46,0,0.6]);

def pmf_diff_in_percentage(first_pmf,other_pmf):
    """This figure makes the pattern clearer:  first babies are less likely to be born
    in week 39, and somewhat more likely to be born in weeks 41 and 42"""
    weeks = range(35,46); # To look near mode
    diffs = [] ;
    for week in weeks:
        p1 = first_pmf.Prob(week) ;
        p2 = other_pmf.Prob(week) ;
        diff = 100 * (p1 - p2) ;
        diffs.append(diff) ;
    thinkplot.Bar(weeks,diffs);
    thinkplot.Show(xlabel = "Weeks", ylabel = "pmf % diff") ;

def PairwiseDiffInPrglngthOfSameResp(preg_map , preg):
    """ select respondents who have at least two live births and compute pairwise differences."""
    hist = thinkstats2.Hist()

    for caseid, indices in preg_map.items():
        if len(indices) >= 2:
            pair = preg.loc[indices[0:2]].prglngth
            diff = np.diff(pair)[0]
            hist[diff] += 1
    thinkplot.Hist(hist) ;

def CalculateMeanFromPmf(pmf):
    sum = 0 ;
    for x,p in pmf.Items():
        sum += p*x ;
    print("Calculated Mean : ",sum," || Defined Mean : ",pmf.Mean());

def CalculateVarFromPmf(pmf,m):
    sum = 0;
    for x,p in pmf.Items():
        sum += p * (x - m)*(x - m) ;
    print("Calculated Variance : ", sum, " || Defined Variance : ", pmf.Var());

def main():
    live,first,other,preg = MakeDataFrames() ;
    first_pmf = ProbilityMassFunction(first.prglngth) ;
    other_pmf = ProbilityMassFunction(other.prglngth) ;
    #plot_bar_step(first_pmf,other_pmf) ;
    #pmf_diff_in_percentage(first_pmf,other_pmf);
    #prg_map = MakePregMap(live) ;
    #PairwiseDiffInPrglngthOfSameResp(prg_map,preg) ;
    CalculateMeanFromPmf(first_pmf) ;
    CalculateVarFromPmf(other_pmf,other_pmf.Mean()) ;

if __name__ == '__main__' :
    main();
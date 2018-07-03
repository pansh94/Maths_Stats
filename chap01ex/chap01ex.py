"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import nsfg
import re
import pandas as pd
import numpy as np
from collections import defaultdict

class FixedWidthVariable(object):

    def __init__(self, variables, index_base=0):
        self.variables = variables ;
        self.colspecs = variables[['start', 'end']] - index_base
        #print(self.colspecs)
        self.colspecs = self.colspecs.astype(np.int).values.tolist()
        #print(self.colspecs)
        self.names = variables['name']

    def ReadFixedWidth(self, filename, **options):
        df = pd.read_fwf(filename,
                             colspecs=self.colspecs,
                             names=self.names,
                             **options)
        return df
def MakePregMap(df):
    d = defaultdict(list);
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d

def readData(dct_file,dat_file):
    type_map= dict(byte=int, int=int, long=int, float=float, double=float) ;
    var_info = [] ;
    for line in open(dct_file):
        match = re.search(r'_column\(([^)]*)\)',line) ;
        if match :
            start = int(match.group(1));
            t = line.split();
            #print(t);
            vtype, name, fstring = t[1:4]
            #print("==>",vtype,name,fstring)
            name = name.lower() ;
            if vtype.startswith('str') :
                vtype = str ;
            else :
                vtype = type_map[vtype] ;
            long_desc = ' '.join(t[4:]).strip('"')
            #print("=====>>>",long_desc)
            var_info.append((start,vtype,name,fstring,long_desc));
    columns = ['start', 'type', 'name', 'fstring', 'desc']
    variables = pd.DataFrame(var_info, columns=columns)
    variables['end'] = variables.start.shift(-1)
    variables.loc[len(variables) - 1, 'end'] = 0
    #print(variables.head()) ;
    dct = FixedWidthVariable(variables, index_base=1)
    return dct


def CleanFemResp(df):
    pass

def createDf():
    nrows = None;
    dct = readData('2002FemResp.dct', '2002FemResp.dat.gz');
    df = dct.ReadFixedWidth('2002FemResp.dat.gz', compression='gzip', nrows=nrows);
    return df ;

def main():
    df_resp= createDf() ;
    #print(df.head())
    print(df_resp.pregnum.value_counts())#num of preg for each resp

    df_preg = nsfg.ReadFemPreg()
    preg_map = MakePregMap(df_preg)

    #print(preg_map);#pregnenacy data
    #checking id num of pregnancy for each easpondant in resp df is equal to no of entry in pregnancy df for that resps
    for index,pregNum in df_resp.pregnum.items() :
        caseid = df_resp.caseid[index] ;
        index_list = preg_map[caseid] ;

        if(len(index_list) != pregNum):
            print(caseid,len(index_list),pregNum);



if __name__ == '__main__':
    main()

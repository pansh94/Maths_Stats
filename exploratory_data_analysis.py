import nsfg;

df = nsfg.ReadFemPreg();
print(df.info()) ;
df = nsfg.CleanFemPreg(df) ;
print(df.totalwgt_lb);


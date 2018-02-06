import pandas as pd
df1=pd.read_table("corpus/play1.txt")#importing all play text files
df2=pd.read_table("corpus/play2.txt")
df3=pd.read_table("corpus/play3.txt")
df4=pd.read_table("corpus/play4.txt")
df5=pd.read_table("corpus/play5.txt")
df6=pd.read_table("corpus/play6.txt")
df7=pd.read_table("corpus/play7.txt")
df8=pd.read_table("corpus/play8.txt")
df9=pd.read_table("corpus/play9.txt")
df10=pd.read_table("corpus/play10.txt")
df11=pd.read_table("corpus/play11.txt")
df12=pd.read_table("corpus/play12.txt")
df13=pd.read_table("corpus/play13.txt")
df14=pd.read_table("corpus/play14.txt")
df15=pd.read_table("corpus/play15.txt")
df16=pd.read_table("corpus/play16.txt")
df17=pd.read_table("corpus/play17.txt")
df18=pd.read_table("corpus/play18.txt")
df19=pd.read_table("corpus/play19.txt")
df20=pd.read_table("corpus/play20.txt")
df21=pd.read_table("corpus/play21.txt")
df22=pd.read_table("corpus/play22.txt")
df23=pd.read_table("corpus/play23.txt")
df24=pd.read_table("corpus/play24.txt")
df25=pd.read_table("corpus/play25.txt")
df26=pd.read_table("corpus/play26.txt")
df27=pd.read_table("corpus/play27.txt")
#making list of all the dataframes
lst=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27]
g=pd.Series(False)#initialized Series object as false
f=pd.Series(False)
def lin_search1(val):
    d=val.columns.values#column header that is name of play
    print "please wait!!Checking in",d
    size=val[d].shape[0]#no. of rows
    for i in range(size):
        series=val[d].iloc[i]#each row becomes series
        g=series.str.contains("Octavius") & series.str.contains("Antony") & ~series.str.contains("Cleopatra")
        if g.any():#if ay true value found
            print "Found in",d
            return -1

def lin_search2(val):
    d=val.columns.values
    print "please wait!!Checking in",d
    size=val[d].shape[0]
    for i in range(size):
        series=val[d].iloc[i]
        global g
        if not g.any():
            g=(series.str.contains("Brutus") | series.str.contains("Julius"))
        global f
        if not f.any():
            f=series.str.contains("Octavius")
        if g.any() and f.any():
            print "Found in",d
            return -1


if __name__ == '__main__':
    print "Looking for first query\n"
    s=0
    print "Searching for 'Antony' and 'Octavius' and not 'Cleopatra'"
    for values in lst:#passing each dataframe one by one
        if s!=-1:
            s=lin_search1(values)#if value returned is -1 it breaks
        else:
            break
    print "Looking for second query\n"
    s=0
    print "Searching for 'Brutus' or 'Julius' and 'Octavius'"
    for values in lst:
        if s!=-1:
            s=lin_search2(values)
        else:
            break

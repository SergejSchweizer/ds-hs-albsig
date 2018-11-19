#3.4

dfst = pd.read_csv("st.csv")
dfavg = pd.read_csv("avg.csv")
dfhzb = pd.read_csv("hzb.csv")
dfmw =  pd.read_csv("mw.csv")
dfsum =dfavg.merge(dfst, on="mtknr")
dfsum =dfsum.merge(dfhzb, on = "mtknr")

dfsum.index = dfsum.iloc[:,0]
dfsum.index.name = "ID"
dfsum = dfsum.iloc[:,[1,2,3,4,5,6,8,10]]
studis = dfsum
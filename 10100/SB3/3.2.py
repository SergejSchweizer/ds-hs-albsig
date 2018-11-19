
#a
dfst = pd.read_csv("st.csv")
dfst.index = dfst.iloc[:,0]
dfst.index.name = "ID"

#b
dfst=dfst.iloc[:,1:]

#c
dfst.sort_index(inplace=True)
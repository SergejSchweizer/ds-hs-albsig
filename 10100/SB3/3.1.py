import pandas as pd

kanzler=pd.DataFrame({"Jahre":[5,8,6,7,13],"Name":["Brandt","Schmidt","Kohl","Schroder","Merkel"],"Partei":["SPD","SPD","CDU","SPD","CDU"],"Start":[1969,1974,1982,1998,2005]})

kanzler.index = ["Eins","Zwei","Drei","Vier","Fünf"]
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import statistics as st
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/Florian/Desktop/2652017.csv",na_values=-9999)
nom = df["NAME"].iloc[0]
moyenne = (df["TMAX"]+df["TMIN"])/2
df["TAVG"] = df["TAVG"].fillna(moyenne)
df = df[["DATE","TAVG","TMAX","TMIN"]]
df["DATE"] = pd.to_datetime(df["DATE"],format="%Y-%m-%d")

def saison(x,a,b,c):
    return x[x["DATE"].dt.month.isin([a,b,c])]

def filtre(x):
    x["DATE"] = x["DATE"].astype(str)
    x["DATE"] = x["DATE"].str.slice(start=0,stop=4)
    x = x.groupby("DATE")
    x = x["TAVG"].mean()
    x = x.reset_index()
    x["DATE"] = x["DATE"].astype(int)
    x = x.loc[(x["DATE"]>=1970)&(x["DATE"]<=2000)]
    return x

def liste(l):
    return [i for i in l]

def y(x):
    results = [ '%.1f' % elem for elem in x ]
    return list(map(float, results))

def arr(x):
    results = [ '%.3f' % elem for elem in x ]
    return list(map(float, results))

x = liste(filtre(saison(df,12,1,2))["DATE"])

def moyenne(x):
    me = st.mean(x)
    return np.repeat(me, len(x)).tolist()

fig = make_subplots(rows=2, cols=2)

def figure(d,a,b,t,z,nom,co):
    fig.add_trace(go.Bar(x=x, y=z,name=nom,marker_color=co),a,b)
    one_more_trace=dict(type='scatter',x=x,y=d,mode='lines',line=dict(color='red'),name="Moyenne",showlegend=t,legendgroup="group2",legendgrouptitle_text="Statistique sur l'intervalle",)
    fig.append_trace(one_more_trace, a, b)
    fig.update_layout(showlegend=t)
    reg = LinearRegression().fit(np.vstack(x), z)
    Z = reg.predict(np.vstack(x))
    reg = dict(type="scatter",name='Ligne de régression', x=x, y=arr(Z), mode='lines',showlegend=t,line=dict(color='#202020'),legendgroup="group1")
    fig.append_trace(reg,a,b)
  
figure(y(moyenne(liste(filtre(saison(df,12,1,2))["TAVG"]))),1,1,False,y(liste(filtre(saison(df,12,1,2))["TAVG"])),"Hiver","#5b63fe")
figure(y(moyenne(liste(filtre(saison(df,6,7,8))["TAVG"]))),1,2,False,y(liste(filtre(saison(df,6,7,8))["TAVG"])),"Eté","#FFF700")
figure(y(moyenne(liste(filtre(saison(df,9,10,11))["TAVG"]))),2,1,False,y(liste(filtre(saison(df,9,10,11))["TAVG"])),"Automne","#FFC500")
figure(y(moyenne(liste(filtre(saison(df,3,4,5))["TAVG"]))),2,2,True,y(liste(filtre(saison(df,3,4,5))["TAVG"])),"Printemps","#4AA02C")

fig.update_layout(title_text=f'Températures moyennes par années et par saisonsStation : {nom}',
    autosize=False,
    width=1100,
    height=800,legend_title_text='Saison :') 
fig.write_html(f"C:/Users/Florian/Desktop/AASITE/public_html/{nom}.html")
fig.write_image(f"C:/Users/Florian/Desktop/AASITE/public_html/imagr/{nom}.png")
fig.show()

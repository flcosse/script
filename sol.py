import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go

ville = "Pau"
outpt = "C:/Users/Florian/Desktop/sortie.gpkg"
processing.run("quickosm:downloadosmdatainareaquery", 
{'KEY':'landuse',
'VALUE':"",
'AREA':ville,
'TIMEOUT':120,
'SERVER':'https://lz4.overpass-api.de/api/interpreter',
'FILE':outpt})
iface.addVectorLayer("C:/Users/Florian/Desktop/sortie.gpkg|layername=sortie_multipolygons","","ogr")

landuse1 = QgsProject.instance().mapLayersByName('sortie sortie_multipolygons')[0]
inpt = QgsVectorLayer('C:/Users/Florian/Desktop/sortie.gpkg|layername=sortie_multipolygons',"","ogr")

processing.run("native:reprojectlayer", 
{'INPUT':inpt,
'TARGET_CRS':QgsCoordinateReferenceSystem('EPSG:2154'),
'OPERATION':'+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=lcc +lat_0=46.5 +lon_0=3 +lat_1=49 +lat_2=44 +x_0=700000 +y_0=6600000 +ellps=GRS80',
'OUTPUT':'C:/Users/Florian/Desktop/poly.shp'})
iface.addVectorLayer("C:/Users/Florian/Desktop/poly.shp","","ogr")
landuse1 = QgsProject.instance().mapLayersByName('poly')[0]

column = QgsField("aire",QVariant.Double)
landuse1.dataProvider().addAttributes([column])
landuse1.updateFields()
exp1 = QgsExpression("$area")
QgsProject.instance().addMapLayer(landuse1)
dehors ="C:/Users/Florian/Desktop/zebi.gpkg"
processing.run("native:refactorfields",
{'INPUT':'C:/Users/Florian/Desktop/poly.shp','FIELDS_MAPPING':[{'expression': '\"fid\"','length': 0,'name': 'fid','precision': 0,'type': 4},{'expression': '\"full_id\"','length': 0,'name': 'full_id','precision': 0,'type': 10},{'expression': '\"osm_id\"','length': 0,'name': 'osm_id','precision': 0,'type': 10},{'expression': '\"osm_type\"','length': 0,'name': 'osm_type','precision': 0,'type': 10},{'expression': '\"check_date\"','length': 0,'name': 'check_date','precision': 0,'type': 10},{'expression': '\"end_date\"','length': 0,'name': 'end_date','precision': 0,'type': 10},{'expression': '\"substance\"','length': 0,'name': 'substance','precision': 0,'type': 10},{'expression': '\"pipeline\"','length': 0,'name': 'pipeline','precision': 0,'type': 10},{'expression': '\"industrial\"','length': 0,'name': 'industrial','precision': 0,'type': 10},{'expression': '\"capacity:disabled\"','length': 0,'name': 'capacity:disabled','precision': 0,'type': 10},{'expression': '\"aire\"','length': 0,'name': 'aire','precision': 0,'type': 6},{'expression': '\"depot\"','length': 0,'name': 'depot','precision': 0,'type': 10},{'expression': '\"user\"','length': 0,'name': 'user','precision': 0,'type': 10},{'expression': '\"parking\"','length': 0,'name': 'parking','precision': 0,'type': 10},{'expression': '\"park_ride\"','length': 0,'name': 'park_ride','precision': 0,'type': 10},{'expression': '\"operator:type\"','length': 0,'name': 'operator:type','precision': 0,'type': 10},{'expression': '\"fee\"','length': 0,'name': 'fee','precision': 0,'type': 10},{'expression': '\"capacity\"','length': 0,'name': 'capacity','precision': 0,'type': 10},{'expression': '\"amenity\"','length': 0,'name': 'amenity','precision': 0,'type': 10},{'expression': '\"leisure\"','length': 0,'name': 'leisure','precision': 0,'type': 10},{'expression': '\"access\"','length': 0,'name': 'access','precision': 0,'type': 10},{'expression': '\"description\"','length': 0,'name': 'description','precision': 0,'type': 10},{'expression': '\"substation\"','length': 0,'name': 'substation','precision': 0,'type': 10},{'expression': '\"power\"','length': 0,'name': 'power','precision': 0,'type': 10},{'expression': '\"start_date\"','length': 0,'name': 'start_date','precision': 0,'type': 10},{'expression': '\"addr:street\"','length': 0,'name': 'addr:street','precision': 0,'type': 10},{'expression': '\"addr:postcode\"','length': 0,'name': 'addr:postcode','precision': 0,'type': 10},{'expression': '\"addr:housenumber\"','length': 0,'name': 'addr:housenumber','precision': 0,'type': 10},{'expression': '\"addr:city\"','length': 0,'name': 'addr:city','precision': 0,'type': 10},{'expression': '\"natural\"','length': 0,'name': 'natural','precision': 0,'type': 10},{'expression': '\"sport\"','length': 0,'name': 'sport','precision': 0,'type': 10},{'expression': '\"intermittent\"','length': 0,'name': 'intermittent','precision': 0,'type': 10},{'expression': '\"wall\"','length': 0,'name': 'wall','precision': 0,'type': 10},{'expression': '\"building\"','length': 0,'name': 'building','precision': 0,'type': 10},{'expression': '\"leaf_type\"','length': 0,'name': 'leaf_type','precision': 0,'type': 10},{'expression': '\"CLC:year\"','length': 0,'name': 'CLC:year','precision': 0,'type': 10},{'expression': '\"CLC:id\"','length': 0,'name': 'CLC:id','precision': 0,'type': 10},{'expression': '\"CLC:code\"','length': 0,'name': 'CLC:code','precision': 0,'type': 10},{'expression': '\"wikipedia\"','length': 0,'name': 'wikipedia','precision': 0,'type': 10},{'expression': '\"research\"','length': 0,'name': 'research','precision': 0,'type': 10},{'expression': '\"operator\"','length': 0,'name': 'operator','precision': 0,'type': 10},{'expression': '\"alt_name\"','length': 0,'name': 'alt_name','precision': 0,'type': 10},{'expression': '\"religion\"','length': 0,'name': 'religion','precision': 0,'type': 10},{'expression': '\"denomination\"','length': 0,'name': 'denomination','precision': 0,'type': 10},{'expression': '\"barrier\"','length': 0,'name': 'barrier','precision': 0,'type': 10},{'expression': '\"residential\"','length': 0,'name': 'residential','precision': 0,'type': 10},{'expression': '\"opening_hours\"','length': 0,'name': 'opening_hours','precision': 0,'type': 10},{'expression': '\"website\"','length': 0,'name': 'website','precision': 0,'type': 10},{'expression': '\"name\"','length': 0,'name': 'name','precision': 0,'type': 10},{'expression': '\"type\"','length': 0,'name': 'type','precision': 0,'type': 10},{'expression': '\"landuse\"','length': 0,'name': 'landuse','precision': 0,'type': 10}],'OUTPUT':dehors})
iface.addVectorLayer(dehors,"","ogr")
landuse = QgsProject.instance().mapLayersByName('zebi')[0]
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(landuse))

output2 = "C:/Users/Florian/Desktop/découpé.shp"
processing.run("native:clip", 
{'INPUT':'C:/Users/Florian/Desktop/poly.shp',
'OVERLAY':'C:/Users/Florian/Desktop/département/COMMUNE.shp|subset=\"NOM_COM\" = \'{}''\''.format(ville),
'OUTPUT':output2})
iface.addVectorLayer(output2,"","ogr")
landuse = QgsProject.instance().mapLayersByName('découpé')[0]

type = []
aire = []

with edit(landuse):
    for f in landuse.getFeatures():
        context.setFeature(f)
        f['aire'] = exp1.evaluate(context)
        landuse.updateFeature(f)

for f in landuse.getFeatures():
    aire.append(f["aire"])
    type.append(f["landuse"])
    
for f in aire:
    f = float(f)
aire[:] = [x / 1000000 for x in aire]
df = pd.DataFrame(type)
df = df.rename(columns={0: "Landuse"})
df["surface"] = aire

df = df.groupby(["Landuse"]).sum()
df = df.sort_values(["surface"], ascending=False)
other = df["surface"].iloc[4:].sum()
df = df.reset_index()
df["Landuse"] = df["Landuse"].replace(
    [
        "farmland",
        "military",
        "forest",
        "meadow",
        "residential",
        "farmyard",
        "grass",
        "industrial",
        "retail",
        "cemetery",
        "vineyard",
        "basin",
        "commercial",
        "village_green",
        "univeristy",
        "construction",
        "tourism",
        "healthcare",
        "quarry",
        "railway",
        "recreation_ground",
        "garages",
        "landfill",
        "brownfield",
        "port",
    ],
    [
        "Terres agricoles",
        "Militaire",
        "Terres boisées",
        "Pré/prairie",
        "Zones résidentielles",
        "Ferme",
        "Pelouse",
        "Industriel",
        "Marché",
        "Cimetière",
        "Vignoble",
        "Bassin",
        "Commercial",
        "Village vert",
        "Université",
        "Construction",
        "Tourisme",
        "Hôpitaux",
        "Carrière de surface",
        "Chemin de fer",
        "Terrains de loisirs",
        "Garages",
        "Décharge",
        "Friches industrielles",
        "Port",
    ],
)

line = {"Landuse": "Autre", "surface": other}
df = df.append(line, ignore_index=True)
df = df.iloc[[0, 1, 2, 3, -1]]
domaine = df["Landuse"].tolist()
surface = df["surface"].tolist()
aire = [round(num) for num in surface]

couleur = []
color = {
    "Terres agricoles": "gold",
    "Militaire": "peru",
    "Industriel": "red",
    "Pré/prairie": "gold",
    "Terres boisées": "sienna",
    "Autre": "lightgrey",
    "Zones résidentielles": "orangered",
    "Marché": "brown",
    "Vignoble": "blueviolet",
    "Construction": "orange",
    "Commercial": "yellow",
    "Pelouse": "lawngreen",
    "Tourisme": "chocolate",
    "Carrière de surface": "darkgrey",
    "Chemin de fer": "grey",
    "Terrains de loisirs": "pink",
    "Garages": "saddlebrown",
    "Décharge": "goldenrod",
    "Friches industrielles": "sienna",
    "port": "royalblue",
}

df["surface"] = df["surface"].round(decimals=1)
df = df.sort_values(by=["Landuse"], ascending=True)
liste = df["Landuse"].tolist()
set = []

liste = sorted(liste, reverse=False)
color = {key: value for key, value in sorted(color.items())}
for i, j in color.items():
    for k in liste:
        if i == k:
            set.append(j)

fig = go.Figure(
    data=[go.Pie(labels=df["Landuse"], values=df["surface"], marker_colors=set)]
)

fig.update_layout(
    title=f"Répartition de l'occupation du sol dans la ville de {ville}",
    font=dict(
        family="Arial",
        size=18,
    ),
)

fig.update_layout(font_family="Arial")
fig.write_html("C:/Users/Florian/Desktop/AASITE/mediumish-html/file.html")
fig.show()

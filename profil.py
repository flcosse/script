import plotly.graph_objects as go
import numpy as np
import uuid

iface.addVectorLayer("C:\packages\COMMUNE EUROPE/COMM_RG_01M_2016_4326.shp","Communes","ogr")
raster= "C:\packages/raster pyre.tif"
iface.addRasterLayer(raster,'SRTM','gdal')
unique_filename3 = str(uuid.uuid4())
unique_filename4 = str(uuid.uuid4())
unique_filename5 = str(uuid.uuid4())
unique_filename6 = str(uuid.uuid4())
unique_filename7 = str(uuid.uuid4())
unique_filename8 = str(uuid.uuid4())
unique_filename9 = str(uuid.uuid4())
vl1 = QgsVectorLayer("Point","Point1","memory")
pr = vl1.dataProvider()
f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(0.03618,42.92890)))
pr.addFeature(f)
vl1.updateExtents()
QgsProject.instance().addMapLayer(vl1)
unique_filename1 = str(uuid.uuid4())
path = (f"C:/packages/TOPO/{unique_filename1}.shp")
writer = QgsVectorFileWriter.writeAsVectorFormat(vl1,path,'utf-8',driverName='ESRI Shapefile')
QgsProject.instance().removeMapLayer(vl1)
vl1 = iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename1}.shp","","ogr")
feat = next(iface.activeLayer().getFeatures())
vl1 = QgsGeometry.asPoint(feat.geometry())
pxy1 = QgsPoint(vl1)

vl2 = QgsVectorLayer("Point","Point2","memory")
pr = vl2.dataProvider()
f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(0.10652,42.82869)))
pr.addFeature(f)
vl2.updateExtents()
QgsProject.instance().addMapLayer(vl2)
unique_filename2 = str(uuid.uuid4())
path = (f"C:/packages/TOPO/{unique_filename2}.shp")
writer = QgsVectorFileWriter.writeAsVectorFormat(vl2,path,'utf-8',driverName='ESRI Shapefile')
QgsProject.instance().removeMapLayer(vl2)
vl2 = iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename2}.shp","","ogr")
feat = next(iface.activeLayer().getFeatures())
vl2 = QgsGeometry.asPoint(feat.geometry())
pxy2 = QgsPoint(vl2)


start_point = pxy1
end_point = pxy2
v_layer = QgsVectorLayer('LineString?crs=epsg:4326', 'line', 'memory')
path = (f"C:/packages/TOPO/{unique_filename5}.shp")
pr = v_layer.dataProvider()
seg = QgsFeature()
seg.setGeometry(QgsGeometry.fromPolyline([start_point, end_point]))
pr.addFeatures([ seg ])
QgsProject.instance().addMapLayers([v_layer])
iface.zoomToActiveLayer()
writer = QgsVectorFileWriter.writeAsVectorFormat(v_layer,path,'utf-8',driverName='ESRI Shapefile')
QgsProject.instance().removeMapLayer(v_layer)
line = iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename5}.shp","","ogr")


fnout = (f"C:/packages/TOPO/{unique_filename3}.shp")
fnpts = (f"C:/packages/TOPO/{unique_filename1}.shp")
fnws = "C:\packages\COMMUNE EUROPE/COMM_RG_01M_2016_4326.shp"

processing.run("native:joinattributesbylocation",
{'INPUT':fnpts,
'JOIN':fnws,
'PREDICATE':[0],
'JOIN_FIELDS':[],
'METHOD':0,
'DISCARD_NONMATCHING':False,
'PREFIX':'',
'OUTPUT':fnout})
v1 = iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename3}.shp","","ogr")


fnout = (f"C:/packages/TOPO/{unique_filename4}.shp")
fnpts = (f"C:/packages/TOPO/{unique_filename2}.shp")
fnws = "C:\packages\COMMUNE EUROPE/COMM_RG_01M_2016_4326.shp"

processing.run("native:joinattributesbylocation",
{'INPUT':fnpts,
'JOIN':fnws,
'PREDICATE':[0],
'JOIN_FIELDS':[],
'METHOD':0,
'DISCARD_NONMATCHING':False,
'PREFIX':'',
'OUTPUT':fnout})
v1 = iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename4}.shp","","ogr")

project = QgsProject.instance()

delete1 = project.mapLayersByName(unique_filename1)[-1]
project.removeMapLayer(delete1.id())

project = QgsProject.instance()

delete1 = project.mapLayersByName(unique_filename2)[-1]
project.removeMapLayer(delete1.id())
layer1 = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename3}.shp","","ogr")
layer2 = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename4}.shp","","ogr")
project = QgsProject.instance()

for nom1 in layer1.getFeatures():
    print(nom1)
rename = project.mapLayersByName(unique_filename3)[0]
rename.setName(nom1["NAME_ASCI"])
for nom2 in layer2.getFeatures():
    print(nom2)
rename = project.mapLayersByName(unique_filename4)[0]
rename.setName(nom2["NAME_ASCI"])
rename = project.mapLayersByName(unique_filename5)[0]
rename.setName("Ligne topographique")
delete2 = project.mapLayersByName("Ligne topographique")[0]
project.removeMapLayer(delete2.id())
line = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename5}.shp","","ogr")
centroides = ("C:/packages/TOPO/centre.shp","","ogr")
d = QgsDistanceArea()
d.setEllipsoid('WGS84')
for feat in line.getFeatures():
    dist_point = (d.convertAreaMeasurement(d.measureLength(feat.geometry()),100))
    dist_point1 = (d.convertAreaMeasurement(d.measureLength(feat.geometry()),100))
print(dist_point)
if dist_point < 500:
    dist_point = 0.00001
elif dist_point < 1000:
    dist_point = 0.00005
elif dist_point < 5000:
    dist_point = 0.00006
elif dist_point < 10000:
    dist_point = 0.00008
elif dist_point < 25000:
    dist_point = 0.0005
elif dist_point < 50000:
    dist_point = 0.00008
else:
    dist_point = 0.00007
processing.run("native:pointsalonglines", 
{'INPUT':line,
'DISTANCE':dist_point,
'START_OFFSET':0,
'END_OFFSET':0,
'OUTPUT':f"C:/packages/TOPO/{unique_filename6}.shp"})
iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename6}.shp",'','ogr')
points_lignes = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename6}.shp")
delete = project.mapLayersByName(unique_filename6)[0]
project.removeMapLayer(delete.id())

processing.run("native:rastersampling", 
{'INPUT':points_lignes,
'RASTERCOPY':raster,
'COLUMN_PREFIX':'SAMPLE_',
'OUTPUT':f"C:/packages/TOPO/{unique_filename7}.shp"})
iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename7}.shp",'','ogr')
points_raster = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename7}.shp",'','ogr')

rename = project.mapLayersByName(unique_filename7)[-1]
rename.setName("Points avec valeurs raster")
y = []
x = []
for f in points_raster.getFeatures():
    y.append(f["SAMPLE_1"])

processing.run("qgis:exportaddgeometrycolumns", 
{'INPUT':line,
'CALC_METHOD':1,
'OUTPUT':f"C:/packages/TOPO/{unique_filename8}.shp"})
iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename8}.shp","","ogr")
line = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename8}.shp","","ogr")
rename = project.mapLayersByName(unique_filename8)[0]
rename.setName("Ligne topographique")

processing.run("qgis:distancematrix",
{'INPUT':f"C:/packages/TOPO/{unique_filename7}.shp",
'INPUT_FIELD':'distance',
'TARGET':f"C:/packages/TOPO/{unique_filename4}.shp",
'TARGET_FIELD':'FID',
'MATRIX_TYPE':0,
'NEAREST_POINTS':0,
'OUTPUT':f"C:/packages/TOPO/{unique_filename9}.shp"})
point_dist = QgsVectorLayer(f"C:/packages/TOPO/{unique_filename9}.shp","","ogr")

iface.addVectorLayer(f"C:/packages/TOPO/{unique_filename9}.shp","","ogr")
for f in point_dist.getFeatures():
    x.append(f["Distance"])

x.append(0)
x.sort()
y1 = y
y.insert(0,y[0])
x = np.array(x)
y = np.array(y)
if dist_point1 > 5000:
    x[:] = [f / 1000 for f in x]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    name="Profil topographique",marker=dict(
            color='saddlebrown')
))
fig.update_layout(hovermode="x"
    title=f"Profil topographique de {(nom1['NAME_ASCI'])} - {(nom2['NAME_ASCI'])}",
    xaxis_title="Distance (en km)",
    yaxis_title="Altitude (en m)",
)

fig.write_html('C:/Users/33788/Desktop/html/filename.html')

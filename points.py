uri = r"C:\Users\Florian\Pictures\TERRITOIRE\fin.shp|layername=fin"
layer = QgsVectorLayer(uri,"points","ogr")
point = QgsVectorLayer(r"C:\Users\Florian\Pictures\TERRITOIRE\PONTAVQ.shp|layername=PONTAVQ","","ogr")

for f in point.getFeatures():
    geom1 = f.geometry()
    X = geom1.asPoint().x()
    Y = geom1.asPoint().y()
    
scr = iface.mapCanvas().mapSettings().destinationCrs().authid()
a = scr.split(":")
X1 = []
Y1 = []

for i in layer.getFeatures():
    geom = i.geometry()
    X1.append(geom.asPoint().x())
    Y1.append(geom.asPoint().y())

for i,j in zip(X1,Y1):
    start_point = QgsPoint(X,Y)
    end_point = QgsPoint(i, j)
    v_layer = QgsVectorLayer('LineString?crs='+scr.lower(), 'line', 'memory')
    pr = v_layer.dataProvider()
    seg = QgsFeature()
    seg.setGeometry(QgsGeometry.fromPolyline([start_point, end_point]))
    pr.addFeatures([ seg ])
    QgsProject.instance().addMapLayers([v_layer])

listLayers = QgsProject.instance().mapLayersByName('line')
output = "C:/Users/Florian/Desktop/Lignes.shp"
processing.runAndLoadResults("native:mergevectorlayers", 
                             {'LAYERS':listLayers,
                             'CRS':a[1],
                             'OUTPUT':output})
                             
layers = QgsProject.instance().mapLayers()

for i in layers.values():
    QgsProject.instance().removeMapLayers([i.id()])

iface.addVectorLayer(output,"","ogr")
iface.addVectorLayer(uri,"","ogr")

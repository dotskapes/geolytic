try:
    from osgeo import ogr
except ImportError:
    import ogr

import sys, os

def difference(f1,f2):
    outputFileName = 'difference_' + f1
    
    driver = ogr.GetDriverByName("GeoJSON")

    f1 = driver.Open(f1,0)
    layer1 = f1.GetLayer()
    feature1 = layer1.GetNextFeature()

    if f1 is None:
        print "Could not open file ", f1
        sys.exit(1)

    f2 = driver.Open(f2,0)
    layer2 = f2.GetLayer()
   
    if f2 is None:
        print "Could not open file ", f2

    ### Create output file ###
    if os.path.exists(outputFileName):
        os.remove(outputFileName)
    try:
        output = driver.CreateDataSource(outputFileName)
    except:
        print 'Could not create output datasource ', outputFileName
        sys.exit(1)

    newLayer = output.CreateLayer('Difference',geom_type=ogr.wkbPolygon,srs=layer1.GetSpatialRef())

    if newLayer is None:
        print "Could not create output layer"
        sys.exit(1)

    newLayerDef = newLayer.GetLayerDefn()
    ##############################

    featureID = 0

    while feature1:

        layer2.ResetReading()
        geom1 = feature1.GetGeometryRef().Clone()
        newgeom = geom1.Clone()
        feature2 = layer2.GetNextFeature()

        while feature2:

            geom2 = feature2.GetGeometryRef().Clone()
            if geom1.Intersect(geom2):
                newgeom = newgeom.Difference(geom2)
            feature2.Destroy()
            feature2 = layer2.GetNextFeature()
        
        if not newgeom.IsEmpty():
            newFeature = ogr.Feature(newLayerDef)
            newFeature.SetGeometry(newgeom)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
            featureID += 1
            newFeature.Destroy()
            
        feature1.Destroy()
        feature1 = layer1.GetNextFeature()
        
    f1.Destroy()
    f2.Destroy()

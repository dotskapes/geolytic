### This function checks two features in a file to see if one crosses another.
### It takes 4 arguments, f1 for the first file, fid1 for the index of the
### first file's feature, f2 for the second file, fid2 for the index of the
### second file's feature. Returns whether crosses is True or False.

try:
    from osgeo import ogr
except ImportError:
    import ogr

import os, sys

def crosses(f1,fid1,f2,fid2):
    driver = ogr.GetDriverByName("GeoJSON")
    
    file1 = driver.Open(f1,0)
    layer1 = file1.GetLayer()
    feat1 = layer1.GetFeature(fid1)
    geom1 = feat1.GetGeometryRef()

    file2 = driver.Open(f2,0)
    layer2 = file2.GetLayer()
    feat2 = layer2.GetFeature(fid2)
    geom2 = feat2.GetGeometryRef()

    if geom1.Crosses(geom2) == 1:
        print f1 + "'S FEATURE", fid1, "CROSSES", f2 + "'S FEATURE", fid2
    else:
        print f1 + "'S FEATURE", fid1, "DOES NOT CROSS",f2 + "'S FEATURE", fid2

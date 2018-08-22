""" Dissolves polygon layer and prints attributes of the new layer. Use COVER63p.shp and field COVER."""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import os


def run_script(iface, **args):
    input_path = args['input_path']
    output_path = args['output_path']
    field = args['field']

    processing.runalg('qgis:dissolve', input_path, False, field, output_path)

    layerName = os.path.splitext(os.path.basename(output_path))[0]
    layer = QgsVectorLayer(output_path, layerName, 'ogr')
    features = processing.getfeatures(layer)
    print "Number of categories: " + str(len(features))
    for feature in features:
        print feature.attributes()




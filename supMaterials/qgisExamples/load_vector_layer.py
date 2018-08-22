""" Loads a vector layer and displays it in QGIS window.
Needs the path to the vector file."""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os


def run_script(iface, **args):
    path = args['path']
    layerName = os.path.splitext(os.path.basename(path))[0]
    mapreg = QgsMapLayerRegistry.instance()
    mapreg.removeAllMapLayers()
    layer = QgsVectorLayer(path, layerName, 'ogr')
    mapreg.instance().addMapLayer(layer)


""" Loads a vector layer and changes color.
Needs the path to the vector file."""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import os


def load_vector(path):
    layerName = os.path.splitext(os.path.basename(path))[0]
    mapreg = QgsMapLayerRegistry.instance()
    mapreg.removeAllMapLayers()
    layer = QgsVectorLayer(path, layerName, 'ogr')
    mapreg.instance().addMapLayer(layer)
    return layer

def set_symbology(renderer, color, alpha):
    symb = renderer.symbol()
    symb.setColor(QColor(Qt.red))
    symb.setAlpha(0.3)

def run_script(iface, **args):
    path = args['path']
    layer = load_vector(path)

    renderer = layer.rendererV2()
    set_symbology(renderer, QColor(Qt.red), 0.3)

    layer.clearCacheImage()
    layer.triggerRepaint()
    iface.legendInterface().refreshLayerSymbology(layer)


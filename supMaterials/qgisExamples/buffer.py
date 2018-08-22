"""Creates buffer around polygons and uses this buffer to clip another polygon layer. """
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import os


def run_script(iface, **args):
    path = args['path']
    fire_damage = "special_regions.shp"
    fire_buffer = fire_damage[:-4] + "_buffer.shp"
    buffer_dist = 5000
    processing.runalg('qgis:fixeddistancebuffer', os.path.join(path, fire_damage), buffer_dist, 1, True, os.path.join(path, fire_buffer))
    
    park = "COVER63p.shp" 
    clip_output = park[:-4] + "_damage_buffer.shp"
    processing.runalg('qgis:clip', os.path.join(path, park), os.path.join(path, fire_buffer), os.path.join(path, clip_output))



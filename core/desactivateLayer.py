# -*- coding: utf-8 -*-
from builtins import str
import os.path
import sys
from qgis.PyQt.QtWidgets import QInputDialog
from qgis.core import QgsGeometry
from qgis.gui import QgsMapTool, QgsMapToolEmitPoint


class DesactivateLayerMapTool(QgsMapTool):
    def __init__(self, canvas, legendInterface, dlg, iface, layerRegistry):
        self.canvas = canvas
        self.iface = iface
        self.legendInterface = legendInterface
        self.layerRegistry = layerRegistry
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.reset()
        self.dlg = dlg

    def reset(self):
        self.startPoint = self.endPoint = None
        self.isEmittingPoint = False

    def canvasPressEvent(self, e):

        self.startPoint = self.toMapCoordinates(e.pos())
        pntGeom = QgsGeometry.fromPoint(self.startPoint)
        pntBuff = pntGeom.buffer((self.canvas.mapUnitsPerPixel() * 10), 0)
        rect = pntBuff.boundingBox()
        layers = self.legendInterface.layers()
        activeLayerHere = []
        for layer in layers:
            l_visible = self.legendInterface.isLayerVisible(layer)
            if l_visible and layer.type() == 0 and layer.hasGeometryType():
                i = 0
                for feature in layer.getFeatures():
                    f_inter = feature.geometry().intersects(rect)
                    if not layer.name() in activeLayerHere and f_inter:
                        activeLayerHere.append(layer.name())

        if len(activeLayerHere) == 0:
            return

        w = QInputDialog(self.dlg)
        w.cancelButtonText = "Annuler"
        w.setOkButtonText("Désactiver")
        item, ok = w.getItem(self.dlg,
                             str("Désactiver une couche", "utf-8"),
                             str("Choisir une couche", "utf-8"),
                             activeLayerHere,
                             current=0,
                             editable=False)

        layerToRemove = self.layerRegistry.mapLayersByName(item)[0]
        if ok:
            self.legendInterface.setLayerVisible(layerToRemove, False)

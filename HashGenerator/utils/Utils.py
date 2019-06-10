#!/usr/bin/python
# -*- coding: utf-8 -*-


class Utils(object):
    windowWidth = 1920
    windowHeight = 1080
    itemHeight = 30

    @staticmethod
    def setWindowWidth(width):
        Utils.windowWidth = width

    @staticmethod
    def setWindowHeight(height):
        Utils.windowHeight = height
        Utils.itemHeight = int(Utils.windowHeight / 36.0)

    @staticmethod
    def getWindowWidth():
        return Utils.windowWidth

    @staticmethod
    def getWindowHeight():
        return Utils.windowHeight

    @staticmethod
    def getItemHeight():
        return Utils.itemHeight


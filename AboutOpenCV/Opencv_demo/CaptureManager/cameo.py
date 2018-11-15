#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:30:16 2018

@author: gehaha
"""

import cv2
from managers import WindowManager ,CaptureManager

class Cameo(object):
    
    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
        
    def run(self):
        """run the main loop"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            #TODO:Filter the frame (Chapter 3).
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
            
    def onKeypress(self,keycode):
        """Handle a keypress .
        space -> Take a screenshot
        tab ->Start/stop recording a screencast
        escape -> Quit.
        """
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screescast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()
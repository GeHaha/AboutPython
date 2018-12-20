# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:50:58 2018

@author: Gehaha
"""

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys, random

class Tetris(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """ initiates application UI"""
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()
        self.resize(180,380)
        self.center()
        self.setWindowTitle('俄罗斯方块')
        self.show()
        
    def center(self):
        '''center the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        
class Board(QFrame):
    msg2Statusbar = pySignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.initBoard()
        
    def initBoard(self):
        '''initiates board'''
        self.timer = QBasicTimer()
        self.inWaitingAfterLine = False
        self.curX = 0
        self.curY = 0 
        self.numLinesRemoved = 0
        self.board = []
        
        self.setFocusPolicy(Qt.StronFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        
    def shapAt(self,x,y):
        '''determines shape at the board position'''
        
        return self.board[(y * Board.BoardWidth) + x]
    
    def setShapeAt(self,x,y,shape):
        '''sets a shape at the board'''
        self.board[(y* Board.BoardWidth) + x]  = shape
        
    def squareWidth(self):
        '''return the width of one square'''
        return self.contentRect().width() //Board.BoardWidth
    
    def squaresHeight(self):
        '''returns the height of one square'''
        return self.contentsRect().height() //Board.BoardHeight 

    def start(self):
        '''start games'''
        if self.isPaused:
            return
        
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        
        self.newPiece()
        self.timer.start(Board.Speed,self)
        
    def pause(self):
        '''pauses game'''
        if not self.isStarted:
            return
        
        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
            
        else:
            self.timer.start(Board.Speed,self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
            
        self.update()
        
    def paintEvent(self,event):
        '''paints all shapes of the game'''
        painter = QPainter(self)
        rect = self.contentsRect()
        
        boardTop = rect.bottom()- Board.BoardHeight * self.squaresHeight()
        
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapAt(j,Board.BoardHeight - i-1)
                if shape !=  Tetrominoe.NoShape:
                    self.drawSquare(painter,rec.left() + j*self.squareWidth(),boardTop + i*self.squaresHeight(),shape)
                if self.curPiece.shape() != Tetrominoe.NoShape:
                    
                    for i in range(4):
                        x = self.curX + self.curPiece.x(i)
                        y = self.curY - self.curPiece.y(i)
                        self.drawSquare(painter,rec.left() + x * self.squareWidth(),
                                        boardTop + (Board.BoardHeight-y-1)*self.squaresHeight,
                                        self.curPiece.shape())
        
        def keyPressEvent(self,event):
            '''processes key press event'''
            if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
                super(Board,self).keyPressEvent(event)
                return
            
            key = event.key()
            
            
            if key == Qt.Key_P:
                self.pause()
                return
            
            if self.isPaused:
                return
            
            elif key == Qt.Key_Left:
                self.tryMove(self.curPiece,self.curX -1 ,self.curY)
                
            elif key == Qt.Key_Right:
                self.tryMove(self.curPiece,self.curX + 1,self.curY)
            
            elif key == Qt.Key_Down:
                self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
            elif key == Qt.Key_Up:
                self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
            elif key == Qt.Key_Space:
                self.dropDown()
                
            elif key == Qt.Key_D:
                self.oneLineDown()
                
            else:
                super(Board,self).keyPressEvent(event)
                
                
        def timerEvent(self,event):
            '''handles timer event'''
            if event.timerId() == self.timer.timerId():
                if self.isWaitingAfterLine:
                    self.isWaitingAfterLine = False
                    self.newPiece()
                    
                else:
                    self.oneLineDown()
                    
            else:
                super(Board,self).timerEvent(event)
                
                
                
        def clearBoard(self):
            '''clears shapes from the board'''
            for i in range(Board.BoardHeight * Board.BoardWidth):
                self.board.append(Tetrominoe.NoShape)
                
        def dropDown(self):
            '''drops down a shape'''
            newY = self.curY
            while newY > 0:
                if not self.tryMove(self.curPiece,self.curX,newY -1):
                    break
                newY -= 1
                
            self.pieceDropped()
            
        def oneLineDown(self):
            '''goes one line dowb with a shape'''
            if not self.tryMove(self.curPiece,self.curX,self.curY-1):
                self.pieceDropped()
                
        def pieceDropped(self):
            '''after dropping shape,remove fu;; lines and create new shape'''
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.setShapeAt(x,y,self.curPiece.shape())
                
            self.removeFullLines()
            if not self.isWaitingAfterLine:
                self.newPiece()
                
                
        def  removeFullLines(self):
            pass
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
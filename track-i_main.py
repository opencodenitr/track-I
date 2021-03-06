# -- coding: utf-8 --

# Form implementation generated from reading ui file 'track-i.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database_reader import*
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import time
import argparse
import numpy as np
import imutils
import cv2
import dlib
import os
import time
from datetime import datetime
from PIL import Image

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QIcon
import sys,os
from pathlib import Path
from PyQt5.QtWidgets import QMessageBox
from report import *
from database_reader import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.f=0
        self.g=1
        self.avg=0
        self.count=[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 624)
        MainWindow.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, -30, 871, 641))
        self.tabWidget.setStyleSheet("background-color:rgb(171, 53, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.start = QtWidgets.QPushButton(self.tab_2)
        self.start.setGeometry(QtCore.QRect(20, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(56, 255, 12);border-radius :30;")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.tab_2)
        self.stop.setGeometry(QtCore.QRect(20, 120, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: rgb(231, 61, 9);border-radius :30;")
        self.stop.setObjectName("stop")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(350, 180, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.label_3.setObjectName("label_3")
        self.report = QtWidgets.QPushButton(self.tab_2)
        self.report.setGeometry(QtCore.QRect(20, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.report.setFont(font)
        self.report.setStyleSheet("background-color: rgb(17, 152, 255);border-radius :30;")
        self.report.setObjectName("report")
        self.health = QtWidgets.QProgressBar(self.tab_2)
       
        self.health.setGeometry(QtCore.QRect(540, 130, 131, 31))
        self.health.setInvertedAppearance(True)
        self.health.setObjectName("health")
        self.blinks = QtWidgets.QLCDNumber(self.tab_2)
        self.blinks.setGeometry(QtCore.QRect(360, 130, 91, 31))
        self.blinks.setObjectName("blinks")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(540, 180, 101, 21))
        self.blinks.setStyleSheet("background-color: rgb(0, 0, 255);")
        font = QtGui.QFont()
        
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QLabel(self.tab_2)
        self.image.setAutoFillBackground(True)
        self.image.setGeometry(QtCore.QRect(170, 220, 451, 351))
        self.image.setStyleSheet("\n"
"background-color: rgb(47, 47, 47);")
        self.image.setText("")
        self.image.setScaledContents(False)
        self.image.setObjectName("image")
        self.time = QtWidgets.QLCDNumber(self.tab_2)
        self.time.setGeometry(QtCore.QRect(190, 130, 81, 31))
        self.time.setObjectName("time")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(190, 180, 81, 20))
        self.time.setStyleSheet("background-color: rgb(0, 0, 255);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(158, 158, 158);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(210, 0, 341, 71))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(720, 100, 151, 31))

        
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(7)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 63 7pt \"Yu Gothic UI Semibold\";\n"
"text-decoration: underline;")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(720, 10, 121, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start.clicked.connect(self.show)
        
        self.stop.clicked.connect(self.Stop)
        self.report.clicked.connect(self.data,self.avg)

    def data(self):
        hour = [10,20,30,40,50,60]
        self.create2=QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi2(self.create2)
        self.create2.setWindowTitle('DAILY REPORT')
        self.ui.avg1.setText(str(self.avg))
        self.ui.normal1.setText(str(0.25))
        self.ui.graph.plot(hour,self.count)
        a,b=get_last_ndays(9)
        self.ui.day1.setText(str(b[0]))
        self.ui.day2.setText(str(b[1]))
        self.ui.day3.setText(str(b[2]))
        self.ui.value1.setText(str(a[0]))
        self.ui.value2.setText(str(a[1]))
        self.ui.value3.setText(str(a[2]))
        self.create2.show()
        self.count=[]
        self.ui.suggest.setScaledContents(True)
        if(self.avg<0.25):
            self.ui.suggest.setText("Your Average blinking rate is\nless than Normal.Use\ntear drops if you\nspend more than 4-5 hours\ninfront of your screeen\nBlink once in every\n5-6 seconds.")
        else:
            self.ui.suggest.setText("Thanks for taking\nCare of your Eyes.\nWell Done!")

        if(a[0]<0.25):
            self.ui.value1.setStyleSheet("background-color: rgb(255,0, 0);")
        if(a[1]<0.25):
            self.ui.value2.setStyleSheet("background-color: rgb(255,0, 0);")
        if(a[2]<0.25):
            self.ui.value3.setStyleSheet("background-color: rgb(255,0, 0);")
        a=time.time()
        b=int(a)
        date2=str(datetime.fromtimestamp(b))
        date2=date2.split(" ")
        tym2=date2[1].split(":")
        tym2=tym2[0]+"-"+tym2[1]+"-"+tym2[2]
        self.ui.label_11.setText(str(tym2))

        if(self.avg<0.25):
            self.ui.avg1.setStyleSheet("background-color: rgb(255, 0, 0);")

        


        b=int(self.a)
        date2=str(datetime.fromtimestamp(b))
        date2=date2.split(" ")
        tym2=date2[1].split(":")
        tym2=tym2[0]+"-"+tym2[1]+"-"+tym2[2]
        self.ui.start1.setText(str(tym2))
        
       


    def eye_aspect_ratio(self,eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        C = dist.euclidean(eye[0], eye[3])

        ear = (A + B) / (2.0 * C)
        return ear
    def get_file_name(self,time_stamp):
        date = str(datetime.fromtimestamp(time_stamp))
        date = date.split(" ")
        tym = date[1].split(":")
        tym = tym[0]+"-"+tym[1]+"-"+tym[2]
        date = date[0]+"x"+tym+".txt"
        return date 
   
    def Stop(self):
        self.f=1
        self.g=1
        
        
    def show(self):
        x=0
        
        if(self.g==1):
            self.a=time.time()
            self.g=0
        
        hrs4=4*60*60
        EYE_AR_THRESH = 0.25
        EYE_AR_CONSEC_FRAMES = 3

        COUNTER = 0
        TOTAL = 0

        print('[INFO] Loading facial landmark predictor...')
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(os.path.join(os.getcwd(), "shape_predictor_68_face_landmarks.dat_2"))

        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

        print('[INFO] Starting video stream thread...')
        fileStream = False
        vs = VideoStream(src=0).start()
        fileStream = False

        time.sleep(1.0)

        start = time.time()
        program_start = start
        stop, prev, curr = 0.0, 0.0, 0.0
        stop_flag = False
        last_tym = 0

        # storage space ---------------------------
        storage_path = os.path.join(os.getcwd(), "database" )
        timestamp = int(start)
        file_name = self.get_file_name(timestamp)
        fs = open(os.path.join(storage_path, file_name), 'w+')
        
        fs.write("STARTED AT "+str(program_start)+"\n")
        check=time.time()
        while True:
            if fileStream and not vs.more():
                break

            frame = vs.read()
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            rects = detector(gray, 0)
            flag = 0
            for rect in rects:
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                leftEye = shape[lStart: lEnd]
                rightEye = shape[rStart: rEnd]
                leftEAR = self.eye_aspect_ratio(leftEye)
                rightEAR = self.eye_aspect_ratio(rightEye)

                ear = (leftEAR + rightEAR) / 2.0

                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                else:
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1

                    COUNTER = 0
                
                
                
                flag = 1
            diff = time.time() - start
            start = time.time()
            difference=time.time()-check
            if(TOTAL>0 and curr>0):
                self.avg=TOTAL/(curr)
                
                
                if(difference>10):
                    x=TOTAL-x
                    self.count.append(x)
                    check=time.time()
                    if(self.avg<0.25):
                        msg =QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setWindowTitle("ALERT")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        
                        msg.setText('RELAX YOUR EYES A LITTLE BIT !!!\n \n Your average blinking rate is less than normal.')
                    

                        
                        retval=msg.exec_()

            if(flag):
                if(stop_flag and int(stop)>0):
                    fs.write("PAUSED FOR "+str(int(stop))+"\n")
                    stop_flag = False
                curr += diff
                stop = 0
                if( (int(curr)%10 == 0) and last_tym!=(int(curr)) ):
                    fs.write(str(int(curr))+" "+str(TOTAL)+"\n")
                    last_tym = int(curr)
            else:
                stop += diff
                stop_flag = True
            
            value=100*(1-min(1,curr/hrs4))
            self.image2=QtGui.QImage(frame.data,frame.shape[1],frame.shape[0],3*frame.shape[1],QtGui.QImage.Format_RGB888).rgbSwapped()

            self.health.setValue(value)
            self.image.setPixmap(QtGui.QPixmap(self.image2))
            
            self.blinks.display(TOTAL)
            self.time.display(curr)
            
            key = cv2.waitKey(1) & 0xFF

            if self.f==1:
                    
                    self.f=0
                    break
            if key == ord("q"):
                break

        
        cv2.destroyAllWindows()
        vs.stop()
        fs.write("STOPPED AT "+str(time.time())+"\n")
        fs.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "TOTAL BLINKS"))
        self.report.setText(_translate("MainWindow", "REPORT"))
        self.label_2.setText(_translate("MainWindow", "HEALTH BAR"))
        self.label_4.setText(_translate("MainWindow", "TIME"))
        self.label_6.setText(_translate("MainWindow", "      track-i"))
        self.label_7.setText(_translate("MainWindow", "YOUR EYES , OUR CARE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSplashScreen, QProgressBar
import os
import cv2 as cv
import subprocess
import matplotlib.pyplot as plt
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
import time


class Ui_login_page(object):
    def setupUi(self, login_page):
        login_page.setObjectName("login_page")
        login_page.resize(1366, 768)
        login_page.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""background:rgb(22, 22, 22);\n""}\n""")
        self.login_frame = QtWidgets.QFrame(login_page)
        self.login_frame.setGeometry(QtCore.QRect(370, 150, 621, 331))
        self.login_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.loginbutton = QtWidgets.QPushButton(self.login_frame)
        self.loginbutton.setGeometry(QtCore.QRect(220, 260, 181, 41))
        self.loginbutton.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.loginbutton.setObjectName("loginbutton")
        self.loginbutton.setAutoDefault(True)
        self.username = QtWidgets.QLineEdit(self.login_frame)
        self.username.setGeometry(QtCore.QRect(50, 140, 521, 41))
        self.username.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.login_frame)
        self.password.setGeometry(QtCore.QRect(50, 200, 521, 41))
        self.password.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.login_frame2 = QtWidgets.QFrame(self.login_frame)
        self.login_frame2.setGeometry(QtCore.QRect(270, 30, 81, 81))
        self.login_frame2.setStyleSheet("QFrame{\n""image:url(icons/cil-user.png);\n""background:rgb(67, 67, 67);\n""border-radius:40px;\n""}")
        self.login_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame2.setObjectName("login_frame2")
        self.background = QtWidgets.QFrame(login_page)
        self.background.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.background.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.background.raise_()
        self.login_frame.raise_()
        self.retranslateUi(login_page)
        QtCore.QMetaObject.connectSlotsByName(login_page)
        self.loginbutton.clicked.connect(self.login)
        self.password.returnPressed.connect(self.loginbutton.click)
        self.tries=0

    def login(self):
        user = self.username.text()
        pswd = self.password.text()
        path_id = "ID/"
        users = os.listdir(path_id)
        users = [users.replace('.txt', '') for users in users]
        if user in users :
         with open ("ID/" + user + ".txt", "r") as data:
          user_pswd=data.readlines()
        if user in users and pswd in user_pswd: 
                menu.showMaximized()
                login_page.hide()

        else:   
                self.username.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(255, 49, 49);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
                self.password.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(255, 49, 49);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}") 
                self.tries=self.tries+1
                Ui_login_page() 
                if self.tries==3 :
                    sys.exit()          

    def retranslateUi(self, login_page):
        _translate = QtCore.QCoreApplication.translate
        login_page.setWindowTitle(_translate("login_page", "Login"))
        self.loginbutton.setText(_translate("login_page", "Connecter"))
        self.username.setPlaceholderText(_translate("login_page", "ID"))
        self.password.setPlaceholderText(_translate("login_page", "Password"))

class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(1238, 542)
        menu.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:#333;\n""}\n""")
        self.menu_frame = QtWidgets.QFrame(menu)
        self.menu_frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.menu_frame.setStyleSheet("QFrame{\n""background:rgb(15, 15, 15)\n""}")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.iqbutton = QtWidgets.QPushButton(self.menu_frame)
        self.iqbutton.setGeometry(QtCore.QRect(100, 110, 201, 121))
        self.iqbutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-lightbulb.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.iqbutton.setIconSize(QtCore.QSize(20, 20))
        self.iqbutton.setObjectName("iqbutton")
        self.memorybutton = QtWidgets.QPushButton(self.menu_frame)
        self.memorybutton.setGeometry(QtCore.QRect(400, 110, 201, 121))
        self.memorybutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-gamepad.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.memorybutton.setIconSize(QtCore.QSize(20, 20))
        self.memorybutton.setObjectName("memorybutton")
        self.puzzlebutton = QtWidgets.QPushButton(self.menu_frame)
        self.puzzlebutton.setGeometry(QtCore.QRect(700, 110, 201, 121))
        self.puzzlebutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-star.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.puzzlebutton.setIconSize(QtCore.QSize(20, 20))
        self.puzzlebutton.setObjectName("puzzlebutton")
        self.storybutton = QtWidgets.QPushButton(self.menu_frame)
        self.storybutton.setGeometry(QtCore.QRect(1000, 110, 201, 121))
        self.storybutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-movie.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.storybutton.setIconSize(QtCore.QSize(20, 20))
        self.storybutton.setObjectName("storybutton")
        self.cahierbutton = QtWidgets.QPushButton(self.menu_frame)
        self.cahierbutton.setGeometry(QtCore.QRect(250, 400, 201, 121))
        self.cahierbutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-description.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.cahierbutton.setIconSize(QtCore.QSize(20, 20))
        self.cahierbutton.setObjectName("cahierbutton")
        self.exitbutton = QtWidgets.QPushButton(self.menu_frame)
        self.exitbutton.setGeometry(QtCore.QRect(860, 400, 201, 121))
        self.exitbutton.setStyleSheet("QPushButton{\n""image:url(icons/cil-power-standby.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.exitbutton.setIconSize(QtCore.QSize(20, 20))
        self.exitbutton.setObjectName("exitbutton")
        self.database = QtWidgets.QPushButton(self.menu_frame)
        self.database.setGeometry(QtCore.QRect(560, 400, 201, 121))
        self.database.setStyleSheet("QPushButton{\n""image:url(icons/cil-save.png);\n""background:rgb(48, 48, 48);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.database.setIconSize(QtCore.QSize(20, 20))
        self.database.setObjectName("database")
        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.iqbutton.clicked.connect(self.Iq_launch)
        self.memorybutton.clicked.connect(self.Memory_launch)
        self.puzzlebutton.clicked.connect(self.Puzzle_launch)
        self.storybutton.clicked.connect(self.Story_launch)
        self.cahierbutton.clicked.connect(self.Cahier_launch)
        self.database.clicked.connect(self.Database)        
        self.exitbutton.clicked.connect(self.Exit_launch)
    
    def Iq_launch(self):
        iq.show()
        iq.move(700,10)

    def Memory_launch(self):
        memory.show()
        memory.move(700,10)

    def Puzzle_launch(self):
        pg.show()
        pg.move(700,10) 

    def Story_launch(self):
        story.showMaximized()

    def Cahier_launch(self):
        cahier.showMaximized()

    def Database(self):
        path="C:/Program Files/Eva/Database"
        subprocess.Popen(f'explorer {os.path.realpath(path)}')

    def Exit_launch(self):
        sys.exit()
   
    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Menu"))
        self.iqbutton.setText(_translate("menu", "\n""\n""IQ IQ test "))
        self.memorybutton.setText(_translate("menu", "\n""\n""memory games"))
        self.puzzlebutton.setText(_translate("menu", "\n""\n""puzzles"))
        self.storybutton.setText(_translate("menu", "\n""\n""a story"))
        self.cahierbutton.setText(_translate("menu", "\n""\n""Section Chair"))
        self.exitbutton.setText(_translate("menu", "\n""\n""Exit"))
        self.database.setText(_translate("menu", "\n""\n""Database"))        

class Ui_iq(object):
    def setupUi(self, iq):
        iq.setObjectName("iq")
        iq.resize(661, 648)
        iq.setMaximumSize(QtCore.QSize(661, 765))
        iq.setLayoutDirection(QtCore.Qt.LeftToRight)
        iq.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""background:rgb(22, 22, 22);\n""}\n""")
        self.iq_frame = QtWidgets.QFrame(iq)
        self.iq_frame.setGeometry(QtCore.QRect(20, 130, 621, 171))
        self.iq_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.iq_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.iq_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.iq_frame.setObjectName("iq_frame")
        self.startiq_button = QtWidgets.QPushButton(self.iq_frame)
        self.startiq_button.setGeometry(QtCore.QRect(220, 100, 181, 41))
        self.startiq_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.startiq_button.setObjectName("startiq_button")
        self.student_name2 = QtWidgets.QLineEdit(self.iq_frame)
        self.student_name2.setGeometry(QtCore.QRect(50, 30, 521, 41))
        self.student_name2.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.student_name2.setAlignment(QtCore.Qt.AlignCenter)
        self.student_name2.setClearButtonEnabled(False)
        self.student_name2.setObjectName("student_name2")
        self.background3 = QtWidgets.QFrame(iq)
        self.background3.setGeometry(QtCore.QRect(0, 0, 661, 768))
        self.background3.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background3.setObjectName("background3")
        self.story_frame_3 = QtWidgets.QFrame(self.background3)
        self.story_frame_3.setGeometry(QtCore.QRect(20, 380, 621, 171))
        self.story_frame_3.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.story_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.story_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.story_frame_3.setObjectName("story_frame_3")
        self.confirm_button2 = QtWidgets.QPushButton(self.story_frame_3)
        self.confirm_button2.setGeometry(QtCore.QRect(220, 90, 181, 41))
        self.confirm_button2.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.confirm_button2.setObjectName("confirm_button2")
        self.answer = QtWidgets.QLineEdit(self.story_frame_3)
        self.answer.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.answer.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setClearButtonEnabled(False)
        self.answer.setObjectName("answer")
        self.background3.raise_()
        self.iq_frame.raise_()       
        self.retranslateUi(iq)
        QtCore.QMetaObject.connectSlotsByName(iq)    
        self.onlyInt = QIntValidator()
        self.answer.setValidator(self.onlyInt)           
        self.answer.setEnabled(False)
        self.confirm_button2.setEnabled(False)
        self.startiq_button.setAutoDefault(True)
        self.student_name2.returnPressed.connect(self.startiq_button.click)
        self.answer.returnPressed.connect(self.confirm_button2.click)
        self.startiq_button.clicked.connect(self.IQ)
        self.confirm_button2.clicked.connect(self.Process_answer)
        self.student= ''

    def IQ(self): 
        save_path = "Database/iq_test"
        y=self.student_name2.text()
        if y:
            if self.student== '' :
                    self.answer.setEnabled(True)
                    self.confirm_button2.setEnabled(True)                
                    self.student= self.student_name2.text()
                    f= os.path.join(save_path, self.student+".txt")
                    self.f1 = open(f, "w")
                    path = "IQ_test/"
                    images = os.listdir(path)
                    images = [images.replace('.jpg', '') for images in images]
                    self.nbr=1
                    self.iq=0
                    self.CA= [3,1,5,1,2,4,3,6,6,2,5,4,5,1,2,5,6,1,5,7]
                         
            im = cv.imread('IQ_test/'+str(self.nbr)+'.jpg')
            image = cv.resize(im, (600, 600))
            cv.imshow("Test IQ",image)
            cv.moveWindow('image',20,5)
            cv.waitKey(10)     
                  
    def Process_answer(self): 
        x = self.answer.text()
        if x :
            x= int(x)
            self.answer.setText('') 
            if (x==self.CA[self.nbr-1]) :
                    self.iq=self.iq+1                    
            self.nbr=self.nbr+1 
            if self.nbr == 21 :
                self.iq=str(self.iq)
                self.f1.write(self.iq)
                self.f1.close()
                cv.destroyAllWindows() 
                self.student_name2.setText('')
                self.answer.setText('') 
                self.student=''
                self.nbr=1
                self.iq=0
                self.answer.setEnabled(False)
                self.confirm_button2.setEnabled(False)                
                iq.hide()  
            else:            
                im = cv.imread('IQ_test/'+str(self.nbr)+'.jpg')
                image = cv.resize(im, (600, 600))
                cv.imshow("Test IQ",image)
                cv.moveWindow('image',20,5)
                cv.waitKey(10)
          
    def retranslateUi(self, iq):
        _translate = QtCore.QCoreApplication.translate
        iq.setWindowTitle(_translate("iq", "IQ Test"))
        self.startiq_button.setText(_translate("iq", "! Start the test "))
        self.student_name2.setPlaceholderText(_translate("iq", "Student's name"))
        self.confirm_button2.setText(_translate("iq", "agree on"))
        self.answer.setPlaceholderText(_translate("iq", "the answer"))

class Ui_memory(object):
    def setupUi(self, memory):
        memory.setObjectName("memory")
        memory.resize(661, 648)
        memory.setMaximumSize(QtCore.QSize(661, 765))
        memory.setLayoutDirection(QtCore.Qt.LeftToRight)
        memory.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""background:rgb(22, 22, 22);\n""}\n""")
        self.mg_frame = QtWidgets.QFrame(memory)
        self.mg_frame.setGeometry(QtCore.QRect(20, 130, 621, 171))
        self.mg_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.mg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mg_frame.setObjectName("mg_frame")
        self.startmg_button = QtWidgets.QPushButton(self.mg_frame)
        self.startmg_button.setGeometry(QtCore.QRect(220, 100, 181, 41))
        self.startmg_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.startmg_button.setObjectName("startmg_button")
        self.student_name2 = QtWidgets.QLineEdit(self.mg_frame)
        self.student_name2.setGeometry(QtCore.QRect(50, 30, 521, 41))
        self.student_name2.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.student_name2.setAlignment(QtCore.Qt.AlignCenter)
        self.student_name2.setClearButtonEnabled(False)
        self.student_name2.setObjectName("student_name2")
        self.background3 = QtWidgets.QFrame(memory)
        self.background3.setGeometry(QtCore.QRect(0, 0, 661, 768))
        self.background3.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background3.setObjectName("background3")
        self.mg_frame_3 = QtWidgets.QFrame(self.background3)
        self.mg_frame_3.setGeometry(QtCore.QRect(20, 380, 621, 171))
        self.mg_frame_3.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.mg_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mg_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mg_frame_3.setObjectName("mg_frame_3")
        self.confirm_button3 = QtWidgets.QPushButton(self.mg_frame_3)
        self.confirm_button3.setGeometry(QtCore.QRect(220, 90, 181, 41))
        self.confirm_button3.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.confirm_button3.setObjectName("confirm_button3")
        self.memory_score = QtWidgets.QLineEdit(self.mg_frame_3)
        self.memory_score.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.memory_score.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.memory_score.setAlignment(QtCore.Qt.AlignCenter)
        self.memory_score.setClearButtonEnabled(False)
        self.memory_score.setObjectName("memory_score")
        self.background3.raise_()
        self.mg_frame.raise_()
        self.retranslateUi(memory)
        QtCore.QMetaObject.connectSlotsByName(memory)
        self.onlyInt = QIntValidator()
        self.memory_score.setValidator(self.onlyInt)         
        self.memory_score.setEnabled(False)
        self.confirm_button3.setEnabled(False)
        self.startmg_button.setAutoDefault(True)
        self.student_name2.returnPressed.connect(self.startmg_button.click)
        self.memory_score.returnPressed.connect(self.confirm_button3.click)        
        self.startmg_button.clicked.connect(self.MG)
        self.confirm_button3.clicked.connect(self.Memory_score)

    def MG(self):
        save_path = "Database/memory"
        student= self.student_name2.text()
        if student:
            self.memory_score.setEnabled(True)
            self.confirm_button3.setEnabled(True)            
            f= os.path.join(save_path, student+".txt")
            self.f1 = open(f, "w")
            game_path = "C:/Program Files/Eva/Memory/1.swf"   
            mediaplayer = "C:/Program Files/Windows Media Player/wmplayer.exe"
            subprocess.Popen((mediaplayer, game_path))        
        

    def Memory_score(self):        
        score = self.memory_score.text()
        if score:
            score=str(score)
            self.f1.write(score)
            self.f1.close()
            self.memory_score.setText('')
            self.student_name2.setText('') 
            self.memory_score.setEnabled(False)
            self.confirm_button3.setEnabled(False)   
            memory.hide()
 
    def retranslateUi(self, memory):
        _translate = QtCore.QCoreApplication.translate
        memory.setWindowTitle(_translate("memory", "Memory Game"))
        self.startmg_button.setText(_translate("memory", "! Start game"))
        self.student_name2.setPlaceholderText(_translate("memory", "Student's name"))
        self.confirm_button3.setText(_translate("memory", "agree on "))
        self.memory_score.setPlaceholderText(_translate("memory", "The result"))

class Ui_pg(object):
    def setupUi(self, pg):
        pg.setObjectName("pg")
        pg.resize(661, 648)
        pg.setMaximumSize(QtCore.QSize(661, 765))
        pg.setLayoutDirection(QtCore.Qt.LeftToRight)
        pg.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""}\n""")
        self.iq_frame = QtWidgets.QFrame(pg)
        self.iq_frame.setGeometry(QtCore.QRect(20, 130, 621, 171))
        self.iq_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.iq_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.iq_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.iq_frame.setObjectName("iq_frame")
        self.startpg_button = QtWidgets.QPushButton(self.iq_frame)
        self.startpg_button.setGeometry(QtCore.QRect(220, 100, 181, 41))
        self.startpg_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.startpg_button.setObjectName("startpg_button")
        self.student_name2 = QtWidgets.QLineEdit(self.iq_frame)
        self.student_name2.setGeometry(QtCore.QRect(50, 30, 521, 41))
        self.student_name2.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""")
        self.student_name2.setAlignment(QtCore.Qt.AlignCenter)
        self.student_name2.setClearButtonEnabled(False)
        self.student_name2.setObjectName("student_name2")
        self.background3 = QtWidgets.QFrame(pg)
        self.background3.setGeometry(QtCore.QRect(0, 0, 661, 768))
        self.background3.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background3.setObjectName("background3")
        self.pg_frame_3 = QtWidgets.QFrame(self.background3)
        self.pg_frame_3.setGeometry(QtCore.QRect(20, 380, 621, 171))
        self.pg_frame_3.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.pg_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pg_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pg_frame_3.setObjectName("pg_frame_3")
        self.confirm_button3 = QtWidgets.QPushButton(self.pg_frame_3)
        self.confirm_button3.setGeometry(QtCore.QRect(220, 90, 181, 41))
        self.confirm_button3.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.confirm_button3.setObjectName("confirm_button3")
        self.answer2 = QtWidgets.QLineEdit(self.pg_frame_3)
        self.answer2.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.answer2.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.answer2.setAlignment(QtCore.Qt.AlignCenter)
        self.answer2.setClearButtonEnabled(False)
        self.answer2.setObjectName("answer2")
        self.background3.raise_()
        self.iq_frame.raise_()
        self.retranslateUi(pg)
        QtCore.QMetaObject.connectSlotsByName(pg)
        self.onlyInt = QIntValidator()
        self.answer2.setValidator(self.onlyInt)        
        self.answer2.setEnabled(False)
        self.confirm_button3.setEnabled(False)
        self.startpg_button.setAutoDefault(True)
        self.student_name2.returnPressed.connect(self.startpg_button.click)
        self.answer2.returnPressed.connect(self.confirm_button3.click)  
        self.startpg_button.clicked.connect(self.PG)
        self.confirm_button3.clicked.connect(self.Process_answer2)
        self.student= ''

    def PG(self):
        save_path = "Database\puzzle"
        z=self.student_name2.text()
        if z:
            if self.student== '' : 
                    self.answer2.setEnabled(True)
                    self.confirm_button3.setEnabled(True)                
                    student= self.student_name2.text()
                    f= os.path.join(save_path, student+".txt")
                    self.f1 = open(f, "w")
                    path = "Puzzle\\"
                    images = os.listdir(path)
                    images = [images.replace('.jpg', '') for images in images]
                    self.nbr2=1
                    self.score=0
                    self.rep= [3,2,2,1,3]
            im = cv.imread(r'Puzzle\\'+str(self.nbr2)+'.jpg')
            image = cv.resize(im, (600, 600))
            cv.imshow("Puzzle",image)
            cv.moveWindow('image',20,5)
            cv.waitKey(10)      

    def Process_answer2(self):
        x = self.answer2.text()
        if x:
            x= int(x)
            self.answer2.setText('')
            if (x==self.rep[self.nbr2-1]) :
                    self.score=self.score+4 
            self.nbr2=self.nbr2+1 
            if self.nbr2 == 6 :
                    self.score=str(self.score)
                    self.f1.write(self.score)
                    self.f1.close() 
                    cv.destroyAllWindows()
                    self.answer2.setText('')
                    self.student_name2.setText('')
                    self.answer2.setEnabled(False)
                    self.confirm_button3.setEnabled(False)
                    pg.hide()
            else:       
                im = cv.imread('Puzzle\\'+str(self.nbr2)+'.jpg')
                image = cv.resize(im, (600, 600))
                cv.imshow("Puzzle",image)
                cv.moveWindow('image',20,5)
                cv.waitKey(10)

    def retranslateUi(self, pg):
        _translate = QtCore.QCoreApplication.translate
        pg.setWindowTitle(_translate("pg", "Puzzle"))
        self.startpg_button.setText(_translate("pg", "! Start the test"))
        self.student_name2.setPlaceholderText(_translate("pg", "Student's name"))
        self.confirm_button3.setText(_translate("pg", "agree on"))
        self.answer2.setPlaceholderText(_translate("pg", "the answer"))

class Ui_story(object):
    def setupUi(self, story):
        story.setObjectName("story")
        story.resize(1366, 768)
        story.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""background:rgb(22, 22, 22);\n""}\n""")
        self.story_frame = QtWidgets.QFrame(story)
        self.story_frame.setGeometry(QtCore.QRect(370, 130, 621, 171))
        self.story_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.story_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.story_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.story_frame.setObjectName("story_frame")
        self.startstory_button = QtWidgets.QPushButton(self.story_frame)
        self.startstory_button.setGeometry(QtCore.QRect(220, 100, 181, 41))
        self.startstory_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.startstory_button.setObjectName("startstory_button")
        self.student_name = QtWidgets.QLineEdit(self.story_frame)
        self.student_name.setGeometry(QtCore.QRect(50, 30, 521, 41))
        self.student_name.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.student_name.setAlignment(QtCore.Qt.AlignCenter)
        self.student_name.setClearButtonEnabled(False)
        self.student_name.setObjectName("student_name")
        self.background2 = QtWidgets.QFrame(story)
        self.background2.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.background2.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background2.setObjectName("background2")
        self.story_frame_2 = QtWidgets.QFrame(self.background2)
        self.story_frame_2.setGeometry(QtCore.QRect(370, 310, 621, 171))
        self.story_frame_2.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.story_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.story_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.story_frame_2.setObjectName("story_frame_2")
        self.confirm_button = QtWidgets.QPushButton(self.story_frame_2)
        self.confirm_button.setGeometry(QtCore.QRect(220, 90, 181, 41))
        self.confirm_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.confirm_button.setObjectName("confirm_button")
        self.result = QtWidgets.QLineEdit(self.story_frame_2)
        self.result.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.result.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setClearButtonEnabled(False)
        self.result.setObjectName("result")
        self.background2.raise_()
        self.story_frame.raise_()
        self.retranslateUi(story)
        QtCore.QMetaObject.connectSlotsByName(story)
        self.result.setEnabled(False)
        self.confirm_button.setEnabled(False)
        self.startstory_button.setAutoDefault(True)
        self.student_name.returnPressed.connect(self.startstory_button.click)
        self.result.returnPressed.connect(self.confirm_button.click)         
        self.startstory_button.clicked.connect(self.Story)
        self.confirm_button.clicked.connect(self.Score)

    def Story(self):
        save_path = "Database/story"
        student = self.student_name.text()
        if student:
            self.result.setEnabled(True)
            self.confirm_button.setEnabled(True)                    
            f= os.path.join(save_path, student+".txt")
            self.f1 = open(f, "w")
            story_path = "C:/Program Files/Eva/Story/1.mp4" 
            mediaplayer = "C:/Program Files/Windows Media Player/wmplayer.exe"
            subprocess.Popen((mediaplayer, story_path))

    def Score(self):
        score= self.result.text()
        if score:
            score=str(score)
            self.f1.write(score)
            self.f1.close() 
            self.result.setText('')
            self.student_name.setText('')
            self.result.setEnabled(False)
            self.confirm_button.setEnabled(False)            
            story.hide()

    def retranslateUi(self, story):
        _translate = QtCore.QCoreApplication.translate
        story.setWindowTitle(_translate("story", "Story"))
        self.startstory_button.setText(_translate("story", "! start the story"))
        self.student_name.setPlaceholderText(_translate("story", "Student's name"))
        self.confirm_button.setText(_translate("story", "agree on "))
        self.result.setPlaceholderText(_translate("story", "The result"))

class Ui_cahier(object):
    def setupUi(self, cahier):
        cahier.setObjectName("cahier")
        cahier.resize(1366, 768)
        cahier.setStyleSheet("*\n""{\n""font: 20pt \"Ebrima\";\n""}\n""#Form{\n""background:rgb(22, 22, 22)\n""}\n""QFrame{\n""background:rgb(22, 22, 22);\n""}\n""")
        self.cahier_frame2 = QtWidgets.QFrame(cahier)
        self.cahier_frame2.setGeometry(QtCore.QRect(370, 110, 621, 191))
        self.cahier_frame2.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.cahier_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cahier_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cahier_frame2.setObjectName("cahier_frame2")
        self.startsaving_button = QtWidgets.QPushButton(self.cahier_frame2)
        self.startsaving_button.setGeometry(QtCore.QRect(220, 130, 181, 41))
        self.startsaving_button.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 194, 255)\n""}")
        self.startsaving_button.setObjectName("startsaving_button")
        self.student_name3 = QtWidgets.QLineEdit(self.cahier_frame2)
        self.student_name3.setGeometry(QtCore.QRect(50, 30, 521, 41))
        self.student_name3.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.student_name3.setAlignment(QtCore.Qt.AlignCenter)
        self.student_name3.setClearButtonEnabled(False)
        self.student_name3.setObjectName("student_name3")
        self.weeks_nbr = QtWidgets.QLineEdit(self.cahier_frame2)
        self.weeks_nbr.setGeometry(QtCore.QRect(80, 80, 461, 41))
        self.weeks_nbr.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.weeks_nbr.setAlignment(QtCore.Qt.AlignCenter)
        self.weeks_nbr.setClearButtonEnabled(False)
        self.weeks_nbr.setObjectName("weeks_nbr")
        self.background6 = QtWidgets.QFrame(cahier)
        self.background6.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.background6.setStyleSheet("QFrame{\n""background:rgb(32, 32, 32);\n""}")
        self.background6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background6.setObjectName("background6")
        self.cahier_frame = QtWidgets.QFrame(self.background6)
        self.cahier_frame.setGeometry(QtCore.QRect(370, 330, 621, 171))
        self.cahier_frame.setStyleSheet("QFrame{\n""background:rgb(22, 22, 22);\n""border-radius:15px;\n""}")
        self.cahier_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cahier_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cahier_frame.setObjectName("cahier_frame")
        self.save = QtWidgets.QPushButton(self.cahier_frame)
        self.save.setGeometry(QtCore.QRect(220, 90, 181, 41))
        self.save.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(24, 255, 21)\n""}")
        self.save.setObjectName("save")
        self.note = QtWidgets.QLineEdit(self.cahier_frame)
        self.note.setGeometry(QtCore.QRect(220, 30, 181, 41))
        self.note.setStyleSheet("QLineEdit{\n""border-radius:15px;\n""background:rgb(67, 67, 67);\n""color:rgb(255, 255, 255);\n""}\n""QLineEdit:hover{\n""border: 2px solid rgb(85, 170, 255)\n""}\n""\n""\n""")
        self.note.setAlignment(QtCore.Qt.AlignCenter)
        self.note.setClearButtonEnabled(False)
        self.note.setObjectName("note")
        self.quit = QtWidgets.QPushButton(self.background6)
        self.quit.setGeometry(QtCore.QRect(590, 560, 181, 41))
        self.quit.setStyleSheet("QPushButton{\n""background:rgb(0, 170, 255);\n""color:#fff;\n""border-radius:15px;\n""}\n""QPushButton:hover{\n""background:rgb(255, 26, 26)\n""}")
        self.quit.setObjectName("quit")
        self.background6.raise_()
        self.cahier_frame2.raise_()
        self.retranslateUi(cahier)
        QtCore.QMetaObject.connectSlotsByName(cahier)
        self.onlyInt = QIntValidator()
        self.weeks_nbr.setValidator(self.onlyInt)   
        self.note.setValidator(QDoubleValidator(0.0, 20.0, 2))
        self.note.setEnabled(False)
        self.save.setEnabled(False)
        self.note.returnPressed.connect(self.save.click) 
        self.startsaving_button.clicked.connect(self.Cahier)
        self.save.clicked.connect(self.Input_notes)
        self.quit.clicked.connect(self.Quit)
        self.student= ''
        self.p=1

    def Cahier(self):      
        xx=self.student_name3.text()
        yy=self.weeks_nbr.text()
        if xx and yy :
            if self.student== '' :
                    self.note.setEnabled(True)
                    self.save.setEnabled(True)                 
                    self.x_axis = [] 
                    self.y_axis = [] 
                    self.student= self.student_name3.text()
                    self.weeks = self.weeks_nbr.text()
                    self.weeks= int(self.weeks)
                    for i in range(1, self.weeks+1): 
                            self.ele1 = int(i) 
                            self.x_axis.append(self.ele1)  
                    self.k=1  
                                        
    def Input_notes(self):
        x =self.note.text()
        if x:
            self.ele2 = float(self.note.text()) 
            self.y_axis.append(self.ele2)
            self.k= self.k+1
            self.note.setText('')
            if self.k == self.weeks+1 :
                    self.Save()  
                
    def Save(self):        
        plt.figure(self.p)    
        plt.plot(self.x_axis, self.y_axis,marker='o', markerfacecolor='red', markersize=12) 
        plt.title("Notes du l'eleve "+self.student+" dans "+str(self.weeks)+" semaines")
        plt.xlabel("Temps")
        plt.ylabel("Note")
        plt.savefig('Database/Cahier/'+self.student) 
        self.Next()

    def Quit(self):
            cahier.hide()
   
    def Next(self):
            self.weeks_nbr.setText('')
            self.student_name3.setText('')
            self.note.setText('')
            self.student= ''  
            self.note.setEnabled(False)
            self.save.setEnabled(False)
            self.p=self.p+1

    def retranslateUi(self, cahier):
        _translate = QtCore.QCoreApplication.translate
        cahier.setWindowTitle(_translate("cahier", "Cahier de classe"))
        self.startsaving_button.setText(_translate("cahier", "موافق"))
        self.student_name3.setPlaceholderText(_translate("cahier", "اسم التلميذ"))
        self.weeks_nbr.setPlaceholderText(_translate("cahier", "عدد الاسابيع"))
        self.save.setText(_translate("cahier", "احفض"))
        self.note.setPlaceholderText(_translate("cahier", "العدد"))
        self.quit.setText(_translate("cahier", "خروج"))


if __name__ == "__main__":
    import sys
      
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))    
    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    progressBar = QProgressBar(splash)
    progressBar.setGeometry(5, 255, 725, 25)
    splash.setMask(splash_pix.mask())
    splash.show()
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.035:
            app.processEvents()           

    login_page = QtWidgets.QWidget()
    ui = Ui_login_page()
    ui.setupUi(login_page)
    login_page.showMaximized()
    splash.finish(login_page)
    app2 = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QWidget()
    ui2 = Ui_menu()
    ui2.setupUi(menu)  
    app3 = QtWidgets.QApplication(sys.argv)
    iq = QtWidgets.QWidget()
    ui3 = Ui_iq()
    ui3.setupUi(iq)
    app4 = QtWidgets.QApplication(sys.argv)
    memory = QtWidgets.QWidget()
    ui4 = Ui_memory()
    ui4.setupUi(memory)
    app5 = QtWidgets.QApplication(sys.argv)
    pg = QtWidgets.QWidget()
    ui5 = Ui_pg()
    ui5.setupUi(pg)
    app6 = QtWidgets.QApplication(sys.argv)
    story = QtWidgets.QWidget()
    ui6 = Ui_story()
    ui6.setupUi(story)
    app7 = QtWidgets.QApplication(sys.argv)
    cahier = QtWidgets.QWidget()
    ui7 = Ui_cahier()
    ui7.setupUi(cahier)
    sys.exit(app.exec_())
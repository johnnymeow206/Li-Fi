import numpy as np
#import transmit
import GUI_imgjpeg
from GUI3 import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.GUI = Ui_Form()
        self.GUI.setupUi(self)
        self.GUI_setup()
        
    def GUI_setup(self):
        self.GUI.spinBox_Q.setValue(50) 
        self.spinbox_prevalue = self.GUI.spinBox_Q.value()

        self.GUI.pushButton_confirm.clicked.connect(self.confirm_clicked) 
        self.GUI.pushButton_open.clicked.connect(self.Open_Clicked)
        self.GUI.pushButton_DCT.clicked.connect(self.Img_DCT_clicked)
        #self.GUI.pushButton_transmit.clicked.connect(self.transmit_Clicked)
        self.box = QtWidgets.QMessageBox(self)
        

    def Open_Clicked(self):
        self.FilePath , self.FilterType = QtWidgets.QFileDialog.getOpenFileNames()
        OutputFilename = "Outputimg"
        try:
            self.Img_Input = GUI_imgjpeg.Img_JPEG(self.FilePath, OutputFilename, self.GUI.spinBox_Q.value())

            self.Img_show_L(self.FilePath[0], self.Img_Input.rows, self.Img_Input.cols)
            self.Img_Input.JPEG_ZigZag(self.GUI.spinBox_Q.value())
            self.Img_Input.JPEG_remain(self.GUI.spinBox_Q.value())
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')

    def Img_show_L(self,FilePath, len, wid):
        self.scene_1 = QtWidgets.QGraphicsScene()
        self.img = QtGui.QPixmap(FilePath)
        img_w = 512                         # 顯示圖片的寬度
        img_h = 512                          # 顯示圖片的高度
        self.img = self.img.scaled(img_w, img_h, QtCore.Qt.KeepAspectRatio)
        dx = int(abs((self.GUI.graphicsView_graphicL.width() - img_w))-3 / 2)        # 修正公式
        dy = int(abs((self.GUI.graphicsView_graphicL.height()  - img_h))-3 / 2)
        self.scene_1.setSceneRect(dx, dy, 512, 512)
        self.scene_1.addPixmap(self.img)

        self.GUI.graphicsView_graphicL.setScene(self.scene_1)
        self.GUI.graphicsView_graphicL.mousePressEvent = self.get_clicked_position
        self.side_CutPicture = self.cutPicture(FilePath)
        self.DCT_CutPicture = self.cutPicture(self.Img_Input.OutputFilename + "DCT.jpg")
        self.ZigZag_CutPicture = self.cutPicture(self.Img_Input.OutputFilename + "Zigzag.jpg")


    def Img_show_R(self, inpfile):
        self.scene_2 = QtWidgets.QGraphicsScene()
        self.img2 = QtGui.QPixmap(inpfile)
        img_w = 512                         # 顯示圖片的寬度
        img_h = 512                          # 顯示圖片的高度
        self.img2 = self.img2.scaled(img_w, img_h, QtCore.Qt.KeepAspectRatio)
        dx = int(abs((self.GUI.graphicsView_graphicR.width() - img_w))-3 / 2)        # 修正公式
        dy = int(abs((self.GUI.graphicsView_graphicR.height()  - img_h))-3 / 2)
        self.scene_2.setSceneRect(dx, dy, 512, 512)
        
        self.scene_2.addPixmap(self.img2)
        self.GUI.graphicsView_graphicR.setScene(self.scene_2)
        self.GUI.graphicsView_graphicR.mousePressEvent = self.get_clicked_position

    def Img_show_side(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_original.setPixmap(temp)

    def Img_show_DCT(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_DCT.setPixmap(temp)
    
    def Img_show_ZigZag(self, Filepath):
        temp = QtGui.QPixmap(Filepath).scaled(139, 139)
        self.GUI.label_side_zigzag.setPixmap(temp)

    def Img_DCT_clicked(self):
        try:
            self.Img_Input.JPEG_DCT()
            if self.GUI.pushButton_DCT.isChecked() == True: 
                self.Img_show_R(self.Img_Input.OutputFilename + "DCT.jpg") 
            else:
                self.scene_2.clear()
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')
    
    def Img_Zigzag_clicked(self):
        if self.spinbox_prevalue != self.GUI.spinBox_Q:
            self.Img_Input.JPEG_ZigZag(self.GUI.spinBox_Q.value())
            self.spinbox_prevalue = self.GUI.spinBox_Q
        self.Img_show_R(self.Img_Input.OutputFilename + "Zigzag.jpg") 

    def confirm_clicked(self):
        try:
            if self.spinbox_prevalue != self.GUI.spinBox_Q.value():
                self.Img_Input.JPEG_ZigZag(self.GUI.spinBox_Q.value())
                self.Img_Input.JPEG_remain(self.GUI.spinBox_Q.value())
                self.spinbox_prevalue = self.GUI.spinBox_Q
            if self.GUI.pushButton_DCT.isChecked() == True:
                self.GUI.pushButton_DCT.toggle()
            self.Img_show_R(self.Img_Input.OutputFilename + "R1.jpg") 
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')
    
    def transmit_Clicked(self):
        try:
            value_to_transmit = self.Img_Input.JPEG_transmit()
            #transmit.transmit_to_Board(value_to_transmit)
        except:
            self.box.critical(self, 'Error', 'No File Selected!!')

    def cutPicture(self, FilePath):
        self.photo = QtGui.QPixmap(FilePath)
        size = min(self.photo.width(), self.photo.height())
        self.photo = self.photo.copy(0, 0, size, size)
        img_piece = [[0 for k1 in range(self.Img_Input.h)]for k2 in range(self.Img_Input.w)]
        for x in range(self.Img_Input.w):
            for y in range(self.Img_Input.h):
                pieceImage = self.photo.copy(x*8, y*8, 8, 8)
                img_piece[x][y] = pieceImage
        return img_piece


    def __update_text_clicked_position(self, x, y):
        self.GUI.label_click_pos.setText(f"Clicked postion = ({x}, {y})")
        self.GUI.label_norm_pos.setText(f"Normalized postion = ({self.norm_x:.3f}, {self.norm_y:.3f})")
        self.GUI.label_real_pos.setText(f"Real postion = ({int(x*self.Img_Input.cols/512)}, {int(y*self.Img_Input.rows/512)})")
    
    

    def get_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y() 
        self.norm_x = x/self.GUI.graphicsView_graphicL.width()
        self.norm_y = y/self.GUI.graphicsView_graphicL.height()

        print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({self.norm_x}, {self.norm_y})")
        try :
            temp = self.side_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            temp_DCT = self.DCT_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            temp_ZigZag = self.ZigZag_CutPicture[int(x*self.Img_Input.h/512)][int(y*self.Img_Input.w/512)]
            #print(int(x*self.Img_Input.h/512), int(y*self.Img_Input.w/512))
            self.Img_show_side(temp)
            self.Img_show_DCT(temp_DCT)
            self.Img_show_ZigZag(temp_ZigZag)
            self.__update_text_clicked_position(x, y)
            print("success")
        except:
            self.__update_text_clicked_position(x, y)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
#Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
#Form.setFixedSize(Form.width(),Form.height())
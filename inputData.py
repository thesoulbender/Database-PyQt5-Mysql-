#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql.cursors

showlist = ["" for i in range(28)]

class InputDialog(QWidget):
    def __init__(self):       
        super(InputDialog,self).__init__()
    #     self.initUi()

    # def initUi(self):
        self.setWindowTitle("项目信息")
        self.setGeometry(100,100,900,960)

        label1=QLabel("项目编号:")
        label2=QLabel("合同名称:")
        label3=QLabel("业主名称:")
        label4=QLabel("业主性质:")
        label5=QLabel("合同金额:")
        label6=QLabel("合同性质:")
        label7=QLabel("合同签订日:")
        label8=QLabel("合同约定开工:")
        label9=QLabel("合同约定日期:")
        label10=QLabel("合同完工日:")
        label11=QLabel("履约保证金:")
        label12=QLabel("安全保证金:")
        label13=QLabel("合同约定支付时间:")
        label14=QLabel("合同约定退还时间:")
        label15=QLabel("款项性质:")
        label16=QLabel("收款条件:")
        label17=QLabel("付款方式（银承、商承、电汇）:")
        label18=QLabel("发票要求:")
        label19=QLabel("收款其他条件（扣贴现息）:")
        label20=QLabel("发票时间:")
        label21=QLabel("发票金额:")
        label22=QLabel("实际收款时间:")
        label23=QLabel("实际收款金额:")
        label24=QLabel("实际收款方式:")
        label25=QLabel("所属部门:")
        label26=QLabel("E:")
        label27=QLabel("P:")
        label28=QLabel("C:")

        nextButton = QPushButton("保存")
        nextButton.clicked.connect(lambda: self.nextPage())

        mainLayout=QGridLayout()
        mainLayout.addWidget(label1,0,0)
        self.text1 = QLineEdit(self)
        mainLayout.addWidget(self.text1,0,1)
        mainLayout.addWidget(label2,1,0)
        self.text2 = QLineEdit(self)
        mainLayout.addWidget(self.text2,1,1)
        mainLayout.addWidget(label3,2,0)
        self.text3 = QLineEdit(self)
        mainLayout.addWidget(self.text3,2,1)
        mainLayout.addWidget(label4,3,0)
        self.text4 = QLineEdit(self)  
        mainLayout.addWidget(self.text4,3,1)  
        mainLayout.addWidget(label5,4,0)
        self.text5 = QLineEdit(self)
        mainLayout.addWidget(self.text5,4,1)
        mainLayout.addWidget(label6,5,0)
        
        self.text6 = QComboBox()
        self.text6.insertItem(0,self.tr("EPC"))
        self.text6.insertItem(1,self.tr("EP"))
        self.text6.insertItem(2,self.tr("EC"))
        self.text6.insertItem(3,self.tr("PC"))
        self.text6.insertItem(4,self.tr("E"))
        self.text6.insertItem(5,self.tr("P"))
        self.text6.insertItem(6,self.tr("C"))

        mainLayout.addWidget(self.text6,5,1)
        mainLayout.addWidget(label7,6,0)
        self.text7 = QDateTimeEdit(self)
        self.text7.setDateTime(QDateTime.currentDateTime())
        self.text7.setDisplayFormat("yyyy/MM/dd")
        self.text7.setCalendarPopup(True)
        mainLayout.addWidget(self.text7,6,1)
        mainLayout.addWidget(label8,7,0)
        self.text8 = QDateTimeEdit(self)
        self.text8.setDateTime(QDateTime.currentDateTime())
        self.text8.setDisplayFormat("yyyy/MM/dd")
        self.text8.setCalendarPopup(True)
        mainLayout.addWidget(self.text8,7,1)
        mainLayout.addWidget(label9,8,0)
        self.text9 = QDateTimeEdit(self)
        self.text9.setDateTime(QDateTime.currentDateTime())
        self.text9.setDisplayFormat("yyyy/MM/dd")
        self.text9.setCalendarPopup(True)
        mainLayout.addWidget(self.text9,8,1)
        mainLayout.addWidget(label10,9,0)
        self.text10 = QDateTimeEdit(self)
        self.text10.setDateTime(QDateTime.currentDateTime())
        self.text10.setDisplayFormat("yyyy/MM/dd")
        self.text10.setCalendarPopup(True)
        mainLayout.addWidget(self.text10,9,1)
        mainLayout.addWidget(label11,10,0)
        self.text11 = QLineEdit(self)
        mainLayout.addWidget(self.text11,10,1)
        mainLayout.addWidget(label12,11,0)
        self.text12 = QLineEdit(self)   
        mainLayout.addWidget(self.text12,11,1) 

        mainLayout.addWidget(label25,12,0)
        self.text28 = QComboBox()
        mainLayout.addWidget(self.text28,12,1)
        self.text28.insertItem(0,self.tr("冶金事业部"))
        self.text28.insertItem(1,self.tr("市政事业部"))
        self.text28.insertItem(2,self.tr("铁合金事业部"))
        self.text28.insertItem(3,self.tr("自动化事业部"))
        self.text28.insertItem(4,self.tr("建工所"))
        self.text28.insertItem(5,self.tr("翻译中心"))
        self.text28.insertItem(6,self.tr("青海分公司"))
        self.text28.insertItem(7,self.tr("包头分院"))
        self.text28.insertItem(8,self.tr("公司"))

        mainLayout.addWidget(label26,12,3)
        self.text25 = QLineEdit(self)
        mainLayout.addWidget(self.text25,12,4)
        mainLayout.addWidget(label27,13,0)
        self.text26 = QLineEdit(self)
        mainLayout.addWidget(self.text26,13,1)
        mainLayout.addWidget(label28,13,3)
        self.text27 = QLineEdit(self)
        mainLayout.addWidget(self.text27,13,4)
        #layout = QFormLayout()
        #layout.addRow(QLabel("Country:"), QComboBox())
        #self.formGroupBox.setLayout(layout)

        mainLayout.addWidget(label13,0,3)
        self.text13 = QDateTimeEdit(self)
        self.text13.setDateTime(QDateTime.currentDateTime())
        self.text13.setDisplayFormat("yyyy/MM/dd")
        self.text13.setCalendarPopup(True)
        mainLayout.addWidget(self.text13,0,4)
        mainLayout.addWidget(label14,1,3)
        self.text14 = QDateTimeEdit(self)
        self.text14.setDateTime(QDateTime.currentDateTime())
        self.text14.setDisplayFormat("yyyy/MM/dd")
        self.text14.setCalendarPopup(True)
        mainLayout.addWidget(self.text14,1,4)
        mainLayout.addWidget(label15,2,3)
        self.text15 = QComboBox()

        self.text15.insertItem(0,self.tr("预付款（第一笔款）"))
        self.text15.insertItem(1,self.tr("第二笔款")) 
        self.text15.insertItem(2,self.tr("第三笔款"))
        self.text15.insertItem(3,self.tr("第四笔款"))
        self.text15.insertItem(4,self.tr("第五笔款"))
        self.text15.insertItem(5,self.tr("第六笔款"))
        self.text15.insertItem(6,self.tr("质保金"))   
        self.text15.insertItem(7,self.tr("······"))    

        mainLayout.addWidget(self.text15,2,4)
        mainLayout.addWidget(label16,3,3)
        self.text16 = QLineEdit(self)
        mainLayout.addWidget(self.text16,3,4)
        mainLayout.addWidget(label17,4,3)
        self.text17 = QComboBox()

        self.text17.insertItem(0,self.tr("银承"))
        self.text17.insertItem(1,self.tr("商承"))
        self.text17.insertItem(2,self.tr("电汇"))

        mainLayout.addWidget(self.text17,4,4)
        mainLayout.addWidget(label18,5,3)
        self.text18 = QLineEdit(self)
        mainLayout.addWidget(self.text18,5,4)
        mainLayout.addWidget(label19,6,3)
        self.text19 = QLineEdit(self)
        mainLayout.addWidget(self.text19,6,4)
        mainLayout.addWidget(label20,7,3)
        self.text20 = QDateTimeEdit(self)
        self.text20.setDateTime(QDateTime.currentDateTime())
        self.text20.setDisplayFormat("yyyy/MM/dd")
        self.text20.setCalendarPopup(True)    
        mainLayout.addWidget(self.text20,7,4)
        mainLayout.addWidget(label21,8,3)
        self.text21 = QLineEdit(self)
        mainLayout.addWidget(self.text21,8,4)
        mainLayout.addWidget(label22,9,3)
        self.text22 = QDateTimeEdit(self)
        self.text22.setDateTime(QDateTime.currentDateTime())
        self.text22.setDisplayFormat("yyyy/MM/dd")
        self.text22.setCalendarPopup(True)
        mainLayout.addWidget(self.text22,9,4)
        mainLayout.addWidget(label23,10,3)
        self.text23 = QLineEdit(self)
        mainLayout.addWidget(self.text23,10,4)
        mainLayout.addWidget(label24,11,3)
        self.text24 = QLineEdit(self)  
        mainLayout.addWidget(self.text24,11,4)  
        mainLayout.addWidget(nextButton,14,1)
        self.setLayout(mainLayout)

    # def select24(self):
    #     global showlist
    #     name,ok = QInputDialog.getText(self,"实际收款方式","输入实际收款方式:",
    #                                    QLineEdit.Normal,self._24Lable.text())
    #     if ok and (len(name)!=0):
    #         self._24Lable.setText(name)
    #         showlist[23] = name
    # def selectStyle(self):
    #     list = ["外包","自研"]

    #     style,ok = QInputDialog.getItem(self,"项目性质","请选择项目性质：",list)
    #     if ok :
    #         self.styleLable.setText(style)

    # def selectNumber(self):
    #     number,ok = QInputDialog.getInt(self,"项目成员","请输入项目成员人数：",int(self.numberLable.text()),20,100,2)
    #     if ok :
    #         self.numberLable.setText(str(number))

    # def selectCost(self):
    #     cost,ok = QInputDialog.getDouble(self,"项目成本","请输入项目成员人数：",float(self.costLable.text()),100.00,500.00,2)
    #     if ok :
    #         self.costLable.setText(str(cost))

    # def selectIntroduction(self):
    #     introduction,ok = QInputDialog.getMultiLineText(self,"项目介绍","介绍：","服务外包第三方公司 \nPython project")
    #     if ok :
    #         self.introductionLable.setText(introduction)
 
    # def nextPage(self):
    #     self.nextbut = inputData2.InputDialog()
    #     self.nextbut.show()
    def nextPage(self):   
        # Connect to the database
        connection = pymysql.connect(host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db='temp',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        temp = connection.cursor()
        sql_ser = "select * from project where 项目编号 = '%s'"
        sql_insert = "insert into project(项目编号,合同名称,业主名称,业主性质,合同金额,合同性质,合同签订日,合同约定开工,合同约定日期,合同完工日,履约保证金,安全保证金,合同约定支付时间,合同约定退还时间,款项性质,收款条件,付款方式（银承、商承、电汇）,发票要求,收款其他条件（扣贴现息）,发票时间,发票金额,实际收款时间,实际收款金额,实际收款方式,所属部门,E,P,C) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        showlist[0] = self.text1.text()
        showlist[1] = self.text2.text()
        showlist[2] = self.text3.text()
        showlist[3] = self.text4.text()
        showlist[4] = self.text5.text()
        showlist[5] = self.text6.currentText()
        showlist[6] = self.text7.text()
        showlist[7] = self.text8.text()
        showlist[8] = self.text9.text()
        showlist[9] = self.text10.text()
        showlist[10] = self.text11.text()
        showlist[11] = self.text12.text()
        showlist[12] = self.text13.text()
        showlist[13] = self.text14.text()
        showlist[14] = self.text15.currentText()
        showlist[15] = self.text16.text()
        showlist[16] = self.text17.currentText()
        showlist[17] = self.text18.text()
        showlist[18] = self.text19.text()
        showlist[19] = self.text20.text()
        showlist[20] = self.text21.text()
        showlist[21] = self.text22.text()
        showlist[22] = self.text23.text()
        showlist[23] = self.text24.text()
        
        showlist[24] = self.text25.text()
        showlist[25] = self.text26.text()
        showlist[26] = self.text27.text()
        showlist[27] = self.text28.currentText()

        try:
            temp.execute(sql_ser%(showlist[0]))
            res_ser = temp.fetchall()
            if len(res_ser) == 0:
                temp.execute(sql_insert%(showlist[0],showlist[1],showlist[2],showlist[3],showlist[4],showlist[5],showlist[6],showlist[7],showlist[8],showlist[9],showlist[10],showlist[11],showlist[12],showlist[13],showlist[14],showlist[15],showlist[16],showlist[17],showlist[18],showlist[19],showlist[20],showlist[21],showlist[22],showlist[23],showlist[24],showlist[25],showlist[26],showlist[27]))
                connection.commit()
            else:
                QMessageBox.critical(self, 'Error', 'Already existed.')
                # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
        except Exception as e:
            raise e
        finally:
            connection.close()

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())

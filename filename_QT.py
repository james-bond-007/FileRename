import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide6.QtCore import QFile, QDir
sys.path.append("ui\\uic")
from ui_test import Ui_MainWindow
from config_handler import YamlHandler
import time

class QMainWindow(QMainWindow):
    def __init__(self) -> None:
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setWindowTitle("文件名处理器_YSP_V1.0")
        self.ui.setupUi(self)
        self.ui.log_data_Text.setMaximumBlockCount(17) #设置最大块数

        self.name = YamlHandler('./name.yaml').read_yaml()
        self.filepath = ""

        self.ui.dir_select_Button.clicked.connect(self.btn1Clicked)
        self.ui.modify_Button.clicked.connect(self.modify)
        self.ui.resume_Button.clicked.connect(self.resume)
        self.ui.rename_Button.clicked.connect(self.rename)
    
    def btn1Clicked(self):
        """
        1.打开一个文件路径  getExistingDirectory

        :return:
        """

        self.filePath = QFileDialog.getExistingDirectory()
        self.ui.init_dir_entry.setText(self.filePath)

        """
        2.打开一个文件 getOpenFileName
        该方法返回值 是一个元组，第一个元素是选择的文件路径，第二个元素是文件类型，
        如果你只想获取文件路径即可，可以采用下面的代码写法。
        如果用户点击了 选择框的 取消选择按钮，返回 空字符串。
        :return:
        """
        # filePath,_ = QFileDialog.getOpenFileName(
        #     self.centralWidget,  # 父窗口对象
        #     "选择你要上传的图片",  # 标题
        #     r"d:\\testsdk",  # 起始目录
        #     "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        # )
        # self.line1.setText(filePath)
        # print(filePath)

        """
        3.保存一个文件  getSaveFileName
        如果你想弹出文件选择框，选择路径和文件名，来 保存一个文件 ，
        可以使用 QFileDialog 静态方法 getSaveFileName ，比如
        """
        # filePath, _ = QFileDialog.getSaveFileName(
        #     self.centralWidget,  # 父窗口对象
        #     "保存文件",  # 标题
        #     r"d:\\testsdk",  # 起始目录
        #     "json类型 (*.json)"  # 选择类型过滤项，过滤内容在括号中
        # )
        # f = open(filePath, 'w', encoding='utf8')
        # f.write('aaa')
        # f.close()
        # self.line1.setText(filePath)
        # print(filePath)

        """
        4.如果要选择多个文件，使用 getOpenFileNames 静态方法
        上例中 filePaths 对应的返回值是一个列表，里面包含了选择的文件。
        如果用户点击了 选择框的 取消选择按钮，返回 空列表。
        
        """
        # filePaths, _ = QFileDialog.getOpenFileNames(
        #     self.centralWidget,  # 父窗口对象
        #     "选择你要上传的图片",  # 标题
        #     r"d:\\testsdk",  # 起始目录
        #     "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        # )
        # print(filePaths)

    # 功能函数 
    def pre_fix_suf(self):
        prefix=self.ui.init_prefix_Text.text().replace('\n',"")
        if prefix != "":
            prefix+='_'
        suffix=self.ui.init_suffix_Text.text().replace('\n',"")
        if suffix != "":
            suffix='_' + suffix
        return prefix, suffix

    def modify(self): 
        prefix, suffix = self.pre_fix_suf()
        dir=self.filePath
        if dir and (prefix or suffix): 
            try: 
                for filename in os.listdir(dir): 
                    tmp=os.path.join(dir,filename)
                    fname,fextension = os.path.splitext(filename)
                    os.replace(tmp,r"{}{}{}{}{}{}".format(dir,os.sep,prefix,fname,suffix,fextension)) 
                self.ui.result_data_Text.clear()
                i=1.0 
                for x in os.listdir(dir): 
                    # x=x+'\n' 
                    self.ui.result_data_Text.appendPlainText(x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except Exception as e:
                print(e)
                self.ui.result_data_Text.clear()
                self.ui.result_data_Text.appendPlainText("修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 
        
    def resume(self): 
        prefix, suffix = self.pre_fix_suf()
        dir=self.filePath
        if dir and (prefix or suffix): 
            try: 
                for filename in os.listdir(dir): 
                    tmp=os.path.join(dir,filename)
                    fname,fextension = os.path.splitext(filename)
                    if prefix == fname[:len(prefix)]:
                        fname = fname[len(prefix):]
                    if suffix == fname[-len(suffix):]:
                        fname = fname[:-len(suffix)]
                    os.replace(tmp,r"{}{}{}{}".format(dir,os.sep,fname,fextension)) 
                self.ui.result_data_Text.clear() 
                i=1.0 
                for x in os.listdir(dir): 
                    # x=x+'\n' 
                    self.ui.result_data_Text.appendPlainText(x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except Exception as e:
                print(e)
                self.ui.result_data_Text.clear() 
                self.ui.result_data_Text.appendPlainText("修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 
    
    def rename(self): 
        prefix, suffix = self.pre_fix_suf()
        dir=self.filePath
        if dir and (prefix or suffix): 
            try: 
                i=1
                for filename in os.listdir(dir): 
                    tmp=os.path.join(dir,filename)
                    fname,fextension = os.path.splitext(filename)
                    is_find = False
                    for name in self.name['title_name']:
                        if fname.find(name) > -1:
                            is_find = True
                            break
                    if is_find:
                        fullname=r"{}{}{}".format(prefix,name,suffix)
                    else:
                        fullname=r"{}{}{}".format(prefix,suffix,r"{:03d}".format(i))
                    os.replace(tmp,r"{}{}{}{}".format(dir,os.sep,fullname,fextension)) 
                    i=i+1 
                self.ui.result_data_Text.clear()
                i=1.0 
                for x in os.listdir(dir): 
                    # x=x+'\n' 
                    self.ui.result_data_Text.appendPlainText(x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except Exception as e:
                print(e)
                self.ui.result_data_Text.clear()
                self.ui.result_data_Text.appendPlainText("修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 

    #获取当前时间 
    def get_current_time(self): 
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
        return current_time 

    #日志动态打印 
    def write_log_to_Text(self,logmsg): 
        
        current_time = self.get_current_time() 
        logmsg_in = str(current_time) +" " + str(logmsg) #+ "\n" #换行 
        self.ui.log_data_Text.appendPlainText(logmsg_in) 
        # if LOG_LINE_NUM <= 7: 
        #     self.ui.log_data_Text.appendPlainText(logmsg_in) 
        #     LOG_LINE_NUM = LOG_LINE_NUM + 1 
        # else: 
        #     self.ui.log_data_Text.clear()
        #     self.ui.log_data_Text.appendPlainText(logmsg_in) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())

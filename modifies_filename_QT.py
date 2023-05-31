import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, QDir
sys.path.append("ui\\uic")
from ui_test import Ui_MainWindow
from config_handler import YamlHandler
import time

class MyMainWindow(QMainWindow):
    """
    重命名器的主窗口类.
    """
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowTitle("文件名处理器_YSP_V1.0")
        self.ui.setupUi(self)
        self.ui.log_data_Text.setMaximumBlockCount(17) # 设置日志显示的最大行数

        self.name = YamlHandler('./name.yaml').read_yaml()
        self.filePath = ""

        # 绑定按钮点击事件
        self.ui.dir_select_Button.clicked.connect(self.select_dir)
        self.ui.modify_Button.clicked.connect(lambda: self.process_files('add'))
        self.ui.resume_Button.clicked.connect(lambda: self.process_files('remove'))
        self.ui.rename_Button.clicked.connect(lambda: self.process_files('rename'))

    def select_dir(self):
        """
        打开一个目录选择对话框.
        """
        self.filePath = QFileDialog.getExistingDirectory()
        self.ui.init_dir_entry.setText(self.filePath)

    def process_files(self, mode):
        """
        处理文件名.
        """
        prefix = self.ui.init_prefix_Text.text().strip()
        if prefix != "":
            prefix+='_'
        suffix = self.ui.init_suffix_Text.text().strip()
        if suffix != "":
            suffix='_' + suffix
        
        if not (self.filePath and (prefix or suffix)):
            self.write_log_to_Text("请同时输入路径和待添加/删除/修改内容")
            return

        count = 0
        for filename in os.listdir(self.filePath):
            tmp = os.path.join(self.filePath, filename)
            fname, f_extension = os.path.splitext(filename)

            if mode == 'add':
                # 在文件名前添加前缀和后缀
                new_fname = f"{prefix}{fname}{suffix}"
            elif mode == 'remove':
                # 去除文件名中的前缀和后缀
                new_fname = fname
                if prefix and fname.startswith(prefix):
                    new_fname = new_fname[len(prefix):]
                if suffix and fname.endswith(suffix):
                    new_fname = new_fname[:-len(suffix)]
            elif mode == 'rename':
                # 根据文件名中是否包含指定字符串，对文件进行重命名.
                is_find = any(name in fname for name in self.name['title_name'])
                name_to_replace = next((name for name in self.name['title_name'] if name in fname), None)
                new_fname = f"{prefix}{name_to_replace}{suffix}" if is_find and name_to_replace else f"{prefix}{suffix}{count:03d}"
            else:
                return
            
            try:
                os.replace(tmp, os.path.join(self.filePath, new_fname+f_extension))
                count += 1
            except Exception as e:
                print(e)
                self.ui.result_data_Text.clear()
                self.ui.result_data_Text.appendPlainText("修改失败")

        # 显示修改结果
        self.ui.result_data_Text.clear()
        for x in os.listdir(self.filePath):
            self.ui.result_data_Text.appendPlainText(x) 
        self.write_log_to_Text(f"{count}个文件名操作成功")

    def get_current_time(self):
        """
        获取当前时间字符串.
        """
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def write_log_to_Text(self, log_msg):
        """
        动态打印日志信息.
        """
        log_message = f"{self.get_current_time()} {log_msg}"
        self.ui.log_data_Text.appendPlainText(log_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
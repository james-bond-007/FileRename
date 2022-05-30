# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import hashlib
# import sys
import time
import os
from tkinter import *
from tkinter import filedialog

LOG_LINE_NUM = 0


class MyGUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("文件名处理器_LKF_V1.1")  # 窗口名
        # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        # self.init_window_name.geometry('320x160+10+10')
        self.init_window_name.geometry('868x681+10+10')
        # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name["bg"] = "pink"
        # 虚化，值越小虚化程度越高
        # self.init_window_name.attributes("-alpha",0.9)

        # 标签
        self.init_dir_label = Label(self.init_window_name, text="请输入文件路径")
        self.init_dir_label.grid(row=0, column=0)

        self.init_data_label = Label(self.init_window_name, text="需要添加内容")
        self.init_data_label.grid(row=4, column=0)

        self.result_data_label = Label(self.init_window_name, text="修改后结果")
        self.result_data_label.grid(row=0, column=12)

        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)

        self.log_label = Label(self.init_window_name, text="By 娄阔峰 2022-05-29")
        self.log_label.grid(row=14, column=8)

        # 文本框
        self.init_dir_Text = Text(self.init_window_name, width=60, height=5)  # 文件路径录入
        self.init_dir_Text.grid(row=1, column=0, rowspan=1, columnspan=10)

        self.init_data_Text = Text(self.init_window_name, width=60, height=5)  # 原始数据录入框
        self.init_data_Text.grid(row=5, column=0, rowspan=1, columnspan=10)

        self.result_data_Text = Text(self.init_window_name, width=60, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="打开文件夹", bg="lightblue", width=10,
                                              command=self.select_fold)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=2, column=6)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="加前缀", bg="lightblue", width=10,
                                              command=self.qianzhui)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=6, column=4)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="加后缀", bg="lightblue", width=10,
                                              command=self.houzhui)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=6, column=5)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="重新命名", bg="lightblue", width=10,
                                              command=self.chongmingming)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=6, column=6)

    # 功能函数
    def select_fold(self):
        folder_path = filedialog.askdirectory(initialdir="/Users/loukuofeng/Downloads")  # 获得选择好的文件夹
        # Filepath = filedialog.askopenfilename()  # 获得选择好的文件
        print(folder_path)
        self.init_dir_Text.insert('0.0', folder_path)

    def fresh_result_data_text(self, file_dir):
        i = 1.0
        filenames = self.clear_hide_file(file_dir)
        for x in filenames:
            print(x)
            x = x + '\n'
            self.result_data_Text.insert(i, x)
            i = i + 1
        self.write_log_to_text("修改成功")

    def clear_hide_file(self, file_dir):
        filenames = []
        for filename in os.listdir(file_dir):
            if not filename.startswith('.'):
                filenames.append(filename)
        filenames.sort()
        return filenames

    def qianzhui(self):
        input1 = self.init_data_Text.get(1.0, END).replace('\n', "")
        file_dir = self.init_dir_Text.get(1.0, END).replace('\\', r'//').replace('\n', "")
        if file_dir and input1:
            try:
                filenames = self.clear_hide_file(file_dir)
                for filename in filenames:
                    tmp = (os.path.join(file_dir, filename)).replace('\\', '//')
                    os.replace(tmp, r"{}//{}".format(file_dir, input1 + filename))
                # self.result_data_Text.delete(1.0, END)
                self.fresh_result_data_text(file_dir)
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "修改失败")
        else:
            self.write_log_to_text("请同时输入路径和待添加内容")

    def houzhui(self):
        input1 = self.init_data_Text.get(1.0, END).replace('\n', "")
        file_dir = self.init_dir_Text.get(1.0, END).replace('\\', r'//').replace('\n', "")
        if file_dir and input1:
            try:
                filenames = self.clear_hide_file(file_dir)
                for filename in filenames:
                    tmp = (os.path.join(file_dir, filename)).replace('\\', '//')
                    hou = tmp.split('.')
                    os.replace(tmp, r"{}{}.{}".format(hou[0], input1, hou[1]))
                self.fresh_result_data_text(file_dir)
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "修改失败")
        else:
            self.write_log_to_text("请同时输入路径和待添加内容")

    def chongmingming(self):
        input1 = self.init_data_Text.get(1.0, END).replace('\n', "")
        file_dir = self.init_dir_Text.get(1.0, END).replace('\\', r'//').replace('\n', "")
        if file_dir:  # and input1:
            try:
                filenames = self.clear_hide_file(file_dir)
                i = 1
                for filename in filenames:
                    # print(filename)
                    tmp = (os.path.join(file_dir, filename)).replace('\\', '//')
                    hou = tmp.split('.')
                    os.replace(tmp, r"{}{}.{}".format(file_dir + '//' + input1, str(i).rjust(3, "0"), hou[1]))
                    i = i + 1
                self.fresh_result_data_text(file_dir)
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "修改失败")
        else:
            self.write_log_to_text("请同时输入路径和待添加内容")

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)


def start():
    init_window = Tk()  # 实例化出一个父窗口
    lkf_portal = MyGUI(init_window)
    # 设置根窗口默认属性
    lkf_portal.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    start()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

#!/usr/bin/env python 
# # -*- coding: utf-8 -*- 
import hashlib 
import time,os,sys 
from tkinter import * 
from tkinter import filedialog
from config_handler import YamlHandler

LOG_LINE_NUM = 0 

class MY_GUI(): 
    def __init__(self,init_window_name): 
        self.init_window_name = init_window_name 
        self.name=YamlHandler('./name.yaml').read_yaml()
    
    #设置窗口 
    def set_init_window(self): 
        self.path = StringVar()
        self.path.set(os.path.abspath("."))

        self.init_window_name.title("文件名处理器_YSP_V1.0") #窗口名 
        # self.init_window_name.geometry('320x160+10+10') #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置 
        self.init_window_name.geometry('868x681+10+10') 
        self.init_window_name["bg"] = "pink" #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887 
        # self.init_window_name.attributes("-alpha",0.9) #虚化，值越小虚化程度越高 
        
        # fm1
        # self.fm1=Frame(self.init_window_name)
        # self.titleLabel=Label(self.fm1,text='名称名修改器 1.0')
        # self.titleLabel.pack()
        # self.fm1.pack(side= TOP)

        self.fm0=Frame(self.init_window_name)
        self.fm0.pack()
        # fm2
        self.fm2=Frame(self.fm0)
        self.fm2.grid(row=1, column=0) 
        # self.fm2.pack(side= TOP)
        # fm3
        self.fm3=Frame(self.fm0)
        self.fm3.grid(row=1, column=2) 
        # 标签 
        self.init_dir_label = Label(self.fm2, text="请输入文件路径") 
        self.init_dir_label.grid(row=0, column=0) 

        self.init_data_label = Label(self.fm2, text="请输入前缀") 
        self.init_data_label.grid(row=2, column=0) 

        self.init_data_label = Label(self.fm2, text="请输入后缀") 
        self.init_data_label.grid(row=4, column=0) 

        self.result_data_label = Label(self.fm3, text="修改后结果") 
        self.result_data_label.grid(row=0, column=12) 

        self.log_label = Label(self.fm2, text="日志") 
        self.log_label.grid(row=12, column=0) 
        # 文本框 
        #文件路径录入
        # self.path = StringVar()
        # self.path.set(os.path.abspath("."))
        self.init_dir_entry = Entry(self.fm2,textvariable=self.path,state="normal",width=60)
        self.init_dir_entry.grid(row=1,column=0,rowspan=1,columnspan=10)

        self.str_trans_to_md5_button = Button(self.fm2, text="路径选择", bg="lightblue", width=10,command=self.select_path) # 调用内部方法 加()为直接调用 
        self.str_trans_to_md5_button.grid(row=0, column=4) 
        # self.init_dir_Text = Text(self.fm2, width=60, height=5, relief=RAISED)  
        # self.init_dir_Text.grid(row=1, column=0, rowspan=1, columnspan=10) 
        #前缀录入框
        self.init_prefix_Text = Text(self.fm2, width=60, height=5)  
        self.init_prefix_Text.grid(row=3, column=0, rowspan=1, columnspan=10) 
        #后缀录入框
        self.init_suffix_Text = Text(self.fm2, width=60, height=5)  
        self.init_suffix_Text.grid(row=5, column=0, rowspan=1, columnspan=10) 
        #处理结果展示
        self.result_data_Text = Text(self.fm3, width=60, height=45)  
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10) 
        # 日志框 
        self.log_data_Text = Text(self.fm2, width=60, height=20) 
        self.log_data_Text.grid(row=13, column=0, columnspan=10) 
        # 按钮 
        self.str_trans_to_md5_button = Button(self.fm2, text="加前后缀", bg="lightblue", width=10,command=self.modify) # 调用内部方法 加()为直接调用 
        self.str_trans_to_md5_button.grid(row=6, column=4) 

        self.str_trans_to_md5_button = Button(self.fm2, text="删前后缀", bg="lightblue", width=10,command=self.resume) # 调用内部方法 加()为直接调用 
        self.str_trans_to_md5_button.grid(row=6, column=5) 
        
        self.str_trans_to_md5_button = Button(self.fm2, text="重新命名", bg="lightblue", width=10,command=self.chongmingming) # 调用内部方法 加()为直接调用 
        self.str_trans_to_md5_button.grid(row=6, column=6) 
    # 功能函数 
    def select_path(self):
        path_ = filedialog.askdirectory(title="Dialog box") # 使用askdirectory()方法返回文件夹的路径
        if path_ == "":
            print(self.path.get())
            # os.path.get() # 当打开文件路径选择框后点击“取消”输入框会清空路径，所以使用get()方法再获取一次路径
            
            # self.path.set(self.path)
            # print(self.path.get())
        else:
            # path_ = path_.replace("/","\\") # 实际在代码中执行的路径为“/”所以替换一下
            self.path.set(path_)
            print(self.path.get())
            # self.init_dir_entry.delete(0,END)
            # self.init_dir_entry.insert(0,path_)

    def modify(self): 
        prefix=self.init_prefix_Text.get(1.0,END).replace('\n',"")+'_'
        suffix='_'+self.init_suffix_Text.get(1.0,END).replace('\n',"")
        dir=self.path.get()
        if dir and (prefix or suffix): 
            try: 
                for filename in os.listdir(dir): 
                    tmp=os.path.join(dir,filename)
                    fname,fextension = os.path.splitext(filename)
                    os.replace(tmp,r"{}{}{}{}{}{}".format(dir,os.sep,prefix,fname,suffix,fextension)) 
                self.result_data_Text.delete(1.0,END) 
                i=1.0 
                for x in os.listdir(dir): 
                    x=x+'\n' 
                    self.result_data_Text.insert(i,x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except: 
                self.result_data_Text.delete(1.0,END) 
                self.result_data_Text.insert(1.0,"修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 
        
    def resume(self): 
        prefix=self.init_prefix_Text.get(1.0,END).replace('\n',"")+'_'
        suffix='_'+self.init_suffix_Text.get(1.0,END).replace('\n',"")
        dir=self.path.get()
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
                self.result_data_Text.delete(1.0,END) 
                i=1.0 
                for x in os.listdir(dir): 
                    x=x+'\n' 
                    self.result_data_Text.insert(i,x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except: 
                self.result_data_Text.delete(1.0,END) 
                self.result_data_Text.insert(1.0,"修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 
    
    def chongmingming(self): 
        prefix=self.init_prefix_Text.get(1.0,END).replace('\n',"")+'_'
        suffix='_'+self.init_suffix_Text.get(1.0,END).replace('\n',"")
        dir=self.path.get()
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
                self.result_data_Text.delete(1.0,END) 
                i=1.0 
                for x in os.listdir(dir): 
                    x=x+'\n' 
                    self.result_data_Text.insert(i,x) 
                    i=i+1 
                self.write_log_to_Text("{}个文件名修改成功".format(int(i))) 
            except: 
                self.result_data_Text.delete(1.0,END) 
                self.result_data_Text.insert(1.0,"修改失败") 
        else: 
            self.write_log_to_Text("请同时输入路径和待添加内容") 

    #获取当前时间 
    def get_current_time(self): 
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
        return current_time 

    #日志动态打印 
    def write_log_to_Text(self,logmsg): 
        global LOG_LINE_NUM 
        current_time = self.get_current_time() 
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n" #换行 
        if LOG_LINE_NUM <= 7: 
            self.log_data_Text.insert(END, logmsg_in) 
            LOG_LINE_NUM = LOG_LINE_NUM + 1 
        else: 
            self.log_data_Text.delete(1.0,2.0) 
            self.log_data_Text.insert(END, logmsg_in) 
def Start(): 
    init_window = Tk() #实例化出一个父窗口 
    path = StringVar()
    ZMJ_PORTAL = MY_GUI(init_window) 
    # 设置根窗口默认属性 
    ZMJ_PORTAL.set_init_window() 
    init_window.mainloop() #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示 
Start()
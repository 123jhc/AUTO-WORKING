import numpy as np
import pandas as pd
import os
import easygui

path = easygui.fileopenbox(msg="导入花名册")
# 花名册姓名数据，其中usecols为第i列减1
print(path)
dataframe = pd.read_excel(r"{0}".format(path))
colnames = dataframe.columns[:]

choice = easygui.multchoicebox(msg = "请选择你需要的列：",choices = colnames)
student_data = dataframe.loc[:][choice]

homework_path = easygui.diropenbox(msg = "选择作业所在文件夹的位置")
homework_yes = ''
homework_no = ''

for file_name in os.listdir(homework_path):
    for student_name in student_data.loc[:]['姓名']:
        if student_name in file_name:
            homework_yes += student_name + '\n'
            break

for student_name in student_data.loc[:]['姓名']:
    if student_name not in homework_yes:
        homework_no += student_name + '\n'

easygui.msgbox("未完成作业名单如下：\n {0}________________________\n已完成名单如下{1}".format(homework_no, homework_yes))

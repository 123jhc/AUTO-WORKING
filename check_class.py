import numpy as np
import pandas as pd
import os

# 指定花名册路径
path = r"H:\学委\AUTO\数智学生花名册.xls"
# 花名册姓名数据，其中usecols为第i列减1
student_data = pd.read_excel(io=path, usecols=[1])
# 首先将pandas读取的数据转化为array
stdudent_list = np.array(student_data.stack())
# 然后转化为list形式,student_list为所有学生姓名列表
stdudent_list = stdudent_list.tolist() 
# print(len(stdudent_list))

#file_list为某文件夹下的所有文件命名列表
file_list = []
#指定某文件夹路径
path = r'H:\学委\商务智能\期中'
#讲该文件夹下的所有文件名添加到file_list列表下
for file_name in os.listdir(path):
#     print(file_name)
    file_list.append(file_name)


#index_name 代表每一个学生状况
index_name = list(range(len(stdudent_list)))
for i in range(len(stdudent_list)):
    for j in range(len(file_list)):
        if stdudent_list[i] in file_list[j]:
            index_name[i] = True
            break
        else:
            index_name[i] = False

#保存每一个student完成信息
result_list = []
no_list = []
no_count = 0
for i in range(len(stdudent_list)):
    item = stdudent_list[i] + ', 作业完成情况：' + str(index_name[i])
    # print(item)
    result_list.append(item)
    if index_name[i] is False:
        item = stdudent_list[i]
        no_list.append(item)
        no_count += 1

#结果保存路径
path = r'H:\result.txt'
f = open(path,'w')

for i in range(len(result_list)):
    f.write(result_list[i] + '\n')

f.write('-----------------' + '\n')
f.write("没有完成的学生名单如下：" + '\n')
for i in range(len(no_list)):
    f.write(no_list[i] + '\n')

f.write('总共未完成的人数：' + str(no_count))

f.close()

print("Done")
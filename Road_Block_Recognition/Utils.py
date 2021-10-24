import os
import cv2

def Get_Img_List_From_File(filename):
    img_list = []
    for file in [filename]:
        for img in os.listdir(file):
            img_list.append(cv2.imread(file+'/' +img))
    return img_list

def Build_List_Negative(filename='negative', creat_filename='negative'):
    for file in [filename]:
        for img in os.listdir(file):
            line = file + '/' + img + '\n'
            with open(creat_filename + '.txt', 'a') as f:
                f.write(line)

def Rename_Img(filename='positive', suffix='-img'):
    for file in [filename]:
        cnt = 1
        for img in os.listdir(file):
            add_cnt_label = '(' + str(cnt) + ')'
            os.rename(file + "/" + img, filename + "/" + 'reset' + add_cnt_label + '.jpg')
            cnt += 1
        cnt = 1
        for img in os.listdir(file):
            add_cnt_label = '(' + str(cnt) + ')'
            os.rename(file + "/" + img, file + "/" + str(filename) + suffix + add_cnt_label + '.jpg')
            cnt += 1
        print(str(filename) + ' img process is ok')

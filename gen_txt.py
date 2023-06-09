import os
def generate(dir, label):
    files = os.listdir(dir) #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    files.sort()  #对文件或文件夹进行排序
    print('input :', dir)
    listText = open('G:\github\\repository\Deep-Learning\Pytorch-Seg\lesson-4\\new1.txt', 'a+')
    for file in files:
        fileType = os.path.split(file) #os.path.split（）返回文件的路径和文件名，【0】为路径，【1】为文件名
        if fileType[1] == '.txt':  #若文件名的后缀为txt,则继续遍历循环，否则退出循环
            continue
        name = '垃圾图片库' +'/' + folder+ '/' +file + '\t' + str(int(label)) + '\n'
        listText.write(name)  #在创建的txt文件中写入name
    listText.close() #关闭txt文件


outer_path = 'G:\github\\repository\Deep-Learning\Pytorch-Seg\lesson-4\垃圾图片库'  # 这里是你的图片路径

if __name__ == '__main__':  #主函数
    i = 0
    folderlist = os.listdir(outer_path)# 列举文件夹
    for folder in folderlist:  #遍历文件夹中的文件夹(若engagement文件夹中存在txt或py文件，则后面会报错）
        generate(os.path.join(outer_path, folder), i)#调用generate函数，函数中的参数为：（图片路径+文件夹名，标签号）
        i += 1

# -*- coding:utf-8 -*-
import random
import os,sys


def workable_file_name(file_name,i=1):
    """
    重命名文件，避免同名
    """
    if os.path.exists(file_name):
        if file_name.find('.')<0:
            new_file_name = file_name + '_%s' % i
        else:#如果多余两个. 可能得到的不是预期
            new_file_name = file_name.replace('.','_%s.'%i)
        i = i + 1
        return workable_file_name(new_file_name, i)
    else:
        return file_name

def rename_all(cwd,remove_word='副本'):
    """
    把文件名特定字符串去掉， 比如 "副本"
    """
    #print('cwd=',cwd)
    get_dir = os.listdir(cwd)  #遍历当前目录，获取文件列表
    #print('get_dir=',get_dir)
    for i in get_dir:          
        sub_dir = os.path.join(cwd,i)  # 把第一步获取的文件加入路径
        if os.path.isdir(sub_dir):     #如果当前仍然是文件夹，递归调用
            rename_all(sub_dir,remove_word)
        else:
            if remove_word in i:
                new_file_name = os.path.join(cwd,i).replace(remove_word,'')
                new_file_name = workable_file_name(new_file_name, i=1)
                os.rename(os.path.join(cwd,i),new_file_name)  #用新名字取代旧名字
            else:
                pass
    return

if __name__ == "__main__":
    #chgdir = 'C:/test/DD帐号有水印/'#'D:/test/'
    chgdir = 'C:/test/'
    #chgdir = 'C:/test/AUPA095GD-US水印/'
    remove_keyword = ' 副本'
    if len(sys.argv)>=2:
        if sys.argv[1] and isinstance(sys.argv[1], str):
            chgdir = sys.argv[1]  #start date string 
        if len(sys.argv)>=3:
            if sys.argv[2] and isinstance(sys.argv[2], str):
                remove_keyword = sys.argv[2]  #start date string
        print('程序将批量重命名目录  %s 下所有递归文件，把文件名中%s字样去掉' % (chgdir,remove_keyword))
        if os.path.exists(chgdir) and os.path.isdir(chgdir):
            rename_all(chgdir, remove_keyword)
            print('成功完成批量重命名')
        else:
            print('错误： 输入的文件夹不存在，请确认已经建立文件夹 %s' % chgdir)
    else:
        #默认无参数时
        if os.path.exists(chgdir) and os.path.isdir(chgdir):
            print('本程序将批量重命名默认目录C:/test/下所有递归文件，把文件名中" 副本"字样去掉')
            rename_all(chgdir, remove_keyword)
            remove_keyword1 = '副本'
            rename_all(chgdir, remove_keyword1)
            remove_keyword1 = '-副本'
            rename_all(chgdir, remove_keyword1)
            remove_keyword1 = '- 副本'
            rename_all(chgdir, remove_keyword1)
            print('成功完成批量重命名')
        else:
            print('错误： 不存在默认文件夹：C:/test/；请创建该文件夹并把需要批处理的文件放入改文件夹！')
    
    
        
    
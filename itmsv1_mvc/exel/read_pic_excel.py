import sys
import os
import xlrd
import zipfile
import base64


class ExcelImgRead(object):

    def change_file_name(self, file_path, old_name, new_type = '.zip'):
        """
        修改指定目录下的文件类型名
        :param file_path:
        :param old:
        :param new:
        :return:
        """
        old_path = os.path.join(file_path, old_name)
        if not os.path.exists(old_path):
            print ('No such File! :%s' % old_path)
            return False
        new_name = str(old_name.split('.')[0]) + new_type
        new_path = os.path.join(file_path, new_name)
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)

    def unzip_file(self, file_path):
        """
        解压缩指定目录下的Zip文件
        :param file_path:
        :return:
        """
        file_list = os.listdir(file_path)
        for file_name in file_list:
            if file_name.split('.')[1] == 'zip':
                file_zip = zipfile.ZipFile(os.path.join(file_path, file_name), 'r')
                zipdir = file_name.split('.')[0]
                for files in file_zip.namelist():
                    file_zip.extract(files, os.path.join(file_path, zipdir))  # 解压到指定文件目录
                file_zip.close()

    def unzip_excel_pic2base64(self, file_path, file_name):
        """
        解压缩的excel目录下获取图片并转成base64编码
        :param file_path:
        :param file_name:
        :return:
        """
        pic_dir = 'xl\media'
        pic_path = os.path.join(file_path, file_name.split('.')[0], pic_dir)
        if not os.path.exists(pic_path):
            print ('No such directory!:%s' % pic_path)
            return ''
        file_list = os.listdir(pic_path)
        try:
            for files in file_list:
                if files.split('.')[1] == 'png':
                    path = os.path.join(pic_path, files)
                    return staionReport().img2base64(path) # 转成base64方法
        except:
            print ('unzip_excel_pic2base64 Error!')
            return ''

def excel_pic_read(file_path, file_name):
    """
        读取excel中的图片base64
        :param file_path:
        :param file_name:
        :return:图片的base64编码字符串
    """
    ExcelImgRead().change_file_name(file_path, file_name)
    ExcelImgRead().unzip_file(file_path)
    return ExcelImgRead().unzip_excel_pic2base64(file_path, file_name)
if __name__ == '__main__':
    file_path='../pict.xlsx'
    file_name='.pic.png'
    excel_pic_read(file_path, file_name)
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''
操作文件
'''


class BaseFile(object):
    def __init__(self):
        pass

    @staticmethod
    def check_file(path):
        if not os.path.isfile(path):
            # sys.exit()
            return False
        else:
            return True

    @staticmethod
    def mk_file(path):
        with open(path, 'w', encoding="utf-8"):
            print("创建文件成功")
            pass

    @staticmethod
    def write(path, line):
        time.sleep(1)
        with open(path, 'a') as fileHandle:
            fileHandle.write(line + "\n")

    @staticmethod
    def read(path):
        result = []
        with open(path, 'r', encoding="utf-8") as fileHandle:
            file_list = fileHandle.readlines()
            for i in file_list:
                temp = [i.replace("\t", ",").strip("\n")]
                result.append(temp)
        return result

    def remove_file(self, path):
        if self.check_file(path):
            os.remove(path)


if __name__ == '__main__':
    pass

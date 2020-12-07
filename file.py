import time


TYPE_FILE = 0
TYPE_DICTIONARY = 1


class FCB:
    def __init__(self):
        self.filename = ""
        self.type = TYPE_FILE
        self.size = 0
        self.permission = 7
        self.use_count = 0
        self.create_time = int(time.time())
        self.last_modify_time = int(time.time())
        self.file_list = None


class FileItem:  # 目录索引项,索引可能是文件的索引，也可能是目录的索引
    def __init__(self):
        self.tag = TYPE_FILE  # 标记位 0 => 文件 1 => 目录
        self.file_name = ""  # 文件名
        self.fcb: FCB = None  # FCB类型列表
        self.dic = []  # FileItem类型


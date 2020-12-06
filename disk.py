import config
import file
import user
import command


# 存储节点
class DiskBlockNode:
    def __init__(self):
        self.id = 0
        self.content = ""
        self.size = config.BLOCK_SIZE
        self.next = None  # 下一个磁盘块


class UserOpenFile:
    def __init__(self):
        self.uid = 0
        self.filename = ""
        self.mode = 0
        self.rw_location = 0
        self.sid = 0


class SystemOpenFile:
    def __init__(self):
        self.sid = 0
        self.filename = ""
        self.dic_item = None
        self.open_count = 0


disk_block_link = None   # 空闲盘块链
root = file.FileItem()              # 根目录结点
user_table = user.userTables        # 用户表

user_open_file_table = []
system_open_file_table = []
current_node = root
current_path = "/"

# 新建disk_block_link
block_num = config.DISK_SIZE / config.BLOCK_SIZE
now_node = None
for i in range (0,int(block_num)):
    if disk_block_link == None:
        disk_block_link = DiskBlockNode()
        now_node = disk_block_link
    else:
        now_node.next = DiskBlockNode()
        now_node.next.id = now_node.id + 1
        now_node = now_node.next


def list_block_info(args):
    now_node = disk_block_link
    while now_node.next is not None:
        print(f"{now_node.id} content:{now_node.content} size:{now_node.size}")
        now_node = now_node.next


        #if root.tag == file.TYPE_FILE:
        #    print("! it is a file item")
        #    return None
def search_dic_item(uri, now1=root):
    now = now1
    dics = uri.split("/")
    for i in dics:
        if i == "":
            continue
        flag = False
        for j in now.dic:
            if i == j.filename:
                now = j
                flag = True
        if not flag:
            print(f"cannot find {i}")
            return None
    print(dics)
    return now

def dir(args):
    res = None
    if len(args) == 1:
        res = find_dic_item("/")
    else:
        res = find_dic_item(args[1])
    if res is None:
        return False
    for i in res.dic:
        print(f" | {i.filename}")
    for i in res.fcb:
        print(f" + {i.filename}")
    return True

def find_dic_item(uri):
    dics = uri.split("/")
    now = root
    for i in dics:
        if i == "":
            continue
        flag = False
        for j in now.dic:
            if i == j.filename:
                now = j
                flag = True
        if not flag:
            print(f"cannot find {i}")
            return None
    print(dics)
    return now


def cd(args):
    global current_node
    res = None
    if args[1][0] == '/': #绝对目录
        res = search_dic_item(args[1])
    else:
        res = search_dic_item(args[1], now1=current_node)
    if res is None:
        print(" cannot find dic")
        return False
    current_node = res
    global current_path
    if args[1][0] == '/': #绝对目录
        current_path = args[1]
    else:
        current_path = current_path + "/" + args[1]
    return True




command.register_command("listDisk", list_block_info, "/listDisk")
command.register_command("dir", dir, "/dir [dictionary]")
command.register_command("cd", cd, "/cd <path>")
command.register_command("create", dir, "/create <filename> <content>")


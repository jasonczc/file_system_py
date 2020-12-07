import config
import file
import user
import command
import time


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


system_open_file_table: SystemOpenFile = None
disk_block_link = None  # 空闲盘块链
root = file.FileItem()  # 根目录结点
user_table = user.userTable  # 用户表

user_open_file_table = []
system_open_file_table = []
current_node = root
current_path = "/"

# 新建disk_block_link
block_num = config.DISK_SIZE / config.BLOCK_SIZE
# 空闲磁盘链表
empty_node = None
for i in range(0, int(block_num)):
    if disk_block_link == None:
        disk_block_link = DiskBlockNode()
        empty_node = disk_block_link
    else:
        empty_node.next = DiskBlockNode()
        empty_node.next.id = empty_node.id + 1
        empty_node = empty_node.next


def get_empty_node_size():
    length = 0
    now = empty_node
    while now is not None:
        now = now.next
        length += 1
    return length


def list_block_info(args):
    now_node = disk_block_link
    while now_node.next is not None:
        print(f"{now_node.id} content:{now_node.content} size:{now_node.size}")
        now_node = now_node.next

        # if root.tag == file.TYPE_FILE:
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
    return now


def dir(args):
    res = None
    if len(args) == 1:
        res = find_dic_item("/")
    else:
        res = find_dic_item(args[1])
    if res is None:
        return False
    print(f"there is {len(res.dic)} objects")
    name_dic = {
        file.TYPE_DICTIONARY: 'dictionary',
        file.TYPE_FILE: 'file'
    }
    for i in res.dic:
        print(f"{name_dic[i.tag]} {i.file_name}")
    return True


def mkdir(args):
    res = None
    if len(args) != 2:
        return False
    nowdict = args[1].split("/")
    need = ""
    node = root
    for i in range(len(nowdict) - 1):
        need += f"/{nowdict[i]}"
    # print(need)
    if need != "":
        node = find_dic_item(need)
        if node is None:
            print("!cannot find path")
            return False
    name = nowdict[len(nowdict) - 1]
    res1 = find_path_in_node(node, name)
    if res1 is not None:
        print("path exists")
        return False
    # print(name)
    print("creating folder")
    obj = file.FileItem()
    obj.tag = file.TYPE_DICTIONARY
    obj.file_name = name
    node.dic.append(obj)
    return True


def find_dic_item(uri):
    dics = uri.split("/")
    now = root
    for i in dics:
        if i == "":
            continue
        flag = False
        for j in now.dic:
            if i == j.file_name:
                now = j
                flag = True
        if not flag:
            print(f"cannot find {i}")
            return None
    return now


def cd(args):
    global current_node
    res = None
    if args[1][0] == '/':  # 绝对目录
        res = search_dic_item(args[1])
    else:
        res = search_dic_item(args[1], now1=current_node)
    if res is None:
        print(" cannot find dic")
        return False
    current_node = res
    global current_path
    if args[1][0] == '/':  # 绝对目录
        current_path = args[1]
    else:
        current_path = current_path + "/" + args[1]
    return True


def find_file_in_node(node: file.FileItem, filename: str):
    for i in node.dic:
        if i.file_name == filename and i.tag == file.TYPE_FILE:
            return i
    return None


def find_path_in_node(node: file.FileItem, pathname: str):
    for i in node.dic:
        if i.file_name == pathname and i.tag == file.TYPE_DICTIONARY:
            return i
    return None


def get_free_disk(target_len):
    block_len = target_len//config.BLOCK_SIZE
    if target_len % config.BLOCK_SIZE != 0:
        block_len += 1
    length = get_empty_node_size()
    if block_len > length:
        return None
    global empty_node
    head = empty_node
    now = head
    for i in range(block_len - 1):
        now = now.next
    empty_node = now.next
    now.next = None
    return head


def create(args):
    if len(args) != 2:
        return False
    nowdict = args[1].split("/")
    need = ""
    node = root
    for i in range(len(nowdict) - 1):
        need += f"/{nowdict[i]}"
    # print(need)
    if need != "":
        node = find_dic_item(need)
        if node is None:
            print("!cannot find path")
            return False
    name = nowdict[len(nowdict) - 1]
    res1 = find_file_in_node(node, name)
    if res1 is not None:
        print(f"file named {name} exists")
        return False
    # print(name)
    print(f"creating file {name}")
    obj = file.FileItem()
    obj.tag = file.TYPE_FILE
    obj.file_name = name
    # fcb init
    obj.fcb = file.FCB()
    obj.fcb.filename = name
    obj.fcb.file_list = get_free_disk(0)
    if obj.fcb.file_list is None:
        print(f"无法请求指定大小")
        return False
    node.dic.append(obj)
    return True


command.register_command("listDisk", list_block_info, "/listDisk")
command.register_command("dir", dir, "/dir [dictionary]")
command.register_command("ls", dir, "/ls [dictionary]")
command.register_command("cd", cd, "/cd <path>")
command.register_command("create", create, "/create <path>")
command.register_command("mkdir", mkdir, "/mkdir <pathname>")

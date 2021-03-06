import config
import file
import user
import command
import time

MODE_READ_ONLY = 1    # 只读
MODE_WRITE_ONLY = 2   # 只写
MODE_READ_WRITE = 3   # 读写(1+2)
MODE_RUN = 4   # 只执行
MODE_ALL = 7   # 全部（1+2+4)


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
        self.file_name = ""
        self.mode = 0
        self.rw_location = 0
        self.sid = 0


class SystemOpenFile:
    def __init__(self):
        self.sid = 0
        self.open_file = ""
        self.dic_item = None
        self.open_count = 0


disk_block_link = None  # 空闲盘块链
root = file.FileItem()  # 根目录结点
user_table = user.userTable  # 用户表

user_open_file_table = []
system_open_file_table = []
current_node = root
current_path = "/"

# 新建disk_block_link
block_num = int(config.DISK_SIZE / config.BLOCK_SIZE)
print(f"block_num{str(block_num)}")
# 空闲磁盘链表
empty_node = None
for i in range(0, int(block_num)):
    if disk_block_link is None:
        disk_block_link = DiskBlockNode()
        empty_node = disk_block_link
    else:
        empty_node.next = DiskBlockNode()
        empty_node.next.id = empty_node.id + 1
        empty_node = empty_node.next


def get_empty_node_size():
    length = 0
    now = disk_block_link
    while now is not None:
        now = now.next
        length += 1
    return length


# 获取链表大小
def get_node_size(node):
    length = 0
    now = node
    while now is not None:
        now = now.next
        length += 1
    return length


def list_block_info(args):
    now_node = disk_block_link
    count = 0
    while now_node.next is not None:
        print(f"{now_node.id} size:{now_node.size}")
        now_node = now_node.next
        count += 1
        # if root.tag == file.TYPE_FILE:
        #    print("! it is a file item")
        #    return None
    print(f"tot free disk block {count}")
    return True

def search_dic_item(uri, now1=root):
    now = now1
    dics = uri.split("/")
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


def dir(args):
    res = None
    if len(args) == 1:
        res = find_dic_item("")
    else:
        res = find_dic_item(args[1])
    if res is None:
        return False
    print(f"there is {len(res.dic)} objects")
    name_dic = {
        file.TYPE_DICTIONARY: 'dictionary',
        file.TYPE_FILE: 'file'
    }
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^20}\t{3:^30}"
    print(tplt.format("type", "name", "permission", "create_time", chr(12288)))
    for i in res.dic:
        permission = ""
        if i.tag == file.TYPE_FILE:
            permission = i.fcb.permission
        print(tplt.format(name_dic[i.tag], i.file_name, permission, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.create_time)),chr(12288)))
    return True


def mkdir(args):
    res = None
    if len(args) != 2:
        return False
    nowdict = args[1].split("/")
    need = ""
    if nowdict[0] == '/':
        node = root
    else:
        node = current_node
    for i in range(len(nowdict) - 1):
        if need == "":
            chars = ""
            if args[1][0] == "/":
                chars = "/"
            need += chars + nowdict[i]
        else:
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
    if len(uri) > 0 and uri[0] == '/':
        now = root
    else:
        now = current_node
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
        if current_path[-1] == '/':
            current_path = current_path + args[1]
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
    global disk_block_link
    head = disk_block_link
    now = head
    for i in range(block_len - 1):
        now = now.next
    disk_block_link = now.next
    now.next = None
    return head


def get_file_node(path):
    nowdict = path.split("/")
    need = ""
    if len(path) > 0 and path[0] == '/':
        node = root
    else:
        node = current_node
    for i in range(len(nowdict) - 1):
        need += f"/{nowdict[i]}"
    # print(need)
    if need != "":
        node = find_dic_item(need)
        if node is None:
            print("!cannot find path")
            return None
    name = nowdict[len(nowdict) - 1]
    return find_file_in_node(node, name)


def get_file_and_dic_nodes(path):
    nowdict = path.split("/")
    need = ""
    node = current_node
    for i in range(len(nowdict) - 1):
        need += f"/{nowdict[i]}"
    # print(need)
    if need != "":
        node = find_dic_item(need)
        if node is None:
            print("!cannot find path")
            return None
    name = nowdict[len(nowdict) - 1]
    return find_file_in_node(node, name), node


def create(args):
    if len(args) != 2:
        return False
    nowdict = args[1].split("/")
    need = ""
    node = current_node
    for i in range(len(nowdict) - 1):
        if need == "":
            chars = ""
            if args[1][0] == "/":
                chars = "/"
            need += chars + nowdict[i]
        else:
            need += f"/{nowdict[i]}"
    #print(need)
    node = current_node
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
    print("created")
    return True


def open_command(args):
    if len(args) < 3:
        return False
    item = get_file_node(args[1])
    mode = int(args[2])
    if item is None:
        print(f"cannot find path {args[1]}")
        return False
    if item.fcb.permission == MODE_RUN or (item.fcb.permission == 1 and mode == 2) or (item.fcb.permission == 2 and mode == 1):
        print("permission is not allowed")
        return False
    mode_list = [MODE_READ_ONLY, MODE_READ_WRITE, MODE_WRITE_ONLY]
    if mode not in mode_list:
        print("unknown mode")
        return False
    sys_table = None
    sid =  len(system_open_file_table)
    for i in system_open_file_table:
        if i.dic_item.file_name == args[1]:
            sys_table = i
            sid = i.sid
    if sys_table is None:
        sid = len(system_open_file_table)
        sys_table = SystemOpenFile()
        sys_table.sid = sid
        sys_table.open_file = args[1]
        sys_table.dic_item = item
        system_open_file_table.append(sys_table)
    sys_table.open_count += 1
    uid = len(user_open_file_table)
    usr_table = UserOpenFile()
    usr_table.sid = sid
    usr_table.uid = uid
    usr_table.mode = mode
    usr_table.file_name = args[1]
    user_open_file_table.append(usr_table)
    print(f"success uid={uid}")
    return True


def close_command(args):
    if len(args) < 2:
        return False
    uid = int(args[1])
    print(f"{uid} - {len(user_open_file_table)}")
    if uid >= len(user_open_file_table):
        print("unknown uid")
        return False
    usr_table = user_open_file_table[uid]
    sid = usr_table.sid
    sys_table = system_open_file_table[sid]
    user_open_file_table.remove(usr_table)
    print(user_open_file_table)
    if sys_table.open_count > 1:
        sys_table.open_count -= 1
    else:
        system_open_file_table.remove(sys_table)
        print(system_open_file_table)
        for i in system_open_file_table:
            if i.sid > sid:
                i.sid -= 1
        for i in user_open_file_table:
            if i.sid > sid:
                i.sid -= 1
    print(f"close uid {uid} successfully")
    return True


def read_command(args):
    if len(args) < 2:
        return False
    uid = int(args[1])
    print(f"{uid} - {len(user_open_file_table)}")
    if uid >= len(user_open_file_table):
        print("unknown uid")
        return False
    usr_table = user_open_file_table[uid]
    if usr_table.mode == MODE_WRITE_ONLY:
        print(f"no permission to read {uid}")
        return False
    sid = usr_table.sid
    sys_table = system_open_file_table[sid]
    file_item  = sys_table.dic_item
    node_start = file_item.fcb.file_list
    res = ""
    while node_start is not None:
        res += node_start.content
        node_start = node_start.next
    print(f"data:{res}")
    return True


def write_command(args):
    if len(args) < 3:
        return False
    uid = int(args[1])
    print(f"{uid} - {len(user_open_file_table)}")
    if uid >= len(user_open_file_table):
        print("unknown uid")
        return False
    usr_table = user_open_file_table[uid]
    if usr_table.mode == MODE_READ_ONLY:
        print(f"no permission to write {uid}")
        return False
    sid = usr_table.sid
    sys_table = system_open_file_table[sid]
    file_item = sys_table.dic_item
    sys_table.dic_item.last_modify_time = int(time.time())
    node_start = file_item.fcb.file_list
    while node_start.next is not None:
        node_start = node_start.next
    length = len(args[2])
    free_size = node_start.size
    need_size = length - free_size
    if need_size > 0:
        node_start.next = get_free_disk(need_size)
        if node_start.next is None:
            print(f"no enough space")
            return False
    left = args[2]
    left_size = length
    while left_size != 0 and left != "":
        cat_size = min(node_start.size - len(node_start.content), len(left))
        left_size -= cat_size
        node_start.content += left[0:cat_size]
        left = left[cat_size:]
        node_start = node_start.next
        print(cat_size)
        print(left_size)
        print(left)
    print("done")
    return True


def move_command(args):
    if len(args) < 3:
        return False
    (f1, d1) = get_file_and_dic_nodes(args[1])
    (f2, d2) = get_file_and_dic_nodes(args[2])
    if d1 is None or d2 is None:
        print("path doesn't exist")
        return False
    if f1 is None:
        print("file doesn't exist")
        return False
    if f2 is not None:
        print("already exist file")
    d2.dic.append(f1)
    d1.dic.remove(f1)
    new_file_name = args[2].split("/")[-1]
    f1.file_name = new_file_name
    print("success")
    return True


def del_node_and_file(node):
    for i in node.dic:
        if i.tag == file.TYPE_FILE:
            return i
        if i.tag == file.TYPE_DICTIONARY:
            del_node_and_file(node)


def del_file(file_obj:file.FileItem):
    node = file_obj.fcb.file_list
    # 将内容归还至空闲盘块链
    while node is not None:
        old_node = node
        node.content = ""
        node = node.next
        global disk_block_link
        old_node.next = disk_block_link
        disk_block_link = old_node


def delete_command(args):
    if len(args) < 2:
        return False
    (file_obj, path) = get_file_and_dic_nodes(args[1])
    if path is not None:
        if file_obj is not None:
            del_file(file_obj)
            path.dic.remove(file_obj)
            print("delete success")
            return True
    p1 = find_path_in_node(path, args[1].split("/")[-1])
    if p1 is not None:
        del_node_and_file(p1)
        path.dic.remove(p1)
        print("delete success")
        return True
    print("cannot find target file or path")
    return False

# 用户登陆指令
def login_user(args):
    if len(args) <= 2:
        return False
    print("- 正在验证")
    table = user.find_user_table(args[1])
    if table is None:
        print("! 未找到该用户")
        return False
    if table.userName != "" and table.userName == args[1]:
        if table.password == args[2]:
            print("! 登陆成功")
            rt = find_dic_item(f"/user/{args[1]}")
            user.userID = args[1]
            if rt is not None:
                global current_node, current_path
                current_node = rt
                current_path = f"/user/{args[1]}"
            return True
        else:
            print("! 登陆失败 密码错误")
            return False


# 用户注册指令
def register_user(args):
    if len(args) < 4:
        return False
    res = user.find_user_table(args[1])
    if res is not None:
        print("! 注册失败 用户已经存在")
        return False
    print(" 开始新建用户")
    if args[2] != args[3]:
        print(" 密码不一致，请重新输入")
        return False
    obj = user.UserTable()
    obj.userName = args[1]
    obj.password = args[2]
    user.userTable.append(obj)
    mkdir(['', '/user'])
    mkdir(['', f"/user/{args[1]}"])
    print("注册成功")
    return True


def chmod_command(args):
    if len(args) < 3:
        return False
    item = get_file_node(args[1])
    mode = int(args[2])
    if item is None:
        print(f"cannot find path {args[1]}")
        return False
    mode_list = [MODE_READ_ONLY, MODE_READ_WRITE, MODE_WRITE_ONLY, MODE_RUN, MODE_ALL]
    if mode not in mode_list:
        print("unknown mode")
        return False
    item.fcb.permission = mode
    print("success")
    return True


mkdir(['', f"/root"])
register_user(['', "user", "user", "user"])
login_user(['', "user", "user"])
command.register_command("login", login_user, "/login <username> <password>")
command.register_command("register", register_user, "/register <username> <password> <repeat-password>")
command.register_command("listDisk", list_block_info, "/listDisk")
command.register_command("dir", dir, "/dir [dictionary]")
command.register_command("ls", dir, "/ls [dictionary]")
command.register_command("cd", cd, "/cd <path>")
command.register_command("create", create, "/create <path>")
command.register_command("mkdir", mkdir, "/mkdir <pathname>")
command.register_command("open", open_command, "/open <pathname> <mode(1=readonly,2=writeonly,3=readwrite,4=runonly,7=all)>")
command.register_command("close", close_command, "/close <uid>")
command.register_command("read", read_command, "/read <uid>")
command.register_command("write", write_command, "/write <uid> <stringbuffer>")
command.register_command("mv", move_command, "/mv <ori_path> <new_path>")
command.register_command("rm", delete_command, "/rm <path_name>")
command.register_command("chmod", chmod_command, "/chmod <pathname> <mode(1=readonly,2=writeonly,3=readwrite,4=runonly,7=all)>")

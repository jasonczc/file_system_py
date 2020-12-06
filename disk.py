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


command.register_command("listDisk", list_block_info, "/listDisk")


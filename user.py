import command
import config
# user 模块 用于控制当前用户


class UserTable:
    def __init__(self):
        self.userName = ""
        self.password = ""
        self.user = None     # 该用户文件目录的指针 类型 UFD
        self.permission = 0


# 树形目录结构
class UFD:
    def __init__(self):
        self.dic_name = ""
        self.nodes = []

    def add_path(self, UFD):
        self.nodes.append(UFD)

    def find_path(self, path):
        for i in self.nodes:
            if i.dic_name == path:
                return i
        return None



userID = None  # 用户登录的ID号，值为None时表示没有用户登录
userTable = []


# 寻找对应的user table文件 假如没有相应记录则返回None
def find_user_table(username):
    # 遍历当前的MFD
    for i in userTable:
        if i.userName != "" and i.userName == username:
            return i
    return None


def require_command(path=""):
    command.execute_command_map(userID, path)


print("+ user module loaded")
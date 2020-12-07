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



userID = -1  # 用户登录的ID号，值为-1时表示没有用户登录
userTable = []


# 寻找对应的user table文件 假如没有相应记录则返回None
def find_user_table(username):
    # 遍历当前的MFD
    for i in userTable:
        if i.userName != "" and i.userName == username:
            return i
    return None


# 用户登陆指令
def login_user(args):
    if len(args) <= 2:
        return False
    print("- 正在验证")
    table = find_user_table(args[1])
    if table is None:
        print("! 未找到该用户")
        return False
    if table.userName != "" and table.userName == args[1]:
        if table.password == args[2]:
            print("! 登陆成功")
            return True
        else:
            print("! 登陆失败 密码错误")
            return False


# 用户注册指令
def register_user(args):
    if len(args) < 4:
        return False
    res = find_user_table(args[1])
    if res is not None:
        print("! 注册失败 用户已经存在")
        return False
    print(" 开始新建用户")
    if args[2] != args[3]:
        print(" 密码不一致，请重新输入")
        return False
    obj = UserTable()
    obj.userName = args[1]
    obj.password = args[2]
    userTable.append(obj)
    return True


# 注册user模块对应的指令
command.register_command("login", login_user, "/login <username> <password>")
command.register_command("register", register_user, "/register <username> <password> <repeat-password>")


# 用户的登陆界面
def require_login():
    command.execute_command_map()


print("+ user module loaded")
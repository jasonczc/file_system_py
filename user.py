import command
import config

# user 模块 用于控制当前用户


class MFD:
    def __init__(self):
        self.userName = ""
        self.password = ""
        # UFD *user  该用户文件目录的指针


userID = -1  # 用户登录的ID号，值为-1时表示没有用户登录
userTable = [MFD()] * config.MAX_USER


# 用户登陆指令
def login_user(args):
    if len(args) <= 2:
        return False
    print("- 正在验证")
    # 遍历当前的MFD
    for i in userTable:
        if i.userName != "" and i.userName == args[1]:
            if i.password == args[2]:
                print("! 登陆成功")
                return True
            else:
                print("! 登陆失败 密码错误")
                return False
    print("! 未找到该用户")
    return False


# 用户注册指令
def register_user():
    print("register")


# 注册user模块对应的指令
command.register_command("login", login_user, "/login <username> <password>")
command.register_command("register", register_user, "/register <username> <password> <repeat-password>")


# 用户的登陆界面
def require_login():
    print(f'''
需要登陆 使用指令进行登陆
登陆指令 /login <username> <password>
注册指令 /register <username> <password> <repeat-password>
''')
    command.execute_command_map()


print("+ user module loaded")
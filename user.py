import command

# user 模块 用于控制当前用户
userID = -1  # 用户登录的ID号，值为-1时表示没有用户登录


# 登陆指令
def login_user(args):
    if len(args) <= 2:
        return False
    print("正在验证")
    return True


def register_user():
    print("register")


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
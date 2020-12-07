import user
import disk

# 系统是否处于运行状态
running = True


# 系统模块
def start_sys():
    print("starting file system...")

    print(f'''
    需要登陆 使用指令进行登陆
    登陆指令 /login <username> <password>
    注册指令 /register <username> <password> <repeat-password>
    ''')
    while running:
        if user.userID == -1:
            user.require_login()
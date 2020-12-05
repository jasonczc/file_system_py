import user

# 系统是否处于运行状态
running = True


# 系统模块
def start_sys():
    while running:
        if user.userID == -1:
            user.require_login()
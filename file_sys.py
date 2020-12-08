import user
import disk

# 系统是否处于运行状态
running = True


# 系统模块
def start_sys():
    print("starting file system...")

    print(f'''
    /login <username> <password>
    /register <username> <password> <repeat-password>
    ''')
    while running:
        user.require_command(disk.current_path)
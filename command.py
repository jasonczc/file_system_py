import user
# 指令模块，用于快速构建指令
global_cmd_map = {}


def help_command(args):
    print("help command")
    for i in global_cmd_map:
        print(f"> /{i} - {global_cmd_map[i]['help']}")
    return True


# 注册一个全局指令
def register_command(cmd, function, help= "to see help"):
    global_cmd_map[cmd] = {
        "function": function,
        "help": help
    }


register_command("help", help_command)


# cmd_map 用于分发command以快速执行分支
def execute_command_map(user_name, path=""):
    needLogin = False
    if user_name is None:
        needLogin = True
        user_name = ""
    cmd = input(f"{user_name} {path}>")
    args = cmd.split(" ")
    allow_login = ['login','register']
    if needLogin and args[0] not in allow_login:
        print("login required")
        return
    if args[0] not in global_cmd_map:
        print("command not found")
        return
    else:
        try:
            res = global_cmd_map[args[0]]["function"](args)
            if not res:
                print(global_cmd_map[args[0]]["help"])
        except Exception:
            print(Exception)



print("+ command module loaded")
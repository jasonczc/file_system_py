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
def execute_command_map():
    cmd = input(">")
    args = cmd.split(" ")
    if args[0] not in global_cmd_map:
        print("输入的命令不存在，请重新输入")
        execute_command_map()
    else:
        res = global_cmd_map[args[0]]["function"](args)
        if not res:
            print(global_cmd_map[args[0]]["help"])


print("+ command module loaded")
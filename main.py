# #define MaxDisk 512*1024    //模拟最大磁盘空间
# #define commandAmount 12    //对文件操作的指令数
# //存储空间管理有关结构体和变量
# char disk[MaxDisk];    //模拟512K的磁盘存储空间
class diskNode:  # 磁盘块结构体
    def __init__(self):
        self.maxlength = 0
        self.start = 0
        self.useFlag = 0
        # diskNode *next;


# diskNode *diskHead;
# struct fileTable   //文件块结构体
# {
#     char fileName[10];
#     int strat;         //文件在磁盘存储空间的起始地址
#     int length;        //文件内容长度
#     int maxlength;     //文件的最大长度
#     char fileKind[3];  //文件的属性——读写方式
#     struct tm *timeinfo;
#     bool openFlag;      //判断是否有进程打开了该文件
#     //fileTable *next;
# };
#
# //两级目录结构体
# typedef struct user_file_directory //用户文件目录文件UFD
# {
#     //char fileName[10];
#     fileTable *file;
#     user_file_directory *next;
# }UFD;
#     //UFD *headFile;

class MFD:
    def __init__(self):
        self.userName = ""
        self.password = ""
        # UFD *user  该用户文件目录的指针


global userTable
userTable = [MFD()] * 100  # MaxUser = 100

# typedef struct master_file_directory //主文件目录MFD
# {
#     char userName[10];
#     char password[10];
#     UFD *user;
# }MFD;
# MFD userTable[MaxUser];

global used
used = 0  # 定义MFD目录中已有的用户数

# //文件管理
# void fileCreate(char fileName[], int length, char fileKind[]);       //创建文件
# void fileWrite(char fileName[]);                   //写文件
# void fileCat(char fileName[]);                   //读文件
# void fileRen(char fileName[], char rename[]);       //重命名文件
# void fileFine(char fileName[]);                  //查询文件
# void fileDir(char UserName[]);                   //显示某一用户的所有文件
# void fileClose(char fileName[]);                 //关闭已打开的文件
# void fileDel(char fileName[]);                   //删除文件
# void chmod(char fileName[], char kind[]);        //修改文件的读写方式
# int requestDist(int &startPostion,int maxLength); //磁盘分配查询
# void initDisk();                                 //初始化磁盘
# void freeDisk(int startPostion);                 //磁盘空间释放
# void diskShow();                                 //显示磁盘使用情况
#
# //用户管理
# void userCreate();
# int login();

global userID
userID = -1  # 用户登录的ID号，值为-1时表示没有用户登录


def main():
    order = ["create", "rm", "cat", "write", "fine", "chmod", "ren", "dir", "close", "return", "exit", "df"]

    #    int i, k, j;
    #    int length;
    #    initDisk();                    //初始化磁盘
    #    for (i = 0; i < MaxUser; i++)         //初始化用户UFD目录文件的头指针
    #    for i in range(0,100)
    #        userTable[i].user = (UFD *)malloc(sizeof(UFD));
    #        userTable[i].user->next = NULL;

    while 1:
        print("********************************************\n")
        print("                 1、Creat user\n")
        print("                 2、login\n")
        print("********************************************\n")
        choice = input("Please choose the function key:>")
        if choice == '1':
            print('1')  # 此行删除
            # userCreat();
        elif choice == '2':
            print('2')  # 此行删除
            # userID = login();
        else:
            print("您的输入有误，请重新输入\n")
        while userID != -1:
            #  fflush(stdin);
            print("———————————————————————————————————————\n")
            print(" create-创建 格式：create a1 1000 rw,将创建名为a1,长度为1000字节可读可写的文件\n")
            print(" rm-删除 格式：rm a1,将删除名为a1的文件\n")
            print(" cat-查看文件内容 格式：cat a1,显示a1的内容\n")
            print(" write-写入  格式：write a1\n")
            print(" fine-查询 格式：fine a1 ,将显示文件 a1的属性\n")
            print(" chmod-修改 格式：chmod a1 r,将文件a1的权限改为只读方式\n")
            print(" ren-重命名 格式：ren a1 b1 ,将a1改名为b1\n")
            print(" dir-显示文件 格式：dir aaa,将显示aaa用户的所有文件\n")
            print(" df-显示磁盘空间使用情况 格式：df\n")
            print(" close-关闭文件 格式：close a1,将关闭文件a1\n")
            print(" return-退出用户，返回登录界面\n")
            print(" exit-退出程序\n")
            print("————————————————————————————————————————\n")
            print("please input your command:>")
            command = input()
            print(command)
            select = 0
            # for (i = 0; command[i] != ' '&&command[i] != '\0'; i++)             //command_str1字符串存储命令的操作类型
            #     command_str1[i] = command[i];
            # k = i;
            # command_str1[k] = '\0';
            # for (i = 0; i < commandAmount; i++)
            # {
            #    if (!strcmp(command_str1, order[i]))
            #    {
            #        select = i;
            #         break;
            #    }
            #    }
            #    if (i == commandAmount)
            #    {
            #        printf("您输入的命令有误，请重新输入\n");
            #        continue;
            #    }
            #    for (i = k + 1, k = 0; command[i] != '\t'&&command[i] != '\0'; i++, k++)   //commmand_str2字符串存储文件名或用户名
            #       command_str2[k]=command[i];
            #    command_str2[k]='\0';
            #    k=i;
            if select == 0:
                # for (i = k + 1, k = 0; command[i] != ' '; i++, k++)
                #     command_str3[k] = command[i];
                # command_str3[k] = '\0';
                # k = i;
                # j = 1;
                # length = 0; // 初始化文件长度
                # for (i = strlen(command_str3) - 1; i >= 0; i--) // 把字符串转换为十进制
                # {
                #     length += (command_str3[i] - 48) * j;
                # j *= 10;
                # }
                # for (i = k + 1, k = 0; command[i] != ' ' & & command[i] != '\0'; i++, k++)
                #     command_str4[k] = command[i];
                # command_str4[k] = '\0';
                # fileCreate(command_str2, length, command_str4);
                print(0)  # 删除此行,以下此位置输出全部删除
            elif select == 1:
                # fileDel(command_str2)
                print(1)
            elif select == 2:
                # fileCat(command_str2);
                print(2)
            elif select == 3:
                # fileWrite(command_str2)
                print(3)
            elif select == 4:
                # fileFine(command_str2)
                print(4)
            elif select == 5:
                # for (i = k + 1, k = 0; command[i] != ' ' & & command[i] != '\0'; i++, k++)
                #     command_str3[k] = command[i];
                # command_str3[k] = '\0';
                # chmod(command_str2, command_str3);
                print(5)
            elif select == 6:
                # for (i = k + 1, k = 0; command[i] != '\0'; i++, k++)
                #     command_str3[k] = command[i];
                # command_str3[k] = '\0';
                # fileRen(command_str2, command_str3);
                print(6)
            elif select == 7:
                # fileDir(command_str2)
                print(7)
            elif select == 8:
                # fileClose(command_str2)
                print(8)
            elif select == 9:
                # UFD * p;
                # for (p = userTable[userID].user->next; p != NULL; p = p->next) // 退出用户之前关闭所有打的文件
                #     if (p->file->openFlag)
                #         p->file->openFlag = false;
                # system("cls");
                # userID = -1;
                print(9)
            elif select == 10:
                exit(0)
            elif select == 11:
                # diskShow()
                print(11)


def userCreate():
    if used < 100:
        i = 0
        userName = input("请输入用户名")
        for i in range(0, used):
            if userTable[i].userName == userName:
                print("\n该用户名已存在，创建用户失败\n")
                return
        userTable[i].userName = userName
        userTable[i].password = input("请输入密码：")
        print("创建用户成功\n")
        used += 1
    else:
        print("创建用户失败，用户数量已达到上限\n")
    # fflush(stdin)


def login():
    name = input("请输入用户名：")
    psw = input("请输入密码：")
    for i in range(0, used):
        if userTable[i].userName == name:
            break
    if i == used:
        print("\n您输入的用户名不存在\n")
        return -1
    for times in range(0, 3):
        psw = input("\n请输入密码：\n")
        if userTable[i].password == psw:
            print("用户登陆成功\n")
            break
        else:
            print("密码输入错误，还有" + 2-times + "次机会\n")
            if times == 2:
                exit(0)
    # fflush(stdin)
    return i

def initDisk():
    # diskHead = (diskNode *)
    # malloc(sizeof(diskNode));
    # diskHead->maxlength = MaxDisk;
    # diskHead->useFlag = 0;
    # diskHead->start = 0;
    # diskHead->next = NULL;
    return

def requestDist():  # 括号内： int &startPostion, int maxLength
    flag = 0  # 标记是否分配成功
    # p = diskHead
    # while (p)
    #     if (p->useFlag == 0 & & p->maxlength > maxLength)
    #         startPostion = p->start;
    #         q = (diskNode *)
    #         malloc(sizeof(diskNode));
    #         q->start = p->start;
    #         q->maxlength = maxLength;
    #         q->useFlag = 1;
    #         q->next = NULL;
    #         diskHead->start = p->start + maxLength;
    #         diskHead->maxlength = p->maxlength - maxLength;
    #         flag = 1;
    #         temp = p;
    #         if (diskHead->next == NULL)
    #             diskHead->next = q;
    #         else
    #             while (temp->next)
    #                 temp = temp->next;
    #                 temp->next = q;
    #         break;
    # p = p->next;
    return flag


def fileCreate():  # 参数：char fileName[], int length, char fileKind[]
    # time_t rawtime
    # int startPos;
    # UFD * fileNode, *p;
    # for (p = userTable[userID].user->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #         printf("文件重名，创建文件失败\n");
    #         system("pause");
    #         return;
    # if (requestDist(startPos, length))
    #     fileNode = (UFD * )malloc(sizeof(UFD));
    #     fileNode->file = (fileTable * )malloc(sizeof(fileTable)); // 这一步必不可少，fileNode里面的指针也需要申请地址，否则fileNode->file指向会出错
    #     strcpy(fileNode->file->fileName, fileName);
    #     strcpy(fileNode->file->fileKind, fileKind);
    #     fileNode->file->maxlength=length;
    #     fileNode->file->strat=startPos;
    #     fileNode->file->openFlag=false;
    #     time( & rawtime);
    #     fileNode->file->timeinfo = localtime( & rawtime);
    #     fileNode->next = NULL;
    #     if (userTable[userID].user->next == NULL)
    #         userTable[userID].user->next = fileNode;
    #     else
    #         p = userTable[userID].user->next;
    #         while (p->next) p = p->next;
    #         p->next = fileNode;
    #     print("创建文件成功\n");
    #     system("pause");
    # else
    #     print("磁盘空间已满或所创建文件超出磁盘空闲容量，磁盘空间分配失败\n");
    #     system("pause");
    return


def freeDisk():  # 参数int startPosition
    # diskNode * p;
    # for (p = diskHead; p != NULL; p = p->next)
    #     if (p->start == startPostion)
    #     break
    # p->useFlag = false;
    return


def fileDel():  # 参数：char fileName[]
    # UFD * p, *q, *temp;
    # q = userTable[userID].user;
    # p = q->next;
    # while (p)
    #     if (!strcmp(p->file->fileName, fileName))
    #         break
    #     else
    #         p = p->next
    #         q = q->next
    # if (p)
    #     if (p->file->openFlag != true) // 先判断是否有进程打开该文件
    #         temp = p;
    #         q->next = p->next;
    #         freeDisk(temp->file->strat); // 磁盘空间回收
    #         free(temp);
    #         print("文件删除成功\n");
    #         system("pause");
    #     else
    #         print("该文件已被进程打开,删除失败\n")
    #         system("pause");
    # else
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    #     system("pause");
    return

def fileCat():
    startPos = 0
    length = 0
    k = 0
    # UFD * p, *q;
    # q = userTable[userID].user
    # for (p = q->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #         break
    # if (p)
    #     startPos = p->file->strat;
    #     length = p->file->length;
    #     p->file->openFlag = true; // 文件打开标记
    #     print("*****************************************************\n")
    #     for (int i = startPos; k < length; i++, k++)
    #         if i % 50 == 0:
    #             print("\n") // 一行大于50个字符换行
    #             print(disk[i])
    #     print("\n\n*****************************************************\n")
    #     printf("%s已被read进程打开,请用close命令将其关闭\n", p->file->fileName);
    #     system("pause");
    # else
    #     printf("没有找到该文件,请检查输入的文件名是否正确\n");
    #     system("pause");


def fileWrite():  # 参数 fileName[]
    # UFD * p, *q;
    # q = userTable[userID].user;
    # int i, k, startPos;
    # for (p = q->next; p != NULL; p = p->next)
    #    if (!strcmp(p->file->fileName, fileName))
    #    break
    # if (p)
    #     if (!strcmp(p->file->fileKind, "r")) // 判断文件类型
    #     {
    #         print("该文件是只读文件,写入失败\n")
    #         return
    #     }
    #     char str[500];
    #     printf("please input content:\n");
    #     gets(str);
    #     startPos = p->file->strat;
    #     p->file->openFlag = true; // 文件打开标记
    #     p->file->length = strlen(str);
    #     if (p->file->length > p->file->maxlength)
    #         print("写入字符串长度大于该文件的总长度,写入失败\n")
    #         return
    #     for (i = startPos, k = 0; k < (int)strlen(str); i++, k++)
    #         disk[i] = str[k];
    #     print("文件写入成功,请用close命令将该文件关闭\n")
    # else
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    # system("pause")
    return


def fileFine():  # 参数: char fileName[]
    # UFD * p, * q;
    # q = userTable[userID].user;
    # for (p = q->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #         break
    # if p:
    #     print("********************************************\n")
    #     print("文件名：" + p->file->fileName + '\n')
    #     print("文件长度：" + p->file->maxlength + '\n')
    #     print("文件在存储空间的起始地址：" + p->file->strat + '\n')
    #     print("文件类型：" + p->file->fileKind + '\n')
    #     print("创建时间：" + asctime(p->file->timeinfo) + '\n')
    #     print("********************************************\n")
    # else:
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    return


def chmod():  # 参数： char fileName[], char kind[]
    # UFD * p, *q;
    # q = userTable[userID].user;
    # for (p = q->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #     break
    # if p:
    #     p->file->fileKind = kind
    #     print("修改文件类型成功\n")
    # else:
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    return


def fileRen():  # char fileName[], char name[]
    # UFD * p, *q;
    # q = userTable[userID].user;
    # for (p = q->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #         break
    # if p:
    #     while (q->next)
    #         if (!strcmp(q->next->file->fileName, name))
    #             print("您输入的文件名已存在,重命名失败\n")
    #             return
    #         q = q->next;
    #     p->file->fileName = name
    #     print("重命名成功\n")
    # else:
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    return


def fileDir():  # 参数：char userName[]
    # UFD * p;
    # int i, k;
    # for (i = 0; i < MaxUser; i++)
    #     if (!strcmp(userTable[i].userName, userName))
    #         k = i;
    #         break
    # if i == MaxUser:
    #     print("没有找到该用户，请检查输入用户名是否正确\n")
    #     return
    # else:
    #     p = userTable[k].user->next;
    #     print("********************************************************************************\n")
    #     print("文件名  文件长度  文件在磁盘的起始地址  文件类型  创建时间\n")
    #     for (; p != NULL; p = p->next)
    #         print("%s       %d             %d           %s  %s", p->file->fileName,p->file->maxlength, p->file->strat, p->file->fileKind, asctime(p->file->timeinfo));
    #     print("********************************************************************************\n");
    return


def diskShow():
    # diskNode * p
    i = 0
    unusedDisk = 0
    print("***************************************************************************\n")
    print(" 盘块号    起始地址       容量(bit)  是否已被使用\n");
    # for (p = diskHead; p != NULL; p = p->next, i++)
    #     if (p->useFlag == false)
    #         unusedDisk += p->maxlength
    # print("  %d        %d             %d         %d    \n", i, p->start, p->maxlength, p->useFlag);
    # print("***************************************************************************\n")
    # print("磁盘空间总容量：512*1024bit 已使用：%dbit  末使用：%dbit\n\n", MaxDisk - unusedDisk, unusedDisk)


def fileClose():  # 参数：char fileName[]
    # UFD * p, *q;
    # q = userTable[userID].user;
    # for (p = q->next; p != NULL; p = p->next)
    #     if (!strcmp(p->file->fileName, fileName))
    #     break
    # if p:
    #     p->file->openFlag = false;
    #     print("%s文件已关闭\n", p->file->fileName)
    # else:
    #     print("没有找到该文件,请检查输入的文件名是否正确\n")
    return


if __name__ == '__main__':
    main()

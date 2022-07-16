"""
UselessOS
By   the-cat1
time 2022/7/16
"""

import os
import sys
import time

DRIVER = "Driver"

directory = DRIVER  # 目录


def cd(args: tuple):
    """
    cd [directory]

    directory   要切换的目录。

    将目录切换到指定的目录。
    在不带参数时，将返回当前目录。


    特殊目录：
    .    当前目录
    ..   上级目录


    例如：
        cd test
    上面的例子将当前目录设置为"当前目录\\test"(当前目录存在"test"文件夹)。

        cd
    上面的例子将返回当前目录。
    """

    global directory

    if len(args) == 0:
        print(directory + "\n")
    else:
        if args[0] == ".":
            directory = directory
        elif args[0] == "..":
            if directory != DRIVER:
                directory = os.path.dirname(directory)
        elif os.path.isdir(os.path.abspath(os.path.join(directory, args[0]))):
            directory = os.path.join(directory, args[0])
        else:
            print("\033[31m错误！\n\033[0m")


def mkdir(args: tuple):
    """
    mkdir (dir)

    dir    要创建的目录。

    创建单层目录。

    注：mkdir命令只能创建单层目录，要创建多层目录，请用makedirs。


    例子：
        mkdir test
    上面的例子在当前目录创建了一个"test"目录。
    """

    if len(args) == 0:
        print("\033[31m\"mkdir\"命令需要一个参数！\033[0m\n")
    else:
        try:
            os.mkdir(os.path.abspath(os.path.join(directory, args[0])))
        except FileNotFoundError:
            print("\033[31m\"mkdir\"命令只能创建单层目录！要创建多层目录，请使用\"makedirs\"\033[0m")
        except FileExistsError:
            print("\033[31m文件已存在！\033[0m")


def makedirs(args: tuple):
    """
    makedirs (dirs)

    dirs   要创建的目录。

    创建多层目录。


    例子：
        makedirs test1\\test2
    上面的例子在当前目录创建了一个"test1"目录，又在"test1"目录中创建了"test2"目录。
    """

    if len(args) == 0:
        print("\033[31m\"makedirs\"命令需要一个参数！\033[0m\n")
    else:
        try:
            os.makedirs(os.path.abspath(os.path.join(directory, args[0])))
        except FileNotFoundError:
            print("\033[31m错误！\033[0m")
        except FileExistsError:
            print("\033[31m文件已存在！\033[0m")


def newfile(args: tuple):
    """
    newfile (filename)

    filename 文件名。

    新建一个文件。

    例子：
        newfile test.txt
    上面的例子在当前目录中创建了一个名为"test.txt"的文件。
    """

    if len(args) == 0:
        print("\033[31m\"newfile\"命令需要一个参数！\033[0m\n")
    else:
        if os.path.isdir(os.path.dirname(os.path.abspath(os.path.join(directory, args[0])))):
            try:
                file = open(os.path.abspath(os.path.join(directory, args[0])), "x", encoding="utf-8")
                file.close()
            except OSError:
                print("\033[31m创建文件失败！\033[0m\n")
        else:
            print("\033[31m无效的目录！\033[0m\n")


def type_(args: tuple):
    """
    type (filename)

    filename 文件名。

    输出某个文件的内容。


    例子：
        type test.txt
    上面的例子将输出当前目录下的"test.txt"文件内容(当前目录下存在"test.txt")。
    """

    if len(args) == 0:
        print("\033[31m\"type\"命令需要一个参数！\033[0m\n")
    else:
        if os.path.isdir(os.path.dirname(os.path.abspath(os.path.join(directory, args[0])))):
            try:
                file = open(os.path.abspath(os.path.join(directory, args[0])), "r", encoding="utf-8")
                print(file.read(), "\n")
                file.close()
            except OSError:
                print("\033[31m读取文件失败！\033[0m\n")
        else:
            print("\033[31m无效的目录！\033[0m\n")


def dir_(args: tuple):
    """
    dir

    返回当前目录下的所有文件和文件夹。


    例子：
        dir
    上面的命令将返回当前目录下的所有文件和文件夹。
    """

    if len(args) != 0:
        print("\033[31m\"dir\"没有参数！\033[0m\n")
        return
    files = os.listdir(directory)
    fileCount = 0
    dirCount = 0

    print("\n", directory, " 目录下的文件(文件夹):")
    for f in files:
        fPath = os.path.abspath(os.path.join(directory, f))
        if os.path.isfile(fPath):
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(fPath)))}\t\t"
                  f"{os.path.getsize(fPath)}\t\t"
                  f"{f}")
            fileCount += 1
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(fPath)))}\t\t"
                  f"<DIR>\t"
                  f"{f}")

            dirCount += 1

    print(f"{fileCount} 个文件，{dirCount} 个文件夹。\n")


def rm(args: tuple):
    """
    rm (filename)

    filename 文件名。

    删除某一文件。

    注：rm只能删除文件，要删除文件夹，请用rmdir。


    例子：
        rm test.txt
    上面的例子将会删除当前目录下的"test.txt"(当前目录存在"test.txt")。
    """

    if len(args) == 0:
        print("\033[31m\"rm\"命令需要一个参数！\033[0m")
    else:
        fPath = os.path.abspath(os.path.join(directory, args[0]))
        try:
            os.remove(fPath)
            print(f"{args[0]} 已删除。")
        except OSError:
            print("\033[31m删除失败！请检查目录是否正确！\033[0m")
            print("\033[31m\"rmdir\"只能删除目录，要删除文件，请用\"rm\"\033[0m")
    print("\n")


def rmdir(args: tuple):
    """
    rmdir (dirname)

    dirname 文件夹名。

    删除某一文件夹(文件夹为空)。

    注：rm只能删除文件，要删除文件夹，请用rmdir。


    例子：
        rmdir test
    上面的例子将会删除当前目录下的"test"文件夹(当前目录存在"test"文件夹)。
    """

    if len(args) == 0:
        print("\"rmdir\"命令需要一个参数！")
    else:
        dPath = os.path.abspath(os.path.join(directory, args[0]))
        try:
            os.rmdir(dPath)
            print(f"{args[0]} 已删除。")
        except OSError:
            print("\033[31m删除失败！请检查目录是否正确！\033[0m")
            print("\033[31m\"rmdir\"只能删除目录，要删除文件，请用\"rm\"\033[0m")
    print("\n")


def rename(args: tuple):
    """
    rename (filename) (newName)

    filename 文件名。
    newName  新文件名。

    重命名某一文件。

    例子：
        rename test.txt hello.txt
    上面的例子会将当前目录下的"test.txt"重命名为"hello.txt"。
    """

    if len(args) != 2:
        print("\033[31m\"rename\"命令需要2个参数！\033[0m\n")
    else:
        try:
            os.rename(os.path.abspath(os.path.join(directory, args[0])),
                      os.path.abspath(os.path.join(directory, args[1])))
        except OSError:
            print("\033[31m重命名失败，请检查路径！\033[0m\n")


def help_(args: tuple):
    """
    help [command]

    command 命令

    返回对应命令的帮助信息。

    例子：
        help
    上面的例子会返回命令列表。

        help cd
    上面的例子会返回cd命令的帮助信息。
    """

    if len(args) == 0:
        print("Help帮助：\n"
              "<cd>\t\t\t跳转到某个目录。\n"
              "<clear>\t\t\t清除屏幕。\n"
              "<dir/ls>\t\t列出目录下的所有文件。\n"
              "<exit>\t\t\t退出UselessOS。\n"
              "<help>\t\t\t帮助命令。\n"
              "<makedirs>\t\t创建多层目录。\n"
              "<mkdir>\t\t\t创建单层目录。\n"
              "<newfile>\t\t创建文件。\n"
              "<rename>\t\t重命名文件。\n"
              "<rm>\t\t\t删除文件。\n"
              "<rmdir>\t\t\t删除文件夹。\n"
              "<type>\t\t\t输出文件的内容。\n")
    else:
        helpDocs = {
            "cd": cd.__doc__,
            "exit": exit_.__doc__,
            "mkdir": mkdir.__doc__,
            "makedirs": makedirs.__doc__,
            "newfile": newfile.__doc__,
            "type": type_.__doc__,
            "dir": dir_.__doc__,
            "ls": dir_.__doc__,
            "rm": rm.__doc__,
            "rmdir": rmdir.__doc__,
            "help": help_.__doc__,
            "rename": rename.__doc__,
            "clear": clear.__doc__
        }
        try:
            print(helpDocs[args[0]])
        except KeyError:
            print("\033[31m指令不存在！\033[0m")
        print("\n")


def exit_(args: tuple):
    """
    exit

    退出UselessOS。


    例子：
        exit
    上面的例子会退出UselessOS。
    """

    if len(args) != 0:
        print("\033[31m\"exit\"没有参数！\033[0m\n")
        return
    print("退出UselessOS！")
    sys.exit()


# noinspection PyUnusedLocal
def clear(args: tuple):
    """
    clear

    清除屏幕上的所有文字。


    例子：
        clear
    上面的例子会清除屏幕上的所有文字。
    """
    os.system("CLS")


# 命令集
commands = {
    "cd": cd,
    "exit": exit_,
    "mkdir": mkdir,
    "makedirs": makedirs,
    "newfile": newfile,
    "type": type_,
    "dir": dir_,
    "ls": dir_,
    "rm": rm,
    "rmdir": rmdir,
    "help": help_,
    "rename": rename,
    "clear": clear
}


def main():
    # 设置命令行
    os.system("CHCP 65001 && CLS")  # 确保能使用彩色字体

    print("*****Welcome to UselessOS!*****")
    while True:
        command = input(f"{directory}>")
        if command == "":  # 空指令
            continue

        """获取主命令"""
        mainCommand = ""
        for c in command:
            if c == " ":
                break
            else:
                mainCommand += c

        """获取参数"""
        args = [""]
        x = 0
        for c in command[(len(mainCommand)):]:
            if c == " ":
                x += 1  # 下一个参数
                args.append("")
                continue
            else:
                args[x] += c
        del args[0]  # 去掉第一个空参数

        # 拿到 主命令mainCommand 和 参数args
        try:
            commands[mainCommand](tuple(args))  # 调用对应方法
        except KeyError:
            print(f"\033[31m不存在的命令\"{mainCommand}\"!\033[0m\n")


if __name__ == "__main__":
    main()

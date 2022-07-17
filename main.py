"""
UselessOS
By      the-cat1
Version 0.1.1
Time    2022/7/17
"""

import json
import os
import shutil
import sys
import time

VERSION = "0.1.1"
VER_MAG = f"UselessOS(无用系统) {VERSION} [2022/7/17]，By the-cat1，Github https://github.com/the-cat1/UselessOS.git。"

DRIVER = "Driver"
HELP = os.path.abspath("HelpFiles\\")
# noinspection SpellCheckingInspection
HELP_FILE_SPLITEXT = ".uselessoshelp"

helpDocs = {}
directory = DRIVER  # 目录


def helpInit():
    """初始化Help系统"""

    """获取帮助文件"""
    helpFiles = os.listdir(HELP)
    for file in range(len(helpFiles)):
        if os.path.splitext(helpFiles[file])[1] != HELP_FILE_SPLITEXT:  # 后缀名不是HELP_FILE_SPLITEXT，即不是帮助文件
            del helpFiles[file]

    """录入帮助信息"""
    for file in helpFiles:
        with open(os.path.abspath(os.path.join(HELP, file)), encoding="utf-8") as f:
            # noinspection PyBroadException
            try:
                helpJson = json.load(f)
                helpDocs.update({helpJson["command"]: "\n".join(helpJson["helps"])})
            except:
                print(f"\033[33m\"{file}\"帮助文件存在问题！\033[0m")


def cd(args: tuple):
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
    if len(args) == 0:
        print("\033[31m\"rm\"命令需要一个参数！\033[0m")
    else:
        fPath = os.path.abspath(os.path.join(directory, args[0]))
        if os.path.isfile(fPath):
            try:
                os.remove(fPath)
                print(f"{args[0]} 已删除。")
            except OSError:
                print("\033[31m删除失败！请检查目录是否正确！\033[0m")
        else:
            print("\033[31m\"rm\"只能删除文件，要删除文件夹，请用\"rmdir\"\033[0m")
    print("\n")


def rmdir(args: tuple):
    if len(args) == 0:
        print("\"rmdir\"命令需要一个参数！")
    else:
        dPath = os.path.abspath(os.path.join(directory, args[0]))
        if os.path.isdir(dPath):
            # 删除所有文件
            if "/a" in args:
                shutil.rmtree(dPath)
                print(f"{os.path.join(directory, args[0])} 及其子文件夹已删除。")
            else:
                try:
                    os.rmdir(dPath)
                    print(f"{os.path.join(directory, args[0])} 已删除。")
                except OSError:
                    print("\033[31m删除失败！请检查目录是否正确、为空！\033[0m")
        else:
            print("\033[31m\"rmdir\"只能删除目录，要删除文件，请用\"rm\"\033[0m")
    print("\n")


def rename(args: tuple):
    if len(args) != 2:
        print("\033[31m\"rename\"命令需要2个参数！\033[0m\n")
    else:
        try:
            os.rename(os.path.abspath(os.path.join(directory, args[0])),
                      os.path.abspath(os.path.join(directory, args[1])))
        except OSError:
            print("\033[31m重命名失败，请检查路径！\033[0m\n")


def help_(args: tuple):
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
              "<type>\t\t\t输出文件的内容。\n"
              "<ver>\t\t\t输出UselessOS的版本信息。\n")
    else:
        try:
            print(helpDocs[args[0]])
        except KeyError:
            print("\033[31m指令不存在或缺少帮助文件！\033[0m")
        print("")  # end="\n"


def exit_(args: tuple):
    if len(args) != 0:
        print("\033[31m\"exit\"没有参数！\033[0m\n")
        return
    print("退出UselessOS！")
    sys.exit()


# noinspection PyUnusedLocal
def ver(args: tuple):
    print(VER_MAG)


# noinspection PyUnusedLocal
def clear(args: tuple):
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
    "clear": clear,
    "ver": ver
}


def main():
    # 设置命令行
    os.system("CHCP 65001 && CLS")  # 确保能使用彩色字体

    # 打印欢迎信息
    print("*****Welcome to UselessOS!*****")
    print(VER_MAG)

    """初始化"""
    # 判断"Driver\"文件夹是否存在
    if not os.path.isdir(os.path.abspath(DRIVER + "\\")):
        print("\033[33m\"Driver\"文件夹不存在，已自动创建！\033[0m")
        os.mkdir(os.path.abspath(DRIVER))

    # 判断"Help\"文件夹是否存在
    if not os.path.isdir(HELP):
        print("\033[33m\"HELP\"文件夹不存在，已自动创建！\033[0m")
        os.mkdir(HELP)

    helpInit()

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

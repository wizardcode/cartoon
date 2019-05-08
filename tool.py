import os
import sys
import re
from flaskr import db
import json


# 重新计算字幕文件中的数字
def format_number():
    path = "s1_subtitle/s1_2.vtt"
    file = open(path, "r").readlines()
    wfile = open(path, "w")
    count = 0
    for i in file:
        num = re.search("^(\d+)\n", i)
        if num is None:
            wfile.write(i)
        else:
            wfile.write(str(count) + "\n")
            count = count + 1
    wfile.close()


# 逐行写入文件
def read_line(episode):
    path = "./subtitle4/s4_{e}.vtt".format(e=episode)
    file = open(path, "r").readlines()
    wfile = open("./s4_subtitle_text/s4_{e}.txt".format(e=episode), "w")
    for i in file:
        num = re.search("^[A-Za-z].+\n", i)
        if num != None:
            content = num.group()
            if content != "WEBVTT\n":
                wfile.write(content)
    wfile.close()


def replace_lines():
    files = os.listdir("./subtitle4/")
    for i in files:
        name = re.search("(\d+)\.", i)
        # print(name.groups()[0])
        read_line(name.groups()[0])


def insert_subtitle():
    files = os.listdir("s4_subtitle_text")
    for i in files:
        con = open("s4_subtitle_text/" + i, "r").read()
        con = con.replace("\"", "'")
        episode = re.search("s4_(\d+).", i).groups()[0]
        # print(episode)
        db.insert_content(4, episode, json.dumps(con))
        # print(json.dumps(con))


insert_subtitle()

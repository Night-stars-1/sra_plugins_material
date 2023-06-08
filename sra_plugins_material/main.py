'''
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2023-06-08 14:19:52
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2023-06-09 00:38:52
Description: 

Copyright (c) 2023 by Night-stars-1, All Rights Reserved. 
'''
from . import *

import re
import time
import orjson

from get_width import get_width
from utils.calculated import calculated
from utils.log import log
from subprocess import run, DEVNULL
from utils.config import read_json_file, modify_json_file, CONFIG_FILE_NAME

data = {
    "version": 2,
    "profiles": {
        "1": {
            "id": "temp",
            "name": "Default",
            "key": "1"
        }
    },
    "storageActionIdx": 1686216111025,
    "nextIdx": 2,
    "data": {
        "stores": {
            "1_inventory": {
                "items": {
                },
                "version": 1
            }
        }
    },
    "curAccountIdx": "1"
}

name2id = {'(信用点)': '29328', '(风雪之角)': '67219', '(苦寒晶壳)': '67220', '(命运的足迹|命运的足边)': '125435', '(生日之影的雷冠|住日之影的雷冠)': '151160', '(炼形者雷枝)': '151161', '(暴风之眼)': '267805', '(守护者的悲愿|于护者的悲愿)': '270195', '(虚幻铸铁)': '351746', '(漫游指南)': '409960', '(冒险记录)': '409961', '(旅情见闻)': '409962', '(往日之影的金饰)': '468391', '(铁卫扣饰)': '549407', '(古代零件)': '549408', '(掠夺的本能)': '549437', '(熄灭原核)': '549438', '(工造机杆|工造机杼|工造机柠)': '549503', '(永寿幼芽)': '549504', '(铁卫军徽)': '633348', '(古代转轴)': '633349', '(篡改的野心)': '633378', '(微光原核)': '633379', '(工造迥轮)': '633444', '(永寿天华)': '633445', '(青铜的执着)': '635668', '(黑黯音淡黑曜)': '635669', '(谐乐小话|谐乐小调)': '635670', '(丰饶之种)': '635671', '(破碎残办|破碎残刀)': '635673', '(猎兽之矢)': '635674', '(灵感之钥)': '635675', '(提纯以太)': '694487', '(凝缩以太)': '694488', '(稀薄以太)': '694489', '(铁卫勋章)': '717289', '(古代引擎)': '717290', '(践踏的意志)': '717319', '(蠢动原核)': '717320', '(工造浑心)': '717385', '(永寿荣枝)': '717386', '(深邃的星外质)': '782692', '(琥珀的坚守)': '836254', '(沉沦黑曜)': '836255', '(群星乐章)': '836256', '(永恒之花)': '836257', '(净世残办)': '836259', '(逐星之矢)': '836260', '(智识之钥)': '836261', '(铁狠碎齿|铁狼碎齿)': '866633', '(寒铁的誓言)': '920195', '(虑虚空黑曜)': '920196', '(家族颂歌)': '920197', '(生命之芽)': '920198', '(无生残办|无生残刀)': '920200', '(屠魔之矢)': '920201', '(启迪之钥)': '920202', '(恒温晶壳)': '983278', '(毁灭者的末路)': '985668'}

pos_data = [(9, 19), (16, 20), (22, 20), (29, 20), (35, 19), (41, 20), (48, 19), (55, 19), (61, 20), (9, 33), (16, 33), (22, 32), (28, 33), (35, 33), (42, 33), (49, 32), (55, 33), (61, 32), (10, 46), (16, 45), (21, 45), (29, 45), (35, 45), (42, 44), (48, 45), (54, 45), (61, 45), (9, 59), (15, 59), (22, 59), (29, 59), (37, 59), (41, 59), (48, 59), (54, 60), (60, 59), (10, 73), (16, 73), (22, 74), (29, 73), (35, 73), (42, 73), (49, 73), (56, 74), (62, 74), (9, 84), (16, 83), (22, 83), (29, 83), (36, 83), (42, 83), (48, 84), (54, 83), (62, 83)]

calculated1 = None
calculated2 = None

def open_knapsack():
    global calculated1
    start_time = time.perf_counter()
    while True:
        calculated1.keyboard.press("b")
        key_time = time.perf_counter()
        while time.perf_counter() - key_time < 1:
            pass
        calculated1.keyboard.release("b")
        knapsack_status = calculated1.part_ocr((3,2,10,10))
        if calculated1.check_list(".*背.*包.*", knapsack_status):
            log.info("进入背包")
            break
        if time.perf_counter() - key_time > 10:
            continue

def main(e=None):
    global calculated1
    global calculated2
    get_width("崩坏：星穹铁道")
    calculated1 = calculated()
    calculated2 = calculated(det_model_name="en_PP-OCRv3_det", rec_model_name="en_PP-OCRv3", number=True)
    calculated1.switch_window()
    import pyautogui # 缩放纠正
    open_knapsack()
    credit_value:dict = calculated2.part_ocr((79,4,85,7))
    credit_value = next(iter(credit_value), 0)
    data["data"]["stores"]["1_inventory"]["items"]['29328'] =  {"count": int(credit_value)}
    last_name = ""
    for pos in pos_data:
        calculated1.Relative_click(pos,0)
        time.sleep(0.1)
        article_name:dict = calculated1.part_ocr((70,10,85,15))
        article_value:dict = calculated2.part_ocr((75,25,80,34))
        matched_keys = [key for key in name2id if any(re.search(key, k) for k in article_name)]
        article_name = matched_keys[0] if matched_keys else next(iter(article_name), '无')
        article_id = name2id.get(article_name, None)
        if not article_id:
            log.info(article_name)
        article_value = next(iter(article_value), 0)
        if last_name == article_name:
            break
        if article_id:
            data["data"]["stores"]["1_inventory"]["items"][article_id] =  {"count": int(article_value)}
        last_name = article_name
    __, file_path = read_json_file("plugins\sra_plugins_material\data.json", path=True)
    with open(file_path, "wb") as f:
        f.write(orjson.dumps(data, option=orjson.OPT_PASSTHROUGH_DATETIME | orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_INDENT_2))
    log.info(f"请访问:https://starrailstation.com/cn/settings#planner，点击\033[0;31;40mimport backup\033[0m将{file_path}上传")

@hookimpl
def add_option(SRA):
    return SRA.add_option("背包材料识别", main, 2)

#!/usr/bin/python3
"""create"""
import sys
import os.path as path


save1 = __import__('7-save_to_json_file').save_to_json_file
load1 = __import__('8-load_from_json_file').load_from_json_file


list1 = []
args = sys.argv[1:]

if path.exists("add_item.json"):
    list1 = load1("add_item.json")  # load return a list
save1(list1 + args, "add_item.json")  # toma una list y la serializa

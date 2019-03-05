#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
import os


""" 获取处理历史 """
def get_history(file:str, history:set):
	with open(file, 'r', encoding='utf8') as fr:
		basePath = '/'.join(file.split('/')[:-2])
		for line in fr.readlines():
			line = line.strip()
			if '' == line:
				continue
			history.add(basePath + '/' + line)
	return history


""" 获取文件夹 """
def get_dir_list(dir:str, dirs:list):
	for i in os.listdir(dir):
		childPath = os.path.join(dir, i)
		if os.path.isdir(childPath):
			dirs.append(childPath)
	return dirs


""" 获取文件 """
def get_book_list(dir:str, files:list):
	for i in os.listdir(dir):
		childPath = os.path.join(dir, i)
		if os.path.isfile(childPath):
			files.append(childPath)
	return files

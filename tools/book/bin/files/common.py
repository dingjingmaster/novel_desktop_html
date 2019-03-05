#!/usr/bin/env python
# -*- encoding=utf-8 -*-
import os


""" 获取文件 """
def get_book_list(dir:str, files:list):
	for i in os.listdir(dir):
		childPath = os.path.join(dir, i)
		if os.path.isfile(childPath):
			files.append(childPath)
	return files


""" 获取文件名 """
""" 获取待处理文件路径和名字 """
def get_book_name(path:str)->str:
	arrs = []
	arr = path.split('/')
	for i in arr:
		tp = i.split('\\')
		if len(tp) == 1:
			arrs.append(tp[0])
		elif len(tp) > 1:
			for j in tp:
				arrs.append(j)
	return arrs[-1].split('.')[0].strip()
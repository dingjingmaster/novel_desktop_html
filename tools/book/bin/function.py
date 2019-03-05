#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
import os
import sys
sys.path.append('files')

from book_detail import BookDetailFactory

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


""" 获取待处理文件路径和名字 """
def get_dir_info(dir:str)->[str,str]:
	arrs = []
	arr = dir.split('/')
	for i in arr:
		tp = i.split('\\')
		if len(tp) == 1:
			arrs.append(tp[0])
		elif len(tp) > 1:
			for j in tp:
				arrs.append(j)
	return '/'.join(arrs[:-1]).strip(), arrs[-1].strip()


""" 保存历史文件 """
def save_history(histroy:set, savePath:str):
	with open(savePath, 'w', encoding='utf8') as fw:
		for line in histroy:
			fw.write(line + '\n')
	return


""" 开始处理文件夹 """
def start_detail(history:set, dirlist:list, resultPath:str):
	for dir in dirlist:
		basePath, dirTmp = get_dir_info(dir)
		if dirTmp in history:
			continue
		detail = BookDetailFactory.book_detail(dir, dirTmp, resultPath)
		detail.run()
		history.add(dirTmp)
	return history

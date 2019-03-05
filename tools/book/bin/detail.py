#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
import sys
sys.path.append('.')

from function import get_history
from function import get_dir_list
from function import get_book_list

if __name__ == '__main__':
	workDirPath = '/'.join(sys.argv[0].split('/')[:-2])
	resourcePath = workDirPath + '/resource'
	resultPath = workDirPath + '/result'
	historyPath = workDirPath + '/bin/history.txt'

	history = set()                                         # 已处理的文件
	dirlist = []                                            # 要处理的文件

	get_history(historyPath, history)                       # 获取历史书籍
	get_dir_list(resourcePath, dirlist)                     # 获取待处理的文件夹
	
	exit(0)

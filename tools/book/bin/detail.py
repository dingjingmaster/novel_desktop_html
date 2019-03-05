#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
import sys
sys.path.append('.')

from function import get_dir_list
from function import get_book_list

if __name__ == '__main__':
	workDirPath = '/'.join(sys.argv[0].split('/')[:-2])
	resourcePath = workDirPath + '/resource'
	resultPath = workDirPath + '/result'
	historyPath = workDirPath + '/bin/history.txt'
	
	dirlist = []
	
	get_dir_list(resourcePath, dirlist)
	
	print(dirlist)
	
	exit(0)

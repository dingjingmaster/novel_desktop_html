#!/usr/bin/env python
# -*- encoding='utf8' -*-
import os
import time

from abc import ABCMeta, abstractmethod


class DetailBase:
	def __init__(self, dir: str, save: str):
		self.dir = dir
		self.save = save

	@abstractmethod
	def run(self):
		pass

	def saveBook(self, name: str, author: str, category: str,  desc: str, chapter: dict):
		basePath = self.save + '/' + name
		tm = int(time.time())
		wordNum = 0
		if not (os.path.exists(basePath) and os.path.isdir(basePath)):
			os.mkdir(basePath)
		for ik, iv in chapter.items():
			wordNum += len(iv) + len(ik)
			fw = open(basePath + '/' + ik + '.txt', 'w', encoding='utf8')
			fw.write(iv + '\n')
			fw.close()
		fw = open(basePath + '/index.txt', 'w', encoding='utf8')
		fw.write(
			'书名:' + name + '\n' +
			'作者名:' + author + '\n' +
			'分类:' + category + '\n' +
			'状态:' + '连载\n' +
			'简介:' + desc + '\n' +
			'章节数:' + str(len(chapter)) + '\n' +
			'字数:' + str(wordNum) + '\n'
			'入库时间:' + str(tm) + '\n' +
			'更新时间:' + str(tm)
		)

	__metaclass__ = ABCMeta
	dir = ''
	save = ''

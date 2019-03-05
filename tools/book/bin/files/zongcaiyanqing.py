#!/usr/bin/env python3.7
# -*- encoding=utf8 -*-
import re
import sys
sys.path.append('.')

from common import get_book_list
from common import get_book_name
from detail_base import DetailBase
from character_trans_int import CharacterTransInt


""" 黑道分类书籍 """
class ZongcaiYanqing(DetailBase):
	def run(self):
		ci = CharacterTransInt()
		get_book_list(self.dir, self.__bookList)
		for book in self.__bookList:
			lines = []
			name, author, category, desc, chapter \
				= '', '', '', '', {}
			""" 检测作者名 + 书名 """
			nameAuthor = get_book_name(book)
			arr = nameAuthor.split(' ')
			if len(arr) != 2:
				continue
			name = arr[1]
			author = arr[0]
			
			""" 删除内容 """
			self.deleteKeyWord.append(author + '《' + name + '》')
			
			""" 分类名 """
			category = '总裁言情'
			
			""" 读取书籍内容 """
			try:
				with open(book, 'r', encoding='gbk', errors='ignore') as fr:
					for line in fr.readlines():
						line = line.strip()
						for dels in self.deleteKeyWord:
							line = re.sub(dels, '', line)
						if '' == line.strip():
							continue
						lines.append(line)
			except BaseException as e:
				print(book + '   ' + e.__str__())

			""" 描述 + 章节内容 """
			descFlag = True
			thisChapter = ''
			chapterSource = ''
			thisChapterTmp = ''
			chapterNum = ''
			for l in lines:
				for tr in self.chapterKeyWord:
					tpl = tr.search(l)
					if '' != tpl and tpl is not None:
						descFlag = False
						thisChapter = tpl.group()
						chapterSource = thisChapter
						thisChapterTmp = thisChapter
						chapterNum = thisChapter
						chapterNum = re.sub('[第章]', '', chapterNum)
						chapterNum = str(ci.chinese_to_arabic(chapterNum))
						if '0' != chapterNum:
							thisChapterTmp = '第' + chapterNum + '章'
						if thisChapter in chapter:
							print(name + '\t' + author + '\t' + thisChapter + '\t' + '可能错误!!!')
							continue
						else:
							thisChapter = thisChapterTmp
						chapter[thisChapter] = ''
				if '' != thisChapter:
					l = l.replace(chapterSource, thisChapter + '\n')
					chapter[thisChapter] += l + '\n'
				if descFlag and len(chapter) == 0:
					desc += l
			self.saveBook(name, author, category, desc, chapter)

	__bookList = []
	chapterKeyWord = [
		re.compile('^第.?\\S+.?章'),
		re.compile('^楔子'),
		re.compile('^序'),
	]
	deleteKeyWord = [
		re.compile('\\s?', re.U),
		re.compile('☆\\S+☆', re.U),
	]


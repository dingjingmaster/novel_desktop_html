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
class HeiDao(DetailBase):
	def run(self):
		ci = CharacterTransInt()
		get_book_list(self.dir, self.__bookList)
		for book in self.__bookList:
			name, author, category, desc, chapter \
				= '', '', '', '', {}
			""" 检测书名 """
			name = get_book_name(book)
			category = '黑道'
			lines = []
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
			""" 检测作者名 """
			author = lines[0]
			author = author.replace(name, '')
			author = re.sub('[\\(|\\)]', '', author)
			""" 检测描述信息及章节信息 """
			descFlag = True
			thisChapter = ''
			for l in lines:
				if l == lines[0]:
					continue
				for tr in self.chapterKeyWord:
					tpl = tr.search(l)
					if '' != tpl and tpl is not None:
						descFlag = False
						thisChapter = tpl.group()
						chapterNum = thisChapter
						chapterNum = re.sub('[第章]', '', chapterNum)
						chapterNum = str(ci.chinese_to_arabic(chapterNum))
						if chapterNum != '0':
							thisChapter = '第' + chapterNum + '章'
						if thisChapter in chapter:
							raise Exception(name + '\t' + author + '\t' + l)
						chapter[thisChapter] = ''
				if '' != thisChapter:
					chapter[thisChapter] += l + '\n'
				if descFlag and len(chapter) == 0:
					desc += l
			self.saveBook(name, author, category,  desc, chapter)

	__bookList = []
	chapterKeyWord = [
		re.compile('第.?\\S+.?章'),
		re.compile('楔子')
	]
	deleteKeyWord = [
		re.compile('\\s?', re.U),
		re.compile('您下载的文件来自http://asuro.cn/bbs/愛書啰大雜燴由 『猪啊猪啊』 为你制作', re.U),
		re.compile('<愛書啰大雜燴-TXT论坛>-全力为你提供最新最全的txt文本格式电子书下载', re.U),
		re.compile('jjwxc', re.U),
		re.compile('晋江文学城\\S?扫描\\S?校对', re.U),
		re.compile('小瓶子整理制作', re.U),
		re.compile('ＸＫＸ', re.U),
		re.compile('言情小说\\S?武侠小说\\S?古典小说\\S?现代小说\\S?科幻小说\\S?侦探小说\\S?纪实小说\\S?军事小说\\S?外国小说\\S?小说更新列表', re.U),
		re.compile('\\d?-\\d?潇湘书院版权所有\\S?小说阅读网站', re.U),
		re.compile('狐狸新娘与黑道少主.第\\S?章\\S+潇湘书院', re.U),
		re.compile('小说分类导航 ： 原创小说 ｜ 言情小说 ｜ 武侠小说 ｜ 古典小说 ｜ 现代小说 ｜ 科幻小说 ｜ 侦探小说 ｜ 纪实小说 ｜ 军事小说 ｜ 外国小说 ｜ 更新列表', re.U),
	]


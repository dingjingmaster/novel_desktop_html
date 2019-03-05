#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from heidao import HeiDao
from zongcaiyanqing import ZongcaiYanqing
from detail_base import DetailBase


class BookDetailFactory:
	@staticmethod
	def book_detail(dir: str, name: str, save: str):
		if '黑道' == name:
			return HeiDao(dir, save)
		elif '总裁系列言情' == name:
			return ZongcaiYanqing(dir, save)
		else:
			return DetailBase(dir, save)

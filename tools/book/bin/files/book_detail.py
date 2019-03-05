#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from heidao import HeiDao


class BookDetailFactory:
	@staticmethod
	def book_detail(dir: str, name: str, save: str):
		if '黑道' == name:
			return HeiDao(dir, save)

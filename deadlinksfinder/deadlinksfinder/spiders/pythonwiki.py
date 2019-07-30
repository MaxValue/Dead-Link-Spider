# -*- coding: utf-8 -*-
import scrapy

class PythonwikiSpider(scrapy.Spider):
	name = 'pythonwiki'
	allowed_domains = ['wiki.python.org']
	start_urls = ['https://wiki.python.org/moin/GesuchteSeiten']
	# https://wiki.python.org/moin/RecentChanges

	def parse(self, response):
		...
		# store wiki page
		# store links

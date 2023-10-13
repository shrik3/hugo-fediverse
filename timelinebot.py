#!/usr/bin/env python
from mastodon import Mastodon
import config as cfg
import time
import re
import os
import re
import utils
import json

class TLBot():
	def __init__(self, config=cfg):
		self.config = cfg

	def init_app(self):
		self.session = Mastodon.create_app(self.config.APPNAME, api_base_url=self.config.BASEURL, to_file=self.config.CLIENTID)

	def init_session(self):
		if not os.path.isfile(self.config.CLIENTID):
			print("[booting] client data doesn't exist..creating...")
			self.session = self.init_app()
		else:
			self.session = Mastodon(client_id=self.config.CLIENTID, access_token=self.config.TOKEN, feature_set="pleroma")
		try:
			self.session.account_verify_credentials()
		except:
			print("invalid credentials, trying to log in with pw")
			try:
				self.login()
			except Exception as e:
				print("can't log in, abort")
				print(e)
				exit()

	def login(self):
		print("trying manual login")
		if self.config.UNAME == "" or self.config.PW == "":
			(self.config.UNAME, self.config.PW) = cfg.get_secrets_from_input()
		try:
			self.session.log_in(username=self.config.UNAME,password=self.config.PW, to_file=self.config.TOKEN)
		except Exception as e:
			print("log in failed, check your credentials")
			print(e)
			exit()

	def get_sanitized_timeline_json(self):
		# TODO make this config options
		tl = self.session.timeline_home(limit=40)
		results = []
		for status in tl:
			s = {}
			if self.config.PUBLIC_ONLY and status['visibility'] != 'public':
				continue
			if status['account']['acct'] != self.config.FOLLOW:
				continue
			if self.config.NO_REBLOG and status['reblog'] != None:
				continue
			s['account'] = status['account']['acct']
			s['content'] = utils.sanitize_html(status['content'])
			s['created_at'] = status['created_at']
			s['url'] = status['url']
			results.append(s)
		sorted_list = sorted(results, key=lambda d: d['created_at'], reverse=True)
		# format datetime string:
		for s in sorted_list:
			s['created_at'] = s['created_at'].strftime("%m/%d/%Y")
		return sorted_list

if __name__ == "__main__":
	bot = TLBot(cfg)
	bot.init_session()
	sl = bot.get_sanitized_timeline_json()
	file = cfg.OUTPUT_JSON_FILE
	with open(file, 'w', encoding='utf8') as json_file:
		json.dump(sl, json_file, ensure_ascii=False)

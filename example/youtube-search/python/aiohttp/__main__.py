#!/usr/bin/env python3

## $ sudo apt-get install python3-aiohttp
## https://aiohttp.readthedocs.io/en/stable/
## https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request

import aiohttp
import asyncio

class YouTubeSearch:

	_App = None

	def getApp (self):
		return self._App

	def setApp (self, val):
		self._App = val
		return self


	_Keyword = ''

	def getKeyword (self):
		return self._Keyword

	def setKeyword (self, val):
		self._Keyword = val
		return self

	def run (self):
		loop = asyncio.get_event_loop()
		loop.run_until_complete(self.go())

	async def fetch (self, session, url):
		async with session.get(url) as response:
			#return await response.text()
			return await response.json()

	async def go (self):
		async with aiohttp.ClientSession() as session:
			from urllib.parse import urlencode
			opt = {
				'key': '{YOUR_API_KEY}',
				'part': 'snippet',
				'type': 'video',
				'maxResults': 10,
				'order': 'relevance',
				'prettyPrint': 'false',
				'q': self.getKeyword()
			}
			query = urlencode(opt)
			url = 'https://www.googleapis.com/youtube/v3/search?{query}'.format(query=query)
			#print(url) ## https://www.googleapis.com/youtube/v3/search?key=%7BYOUR_API_KEY%7D&part=snippet&type=video&maxResults=10&order=relevance&prettyPrint=false&q=blcak+bird
			#print("\n")


			json = await self.fetch(session, url)
			list = []
			#print(json['items'])

			for atom in json['items']:

				#print(atom)
				#print("\n")

				if atom['id']['kind'] == 'youtube#video':
					#print(item['id']['videoId'])

					item = {}
					item['title'] = atom['snippet']['title']
					item['id'] = atom['id']['videoId']
					#item['url'] = 'https://www.youtube.com/watch?v={id}'.format(id=item['id'])
					list.append(item)

			self.getApp().go_load_list(list)

class App:
	def run (self):
		YouTubeSearch().setKeyword('blcak bird').setApp(self).run()

	def go_load_list (self, list):
		total = 0

		for item in list:
			total += 1
			print('id: {}'.format(item['id']))
			print('title: {}'.format(item['title']))
			#print('url: {}'.format(item['url']))
			print('mpv_play_command_1: mpv ytdl://{id}'.format(id=item['id']))
			print('mpv_play_command_2: mpv --cache-secs=600 ytdl://{id}'.format(id=item['id']))
			print("mpv_play_command_3: mpv 'https://www.youtube.com/watch?v={id}'".format(id=item['id']))
			print("firefox_view_command: firefox 'https://www.youtube.com/watch?v={id}'".format(id=item['id']))
			print("youtube_dl_download_command_1: youtube-dl 'https://www.youtube.com/watch?v={id}'".format(id=item['id']))
			print("youtube_dl_download_command_2: youtube-dl '{id}'".format(id=item['id']))

			print('')

if __name__ == '__main__':
	App().run()

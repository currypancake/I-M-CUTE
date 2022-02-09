from tkinter import *
from bs4 import BeautifulSoup
from _info import CardInfo
import requests

# ------------*save Image*------------------------

def saveImage(r, kind, rare, i, j, P, extension):
	img_url = f'http://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2021081301%2Fcard%2F{kind}%2F{CardInfo.character[i]}_{rare}{j}{P}{r.scode}.{extension}'
	img_req = requests.get(img_url, cookies=r.dummy_cookies, headers=r.headers, stream=True)

	if kind == 'bromide/l':
		img_name = f'{CardInfo.character[i]}_SRBR{j}{P}.jpg'

	elif kind == 'l' :
		temp = CardInfo.character[i].split('_')[1]
		chara_name = temp[2:len(temp) - 1]
		img_name = f'{chara_name}{rare}{j}{P}.jpg'
	else :
		chara_name = CardInfo.character[i].split('_', 1)
		img_name = f'{chara_name[1]}_{rare}{j}{P}.png'

	res = r.dir_path + '/' + img_name
	with open(res, 'wb') as f:
		f.write(img_req.content)


def saveAllImage(r, rare, i, j):
	r.makeDir('../standing')
	saveImage(r, 'quest', rare, i, j, '', 'png')
	saveImage(r, 'quest', rare, i, j, 'P', 'png')

	r.makeDir('../frameCard')
	saveImage(r, 'l', rare, i, j, '', 'jpg')
	saveImage(r, 'l', rare, i, j, 'P', 'jpg')

	if rare == 'SR':
		r.makeDir('../bromide')
		saveImage(r, 'bromide/l', rare, i, j, '', 'jpg')
		saveImage(r, 'bromide/l', rare, i, j, 'P', 'jpg')

# # -------------------------------------------------

# # ------------*check Image*------------------------

def isImage(r, rare, i, j, P):
	img_url = f'http://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2021081301%2Fcard%2Fquest%2F{CardInfo.character[i]}_{rare}{j}{P}{r.scode}.png'
	img_req = requests.get(img_url, cookies=r.dummy_cookies, headers=r.headers, stream=True)
	soup = BeautifulSoup(img_req.text, 'html.parser')
	target = soup.find(text='Not Found')

	if target is None :
		return (True)
	return (False)

def setCardInfo(rare, i, j, fuck):
	bromide = f'{CardInfo.character[i]}_SRBR{j}P.jpg'

	temp = CardInfo.character[i].split('_', 1)
	stand = f'{temp[1]}_{rare}{j}P.png'

	temp = CardInfo.character[i].split('_')[1]
	chara_name = temp[2:len(temp) - 1]
	frame = f'{chara_name}{rare}{j}P.jpg'
	
	card = CardInfo(rare, chara_name, stand, bromide, frame, fuck)
	return (card)

def checkCard(cards, r, i, j):
	after = isImage(r, 'SR', i, j, 'P')
	if after == True :
		before = isImage(r, 'SR', i, j, '')
		if before == False:
			cards.addImage(setCardInfo('SR', i, j, 1))
			r.makeDir('../standing')
			saveImage(r, 'quest', 'SR', i, j, 'P', 'png')

			r.makeDir('../frameCard')
			saveImage(r, 'l', 'SR', i, j, 'P', 'jpg')

			r.makeDir('../bromide')
			saveImage(r, 'bromide/l', 'SR', i, j, 'P', 'jpg')

		else:
			cards.addImage(setCardInfo('SR', i, j, 0))
			saveAllImage(r, 'SR', i, j)

def findSRImage(cards, r):
	# 쥬피터 ~ 코가도
	for i in range(1, 42) :
		for j in range(cards.s1, cards.s2) :
			checkCard(cards, r, i, j)

	# 깃발 ~ 레제
	for i in range(42, 47) :
		for j in range(cards.s3, cards.s4) :
			checkCard(cards, r, i, j)

def findRImage(cards, r):
	# 쥬피터 ~ 깃발
	for i in range(1, 44) :
		for j in range(cards.r1, cards.r2) :
			find = isImage(r, 'R', i, j, 'P')
			if find == True:
				cards.addImage(setCardInfo('R', i, j, 0))
				saveAllImage(r, 'R', i, j)

	# 레제
	for i in range(44, 47) :
		for j in range(cards.r3, cards.r4) :
			find = isImage(r, 'R', i, j, 'P')
			if find == True:
				cards.addImage(setCardInfo('R', i, j, 0))
				saveAllImage(r, 'R', i, j)

# -------------------------------------------------

# ------------*Event Image*------------------------

def saveEventImage(r, img_url, img_name):
	img_req = requests.get(img_url, cookies=r.dummy_cookies, headers=r.headers, stream=True)
	dir_path = '../event'
	r.makeDir(dir_path)
	res = dir_path + '/' + img_name
	with open(res, 'wb') as f:
		f.write(img_req.content)

def setEventImage(r, e):
	# event banner
	img_url = f'http://sp.pf-img-a.mbga.jp/12017647?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2022020702%2F%2Fbanner%2Fevent%2Fbanner_event_{e.event_num}{e.event_code}.png'
	saveEventImage(r, img_url, e.event_banner)
	# gacha banner
	img_url = f'http://sp.pf-img-a.mbga.jp/12017647?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2022020702%2F%2Fbanner%2Fgacha%2Fbanner_eventgacha_{e.event_num}{e.event_code}.png'
	saveEventImage(r, img_url, e.gacha_banner)

# -------------------------------------------------

def save(label, cards, e, r):
	with requests.Session() as s:
		try:
			label.config(text="Start downloading SR images...")
			findSRImage(cards, r)
			label.config(text="All SR images are downloaded.")
			
			label.config(text="Start downloading R images...")
			findRImage(cards, r)
			label.config(text="All R images are downloaded.")

			label.config(text="Start downloading Event images...")
			setEventImage(r, e)
			label.config(text="All Event images are downloaded.")

		except:
			label.config(text="Image Download Error......")

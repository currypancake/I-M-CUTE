import json
from datetime import datetime, timedelta

# ------------*set Data*------------------------

def setType(cards, info, chara):
	if chara['k_name'] == cards.point_r:
		info.setType('포인트')
	elif chara['k_name'] == cards.ranking_r or chara['k_name'] == cards.ranking_sr :
		info.setType('랭킹')
	else :
		info.setType('가챠')

def find_chara(info):
	with open('../utils/chara_info.json', encoding='UTF-8') as json_file:
		json_data = json.load(json_file)

		for i in json_data:
			if json_data[i]['e_name'] == info.name:
				chara = json_data[i]
	return (chara)


def calu_cost(info):
	if info.rare == 'SR':
		cost = '16'
	if info.rare == 'R':
		if info.type == '포인트':
			cost = '8'
		elif info.type == '랭킹':
			cost = '9'
		else :
			cost = '10'
	return (cost)


def get_scout(e, info):
	if info.type == '가챠' and info.fuck == 0:
		return ("기간한정 「[[" + e.gacha + "]]」 가챠")
	if info.type == '가챠' and info.fuck == 1:
		return ("기간한정 「[[" + e.fuck_gacha + "]]」 가챠")
	return ("이벤트 「[[" + e.event + "]]」 " + info.type + "보상")


def get_spec(info, chara):
	if info.type == 'SR' :
		return (chara['specialization'] + " 대 UP")
	return (chara['specialization'] + " 중 UP")

# # -------------------------------------------------

# ------------*write chara Info*-----------------

def default_card(e, cards, info, file) :
	chara = find_chara(info)
	setType(cards, info, chara)
	
	file = file.replace('k_name', chara['k_name'])
	file = file.replace('j_name', chara['j_name'])
	file = file.replace('card_nameP', info.frame)
	file = file.replace('card_name', info.frame.replace('P', ''))
	file = file.replace('_rare', info.rare)
	file = file.replace('cost', calu_cost(info))
	file = file.replace('specialization', get_spec(info, chara))
	file = file.replace('event', get_scout(e, info))

	return (file)

def one_card(e, cards, info, file) :
	chara = find_chara(info)
	info.type = '가챠'

	file = file.replace('k_name', chara['k_name'])
	file = file.replace('j_name', chara['j_name'])
	file = file.replace('card_name', info.frame)
	file = file.replace('_rare', info.rare)
	file = file.replace('cost', calu_cost(info))
	file = file.replace('specialization', get_spec(info, chara))
	file = file.replace('event', e.fuck_gacha)

	return (file)

def open_file(e, cards, info, res_file, script_file, card_file):
	f = open(res_file, "a", encoding='UTF-8')
	fscript = open(script_file, "r", encoding='UTF-8')
	fcard = open(card_file, "r", encoding='UTF-8')
	
	script = fscript.read()
	card = fcard.read()
	
	fscript.close()
	fcard.close()

	if info.fuck == 1:
		f.write(one_card(e, cards, info, card))
		f.write("\n\n")
		f.write(one_card(e, cards,info, script))
		f.write("\n\n=================\n\n")
	else :
		f.write(default_card(e, cards, info, card))
		f.write("\n\n")
		f.write(default_card(e, cards, info, script))
		f.write("\n\n=================\n\n")

	f.close();

# # -------------------------------------------------

# ------------*write event Info*---------------------

def find_index(info):
	with open('../utils/chara_info.json', encoding='UTF-8') as json_file:
		json_data = json.load(json_file)

		cnt = 0
		for i in json_data:
			if json_data[i]['e_name'] == info.name:
				break
			cnt += 1
	return (cnt)

def return_k_name(name):
	with open('../utils/chara_info.json', encoding='UTF-8') as json_file:
		json_data = json.load(json_file)

		for i in json_data:
			if json_data[i]['e_name'] == name:
				return (json_data[i]['k_name'])
	return (0)

def write_info(i, page, chara, num):
	print()
	page = page.replace(f'event_idol{num}_name', chara['k_name'])
	page = page.replace(f'event_idol{num}_j_name', chara['j_name'])
	page = page.replace(f'event_idol{num}_bromideP', i.bromide)
	page = page.replace(f'event_idol{num}_bromide', i.bromide.replace('P', ''))
	page = page.replace(f'event_idol{num}_standP', i.stand)
	page = page.replace(f'event_idol{num}_stand', i.stand.replace('P', ''))
	page = page.replace(f'event_idol{num}', i.frame)

	return (page)

def write_event_page(cards, e):
	f = open('../event_page.txt', 'w', encoding='UTF-8')
	fpage = open('../utils/event.txt', "r", encoding='UTF-8')
	page = fpage.read()
	fpage.close()

	now_ = datetime.now()
	end_ = now_ + timedelta(days=e.day)

	page = page.replace('event_num', str(e.event_num))
	page = page.replace('end_year', str(end_.year))
	page = page.replace('end_month', str(end_.month))
	page = page.replace('end_day', str(end_.day))
	page = page.replace('year', str(now_.year))
	page = page.replace('month', str(now_.month))
	page = page.replace('day', str(now_.day))

	page = page.replace('gacha_name', e.gacha)

	done = 0
	member = {}

	for i in cards.image_list:
		if i.fuck != 1:
			chara = find_chara(i)
			if i.rare == 'SR' and i.type == '랭킹':
				page = write_info(i, page, chara, 1)
			elif i.rare == 'R' and i.type == '랭킹':
				page = write_info(i, page, chara, 2)
			elif i.rare == 'R' and i.type == '포인트':
				page = write_info(i, page, chara, 3)
			elif i.rare == 'SR' and i.type == '가챠':
				page = write_info(i, page, chara, 4)
			elif i.rare == 'R' and i.type == '가챠' and done == 0:
				page = write_info(i, page, chara, 5)
				done = 1
			elif i.rare == 'R' and i.type == '가챠' and done == 1:
				page = write_info(i, page, chara, 6)
				done = 2
			temp = find_index(i)
			member[temp] = i.name

	res = sorted(member.items())

	num = 1
	for i in res:
		page = page.replace(f'idol{num}', return_k_name(i[1]))
		num += 1;

	if done == 1 :
		page = page.replace('|[[file:event_idol6]]', '')
		page = page.replace('|[[event_idol6_name/카드 목록#【】event_idol6_j_name|【】event_idol6_j_name]]', '')
		page = page.replace('|[[file:event_idol6_stand]]', '')
		page = page.replace('|[[file:event_idol6_standP]]', '')
		page = page.replace('!idol6|| 제목 || 링크(있으면)', '')
		page = page.replace('!가챠R2', '')

	if done == 2:
		page = page.replace('!가챠R2', '!가챠R')

	f.write(page)

	f.close()

# # -------------------------------------------------

def auto_write(cards, e):
	for i in cards.image_list:
		if i.fuck == 1:
			open_file(e, cards, i, "../one_res.txt", '../utils/one_script.txt', "../utils/one_card.txt")
		else :
			open_file(e, cards, i, "../res.txt", '../utils/script.txt', "../utils/card.txt")

	write_event_page(cards, e)

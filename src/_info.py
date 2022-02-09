import os

class CardInfo:
	# 캐릭터 목록
	character = [
		'no',
		'01jupiter_01toumaa_2',		# 1
		'01jupiter_02syoutam_3',	# 2
		'01jupiter_03hokutoi_1',	# 3
		'02drasta_01terut_2',		# 4
		'02drasta_02kaorus_1',		# 5
		'02drasta_03tubasak_3',		# 6
		'03alte_01keit_3',			# 7
		'03alte_02reik_1',			# 8
		'04beit_01kyoujit_1',		# 9
		'04beit_02pierre_3',		# 10
		'04beit_03minoriw_2',		# 11
		'05w_01yusukea_3',			# 12
		'05w_02kyosukea_1',			# 13
		'06frame_01hideoa_1',		# 14
		'06frame_02ryuk_2',			# 15
		'06frame_03seijis_3',		# 16
		'07sai_01kirion_1',			# 17
		'07sai_02syomah_3',			# 18
		'07sai_03kuros_3',			# 19
		'08highj_01hayatoa_2',		# 20
		'08highj_02junf_1',			# 21
		'08highj_03natukis_1',		# 22
		'08highj_04harunaw_3',		# 23
		'08highj_05sikii_2',		# 24
		'09godp_01suzakua_2',		# 25
		'09godp_02genbuk_1',		# 26
		'10cafe_01yukihirok_3',		# 27
		'10cafe_02souichiros_1',	# 28
		'10cafe_03asselin_2',		# 29
		'10cafe_04makiou_3',		# 30
		'10cafe_05sakim_2',			# 31
		'11mofu_01naoo_1',			# 32
		'11mofu_02sirot_2',			# 33
		'11mofu_03kanonh_3',		# 34
		'12sem_01michioh_1',		# 35
		'12sem_02ruim_3',			# 36
		'12sem_03jiroy_1',			# 37
		'13kogado_01takerut_2',		# 38
		'13kogado_02michirue_2',	# 39
		'13kogado_03reng_2',		# 40
		'14flags_01ryoa_3',			# 41
		'14flags_02daigok_2',		# 42
		'14flags_03kazukit_1',		# 43
		'15legend_01amehikok_1',	# 44
		'15legend_02sorak_3',		# 45
		'15legend_03chrisk_1'		# 46
	]

	def __init__(self, rare, name, stand, bromide, frame, fuck):
		self.rare = rare
		self.name = name
		self.stand = stand
		self.bromide = bromide
		self.frame = frame
		self.fuck = fuck;

	def setType(self, type):
		self.type = type

class Event:
	def __init__(self, event, gacha, code, num, day, fuck_gacha):
		self.event = event
		self.gacha = gacha
		self.event_code = code
		self.event_num = num
		self.fuck_gacha = fuck_gacha
		self.day = day
		self.event_banner = f'banner_event_{self.event_num}.png'
		self.gacha_banner = f'banner_eventgacha_{self.event_num}.png'


class CardImage:
	def __init__(self, point , r, sr):
		self.point_r = point
		self.ranking_r = r
		self.ranking_sr = sr
		self.image_list = []

	def addImage(self, _image):
		self.image_list.append(_image)

	def setSrRange(self, s1, s2, s3, s4):
		if s1 > s2 or s3 >s4 :
			print("wrong range.")
		if s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0:
			print("wrong range.")
		self.s1 = s1
		self.s2 = s2
		if s3 == 0:
			self.s3 = s1
		self.s3 = s3
		if s3 == 0:
			self.s4 = s2
		self.s4 = s4

	def setRRange(self, r1, r2, r3, r4):
		if r1 > r2 or r3 >r4 :
			print("wrong range.")
		if r1 < 0 or r2 < 0 or r3 < 0 or r4 < 0:
			print("wrong range.")
		self.r1 = r1
		self.r2 = r2
		if r3 == 0:
			self.r3 = r1
		self.r3 = r3
		if r3 == 0:
			self.r4 = r2
		self.r4 = r4


class RequestInfo:
	def __init__(self, code):
		self.scode = code
		self.set_data()

	def set_data(self):
		f = open('../utils/login_cookie.txt', 'r')
		self.login_cookie = f.read()
		f.close()

		self.user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
		self.headers = {'User-Agent': self.user_agent}
		self.dummy_cookies = {'SP_LOGIN_SESSION' : self.login_cookie}

	def makeDir(self, path):
		self.dir_path = path			
		if os.path.isdir(self.dir_path) == False:
			os.mkdir(self.dir_path)

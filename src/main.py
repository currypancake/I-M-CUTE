from cgitb import text
from tkinter import *
from _info import *
import save_image
import make_file

def closeWindow():
	window.destroy()

def execute_programe():
	r = RequestInfo(scode.get()) # _59822b672f
	e = Event(event_name.get(), gacha_name.get(), event_code.get(), int(event_num.get()), int(event_day.get()), fuck_gacha.get())
	# _dhhecgpnvks
	cards = CardImage(point_r.get(), rank_r.get(), rank_sr.get())
	cards.setSrRange(int(s1.get()), int(s2.get()) + 1, int(s3.get()), int(s4.get()) + 1)
	cards.setRRange(int(r1.get()), int(r2.get()) + 1, int(r3.get()), int(r4.get()) + 1)

	label = Label(window, text="I M CUTE")
	label.grid(row=6, column=2)

	res_btn['state'] = DISABLED

	save_image.save(label, cards, e, r)

	label.config(text="Start writing wiki files.")
	make_file.auto_write(cards, e)
	
	label.config(text="All Done!")	

	close_btn = Button(window, text="종료", command=closeWindow)
	close_btn.grid(row=20, column=1)

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


window = Tk()
window.title("I'm CUTE")

make_menu(window)

w = 570
h = 480
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
x = (sw - w)/2
y = (sh - h)/2

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False, False)


event_name_label = Label(window, text="이벤트 명")
event_name = Entry(window, width=20)
event_name_label.grid(row=0, column=0)
event_name.grid(row=0, column=1)
event_name.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

gacha_name_label = Label(window, text="가챠명")
gacha_name = Entry(window, width=20)
gacha_name_label.grid(row=1, column=0)
gacha_name.grid(row=1, column=1)
gacha_name.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

fuck_gacha_label = Label(window, text="거불카 가챠")
fuck_gacha = Entry(window, width=20)
fuck_gacha_label.grid(row=2, column=0)
fuck_gacha.grid(row=2, column=1)
fuck_gacha.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)


scode_label = Label(window, text="카드 보안코드")
scode = Entry(window)
scode_label.grid(row=0, column=2)
scode.grid(row=0, column=3)
scode.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

event_code_label = Label(window, text="이벤트 보안코드")
event_code = Entry(window)
event_code_label.grid(row=1, column=2)
event_code.grid(row=1, column=3)
event_code.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

event_num_label = Label(window, text="이벤트 번호")
event_num = Entry(window, width=20)
event_num_label.grid(row=2, column=2)
event_num.grid(row=2, column=3)
event_num.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

event_day_label = Label(window, text="이벤트 기간")
event_day = Entry(window, width=20)
event_day_label.grid(row=3, column=2)
event_day.grid(row=3, column=3)
event_day.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

#---

point_r_label = Label(window, text="포인트 보상")
point_r = Entry(window, width=20)
point_r_label.grid(row=5, column=0)
point_r.grid(row=5, column=1)
point_r.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

rank_r_label = Label(window, text="랭킹(R) 보상")
rank_r = Entry(window, width=20)
rank_r_label.grid(row=6, column=0)
rank_r.grid(row=6, column=1)
rank_r.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

rank_sr_label = Label(window, text="랭킹(SR) 보상")
rank_sr = Entry(window, width=20)
rank_sr_label.grid(row=7, column=0)
rank_sr.grid(row=7, column=1)
rank_sr.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

#---

srange_label = Label(window, text="SR 탐색 범위")
range1_label = Label(window, text="쥬피터 ~ 코가도")
range2_label = Label(window, text="깃발 ~ 레제")
srange_label.grid(row=10, column=1)
range1_label.grid(row=11, column=0)
range2_label.grid(row=13, column=0)

s1_label = Label(window, text="시작 번호")
s1 = Entry(window, width=20)
s1_label.grid(row=12, column=0)
s1.grid(row=12, column=1)

s2_label = Label(window, text="끝 번호")
s2 = Entry(window, width=20)
s2_label.grid(row=12, column=2)
s2.grid(row=12, column=3)

s3_label = Label(window, text="시작 번호")
s3 = Entry(window, width=20)
s3_label.grid(row=14, column=0)
s3.grid(row=14, column=1)

s4_label = Label(window, text="끝 번호")
s4 = Entry(window, width=20)
s4_label.grid(row=14, column=2)
s4.grid(row=14, column=3)

# #---

srange_label = Label(window, text="R 탐색 범위")
range1_label = Label(window, text="쥬피터 ~ 깃발")
range2_label = Label(window, text="레제")
srange_label.grid(row=15, column=1)
range1_label.grid(row=16, column=0)
range2_label.grid(row=18, column=0)

r1_label = Label(window, text="시작 번호")
r1 = Entry(window, width=20)
r1_label.grid(row=17, column=0)
r1.grid(row=17, column=1)

r2_label = Label(window, text="끝 번호")
r2 = Entry(window, width=20)
r2_label.grid(row=17, column=2)
r2.grid(row=17, column=3)

r3_label = Label(window, text="시작 번호")
r3 = Entry(window, width=20)
r3_label.grid(row=19, column=0)
r3.grid(row=19, column=1)

r4_label = Label(window, text="끝 번호")
r4 = Entry(window, width=20)
r4_label.grid(row=19, column=2)
r4.grid(row=19, column=3)

res_btn = Button(window, text="확인", command=execute_programe)
res_btn.grid(row=20, column=2)

window.mainloop()

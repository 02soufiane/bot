import pyautogui
import pyperclip
import random
import time


text=['LFG','LFG GUYS','hello','hype hype guys','i love this community','yes sure','lets do iiit','doo it brooo','OG broooo!','fine and uu','hype hype']
print("BOT start now....")
timesl=float(input("[+] dakhal taw9it b seconde:"))
number=int(input("[+] dakhal ch7al mn merra bghitih iktab:"))
for i in range(number):
	r=random.choice(text)
	pyperclip.copy(r)
	pyautogui.hotkey('ctrl','v')
	pyautogui.hotkey('enter')
	time.sleep(timesl)
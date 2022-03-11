#library
from datetime import date
from datetime import datetime
import webbrowser
import subprocess,json,time
import requests
import os
import ctypes	
import winshell
from colorama import Fore, Back, Style
import socket
import sys
import smtplib, ssl
import ctypes, sys
from socket import gaierror
#code
os.system("cls")
print(Fore.GREEN+"đang checking kết nối mạng")
try:
    requests.get('https://www.google.com/').status_code
    print(Fore.GREEN+"Connected to internet is successfully")
    pass
except:
	print(Fore.RED+"Connected to internet is not successfully please check your internet connection again ")
	print(Style.RESET_ALL)
	time.sleep(5)
	exit()

class ProgressBar(object):
    DEFAULT_BAR_LENGTH = 75
    DEFAULT_CHAR_ON  = '='
    DEFAULT_CHAR_OFF = ' '

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = self.__class__.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            self.__class__.DEFAULT_CHAR_ON  * int(self._levelChars),
            self.__class__.DEFAULT_CHAR_OFF * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __add__(self, other):
        assert type(other) in [float, int], "can only add a number"
        self.setAndPlot(self._level + other)
        return self
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__add__(-other)
    def __del__(self):
        sys.stdout.write("\n")

if __name__ == "__main__":
    count = 150
    print ("Loadding tool...")
    pb = ProgressBar(count)
    for i in range(0, count):
        pb += 1
        time.sleep(0.01)
    del pb

    print ("done")

b ="sever"
r = requests.get('https://api.npoint.io/365dfdd4fe77a000f2d2')
r = json.loads(r.text)
start = "\033[1m"
end = "\033[0;0m"
try:
	key = r[b]
	if key == True:
		mess=r['message']
		print(Fore.GREEN+start+mess+end)
		print(Fore.GREEN+start+"Connected to sever is successfully"+end)
		time.sleep(1)
		print("Sever sẽ đóng vào 12h->7h30 sáng để bảo trì")
		time.sleep(1)
		print(Fore.GREEN+start+"sever is open"+end)
		time.sleep(1)
		print(Fore.GREEN+start+"Loading...!"+end)
		time.sleep(1)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print("""
_________    __           .__   __________
\_   ___ \ _/  |_ _______ |  |  \____    /
/    \  \/ \   __\\_  __ \|  |    /     / 
\     \____ |  |   |  | \/|  |__ /     /_ 
 \_______/ |__|   |__|   |____//_________\
                                       

""")
		print(Fore.CYAN+"""
                                                                 ÛÛ
                                                                ÛÛ  
                                                              ÛÛ 
                                                                            
                        ±Û          ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛÛÛÛÛÛÛÛ         
                          Û         ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ            
                           ²Û       ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ             
                          Û         ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ           
                        ±Û   ²²²²²  ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛÛÛÛ   
                                          Tool change mode:On   

                                           """)
		print(Style.RESET_ALL)

		while True:
			os.system("cls")
			print(Fore.GREEN+"""
			=======================================================================================
			#Project:The product is copyrighted by Nguyễn Hoàng Phúc
			=======================================================================================

			#Support product:
			- 1.Download Windows 11(cập nhật thường xuyên nếu có bản mới)
			- 2.Bật chế độ chống virus máy tính và tường lửa
			- 3.Tắt chế độ chống virus máy tính và tường lửa
			- 4.Update full driver
			- 5.Download Windows 10(cập nhật thường xuyên nếu có bản mới)
			- 6.Sử dụng các loại hỗ trợ về máy tính(17 chức năng)
			- 7.Giảm lag máy tính và mạng máy tính hoặc wifi
			- 8.Sử dụng AI(phần mềm trí tuệ nhân tạo)
			- 9.Liên hệ hỗ trợ qua gmail
			=======================================================================================
			We are very thanks you for used my tool <3 have a good day
			Tool copyright by : PhCtrlZ
			""")
			print(Style.RESET_ALL)
			ngdung=input("nhập vào số mà bạn muốn chọn:")
			if ngdung=="1":
				url5=r['url1']
				url4=url5
				runprf = webbrowser.open_new_tab(url4)
			if ngdung=="2":
				f=os.startfile("win10.exe")
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)   #ctypes.windll.user32.MessageBoxW(0, "tin báo", "tiêu đề", kiểu)
			if ngdung=="3":
				f=os.startfile("win10.exe")
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)
			if ngdung=="4":
				os.system('pnputil')
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)
			if ngdung=="5":
				url6=r['url2']
				url3=url6
				runprf=webbrowser.open_new_tab(url3)
			if ngdung=="6":	
				os.startfile('sp.cmd')
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)
			if ngdung=="7":
				os.system("powercfg -h off>nul")
				os.system("del /f /s /q %temp%")
				os.system("del /f /s /q %windir%\prefetch\ ")
				os.system("ipconfig /all")
				os.system("ipconfig /flushdns")
				os.system("ipconfig /release")
				os.system("ipconfig /renew")
				os.system("Netsh int tcp show global")
				os.system("Netsh int tcp set global chimney=enabled")
				os.system("Netsh int tcp set global autotuninglevel=normal")
				os.system("Netsh int set global congestionprovider=ctcp ")
				os.system("netsh interface tcp set global autotuning=disable")
				os.system("netsh interface tcp set heuristics disabled")
				os.system("netsh int ip reset c:\resetlog.txt")
				os.system("EmptyStandbyList.exe workingsets")
				os.system("mptyStandbyList.exe modifiedpagelist")
				os.system("EmptyStandbyList.exe priority0standbylist")
				os.system("EmptyStandbyList.exe standbylist")
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)
			if ngdung=="8":
				f=os.startfile("ttnt.exe")
				ctypes.windll.user32.MessageBoxW(0, "Hoàn Tất", "Thông báo", 1)
			if ngdung=="9":
				url5="https://mail.google.com/mail/u/0/#sent?compose=GTvVlcSHxjNTDBtJNWHVzvsPKHVNhNDKQbMmwGKqlJkNxcwDMwkPxWNKpvJtRmJxsSVCkPDqgTChS"
				runprf=webbrowser.open_new_tab(url5)
	elif key == False:
		os.system("cls")
		error=r['error']
		error2=r['error2']
		error3=r['error3']
		print(Fore.RED+error)
		print(Fore.RED+error2)
		print(Fore.RED+error3)
		print(Style.RESET_ALL)
		time.sleep(10)
		exit()

except:
	os.system("cls")
	error=r['error']
	error2=r['error2']
	error3=r['error3']
	print(Fore.RED+error)
	print(Fore.RED+error2)
	print(Fore.RED+error3)
	print(Style.RESET_ALL)
	time.sleep(10)
	exit()

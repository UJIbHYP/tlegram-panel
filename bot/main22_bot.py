from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession, CreateNewSession
import asyncio
from telebot import types 
import socket
from zipfile import ZipFile
import socks
import requests
import json
import os
import telebot
import requests
import wget
import time
from telethon.sessions import StringSession
import sys
def convert_tdata(destination,user_id):
	# os.chdir(destination)
	c=0
	proxy_c=0
	json_info={"accounts":[]}
	os.system('find \"$(pwd)\" -name \"tdata\" > source.txt')
	# time.sleep(20000)
	for str1 in open("source.txt","r"):
		if c==3:
			proxy_c=proxy_c+1
			c=0
		ll=len(list(open('proxy.txt')))
		# print(ll)
		proxyn=(list(open('proxy.txt')))[proxy_c].split("\n")[0]
		print(proxyn)
		ip=proxyn.split(":")[2]
		port=proxyn.split(":")[3]
		login=proxyn.split(":")[0]
		psw=proxyn.split(":")[1]
		url=str1.split('\n')[0]
		print(url)

		tdataFolder = url
		# flag=UseCurrentSession
		#
		api = API.TelegramIOS.Generate()
		print(api)
		proxy=dict(proxy_type=socks.SOCKS5, addr=ip,
                               port=int(port),
                               username=login, password=psw
                               )
		try:
			try:
				# print(tdataFolder)
				print('\n')
				print('\n')
				tdesk = TDesktop(tdataFolder)
				print(tdesk)
				pass
			except Exception as e:
				print(e)
		# Check if we have loaded any accounts
			assert tdesk.isLoaded()
		# Convert TDesktop to Telethon using the current session.
			print(url)
			# client = tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)
			client = tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession, proxy=proxy)
		# os.chdir('/media/ilnur/f848c342-9aa7-40e0-b3f6-7319d8717c55/tg/1_40/')
		# number=url.split("1_40/")[1].split(".session")[1]

			client.connect()
			# client=TelegramClient(
   #                  session=number,
   #                  api_id=api_id,
   #                  api_hash=api_hash,
   #                  proxy=proxy
   #              )

			string = StringSession.save(client.session)
			print("				***")
			print(string)
			print("				***")
			client.PrintSessions()
			client.disconnect()
			time.sleep(5)
			pass
		except Exception as e:
			string="none"
			print(e)
			print("wtf")
		# with open("tokens_a.txt","a") as t_a:
			# t_a.write(string+"\n")
		
		api_id=10840
		api_hash="33c45224029d59cb3ad0c16134215aeb"
		json_info["accounts"].append({"token": string, "proxy" :proxyn, "api_id":api_id, "api_hash":api_hash})
		c=c+1
	pass
	print(json_info)
	with open('tokens.json', 'w') as outfile:
		json.dump(json_info, outfile)
	bot_sender("tokens.json", user_id)

pass







async def convert_sessions(destination,user_id):
	json_counter=0
	json_prefix=1
	c=0
	proxy_c=0
	json_info={"accounts":[]}
	os.system("ls accounts/ | grep json > source.txt")
	liners=open("source.txt","r").readlines()
	os.chdir("accounts")
	# time.sleep(9999)
	for x in range(len(liners)):

		# data=json.load("")
		# ll=len(list(open('../proxy.txt')))
		# print(ll)
		f=open('../proxy.txt',"r")
		proxyn=(list(f))[proxy_c].split("\n")[0]
		f.close()
		# print(proxyn)
		ip=proxyn.split(":")[2]
		port=proxyn.split(":")[3]
		login=proxyn.split(":")[0]
		psw=proxyn.split(":")[1]
		try:
			f = open(liners[x].split("\n")[0])
			pass
		except Exception as e:
			print(e)
			string="none"
			
		print(f)
		data = json.load(f)
		# login=proxyn.split(":")[0]
		# psw=proxyn.split(":")[1]
		# url=str1.split('\n')[0
		# flag=UseCurrentSession
		#
		# api = API.TelegramIOS.Generate()
		# print(api)
		api_id=data["app_id"]
		api_hash=data["app_hash"]
		session=data["session_file"]
		proxy=dict(proxy_type=socks.SOCKS5, addr=ip,
                               port=int(port),
                               username=login, password=psw
                               )

		# print(url)

		# os.chdir('/media/ilnur/f848c342-9aa7-40e0-b3f6-7319d8717c55/tg/1_40/')
		# number=url.split("1_40/")[1].split(".session")[1]

			# client=TelegramClient(
   #                  session=number,
   #                  api_id=api_id,
   #                  api_hash=api_hash,
                    # proxy=proxy
   #              )

		try: 
			# client = TelegramClient(session=session, api_hash=api_hash, api_id=api_id)
			client = TelegramClient(session=session, api_hash=api_hash, api_id=api_id, proxy=proxy)
			string = StringSession.save(client.session)
			print("***")
			print(string)
			print("***")
			await client.connect()
			await client.PrintSessions()
			await client.disconnect()
			time.sleep(1)
			pass
		except Exception as e:
			string="none"
			print(e)
		x=x+1
		pass
		if "none" not in string :
			json_info["accounts"].append({"token": string, "proxy" :proxyn, "api_id":api_id, "api_hash":api_hash})
			c=c+1
			if c==3:
				proxy_c=proxy_c+1
				c=0
		
		with open('tokens.json', 'w') as outfile:
			json.dump(json_info, outfile)
			# json_counter=0
			print(json_info)
			# json_info={"accounts":[]}
			json_prefix=json_prefix+1
		pass
	pass
	bot_sender("tokens.json", user_id)

pass


def bot_sender(filename, user_id):

	TOKEN="5857620052:AAHRrJq16_FHv6AT836sksYlI6o2A7oERzE"
	# bot = telebot.TeleBot(TOKEN)
	bot = telebot.TeleBot(TOKEN)
	img = open(filename, 'rb')
	bot.send_document(user_id, img)

	# bot.polling()

	pass



def bot_init():
	

	str_info="Вам нужно создать архив zip и прислать его сюда, боту.\n В архиве нужно создать папку accounts - в неё надо выгрузить аккаунты либо в формате tdata, либо session_json.\nВ архиве так же должен быть файл proxy.txt - там должны быть прокси. Socks5 ipv4, из расчёта - количество аккаунтов делим на 3 = кол-во прокси. Формат прокси  - user:pass:host:port.\nИспользуем tokens.json, который пришлёт бот.\n\n\nP.S. Отправить zip боту можете в любой момент - перезапускать его необязательно..."



	TOKEN="5857620052:AAHRrJq16_FHv6AT836sksYlI6o2A7oERzE"
	# bot = telebot.TeleBot(TOKEN)
	bot = telebot.TeleBot(TOKEN)
	@bot.message_handler(commands=['start'])
	def send_welcome(message):

		markup=telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Выгрузить zip.', callback_data='send_zip'))
		markup.add(telebot.types.InlineKeyboardButton(text='Инструкция по использованию.', callback_data='info'))
		ms_data=bot.reply_to(message, "Привет. \n Этот бот является частью проекта по рассылку и инваиту.",reply_markup=markup)
		
	@bot.callback_query_handler(func=lambda call: 'info' in call.data)
	def refferr(call):
		# print(call)
		# send_ref=get_joke_html()

		markup=telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Понял.', callback_data='main'))
		bot.edit_message_text(text=str_info, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
	@bot.callback_query_handler(func=lambda call: 'main' in call.data)
	def main(call):
		markup=telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Выгрузить zip.', callback_data='send_zip'))
		markup.add(telebot.types.InlineKeyboardButton(text='Инструкция по использованию.', callback_data='info'))
		bot.edit_message_text(text="Привет. \n Этот бот является частью проекта по рассылку и инваиту.", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
		# ms_data=bot.edit_message_text(call.message, ,reply_markup=markup)

	@bot.callback_query_handler(func=lambda call: 'send_zip' in call.data)
	def main(call):
		# markup=telebot.types.InlineKeyboardMarkup()
		# markup.add(telebot.types.InlineKeyboardButton(text='Выгрузить zip.', callback_data='send_zip'))
		# markup.add(telebot.types.InlineKeyboardButton(text='Инструкция по использованию.', callback_data='info'))
		bot.edit_message_text(text="Отправь сюда zip-файл,который соответствует инструкции.", chat_id=call.message.chat.id, message_id=call.message.message_id)
		# ms_data=bot.edit_message_text(call.message, ,reply_markup=markup)




	@bot.message_handler(content_types=["document"])
	def handle_reply(message):
		result = message.document
		print(result)
		url="https://api.telegram.org/bot"+TOKEN+"/getFile?file_id="+result.file_id
		r=requests.get(url)
		print(r.json())
		url2="https://api.telegram.org/file/bot"+TOKEN+"/"+r.json()["result"]["file_path"]
		global filename 
		filename = wget.download(url2)
		markup=telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='TData.', callback_data='tdata'))
		markup.add(telebot.types.InlineKeyboardButton(text='Session-JSON', callback_data='sj'))
		ms_data=bot.reply_to(message, "TDATA или Session-JSON?",reply_markup=markup)


	@bot.callback_query_handler(func=lambda call: 'tdata' in call.data)
	def tdata(call):
		zipper_worker("tdata",call.message.chat.id, filename)

		# markup=telebot.types.InlineKeyboardMarkup()
		# markup.add(telebot.types.InlineKeyboardButton(text='Выгрузить zip.', callback_data='send_zip'))
		# markup.add(telebot.types.InlineKeyboardButton(text='Инструкция по использованию.', callback_data='info'))
		bot.edit_message_text(text="Отправь сюда zip-файл,который соответствует инструкции.", chat_id=call.message.chat.id, message_id=call.message.message_id)
		# ms_data=bot.edit_message_text(call.message, ,reply_markup=markup)

	@bot.callback_query_handler(func=lambda call: 'sj' in call.data)
	def sj(call):
		zipper_worker("sj", call.message.chat.id, filename)
		# markup=telebot.types.InlineKeyboardMarkup()
		# markup.add(telebot.types.InlineKeyboardButton(text='Выгрузить zip.', callback_data='send_zip'))
		# markup.add(telebot.types.InlineKeyboardButton(text='Инструкция по использованию.', callback_data='info'))
		bot.edit_message_text(text="Отправь сюда zip-файл,который соответствует инструкции.", chat_id=call.message.chat.id, message_id=call.message.message_id)
		# ms_data=bot.edit_message_text(call.message, ,reply_markup=markup)
	bot.polling()

pass

def zipper_worker(tdsj, user_id, file_name):
	
	with ZipFile(file_name, 'r') as zip:
		zipname=file_name.split(".")[0]
		os.system("mkdir "+zipname)
		os.chdir(zipname)
		# printing all the contents of the zip file
		# zip.printdir()

		# extracting all the files
		print('Extracting all the files now...')
		zip.extractall()
		print('Done!')

		if tdsj=="sj":
			asyncio.run(convert_sessions(zipname, user_id))
			pass
		else:
			convert_tdata(zipname, user_id)

		os.chdir("../")
		os.chdir("../")
		print(os.getcwd())
		os.system("rm -rf "+zipname)
		os.system("rm "+zipname+".zip")
	pass








bot_init()
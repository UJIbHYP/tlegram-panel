
#!/usr/bin/env python
import sys
import os
import PySimpleGUI as sg
# import vkadder
# from vkadder import *
import vk_api
from instagrapi import Client
import time
from os import walk
# 6ea1ba87fc429e807182d512dae6c502b89a85c43b455215883a1076c07e9b825dfb37d0966b98a0e3489
# 24aa810149f9fcee0755dccb54abedf13541e1265bd107d71a2c5f3ab76bfbae79411804708ce1cccae8c
import socks
import vk_api
from telethon.tl.functions.channels import JoinChannelRequest

from telethon.tl.functions.messages import ImportChatInviteRequest
import time
from selenium import webdriver # 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import requests
import bs4
from telethon.tl.functions.messages import AddChatUserRequest

import random# from telethon import GetParticipantsRequest
# from telethon import GetFullChannelRequest
# from telethon import ChannelParticipantsSearch
# from telethon.sync import TelegramClient/
# from telethon import functions, types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
import asyncio
from telethon import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import InviteToChannelRequest
# from telethon.tl.functions.channels import InputPeerChannel
# from telethon.tl.functions.channels import InputPeerUser
from telethon.tl.types import InputPeerUser
from telethon.sessions import StringSession
from telethon import TelegramClient, connection
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import json
import re
import sys
import csv
import traceback
import time
import random
import time
from telethon.tl.types import InputPeerChannel
import threading
import re
import time
from random import randrange
import webbrowser
import os
import urllib.parse
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#303030',
                                        'TEXT': '#ffffff',
                                        'INPUT': '#444444',
                                        'TEXT_INPUT': '#aaaaaa',
                                        'SCROLL': '#000000',
                                        'BUTTON': ('#f0f0f0', '#555555'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, }
sg.theme('MyCreatedTheme')




def telegram_getnumber():
    f=open("telegram_nums.txt", "r")
    lines=f.readlines()
    return lines
    pass
def telegram_get_main_account(accounts):
    return accounts[0]
    pass















def telegram_appearance(username, name, surname,bio):
    with open('tokens.json') as json_file:
        data = json.load(json_file)
        # print(data)
    ll=len(data["accounts"])
    # print(tokens[0])
    ind=0
    j=0
    for j in range(ll):
        # tkn=token.split("\n")[0]
        ind=ind+1
        api_id=12483931
        api_hash="722eea8b7553a0ea2bb0884edb325c02"
        acc=telegram_account(j)
        try:
            acc.connect()
        except:
            continue
        try:
            res=acc(functions.account.UpdateUsernameRequest(username=username+"_"+str(ind)))     
            pass
        except Exception as e:
            print(e)
        try:
            acc(functions.account.UpdateProfileRequest(first_name=name,last_name=surname ))
            pass
        except Exception as e:
            print(e)
        pass
        try:
            acc(functions.account.UpdateProfileRequest(about=bio))
            pass
        except Exception as e:
            print(e)
        pass
        # res=acc.get_messages('delega_non_ofcl', limit=1)[0]
        # print (res.media.photo)
        try:
            acc(functions.photos.UploadProfilePhotoRequest(file=acc.upload_file('profile2.jpg')))
            pass
        except Exception as e:
            print(e)
        # print (res.media.id)
        print("Network is ready.")
            
        time.sleep(1)
    pass


def telegram_account(n):
    with open('tokens.json') as json_file:
        data = json.load(json_file)
        # print(data)
    ll=len(data["accounts"])
    print(ll)
    proxyn=data["accounts"][(n)%ll]["proxy"]
    token=data["accounts"][(n)%ll]["token"]   
    # print(proxyn)
    # print(token)

    api_id=data["accounts"][(n)%ll]["api_id"]
    api_hash=data["accounts"][(n)%ll]["api_hash"]
    ip=proxyn.split(":")[2]
    port=proxyn.split(":")[3]
    login=proxyn.split(":")[0]
    psw=proxyn.split(":")[1]
    proxy=dict(proxy_type=socks.SOCKS5, addr=ip, port=int(port), username=login, password=psw)
     # this mode supports most proxies
    try:
        #PROXYENABLER
        # acc=TelegramClient(StringSession(token), api_id, api_hash, proxy=proxy)
        acc=TelegramClient(StringSession(token), api_id, api_hash)
        
        return acc
        pass
    except Exception as e:
        print(e)
        # return(telegram_account(n+1))
    # acc.connect()
    pass






def telegram_set_first_wave(accs, name):
    # print(receivers)
    # print(msg_frwrd)
    f=open("telegram_minions.txt", "r")

    receivers=f.readlines()
    j=0
    for iter12 in accs:
        # try:
        minion=telegram_account(j)
        j=j+1
        minion.connect()
        try:
            msg_frwrd=client.get_messages("rassilki_peace", limit=1)[0]
            # print(str(msg_frwrd))
            minion.send_message('me', msg_frwrd)
            pass
        except Exception as e:
            print(e)
            
        pass
    pass



def telegram_launch(acc, username, j):
    try:
        api_id=12483931
        api_hash="722eea8b7553a0ea2bb0884edb325c02"
        client=telegram_account(j)
        client.connect()
        f=open("telegram_auditory.txt", "r")
        msg_frwrd=client.get_messages("me", limit=1)[0]
        # print(msg_frwrd)
        client.send_message(username, msg_frwrd)
            

        pass
    except Exception as e:
        print(e)

    pass



# writers=getaccounts()
# set_first_wave(writers)





def telegram_start(name):

    f=open("telegram_minions.txt", "w")
    f.write("")
    # try:
    print("Получение аккаунтов...")
    with open('tokens.json') as json_file:
        data = json.load(json_file)
    army=data["accounts"]
        # pass
    # except Exception as e:
    
    # print("Сохраненик базы акков-миньонов.")
    # telegram_save_txt(army,name)

 
    # try:
    print("Запускаю первую волну - сохраняю в избранное сообщение для рассылки")
    # telegram_set_first_wave(army, name)
        # pass
    # except Exception as e:
        # print(e)
    fe=open("telegram_auditory.txt","r")
    i=0
    y=0
    audit=fe.readlines()
    for user in audit:
        audit=fe.readlines()
        acc_workin=army[i%len(army)]
        user=user.split("\n")[0]
        print("Рассылаю сообщение №"+str(y)+" c аккаунта "+str(i%len(army)))
        try:
            y=y+1
            telegram_launch(acc_workin,user, y)
            pass
        except Exception as e:
            print(e)
        pass

        i=i+1
        with open("telegram_auditory.txt","w"):
            for use in audit:
                f.write(use+"\n")
                pass
    pass
    print("Рассылка завершена")
    pass
        
#getterphone


def telegram_get_entity_phone(number):
    # print(res)
    # with open("entities.txt", "a") as file_object:
        # file_object.write("TEST")
    # writer.write("TEST")
    # return 0
    numbers=open("numbers_in.txt", "r").readlines()
    for number in numbers:
        numbers=open("numbers_in.txt", "r").readlines()
        i=0
        electory_f="telegram_auditory.txt"
        chats_target_f="CAO_out.txt"
        electory=open(electory_f).readlines()
        
        i=i+1
        acc=telegram_account(i)
        try:
            acc.connect()
            pass
        except Exception as e:
            print("")

        id_inv=str((open(chats_target_f).readlines())[0].split("\n")[0])
        # acc=telegram_account(i)
        i=i+1
        try:
            acc.connect()
            pass
        except Exception as e:
            return 0
        number=str(number.split("\n")[0])
        try:
            contact = InputPhoneContact(client_id=0, phone=number, first_name="mskkk", last_name="_"+str(i)+"")
            result = acc(ImportContactsRequest([contact], replace=True))

            res=acc.get_entity(number)
            print("res")
            print(res)
            print("res")
            with open("entities.txt", "a") as file_object:
                # file_object.write("TEST")
                file_object.write(str(res.username)+"\n")

            print(res.username+"\t"+number)
            # time.sleep(1)
            pass
        except Exception as e:
            print("ex1")
            try:
                # time.sleep(1)
                res=acc.get_entity(number)
                with open("entities.txt", "a") as file_object:
                    file_object.write((res.username)+"\n")

                print(res.username+"\t"+number)
                pass
            except Exception as e:
                print(e)
        with open("numbers_in.txt", "w") as f:
            f.write("")
            pass
        with open("numbers_in.txt", "a") as f:
            for x in numbers[1:]:
                f.write(x)
                pass
        pass
    
    pass




def telegram_region_parse(prefix, token):
    # army=telegram_getaccounts()
    try:
        # os.chdir("sessions/")
        pass
    except Exception as e:
        print(e)
    f_from="chat_from.txt"
    f_out="telegram_auditory.txt"
    numbers=[]


    acc=telegram_account(3)
    acc.connect()

    if 1==1:

        chats_from=(open(f_from).readlines())
        print(numbers)
        for item in chats_from:     
            
            # print(item)
            try:
                result = acc(functions.messages.CheckChatInviteRequest(
            hash=item.split("t.me/+")[1]
        ))
                pass
            except Exception as e:
                result=acc.get_entity(item.split("t.me/")[1])
                print(e)
            try:
                print(result.chat.id)
                users_w=acc.get_participants(result, aggressive=False,offset=1000, limit=1000)
                pass
            except Exception as e:
                print(result.id)
                users_w=acc.get_participants(result, aggressive=False,offset=1000, limit=1000)
            # print(rs)
            for ppl in users_w:
                # print(ppl.username)
                writer=open(f_out,"a")
                if "None" not in str(ppl.username):
                    writer.write(str(ppl.username)+"\n")
                    pass
                pass
            pass
            
            print("*********************\n\n\n\tПарсинг "+str(item).split("\n")[0]+" завершен")
        pass
        
    print("*********************\n\n\n\tПарсинг всех чатов завершен")

    pass 

def telegram_inviter(prefix, token, counter):
    electory_f="telegram_auditory.txt"
    chats_target_f="chat_out.txt"
    electory=open(electory_f).readlines()
    
    acc=telegram_account(counter)
    acc.connect()

    id_inv=str((open(chats_target_f).readlines())[0].split("\n")[0])
    try:
        group=acc.get_entity(id_inv)
        pass
    except Exception as e:
        print(e)
    
    acc(JoinChannelRequest(group))
    id_inv=group.id
    # time.sleep(10)
    electory_in=[]
    f_elec=open(electory_f, "r")
    z=0
    narod=f_elec.readlines()
    for zy in range(20):

        electory_in.append(acc.get_entity(str(narod[zy]).split("\n")[0]))
        pass
    print(electory_in)  
    # try:
        # print("INVITIN")
    res_inv=acc(InviteToChannelRequest(
    group,
    electory_in
))
    print("\n\n\n")
    print(res_inv.users)        
    print(len(res_inv.users))
    print("\n\n\n")
    if len(res_inv.users)>0:
        for elem in narod:
                with open(electory_f, "w") as f_elec2:
                    for items in narod[20:]: 
                        f_elec2.write(str(items))
                        pass
                pass
        pass
        
    # time.sleep(10)
        # pass
    # except Exception as e:
        # print(e)
    pass




def telegram_invite(reg,t):
    # army=telegram_getaccounts()
    regions={
    "ЦАО":"CAO","ЮВАО":"UVAO","ВАО":"VAO","ЮАО":"UAO","ЗАО":"ZAO","СВАО":"SVAO","СЗАО":"SZAO","ЗелАО":"ZelAO","ЮЗАО":"UZAO","САО":"SAO"
    }
    reg_f=regions["ЦАО"]
    with open('tokens.json') as json_file:
        data = json.load(json_file)
        # print(data)
    tokens=data["accounts"]
    ll=len(data["accounts"])
    # counter=0
    j=0
    x=0
    for x in range(100):
        if 1==1:
            try:
                # counter=counter+1
                telegram_inviter(reg_f, '', x%ll)
                time.sleep(t)
                pass
            except Exception as e:
                print(e)
                print("ЖДАТЬ.")

            # time.sleep(10)
        pass
    pass
    # f=open("telegram_auditory.txt","r")
    
    pass

    pass
        


# telegram_start("azam_adder_123")


def main():

    # import PySimpleGUIWeb as sg

    # Usage of Tabs in PSG
    #
    # sg.set_options(background_color='cornsilk4',
    #         element_background_color='cornsilk2',
    #         input_elements_background_color='cornsilk2')
    tab1_tg = [
    [sg.Text("TG writer by PEACE.")],
    [sg.Button('Свяжитесь со мной.', enable_events=True, key='-LINK-')],
    [sg.Text("Код"), sg.Input(size=(5,1), key="code_tg")],
    [sg.Button('Авторизация аккаунтов.')],
    [sg.Button('Посмотреть акки.')]
    ]
    rayons=["ЦАО","ЮВАО","ВАО","ЮАО","ЗАО","СВАО","СЗАО","ЗелАО","ЮЗАО","САО"]
    tab2_tg=[
    [sg.Text("TG parser & inviter")],
    [sg.Text("TIMER"),sg.Input(181,size=(4,1) ,key="timer")],
    [sg.Text("Ссылка на чат (выгрузка)" ,size=(26, 1)), sg.Input("", size=(25,1), key="msg_inst") ],

    [sg.Button("Спарсить.", key="-parse-"),sg.Button("INVITE", key="-invite-")],
    ]
    tab3_tg=[
    [sg.Text("TG Writer by PEACE.")],
    # [sg.Radio('Разослать текст сообщения', "tg_type", default=False)],
    [sg.Button("Запустить пересылку!")],
    ]
    tab4_tg=[
    [sg.Text("TG Appear by PEACE.")],


    [sg.Text("Имя | Фамилия:"), sg.Input("Новый", size=(20,1), key="name_tg"),sg.Input("район", size=(20,1), key="surname_tg")],
    [sg.Text("Имя пользователя (eng):"), sg.Input("nl_msk11_1", size=(20,1), key="username_tg") ],
    [sg.Text("Описание:"), sg.Input("nl_msk11_1", size=(47,1), key="bio_tg") ],
    [sg.Button("Упаковать аккаунты")],

    ]
    tab5_tg=[
    [sg.Text("TG Parse by PEACE.")],


    [sg.Text("Номер телефона"), sg.Input("", size=(20,1), key="phone_entity"),],
    # [sg.Text("Имя пользователя (eng):"), sg.Input("", size=(20,1), key="username_tg") ],
    [sg.Button("Получить сущность")],

    ]
    layout = [[sg.TabGroup([[
                             
                             
                             sg.Tab('TG Парсинг', tab2_tg),
                             sg.Tab('TG Рассылка', tab3_tg),
                             sg.Tab('TG Упаковка', tab4_tg),
                             sg.Tab('Парсинг телефонов', tab5_tg),
                             sg.Tab('Обратная связь', tab1_tg),

                             ]])]]

    # Switch to use your newly created theme
    global window
    window = sg.Window('PEACE TG Writer', layout, margins=(0,0) , default_element_size=(85, 100), modal=True)


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:        
            break
        
        if event =="Запустить пересылку!":
            name_tg=str(values["name_tg"])
            print(name_tg)
            # my_thread228 = threading.Thread(target=telegram_start, args=(str(name_tg)))
            telegram_start(name_tg)
            # my_thread228.start()
            pass

        if event =="Упаковать аккаунты":
            name=str(values["name_tg"])
            surname=str(values["surname_tg"])
            bio=str(values["bio_tg"])
            username=str(values["username_tg"])
            telegram_appearance(username, name, surname, bio)
            pass
        if event =="Получить сущность":
            phone_num=str(values["phone_entity"])
            telegram_get_entity_phone(phone_num)
            pass
        if event =="-register-":
            telegram_register()
            pass
        if event =="-parse-":
                # telegram_set_first_wave(army)
                # print(tokens)
                regions={
                    "ЦАО":"CAO","ЮВАО":"UVAO","ВАО":"VAO","ЮАО":"UAO","ЗАО":"ZAO","СВАО":"SVAO","СЗАО":"SZAO","ЗелАО":"ZelAO","ЮЗАО":"UZAO","САО":"SAO"
                    }
                reg_f="CAO"
                for x in range(1):
                    try:
                        telegram_region_parse(reg_f, "")
                        pass
                    except Exception as e:
                        print(e)
                        telegram_region_parse(reg_f, "")

                    pass
                pass
        if event =="-invite-":
            print("in")
            reg="CAO"
            timer=int(values["timer"])
            telegram_invite(reg, timer)
            pass
        if event =="Авторизация аккаунтов.":
            my_thread22 = threading.Thread(target=telegram_getaccounts, args=())
            my_thread22.start()
            
            pass
        if event =="Посмотреть акки.":
            with open('tokens.json') as json_file:
                data = json.load(json_file)
            for i in range(len(data["accounts"])):
                try:
                    acc=telegram_account(i)
                    acc.connect()
                    print("|"+str(i+1)+" "+str(acc.get_entity("me").username)+"|")
                    if (acc.get_entity("me").id)>0:
                        # with open("tokens2.txt",'a') as fi:
                            # fi.write(token)
                        pass
                        
                    pass
                except Exception as e:
                    print(e)
                    # print()
                    print("|"+str(i+1)+"Error in acc (maybe deleted)"+"|")
                # i=i+1
                pass
            pass


    window.close()




    # token = "ba9f6de2d278c360722c7458e8b67a51a3e01d528b67d6ded02394c7a3dd9833dd80784543d49193c7d57" #ME
    # token = "66950778a847d30e728bb78d8e142ea8a36f808e295a0c673a515118dfd8db0c5efba98e28ed2ba8de62e" #Илькин
      # vk.method("status.set", {"text": lrn })
      # 
    i=0




pass
main()
#!/usr/bin/env python

from sys import argv, stdout

if len(argv) == 1:
    print('\nusage: stuycs-submit authenticate')
    print('       stuycs-submit [file name]\n')
    exit()

from requests import post
from getpass import getpass
from pickle import load, dump
from bs4 import BeautifulSoup, Tag
from PyInquirer import prompt
from examples import custom_style_2, custom_style_3
from subprocess import run, PIPE
from os import environ
from platform import system

p = {
    'p2': {
        'ABEDIN, NAKIB': 'ad135741e4b',
        'BULIC, EDWARD': 'a4989a4b172',
        'CHAN, JOSHUA': 'ac02f444a0a',
        'CHEN, EVELYN': 'ab108822a8d',
        'COWAN, SAM': 'a3fd88e8895',
        'DENIS, IAN': 'ac024717e3a',
        'FENG, Jing': 'ac03ef62d4a',
        'FRIEDMAN, RUBY': 'a48feffe4b2',
        'GLUSKER, SAMUEL': 'ac07ee51d2a',
        'HERNANDEZ-CRUZ, JORGE': 'a780daee5f1',
        'HO, KAITLIN': 'ae232160cc8',
        'IRELAND, SLOAN': 'ac003635dfa',
        'JIA, Izzy': 'aa6659a4a1c',
        'JIAN, ZIYING': 'af396206809',
        'JIANG, MARC': 'aa6418b3f6c',
        'KANG, BRIAN': 'a0f6d28a6a6',
        'KATARI, ANJINI': 'a0addfdf7a6',
        'LEE, LAUREN': 'a1dfafb75b7',
        'LIN, ETHAN': 'a4b3e6d93a2',
        'LIN, JASON': 'a7b9fddfc91',
        'LIU, NICOLE': 'ad10043177b',
        'PHULARA, Ash': 'a8571353f7e',
        'QIN, DAPHNE': 'a2daa8c9684',
        'SAKIB, RAFID': 'ac01ff70a6a',
        'SELTZER, HAILEY': 'a2eec9dc814',
        'SOLER, NATALIE': 'a3ff00da1c5',
        'SONG, JONATHAN': 'af315152569',
        'SUN, ANTHONY': 'a847b540cae',
        'TAN, TERRY': 'a0cdddfe0f6',
        'YUDITSKY, Emma': 'ab777943b4d',
        'ZHANG, JUSTIN': 'ad134e76d0b',
        'ZHANG, ZELEN': 'a7b94fffca1',
        'ZHENG, ELIE': 'aa659757a0c',
        'ZHENG, PHOEBE': 'a842079422e',
        },
    'p5': {
        'ALNASSER, AMEER': 'a8707297dae',
        'BAROI, BERNADETTE': 'ad72e4c7feb',
        'BHUIYAN, SUBHA': 'ad11305a96b',
        'CAOTHIEN, KAI': 'a3ffbdde385',
        'CHAN, ELLA': 'ac026624c2a',
        'CHAO, AIDEN': 'a8437454c1e',
        'CHEN, CORINA': 'af394c44e69',
        'CHEN, CRAIG': 'a841b396b3e',
        'CHO, GOOK PETER': 'a1ccafaa6d7',
        'GAO, CHLOE J': 'ad16421b72b',
        'GRAEBER, VIVIAN': 'a8447393f3e',
        'HOSSAIN, TAHRIM': 'aa642343a8c',
        'JIANG, GRACE': 'a2ec8acf194',
        'LEW, MELODY': 'a48aecac7a2',
        'LI, ANN': 'a7bbc5ee6d1',
        'LIU, CALVIN': 'a59dfaab5c3',
        'LIU, WEICHEN': 'a2ea0cac614',
        'LIU, ZHI XUAN': 'a2fea0af614',
        'MANGAR, RAVINDRA': 'ac00603ac0a',
        'OTHMAN, JOSEPH': 'ad1366dae5b',
        'PRATHIBAN, PRAHALATAN': 'a0ceb9dc186',
        'RAHMAN, ALIF': 'ab77105307d',
        'RAHMAN, NASHIF': 'ad1362c4f3b',
        'RIKI, MAHIR': 'a59866bafa3',
        'RUAN, AILEEN': 'a1df2bdb1c7',
        'SHI, MARILYN': 'ad1370069fb',
        'SMALL, GABRIEL': 'ae21d478d38',
        'TAN, JEFFREY': 'a58bbdab5e3',
        'TANG, Raven': 'ad11e0c7e5b',
        'TARSIS, NICHOLAS': 'a8462527f4e',
        'YENLEE, MAX': 'a8456396f2e',
        'ZHAO, KATHERINE': 'ac025f629fa',
        'ZHOU, JERRY': 'aa64141691c',
        'ZHU, VINCENT': 'a39cad99195',
        },
    'p6': {
        'ABIR, ABDAL': 'ae2556e8a28',
        'ASTAFUROV, KONSTANTIN': 'a58ba9e8593',
        'BENTO, FELIX': 'a488d69a492',
        'CEN, STEVEN': 'af315704a39',
        'CHEN, ANTHONY': 'ac1206d7f4a',
        'CHEN, RICHARD': 'ac024e5587a',
        'GARBUTT, ADEN': 'ae232ce6d48',
        'HUANG, HUA': 'ab70194291d',
        'HUANG, MAGGIE': 'a7bfd8b1291',
        'KALOUDIS, HANA': 'a59ffbcf1b3',
        'KAPNISAKIS, LEFTERI': 'a2eed92c7e4',
        'KITAGUCHI, KANO': 'a59bddab593',
        'LEE, ALLISON': 'ab763414b1d',
        'LIANG, ANITA': 'a0ca8f1c0f6',
        'LIN, MARK': 'ab7510b709d',
        'MOLTZ, JOSIAH': 'ad135523c3b',
        'NATH, ABHEEK': 'ab75207dd0d',
        'QUE, DANIELLE': 'a0ce9f8c6a6',
        'RAHMAN, ZESAN': 'a3fdbbfb6a5',
        'SHAH, VANSH': 'aa5d473385c',
        'SIFAT, JAWAD': 'ac36e5d1e7a',
        'TENEZACA, CYNTHIA': 'a0ccaef6796',
        'THOMPSON, GABRIEL': 'ac02567763a',
        'TONG, ETHAN': 'a7ba84e0381',
        'VONGPHANITH, WILLIAM': 'a1cb8af6627',
        'WANG, KEVIN': 'ae225043478',
        'WANG, VINCENT': 'a2e8bd99604',
        'WU, YONG LIN': 'a59a764f463',
        'XUE, Julia': 'ae36cc51bc8',
        'YE, BENNY': 'aa5d1616a0c',
        'YU, KEITH': 'a3ff8d9e6c5',
        'ZHENG, ANDY': 'ad173456c5b',
        'ZHENG, STANLEY': 'a0f7e31bb36',
        'ZOU, ZENG WEN': 'a1cfe9eb5a7',
        },
    'p7': {
        'AGNIHOTRI, SATVIK': 'af316778a69',
        'ALLIE, RAYMOND': 'af316c26b79',
        'BARUA, PRITOM': 'a3fcecb86d5',
        'CHAN, KYLE': 'a0f7f3fb4a6',
        'CHEN, SKY': 'a8412a60a5e',
        'CHIN, LAUREN': 'ac0037c387a',
        'DENKER, WILLOW': 'a7814490781',
        'DEY, PRATTAY': 'ab75325303d',
        'GOSFIELD, ROXANA': 'ac07564792a',
        'GOYCHAYEV, RUSSELL': 'a1ddabbe1b7',
        'GRUNEBAUM, MAX': 'a8712a85aae',
        'JEONG, BINA': 'a7b9c4c9041',
        'JHA, SHWETLANA': 'a0c9e29b7f6',
        'JIANG, IAN': 'a0ceb2197a6',
        'KAISHIBAYEV, NURDAULET': 'a1eb88d96f7',
        'KHAN, FAHIM': 'ae217428c58',
        'LEI, ANGIER': 'a2eedf8d8a4',
        'LI, AIDEN': 'af355512969',
        'LIN, IVAN': 'ae24dd26538',
        'LOZANO, EDUARDO': 'a2ec9aaa8c4',
        'MEHTA, AAHAN': 'a7afc48edc1',
        'MIZHEN, AIDEN': 'af3226e4939',
        'NALYWAJKO, ANDREA': 'ae2561f7d18',
        'NISSON, ROY': 'ab77884799d',
        'REES, ABIGAIL': 'af33dd09c49',
        'SAFRONOV, NIKITA': 'a825339f30e',
        'TALUKDER, ABID': 'ae272211428',
        'TANG, DAVID': 'a2ee1d3e6f4',
        'TAYLOR, RORIE': 'ac0267c4b4a',
        'WONG, ANSON': 'a1de2eeab27',
        'WONG, LINSEY': 'a488ccfc182',
        'YAN, MEGAN': 'ab5d3440a5d',
        'YENTIN, DANIEL': 'a1dfae0da37',
        'ZAKI, RANIA': 'ae192471c68',
        },
    }

print('''\x1b[38;5;186m
 _____  _____               _                 _
/  __ \/  ___|             | |               | |
| /  \/\ `--.   _   _ _ __ | | ___   __ _  __| | ___ _ __
| |     `--. \ | | | | '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| \__/\/\__/ / | |_| | |_) | | (_) | (_| | (_| |  __/ |
 \____/\____/   \__,_| .__/|_|\___/ \__,_|\__,_|\___|_|
                     | |
                     |_|
\033[0m''')

platform = system()

filepath = environ['HOME']

directory = environ['PWD']

if argv[1] in 'setup':
    if platform == "Darwin":
        print('\033[92;1;3mWelcome to setup! To view this in the browser \033[0m(\033[31;1;4;3mStrongly recommended\033[0m)\033[92;1;3m, visit:\033[0m\n\n\033[92mhttps://github.com/gthompson30/stuycs-submit/blob/main/README.md\033[0m')
        print('\n\033[95mTo install stuycs-submit and allow it to be run from a Terminal command, run the following command:\033[0m')
        print('\n\033[96mcp stuycs-submit.py stuycs-submit\ncd ~/\033[0m')
        print('\n\033[95mCopy (don\'t run yet!) the following command:\n\033[0m')
        print('\033[96malias stuycs-submit="'+directory+'/stuycs-submit"\033[0m')
        print('\n\033[95mThen, run the following command (WARNING: this screen will go away):\n\033[0m')
        print('\033[96mnano .bash_profile\033[0m\n')
        print('\033[95m... and add the line you previously copied to the end of the file. When you\'re done, do Ctrl+X do exit.\033[0m\n')
        print('\033[33;1;3mCongrats! You now have stuycs-submit set up. To authenticate, run \'stuycs-submit authenticate\'\033[0m\n')
elif argv[1] == 'authenticate' or argv[1] == 'authentication':
    period = prompt({
        'type': 'list',
        'name': 'period',
        'message': 'Select your class period',
        'choices': ['p2', 'p5', 'p6', 'p7'],
        }, style=custom_style_3).get('period')

    names = [i for i in p[period]]

    id = p[period][prompt({
        'type': 'list',
        'name': 'name',
        'message': 'Select your name',
        'choices': names,
        }).get('name')]

    password = prompt({'type': 'password', 'name': 'password',
                      'message': 'Enter your bert.stuy.edu password:'},
                      style=custom_style_2).get('password')

    dumperee = open(filepath + '/info.p', 'wb')
    info = dump({'id': id, 'period': period, 'password': password},
                dumperee)

    print('''
\033[92mAuthenticating ...\033[0m
''')

    r = post('http://bert.stuy.edu/mykolyk/spring2021/pages.py', data={
        'page': 'homework_view2',
        'password': password,
        'students': id + ';',
        'classes': 'p6',
        }).text

    if 'homework/' in r:
        print('''\033[96mAuthenticated!
You can now submit assignments using: stuycs-submit [FILE]\033[0m
''')
    else:
        print('\033[91mAuthentication failed! Password incorrect.\033[0m\n')
        exit()
else:
    loaded = load(open(filepath + '/info.p', 'rb'))

    data = {
        'students': loaded['id'] + ';',
        'classes': loaded['period'],
        'password': loaded['password'],
        'page': 'submit_homework2',
        }

    r = post('http://bert.stuy.edu/mykolyk/spring2021/pages.py',
             data=data).text

    try:
        f = open(argv[1], 'rb')
    except:
        print('\nError: Either your file does not exist, is not in the directory, or your command format is wrong\n')
        exit()

    soup = BeautifulSoup(r, features='lxml')
    id4 = [i['value'] for i in soup.find_all('input') if i['name']
           == 'id4'][0]
    data['page'] = 'submit_homework2'
    r = post('http://bert.stuy.edu/mykolyk/spring2021/pages.py',
             data=data).text
    soup = BeautifulSoup(r, features='lxml')
    assignments = [i['value'] for i in soup.find_all('option')]

    assignment = prompt({
        'type': 'list',
        'name': 'assignment',
        'message': 'Select the assignment you would like to submit to',
        'choices': assignments,
        }, style=custom_style_3).get('assignment')

    if assignment not in assignments:
        print('Not a valid assignment!\n')
        exit()
    else:
        comment = prompt({'type': 'input', 'name': 'comment',
                         'message': '''Comments to teacher (leave blank for none):

'''},
                         style=custom_style_2).get('comment')

        post('http://bert.stuy.edu/mykolyk/spring2021/pages.py', data={
            'page': 'store_homework',
            'classid': loaded['period'],
            'id4': id4,
            'assignmentid': assignment,
            'teacher_comment': comment,
            }, files={'filecontents': f})

        r = post('http://bert.stuy.edu/mykolyk/spring2021/pages.py',
                 data={
            'page': 'homework_view2',
            'password': loaded['password'],
            'students': loaded['id'] + ';',
            'classes': loaded['period'],
            }).text

        index = r.index('-' + assignment + '-')

        print('''
\033[96mUpload successful! You can view your submission at:\033[0m
''')
        print('\033[96mhttp://bert.stuy.edu/mykolyk/spring2021/%s\033[0m\n' \
            % r[index - 21:index + 13])

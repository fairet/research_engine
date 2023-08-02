import requests
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import *
from bs4 import BeautifulSoup
from lxml import html

logging.basicConfig(level=logging.INFO)

def replace_spaces_with_percent20(input_string):
    char_list = list(input_string)
    for i in range(len(char_list)):
        if char_list[i] == ' ':
            char_list[i] = '%20'
    modified_str = ''.join(char_list)
    return modified_str

def search(input_string):
    result = replace_spaces_with_percent20(input_string)
    market = f"https://market.yandex.ru/search?text={result}"
    avito = f"https://www.avito.ru/ekaterinburg?q={result}"
    
    result0 = f'Ваш результат по запросу "{input_string}":\n\nАвито: {avito}\nЯндекс маркет: {market}'
    return result0





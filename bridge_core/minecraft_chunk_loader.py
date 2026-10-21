# -*- coding: utf-8 -*-
import time
from colorama import Fore

def load_cursed_chunks():
    print(Fore.BLUE + "\n[MINECRAFT] Загрузка поврежденных кубических чанков...")
    time.sleep(0.6)
    
    chunks = [
        "   [#] [Dirt_Bugged] [Bedrock_Crash] [Стив с дробовиком] [#]   ",
        "   [!] Предупреждение: Деревня жителей упала на завод по переработке меди."
    ]
    
    for c in chunks:
        print(Fore.LIGHTBLUE_EX + c)
        time.sleep(0.25)
        
    print(Fore.BLUE + "[MINECRAFT] Чанки успешно превращены в кашу.")
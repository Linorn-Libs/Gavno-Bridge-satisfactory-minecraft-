# -*- coding: utf-8 -*-
import time
from colorama import Fore

def pump_radioactive_poop():
    print(Fore.YELLOW + "\n[SATISFACTORY] Запуск конвейерной ленты MK.10 прямо в Майнкрафт...")
    time.sleep(0.6)
    
    conveyors = [
        "   === [ > ] === [ > ] === [ Ящик с радиоактивным говном ] === [ > ] ===   ",
        "   [FICSIT] Ошибка: Конвейер уходит в текстуры и ломает физику мира."
    ]
    
    for cv in conveyors:
        print(Fore.LIGHTYELLOW_EX + cv)
        time.sleep(0.25)
        
    print(Fore.YELLOW + "[SATISFACTORY] Логистика замкнута, завод работает в глубокий минус.")
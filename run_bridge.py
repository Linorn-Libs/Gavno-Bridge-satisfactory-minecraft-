# -*- coding: utf-8 -*-
import sys
import time
import threading
from colorama import init, Fore
from bridge_core.minecraft_chunk_loader import load_cursed_chunks
from bridge_core.satisfactory_conveyor import pump_radioactive_poop

init(autoreset=True)

def cpu_heater_leak():
    """Фоновый поток для уничтожения ПК"""
    garbage_collector_mock = []
    while True:
        garbage_collector_mock.append([i * 2 for i in range(10000)])
        time.sleep(0.01)

if __name__ == "__main__":
    # Запускаем печку в фоне
    heater = threading.Thread(target=cpu_heater_leak, daemon=True)
    heater.start()

    print(Fore.RED + "=" * 75)
    print(Fore.YELLOW + "🏭 SATISFACTORY x MINECRAFT GOVNO-BRIDGE v0.0.1-ALPHA 💩")
    print(Fore.RED + "=" * 75)
    
    ip = input(Fore.GREEN + "Введите IP сервера (или напишите 'говно'): ")
    if not ip:
        ip = "127.0.0.1:666"
        
    print(Fore.CYAN + f"\n[BRIDGE] Подключаемся к квантовой помойке {ip}...")
    time.sleep(1.0)
    
    load_cursed_chunks()
    pump_radioactive_poop()
    
    print(Fore.RED + "-" * 75)
    print(Fore.GREEN + "✅ МОСТ ГОТОВ! Стив строит конвейер MK.6 прямо в текстурах урана.")
    print(Fore.MAGENTA + "🔥 Внимание: Компьютер начал пахнуть жареным текстолитом.")
    print(Fore.RED + "=" * 75)
    
    # Бесконечный тупик, чтобы консоль не закрывалась
    while True:
        time.sleep(60)
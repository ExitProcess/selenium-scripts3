# при написании и отладке скриптов, driver.quit() как правило добавляется в скрипт
# в самом конце разработки. если пк время от времени перезагружается, то проблема неактуальна.
# но ноутбуки в основном находятся в режиме ожидания, поэтому количество процессов
# chromedriver.exe может доходить до 100 и более (каждый процесс весит 5-7 МБ).
# скрипт убивает все процессы chromedriver.exe.
# документация
# https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill

import os

os.system("taskkill /f /im chromedriver.exe")

# �ᯥ譮: ����� "chromedriver.exe", � �����䨪��஬ 14764, �� �����襭.
# �ᯥ譮: ����� "chromedriver.exe", � �����䨪��஬ 17284, �� �����襭.
# �ᯥ譮: ����� "chromedriver.exe", � �����䨪��஬ 16480, �� �����襭.
# �ᯥ譮: ����� "chromedriver.exe", � �����䨪��஬ 8568, �� �����襭.
# �ᯥ譮: ����� "chromedriver.exe", � �����䨪��஬ 17904, �� �����襭.

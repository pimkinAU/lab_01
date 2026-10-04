import subprocess
import sys


class TestCLI:
	def test_cli_calc(self):
		result = subprocess.run(
			[sys.executable, "-m", "toolkit", "calc", "2 + 3"],
			capture_output=True, # Положим вывод в переменную result.stdout
			text=True, # Вывод текстом (str), а не байтами
			cwd="src", # Указание директории, где лежит toolkit
			check=False # Не выдавать ошибку CalledProcessError, если процесс завершился не с кодом 0
		)
		assert result.returncode == 0
		assert result.stdout.strip() == "5.0"
	def test_cli_convert(self):
		result = subprocess.run(
			[sys.executable, '-m', 'toolkit', 'convert', '10', '--from', 'km', '--to', 'm'],
			capture_output=True,
			text=True,
			cwd='src',
			check=False
		)
		assert result.returncode == 0
		assert result.stdout.strip() == '10000.0'


from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	'''Тест нового посетителя'''

	def setUp(self):
		'''установка (конструктор)'''
		self.browser = webdriver.Firefox()

	def tearDown(self):
		'''демонтаж (деструктор)'''
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		'''тест: можно начать список и получить его позже'''
		# открываем домашнюю страницу
		self.browser.get('http://localhost:8000')
		# заголовок и шапка должны соответствовать
		self.assertIn('To-Do', self.browser.title)
		self.fail('Закончить тест!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')

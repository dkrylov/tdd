from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		#Предлагается сразу ввести эл-и списка
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		#Добавляем что нужно сделать
		inputbox.send_keys('Купить павлиньи перья')

		#после нажатия enter, страница обновляетсяи содержит эл-т списка
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Купить павлиньи перья' for row in rows)
		)

		self.fail('Закончить тест!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class AvitoFavoritesTest(unittest.TestCase):

    def setUp(self):
        # Задаем путь к исполняемому файлу ChromeDriver
        service = Service(executable_path='./chromedriver.exe')
        # Инициализируем веб-драйвер Chrome
        self.driver = webdriver.Chrome(service=service)
        # Максимизируем окно браузера
        self.driver.maximize_window()
        # Задаем базовый URL для тестируемого сайта
        self.base_url = "https://www.avito.ru"

    def test_add_favorite(self):
        driver = self.driver

        # Открываем страницу товара
        driver.get(self.base_url + "/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

        # Находим кнопку "Добавить в избранное" и кликаем на нее
        add_to_fav_button = driver.find_element(By.CLASS_NAME, "desktop-usq1f1")
        add_to_fav_button.click()

        # Проверяем, успешно ли добавлено в избранное
        driver.get(self.base_url + "/favorites")
        try:
            # Пытаемся найти ссылку на добавленное объявление в избранном
            check_fav = driver.find_element(By.XPATH,
                                            '//a[@href="/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"]')
        except:
            # Если ссылка не найдена, то тест считается неудачным
            self.assertTrue(False, "Ad not in favorites")

    def tearDown(self):
        # Завершаем работу веб-драйвера и закрываем браузер
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

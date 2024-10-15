import allure
import pytest
from allure import feature, story
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from playwright.sync_api import sync_playwright, Page
from browser import set_up_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass:
    def setup_method(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
        self.page.goto("https://pizzeria.skillbox.cc")

    def teardown_method(self):
        self.browser.close()
        self.playwright.stop()

    @allure.title("Проверка отображения слайдера на главной странице")
    def test_slider_display(self):
        slider = self.page.locator(".prod1-slider")
        assert slider.is_visible()

    @allure.title("Добавление в корзину")
    def test_add_to_cart(self, set_up_browser):
        driver = set_up_browser

        with allure.step("Открытие главной страницы"):

            driver.get("https://pizzeria.skillbox.cc/")

        with allure.step("Кладём два товара в корзину"):

            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )

            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )

            el_3 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )

            el_4 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )

            actions = ActionChains(driver)

            actions.move_to_element(el_1).pause(2)

            actions.click(el_2).pause(2)

            actions.perform()

            actions.move_to_element(el_3).pause(2)

            actions.click(el_4).pause(2)

            actions.perform()
        with allure.step("Проверяем наличие товара в корзине"):
            cart_text = self.page.text_content(".cart-contents")
            assert (
                "\n\t\t\t\t\t [ 0,00₽ ]\n\t\t\t\t" in cart_text
            ), "Товар не добавлен в корзину"

    @allure.step("Переход к описанию пиццы")
    def test_view_pizza_description(self):
        slider = self.page.locator(".prod1-slider")
        pizza_image = slider.locator(
            "#accesspress_store_product-5 > ul > div > div > li:nth-child(6) > div > a:nth-child(1) > img"
        ).first
        pizza_image.click()
        assert "product" in self.page.url, "URL does not contain 'product'"

    @allure.step("Регистрация нового пользователя")
    def test_register_new_user(self):
        self.page.goto("https://pizzeria.skillbox.cc/register/")
        self.page.fill("input[name='username']", "newuser")
        self.page.fill("input[name='email']", "newuser@example.com")
        self.page.fill("input[name='password']", "password123")
        self.page.click(
            "button.woocommerce-Button.woocommerce-button.button.woocommerce-form-register__submit"
        )
        self.page.goto("https://pizzeria.skillbox.cc/my-account/")

    @allure.step("Проверка корзины и редактирование количества пиццы")
    def test_cart_edit_quantity(self, set_up_browser):
        driver = set_up_browser

        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")

        with allure.step("Кладём два товара в корзину"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )
            el_3 = driver.find_element(
                By.XPATH,
                "(//img[@src='http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-katerina-holmes-5908222-300x300.jpg'])[2]",
            )
            el_4 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[6]",
            )

            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
            actions.move_to_element(el_3).pause(2)
            actions.click(el_4).pause(2)
            actions.perform()

        with allure.step("Редактирование количества товара в корзине"):
            driver.get("https://pizzeria.skillbox.cc/cart/")
            quantity_input = driver.find_element(
                By.CSS_SELECTOR, "input.input-text.qty.text"
            )
            quantity_input.clear()
            quantity_input.send_keys("2")

            update_button = driver.find_element(
                By.XPATH, '//button[contains(text(), "Обновить корзину")]'
            )
            update_button.click()
            driver.implicitly_wait(2)

            assert quantity_input.get_attribute("value") == "2"

    @allure.step("Добавление товара в корзину и его удаление")
    def test_add_and_remove_item_from_cart(self, set_up_browser):
        driver = set_up_browser

        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")

        with allure.step("Кладём товар в корзину"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )

            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()
        with allure.step("Переход в корзину"):
            driver.get("https://pizzeria.skillbox.cc/cart/")

        with allure.step("Проверка наличия товара в корзине"):
            cart_item = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[1]/td[3]/a',
                    )
                )
            )
            assert cart_item.is_displayed(), "Item not found in the cart"

        with allure.step("Удаление товара из корзины"):
            remove_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        '//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[1]/td[1]/a',
                    )
                )
            )
            actions = ActionChains(driver)
            actions.move_to_element(remove_button).pause(2)
            actions.click(remove_button).pause(2)
            actions.perform()

        with allure.step("Проверка, что товар удален из корзины"):
            # Заново ищем элемент, чтобы избежать StaleElementReferenceException
            WebDriverWait(driver, 10).until(EC.staleness_of(cart_item))
            assert not driver.find_elements(
                By.XPATH,
                '//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[1]/td[3]/a',
            ), "Item still visible in the cart after removal"

    @allure.feature("Тестирование веб-сайта Pizzeria")
    @allure.story("Проверка функциональности фильтрации десертов")
    def test_filter_desserts_by_price(self, set_up_browser):
        driver = set_up_browser

        with allure.step("Инициализация драйвера и открытие страницы"):
            try:
                driver.get("https://pizzeria.skillbox.cc/product-category/menu/")
                driver.set_window_size(1920, 1080)
            except Exception as e:
                pytest.fail(f"Ошибка при загрузке страницы: {e}")

        with allure.step("Переход к разделу десертов"):
            desserts_link = driver.find_element(
                By.XPATH, '//*[@id="woocommerce_product_categories-2"]/ul/li[1]/a'
            )
            desserts_link.click()

        with allure.step("Изменение диапазона цены"):
            price_slider_start = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[1]',
                    )
                )
            )
            price_slider_end = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]',
                    )
                )
            )

        with allure.step("Изменение значений ползунков с использованием Selenium"):
            try:
                actions = ActionChains(driver)
                actions.click_and_hold(price_slider_start).move_by_offset(
                    80, 0
                ).release().perform()
                actions.click_and_hold(price_slider_end).move_by_offset(
                    -100, 0
                ).release().perform()
                accept_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            '//*[@id="woocommerce_price_filter-2"]/form/div/div[2]/button',
                        )
                    )
                )
                actions = ActionChains(driver)
                actions.move_to_element(accept_button).pause(2)
                actions.click(accept_button).pause(2)
                actions.perform()
            except Exception as e:
                pytest.fail(f"Ошибка при изменении значений ползунков: {e}")

        with allure.step("Проверка наличия десертов с ценой 135 на странице"):
            dessert_elements = driver.find_elements(
                By.CSS_SELECTOR, "#primary > div > div.wc-products > ul"
            )
            dessert_texts = [element.text for element in dessert_elements]
            assert any(
                "135" in text for text in dessert_texts
            ), "Десерты с ценой 135 не найдены на странице"

    @allure.feature("Оформление заказа")
    def test_place_order(self, set_up_browser):
        driver = set_up_browser

        with allure.step("Проходим авторизацию"):
            driver.get("https://pizzeria.skillbox.cc/my-account/")
            username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
            password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
            login_button = driver.find_element(By.XPATH, '//*[@name="login"]')

            username_input.send_keys("esenin1993")
            password_input.send_keys("123Kent_")
            login_button.click()

        with allure.step("Открытие главной страницы"):
            driver.get("https://pizzeria.skillbox.cc/")

        with allure.step("Кладём товар в корзину"):
            el_1 = driver.find_element(
                By.XPATH,
                '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]',
            )
            el_2 = driver.find_element(
                By.XPATH,
                "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]",
            )

            actions = ActionChains(driver)
            actions.move_to_element(el_1).pause(2)
            actions.click(el_2).pause(2)
            actions.perform()

        with allure.step("Переход в корзину"):
            driver.get("https://pizzeria.skillbox.cc/cart/")

        with allure.step("Переход к оформлению товара"):
            buy_button = driver.find_element(
                By.XPATH,
                '//*[@id="post-20"]/div/div/div/div[2]/div[2]/div/div/a',
            )
            actions = ActionChains(driver)
            actions.move_to_element(buy_button).pause(2)
            actions.click(buy_button).pause(2)
            actions.perform()

        with allure.step("Заполнение информации для заказа"):
            driver.find_element(By.XPATH, '//*[@id="billing_first_name"]').send_keys(
                "Александр"
            )
            driver.find_element(By.XPATH, '//*[@id="billing_last_name"]').send_keys(
                "Бастрыгин"
            )
            driver.find_element(By.XPATH, '//*[@id="billing_address_1"]').send_keys(
                "Адрес"
            )
            driver.find_element(By.XPATH, '//*[@id="billing_city"]').send_keys("Город")
            driver.find_element(By.XPATH, '//*[@id="billing_state"]').send_keys(
                "Область"
            )
            driver.find_element(By.XPATH, '//*[@id="billing_postcode"]').send_keys(
                "612612"
            )
            driver.find_element(By.XPATH, '//*[@id="billing_phone"]').send_keys(
                "89121211212"
            )

        with allure.step("Подтверждение заказа"):
            terms = driver.find_element(By.XPATH, '//*[@id="terms"]')
            actions = ActionChains(driver)
            actions.move_to_element(terms).pause(2)
            actions.click(terms).pause(2)
            actions.perform()

            order_button = driver.find_element(By.XPATH, '//*[@id="place_order"]')
            actions = ActionChains(driver)
            actions.move_to_element(order_button).pause(2)
            actions.click(order_button).pause(2)
            actions.perform()

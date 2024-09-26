import allure
from allure import feature, story
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from playwright.sync_api import sync_playwright, Page


# service = Service('C:/Users/eseni/.wdm/drivers/chromedriver/win64/126.0.6478.126/chromedriver-win32/chromedriver.exe')
# driver = webdriver.Chrome(service=service)

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
            assert "\n\t\t\t\t\t [ 0,00₽ ]\n\t\t\t\t" in cart_text, "Товар не добавлен в корзину"



    @allure.step("Переход к описанию пиццы")
    def test_view_pizza_description(self):
        slider = self.page.locator(".prod1-slider")
        pizza_image = slider.locator("#accesspress_store_product-5 > ul > div > div > li:nth-child(6) > div > a:nth-child(1) > img").first
        pizza_image.click()
        assert "product" in self.page.url, "URL does not contain 'product'"
        
        
    @allure.step("Регистрация нового пользователя")
    def test_register_new_user(self):
        self.page.goto("https://pizzeria.skillbox.cc/register/")
        self.page.fill("input[name='username']", "newuser")
        self.page.fill("input[name='email']", "newuser@example.com")
        self.page.fill("input[name='password']", "password123")
        self.page.click("button.woocommerce-Button.woocommerce-button.button.woocommerce-form-register__submit")
        self.page.goto("https://pizzeria.skillbox.cc/my-account/")


    @allure.step("Проверка корзины и редактирование количества пиццы")
    def test_cart_edit_quantity(self):
        
        self.page.goto("https://pizzeria.skillbox.cc/product-category/menu/pizza/")
        add_to_cart_button = self.page.locator('//*[@id="primary"]/div/div[3]/ul/li[1]/div[2]/div/a')
        add_to_cart_button.click()
        
        self.page.goto("https://pizzeria.skillbox.cc/cart/")
        
        quantity_input = self.page.locator('input.input-text.qty.text')
        quantity_input.wait_for(state='visible', timeout=60000)
        
        quantity_input.focus()
        quantity_input.fill("2")
        
        update_button = self.page.locator('//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[2]/td/button')
        update_button.click()
        
        self.page.wait_for_timeout(2000)
        
        assert quantity_input.input_value() == "2"

    # @allure.step("Добавление товара в корзину и его удаление")
    # def test_add_and_remove_item_from_cart(self):
        
    #     # Перейдите на страницу товара и добавьте его в корзину
    #     self.page.goto("https://pizzeria.skillbox.cc/product-category/menu/pizza/")
    #     add_to_cart_button = self.page.locator('//*[@id="primary"]/div/div[3]/ul/li[1]/div[2]/div/a')
    #     add_to_cart_button.click()
        
    #     # Перейдите в корзину
    #     self.page.locator('//*[@id="primary"]/div/div[3]/ul/li[1]/div[2]/div/a[2]')
        
    #     # Убедитесь, что товар добавлен в корзину
    #     cart_item = self.page.locator('//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[1]/td[3]/a')
    #     assert cart_item.is_visible(), "Item not found in the cart"
        
    #     # Нажмите кнопку удаления товара
    #     remove_button = self.page.locator('//*[@id="post-20"]/div/div/div/div[2]/form/table/tbody/tr[1]/td[1]/a')
    #     remove_button.click()
        
    #     # Проверьте, что товар удален из корзины
    #     assert not cart_item.is_visible(), "Item still visible in the cart after removal"


    # @allure.feature('Тестирование веб-сайта Pizzeria')
    # @allure.story('Проверка функциональности фильтрации десертов')
    # @pytest.mark.asyncio(scope="function")
    # async def test_filter_desserts_by_price(self):
    #     async with async_playwright() as p:
    #         browser = await p.chromium.launch()
    #         page = await browser.new_page()
    #         with allure.step('Инициализация драйвера и открытие страницы'):
    #             try:
    #                 await page.goto("https://pizzeria.skillbox.cc/product-category/menu/", timeout=180000)
    #                 await page.set_viewport_size({"width": 1920, "height": 1080})
    #             except Exception as e:
    #                 print(f"Ошибка при загрузке страницы: {e}")
    #                 await browser.close()
    #                 return

    #         with allure.step('Переход к разделу десертов'):
    #             await page.click('//*[@id="woocommerce_product_categories-2"]/ul/li[1]/a')

    #         with allure.step('Изменение диапазона цены'):
    #             price_slider_start = await page.locator('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[1]')
    #             price_slider_end = await page.locator('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')

    #         with allure.step('Ожидание загрузки элементов'):
    #             await price_slider_start.wait_for(state='visible', timeout=20000)
    #             await price_slider_end.wait_for(state='visible', timeout=20000)

    #         with allure.step('Изменение значений ползунков с использованием Playwright'):
    #             try:
    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[1]', 'mousedown', timeout=60000)
    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[1]', 'mousemove', {'clientX': 100}, timeout=60000)
    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[1]', 'mouseup', timeout=60000)

    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]', 'mousedown', timeout=60000)
    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]', 'mousemove', {'clientX': -100}, timeout=60000)
    #                 await page.dispatch_event('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]', 'mouseup', timeout=60000)
    #             except Exception as e:
    #                 print(f"Ошибка при изменении значений ползунков: {e}")
    #                 await browser.close()
    #                 return

    #         with allure.step('Проверка наличия десертов с ценой 135 на странице'):
    #             dessert_elements = await page.locator('.dessert-item').all_text_contents()
    #             assert any("135" in element for element in dessert_elements), "Десерты с ценой 135 не найдены на странице"

    #         await browser.close()
    #         await p.stop()
    #         await asyncio.sleep(0)
    
    # @allure.step("Оформление заказа")
    # def test_place_order(self):
    #     logger.info("Testing place order")
    #     self.page.goto("https://pizzeria.skillbox.cc/cart")
    #     self.page.locator("button", has_text="Оформить заказ").click()
    #     self.page.fill("input[name='address']", "123 Main St")
    #     self.page.fill("input[name='date']", "2024-09-04")
    #     self.page.locator("button", has_text="Подтвердить заказ").click()
    #     logger.info("Order placed successfully")
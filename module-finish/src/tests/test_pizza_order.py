import allure
from allure import feature, story
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from playwright.sync_api import sync_playwright, Page

driver = webdriver.Chrome()
actions = ActionChains(driver)

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
    def test_add_to_cart(self):
        self.page.goto("http://pizzeria.skillbox.cc/")

        # Достаем элемент картинки
        img_selector = '(//img[@src="http://pizzeria.skillbox.cc/wp-content/uploads/2021/10/pexels-natasha-filippovskaya-4394612-300x300.jpg"])[1]'

        # Достаем элемент кнопки "Добавить в корзину"
        add_to_cart_button_selector = "(//*[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'])[5]"

        self.page.hover(img_selector)
        self.page.click(add_to_cart_button_selector)

        cart_text = self.page.text_content(".cart-contents")
        assert "1 item" in cart_text, "Товар не добавлен в корзину"



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



    # @allure.step("Проверка корзины и редактирование количества пиццы")
    # def test_cart_edit_quantity(self):
    #     logger.info("Testing cart edit quantity")
        
    #     # Перейдите на страницу товара и добавьте его в корзину
    #     self.page.goto("https://pizzeria.skillbox.cc/product-category/menu/pizza/")
    #     add_to_cart_button = self.page.locator('#primary > div > div.wc-products > ul > li.product.type-product.post-425.status-publish.first.instock.product_cat-pizza.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > div.collection_desc.clearfix > div > a')  # Предположим, что селектор обновлен
    #     add_to_cart_button.click()
        
    #     # Перейдите в корзину
    #     self.page.goto("https://pizzeria.skillbox.cc/cart/")
        
    #     # Ожидание полной загрузки страницы
    #     self.page.wait_for_load_state('networkidle')
        
    #     # Ожидание, пока поле количества станет видимым
    #     quantity_input = self.page.locator('input.input-text.qty.text')
    #     quantity_input.wait_for(state='visible', timeout=60000)  # Увеличьте таймаут, если нужно
        
    #     # Установите фокус и заполните поле
    #     quantity_input.focus()
    #     quantity_input.fill("2")
        
    #     # Нажмите кнопку обновления корзины
    #     update_button = self.page.locator('update_cart')  # Обновите селектор
    #     update_button.click()
        
    #     # Подождите некоторое время, чтобы изменения вступили в силу
    #     self.page.wait_for_timeout(2000)  # 2 секунды
        
    #     # Проверьте, что значение обновилось
    #     assert quantity_input.input_value() == "2"

    # @allure.step("Добавление товара в корзину и его удаление")
    # def test_add_and_remove_item_from_cart(self):
    #     logger.info("Testing add and remove item from cart")
        
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

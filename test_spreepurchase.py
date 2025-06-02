import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import logging

class TestSpreepurchase():
    @pytest.fixture()
    def setup(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.get("https://demo.spreecommerce.org/products")
      yield self.driver
      self.driver.quit()

    def test_product_purchase(self,setup):
       product = WebDriverWait(self.driver,20).until(
           EC.visibility_of_element_located((By.XPATH,"//*[@id='product-255']/div[1]/div/div/figure/img"))
       )
       product.click()
       time.sleep(5)
       select_size = WebDriverWait(self.driver,20).until(
           EC.visibility_of_element_located((By.XPATH,"/html/body/main/turbo-frame[1]/div/div/div/div[3]/div/div[2]/form/div[3]/div[1]/button"))
       )
       select_size.click()
       time.sleep(5)
       selected_size = WebDriverWait(self.driver,20).until(
           EC.visibility_of_element_located((By.XPATH,"//*[@id='product-variant-picker']/fieldset[2]/div/div[2]/div/label[1]"))
       )
       selected_size.click()
       time.sleep(5)
       add_to_cart = WebDriverWait(self.driver,30).until(
           EC.visibility_of_element_located((By.XPATH,"//*[@id='product-details-page']/div[3]/div/div[2]/form/div[3]/div[1]/button"))
       )
       add_to_cart.click()
       time.sleep(10)
       checkout = WebDriverWait(self.driver,30).until(
           EC.visibility_of_element_located((By.XPATH,"//*[@id='cart_summary']/div/div[2]/div[2]/a"))
       )
       checkout.click()
       time.sleep(2)
       email_id = WebDriverWait(self.driver,20).until(
           EC.visibility_of_element_located((By.ID,"order_ship_address_attributes_email"))
       )
       email_id.send_keys("remya@gmail.com")
       time.sleep(2)
       country_dropdown = self.driver.find_element(By.ID, "order_ship_address_attributes_country_id")
       select = Select(country_dropdown)
       select.select_by_visible_text("India")
       time.sleep(2)
       firstname = self.driver.find_element(By.ID,"order_ship_address_attributes_firstname")
       firstname.send_keys("REMYA")
       lastname = self.driver.find_element(By.ID,"order_ship_address_attributes_lastname")
       lastname.send_keys("RAVI")
       self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(2)
       street_name = self.driver.find_element(By.ID,"order_ship_address_attributes_address1")
       street_name.send_keys("Irkkur")
       city = self.driver.find_element(By.ID,"order_ship_address_attributes_city")
       self.driver.execute_script("arguments[0].scrollIntoView(true);", city)
       city.send_keys("Kannur")
       state_dropdown = self.driver.find_element(By.ID, "order_ship_address_attributes_state_id")
       select = Select(state_dropdown)
       select.select_by_value("5999")
       postalcode = self.driver.find_element(By.ID, "order_ship_address_attributes_zipcode")
       postalcode.send_keys("670593")
       submit_button = self.driver.find_element(By.XPATH, "//*[@id='checkout_form_address']/div[2]/button")
       submit_button.click()
       time.sleep(5)
       submit_button2 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[3]/form/div[2]/div/button")
       submit_button2.click()
       pay_now = WebDriverWait(self.driver, 20).until(
           EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout-payment-submit']"))
       )
       self.driver.execute_script("arguments[0].scrollIntoView(true);", pay_now)
       pay_now.click()
       time.sleep(2)
       confirmation_message = WebDriverWait(self.driver, 20).until(
           EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your order is confirmed!')]"))
       )

       assert "Order Confirmation Failed" in confirmation_message.text
       logging.info("[INFO]order placed successfully as expected..")



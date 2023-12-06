import time
from selenium import webdriver

class Utils:
    @staticmethod
    def escribir(element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.15)

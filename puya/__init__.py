from selenium import webdriver
import os

def clean():
    clearScreen = os.system('cls')

def initializeDriver():
    driver = webdriver.chrome
    driver.get("www.google.com")

print("       - Welcome Senpai! to PUYA-CHAN v.1.0.0 - \n")

initializeDriver()
input()









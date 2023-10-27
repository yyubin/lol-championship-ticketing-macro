from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui
import time
import smtplib
from email.message import EmailMessage

def send_mail():
    gmail_smtp = "smtp.gmail.com"
    gmail_port = 465
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

    account = ""
    pwd = ""
    smtp.login(account, pwd)

    to_mail = ""

    message = EmailMessage()
    message.set_content('결제를 마무리 해주세요')
    message["Subject"] = "롤드컵 티켓팅 성공"
    message["From"] = account
    message["To"] = to_mail

    smtp.send_message(message)
    smtp.quit()

currentmouseX, currentmouseY = pyautogui.position()
print(currentmouseX, currentmouseY)

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.set_window_size(1400, 1000)

driver.get('https://ticket.interpark.com/Gate/TPLogin.asp')

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))

id = driver.find_element(By.ID, 'userId')
id.send_keys('')
pw = driver.find_element(By.ID, 'userPwd')
pw.send_keys('')
pw.send_keys(Keys.ENTER)

li = [0 for i in range(8)]
flag = False
def ticketing():
    global flag
    driver.get("https://poticket.interpark.com/SportsBook/BookMain.asp?GroupCode=23010160")

    driver.switch_to.frame('ifrmSeat')

    for i in range(8):
        li[i] = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div[2]/div[1]/a[{i + 1}]")

    for i in li:
        if i.get_attribute('rc') != '0':
            pyautogui.keyDown('command')
            pyautogui.keyDown('option')
            pyautogui.press('i')
            pyautogui.keyUp('option')
            pyautogui.keyUp('command')

            pyautogui.moveTo(1200, 420)
            pyautogui.click()

            pyautogui.keyDown('command')
            pyautogui.press('f')
            pyautogui.keyUp('command')

            # captchSliderLayer

            pyautogui.press('c')
            pyautogui.press('a')
            pyautogui.press('p')
            pyautogui.press('t')
            pyautogui.press('c')
            pyautogui.press('h')
            pyautogui.press('s')
            pyautogui.press('l')
            pyautogui.press('i')
            pyautogui.press('d')
            pyautogui.press('e')
            pyautogui.press('r')

            pyautogui.moveTo(1200, 420)
            time.sleep(0.01)
            pyautogui.click()
            pyautogui.press('enter')
            pyautogui.press('tab')

            pyautogui.press('=')
            pyautogui.press('d')
            pyautogui.press('i')
            pyautogui.press('s')
            pyautogui.press('p')
            pyautogui.press('l')
            pyautogui.press('a')
            pyautogui.press('y')
            pyautogui.keyDown('shift')
            pyautogui.press(';')
            pyautogui.keyUp('shift')
            pyautogui.press('n')
            pyautogui.press('o')
            pyautogui.press('n')
            pyautogui.press('e')
            pyautogui.press(';')
            pyautogui.press('enter')

            i.click()
            flag = True
            driver.find_element(By.XPATH, "//div[@class='twoBtn']/a[1]").click()

            pyautogui.moveTo(1200, 420)
            pyautogui.click()
            pyautogui.keyDown('command')
            pyautogui.press('f')
            pyautogui.keyUp('command')

            pyautogui.press('f')
            pyautogui.press('n')
            pyautogui.press('c')
            pyautogui.press('h')
            pyautogui.press('e')
            pyautogui.press('c')
            pyautogui.press('k')
            pyautogui.press('enter')

            pyautogui.moveTo(1200, 420)
            time.sleep(0.01)
            pyautogui.click()
            pyautogui.press('enter')
            pyautogui.press('tab')

            pyautogui.press('right')
            pyautogui.press('left')
            pyautogui.press('left')
            pyautogui.keyDown('shift')
            pyautogui.press('o')
            pyautogui.press('k')
            pyautogui.keyUp('shift')
            pyautogui.press('enter')

            driver.find_element(By.XPATH, '//*[@id="divRecaptcha"]/div[1]/div[4]/a').click()
            driver.find_element(By.XPATH, "//div[@class='twoBtn']/a[1]").click()

            time.sleep(1)

            send_mail()
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/iframe'))
            select = Select(driver.find_element(By.XPATH, '//*[@id="PriceRow000"]/td[3]/select'))
            select.select_by_index(1)
            driver.switch_to.default_content()
            driver.find_element(By.ID, 'SmallNextBtnImage').click()

            driver.switch_to.frame('ifrmBookCertify')
            driver.find_element(By.ID, "Agree").click()
            driver.find_element(By.XPATH, '//*[@id="information"]/div[2]/a[1]/img').click()

            driver.switch_to.default_content()
            driver.find_element(By.ID, 'SmallNextBtnImage').click()

            time.sleep(100000)

    pyautogui.keyDown('command')
    pyautogui.keyDown('option')
    pyautogui.press('i')
    pyautogui.keyUp('option')
    pyautogui.keyUp('command')

while not flag:
    ticketing()

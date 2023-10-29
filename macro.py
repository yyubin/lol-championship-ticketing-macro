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
    time.sleep(1)
    driver.get("https://poticket.interpark.com/SportsBook/BookMain.asp?GroupCode=23010160")

    driver.switch_to.frame('ifrmSeat')

    for i in range(8):
        li[i] = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div[2]/div[1]/a[{i + 1}]")

    for i in li:
        if i.get_attribute('rc') != '0':
            slider = driver.find_element(By.CLASS_NAME, "captchSliderLayer")
            driver.execute_script("arguments[0].style.display = 'none';", slider)
            i.click()
            flag = True
            driver.find_element(By.XPATH, "//div[@class='twoBtn']/a[1]").click()

            blank = driver.find_element(By.XPATH, "//*[@id='divRecaptcha']/div[1]/div[4]/a")
            driver.execute_script("arguments[0].setAttribute('onclick', 'fnCheckOK();')", blank)

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

while not flag:
    ticketing()






#https://ticket.interpark.com/Gate/TPLogOut.asp?From=T&tid1=main_gnb&tid2=right_top&tid3=logout&tid4=logout
#https://poticket.interpark.com/SportsBook/BookMain.asp?GroupCode=23010160
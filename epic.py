from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import base64
import time

state = "Tamil Nadu"
total = []
datas = ['ZBC2794394',
 'ZBC2794402']
#  ,'ZBC2072882',
#  '2BC2794410',
#  'FMS1957802',
#  'ZBC2451508',
#  'ZBC2127025',
#  '2BC2226462',
#  '2BC2226553']

def solve(f):
    with open(f, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')
            url = 'http://127.0.0.1:5000/captcha'

            data = { 
                'base64':encoded_string
            }
            response = requests.post(url = url, json = data)
            final = response.json()
            print(final)
            return final['Captcha']

def find(data,state):
    driver = webdriver.Firefox()
    driver.get("https://electoralsearch.in/")
    time.sleep(2)

    cont = driver.find_element("id","continue")
    cont.click()
    tab = driver.find_element("css selector",".tabs > ul:nth-child(2) > li:nth-child(2)")
    tab.click()
    
    epic = driver.find_element("id","name")
    epic.send_keys(data,Keys.TAB)

    epic_state = driver.find_element("id","epicStateList")
    epic_state.click()
    options = epic_state.find_elements("css selector","option")
    for option in options:
        if option.text == state:
            option.click()

    #captcha code
    while(True):
        try:
            views = driver.find_element("xpath", "/html/body/div[5]/div[3]/div[2]/div/table/tbody/tr/td[1]/form/input[25]")
            break
        except:
            with open('filename.jpg', 'wb') as file:
                file.write(driver.find_element('id','captchaEpicImg').screenshot_as_png)
            captch = solve("filename.jpg")

            enter = driver.find_element('id','txtEpicCaptcha')
            enter.send_keys(captch,Keys.TAB)

            driver.find_element("css selector","#btnEpicSubmit").click()
            time.sleep(1)
            
    person = []

    try:
        age =driver.find_element('xpath','/html/body/div[5]/div[3]/div[2]/div/table/tbody/tr/td[4]').text
        print(age)
        views = driver.find_element("xpath", "/html/body/div[5]/div[3]/div[2]/div/table/tbody/tr/td[1]/form/input[25]")
        views.click();
        driver.switch_to.window(driver.window_handles[1])
        p = driver.page_source
        #print(p)
        time.sleep(10)

        og_name = driver.find_element("xpath","/html/body/bo/div[2]/div/div[1]/form/table/tbody/tr[7]/td").text
        print(og_name)
        husBro = driver.find_element('xpath','/html/body/bo/div[2]/div/div[1]/form/table/tbody/tr[10]/td[1]').text
        print(husBro.split('/')[1].split("'")[0]) 
        sp_name = driver.find_element('xpath',"/html/body/bo/div[2]/div/div[1]/form/table/tbody/tr[11]/td").text
        print(sp_name)

        person = {'age':age,'name':og_name,'relationship':husBro.split('/')[1].split("'")[0],"relation-name":sp_name}

    except:
        print('No Load')
        driver.close()

    return person

for data in datas:
    total.append(find(data,state))

print(total)
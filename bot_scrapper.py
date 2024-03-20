from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings

from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

warnings.simplefilter.("ignore")
url = f'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Talk%20T0%20AVA%22%2C%22botConversationDescription%C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3А%22bp-web-widget%22%2C%22encryptionKey%22%3А%22Irg]j02qz6miJtEKUVSASHAOFQNwG0fv%22%7D%7D'
chrome_driver_path = 'chromedriver exe'
chrome_options = Options()

# chrome_options.add_argument("--headless=new") # Enable headless mode (runs Chrome without GUI)


chrome_options.add_argument ('--log-level=3') # Set Chrome Log Level


service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')


driver = webdriver.Chrome(service-service, options-chrome_options)


driver.maximize_window()
driver.get(url)

sleep(3)



def click_on_chat_button():
    
    button = driver.find_element(By.XPATH, '/html/body/div/div/button').click()
    sleep (2)
    while True:
        
        try:
            
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            print('Initializing ava...')
            
            if not is_visible:
                
                break
            
            else:
                pass
        except NoSuchElementException:
            
            print('AVA is Initializing.')
            
            break
        sleep(1)
        
        
        
def sendQuery(text):
    
    # Find and interact with the textarea element
    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    sleep(1)
    
    send_btn = driver.find_element(By.ID, 'btn-send').click()
    sleep(1)
    
    
    
def isBubbleLoaderVisible():
    
    print('AVA Is Typing...')
    while True:
        
        try:
            
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader. is_displayed()
            
            if not is_visible:
                break
            
            else:
                pass
            
        except NoSuchElementException:
            
            print('AVA Is Sending Mesage...')
            break
        
        sleep(1)
        
        
chatnumber = 2


def retriveData():
    
    print('Retriving Chat...')
    global chatnumber
    sleep(1)
    p = driver.find_element(
        By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div|{chatnumber}]/div/div[2]/div/div/div/div/div/p')
    
    print("\nAVA: " + p.text)
    chatnumber = chatnumber + 2
    
    return(p.text)


# click_on_chat_button()

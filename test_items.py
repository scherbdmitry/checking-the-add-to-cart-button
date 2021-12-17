from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def test_check_button_add_basket(browser):
    
    button_text = ""
    
    try:
        #go to link site
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
    	
        #pause, install manually
        time.sleep(5)
     
        #looking for 'add to cart' button
        button_text = browser.find_element(By.CLASS_NAME,"btn-add-to-basket").text
    
    except NoSuchElementException:
        
        #checking and displaying a message when the button is not found
        assert len(button_text) !=0,"'add to cart' button is missing"
    
    

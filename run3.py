from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from . import humar


from urllib.parse import quote  #Uncomment line below to use python 3 

from time import sleep

#update css selector if you have any issues
css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
Thank you so much for your purchase of Paricott Paper cups from Amazon!
A little of your time and a few brief words would go a long way to help other customers make a decision!
Simply click on the link below to give us star rating & post your review.
https://www.amazon.in/review/create-review/?ie=UTF8&channel=glance-detail&asin='''     


driver = webdriver.Chrome("C:\\Atharva\\Webdriver\\chromedriver.exe")


msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
driver.get("https://web.whatsapp.com")  # first call without delay in order to scan qr code
sleep(2)

object_atharva = humar.ReturnListOfNumbers()
ten_digit_codes_list = object_atharva.return_list('C:\\Users\\hp\\Downloads\\Compressed\\WhatsAppBulkMessenger-master\\New folder\\ASIN.txt')

object_contact_number = number_extractor.Number_Extractor()
contact_number_list = object_contact_number.number_extractor_list_return('C:\\Users\\hp\\Downloads\\Compressed\\WhatsAppBulkMessenger-master\\New folder\\numbers.txt')

length= len(contact_number_list)
final_url_list = []
basic_url = "https://web.whatsapp.com/send?phone=91"
for i in range(0,length):
    final_url_list.append(basic_url)


for i in range(0,length):
    final_url = str(final_url_list[i]) + str(contact_number_list[i]) +"&text="+msg+str(ten_digit_codes_list[i])
    final_url_list[i]= final_url
	
print(final_url_list)
for url in final_url_list:
    driver.get(url)
    sleep(3) 

    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
    # print('Last Number '+ str(number))
    print("Working on ")
print ("Done")


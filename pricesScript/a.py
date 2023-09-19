from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import date
from datetime import timedelta
import time
import json 


#base product URL
URL = "https://e-katanalotis.gov.gr"

#final JSON
results = {}
results['fetch_date']=int(time.time())
results['data']=[]

service = Service(executable_path="/Users/User/Desktop/test/chromedriver.exe")
#get product information
options = webdriver.ChromeOptions()
options.add_argument('--headless')

options.add_experimental_option('excludeSwitches', ['enable-logging'])
# executable_path param is where the Chrome driver is installed
browser = webdriver.Chrome(service=service,options=options)
browser.get(URL)

#get product information
productid = browser.execute_script("return Array.from(Ember.Namespace.NAMESPACES_BY_ID['katanalotis-microsite'].__container__.cache['service:store'].recordArrayManager._liveRecordArrays.product.content).map(({id}) => id)")
browser.quit()
#get product information 
for i in range(len(productid)):
    print(productid[i])
    options = webdriver.ChromeOptions()
   
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # executable_path param is where the Chrome driver is installed
    browser = webdriver.Chrome(options=options)
    browser.get("https://e-katanalotis.gov.gr/product/"+str(productid[i]))
    
    #find product name
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    price_data=[]
    date_data=[]

    price=soup.find('div',attrs={'class':'product-market-container col-12col-md-6 col-lg-6 offset-lg-3'})
    priced=price.find('span',attrs={'class':'product-price-number'}).text
    for j in range(6):
        price_d=priced
        price_d=price_d[0:4]
        price_d=float(price_d)
        price_data.append(price_d)
        dt=date.today()-timedelta(days = 6-j)
        date_data.append(dt)


    browser.quit()

    for j in range(6):
        date_data[j]=str(date_data[j])
        
    #create a result object
    result = {}
    result['id']=productid[i]
    result['prices']=[]
    for j in range(6):
        result['prices'].append({'date':date_data[j], 'price':price_data[j]})
    
    #append it to the list
    results['data'].append(result)
    

print('Done')
with open("prices"+".json", "w", encoding='utf-8') as outfile:
    json.dump(results, outfile, ensure_ascii=False, indent=2)

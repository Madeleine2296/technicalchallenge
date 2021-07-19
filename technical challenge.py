#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import logging
import unittest
from selenium.common.exceptions import NoSuchElementException


# In[2]:



##unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\\Chrome Driver\\chromedriver.exe")
        print("Browser Opened")
    def test_open_amazon(self):
        self.driver.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books_home_all?pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583&pf_rd_s=center-5&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583')
        print("Opening Amazon.com")

    def tearDown(self):
        self.driver.quit()
        print("Browser closed")
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[3]:


##
driver = webdriver.Chrome("C:\\Chrome Driver\\chromedriver.exe")


# In[4]:


driver.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books_home_all?pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583&pf_rd_s=center-5&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583')


# In[5]:


books = driver.find_elements_by_class_name('zg-item-immersion')


# In[6]:


len(books)


# In[7]:


print(books[0].text)


# In[8]:


name = books[0].find_elements_by_class_name('p13n-sc-truncated')[0].text
print(name)


# In[9]:


price = books[0].find_elements_by_class_name('p13n-sc-price')[0].text
print(price)


# In[10]:


data = []
for book in  books[:50]:
    name = book.find_elements_by_class_name('p13n-sc-truncated')[0].text
    price = book.find_elements_by_class_name('p13n-sc-price')[0].text
    print('Name:', name)
    print('Price:', price)
    new = ((name, price))
    data.append(new)


# In[11]:


## converting it into a pandas dataframe
df = pd.DataFrame(data,columns=['name','price'])


# In[12]:


## printing the top 50 results 
df.head(50)


# In[15]:



##logging
def main():
    logging.basicConfig(filename="C:\\Users\\16126\\Documents\\Data Engineer Technical Challenge\\app.log", filemode='w', level=logging.INFO)
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    
if __name__ == '__main__':
    main()


# In[16]:



##exception handling at index 0
driver = webdriver.Chrome(executable_path="C:\\Chrome Driver\\chromedriver.exe")
driver.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books_home_all?pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583&pf_rd_s=center-5&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_r=GGY2FZ9VD6P8RZZZXH1T&pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583')

try:
    webElement = driver.find_elements_by_class_name('zg-item-immersion')[0].click()
 
except NoSuchElementException as exception:
    print ("Element not found and test failed")


# In[ ]:





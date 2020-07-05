#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from getpass import getpass


# In[6]:


browser = webdriver.Chrome(chrome Path if needed)


# In[14]:


# Initilizing url for which you have to automate
browser.get("https://codechef.com")


# In[15]:


# finding username field using inspect function within a site
username_element = browser.find_element_by_id('edit-name')


# In[16]:


# Providing username
username_element.send_keys('Username')


# In[17]:


password_element = browser.find_element_by_id('edit-pass')


# In[18]:


password_element.send_keys(getpass("Enter password"))


# In[19]:


# accessing submit button
browser.find_element_by_id("edit-submit").click()


# In[20]:


# redirecting to new page of same website
browser.get("https://www.codechef.com/submit/TEST")


# In[26]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[27]:


with open("basic.py",'r') as f:
    code = f.read()


# In[28]:


code_element = browser.find_element_by_id('edit-program')


# In[29]:


code_element.send_keys(code)


# In[31]:


browser.find_element_by_id("edit-submit-1").click()


# In[ ]:





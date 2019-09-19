#!/usr/bin/env python
# coding: utf-8

# In[13]:


from newspaper import Article
import nltk
from textblob import TextBlob


# In[19]:


url='https://www.aljazeera.com/news/2019/09/600000-rohingya-myanmar-face-risk-genocide-190916143753819.html'
article = Article(url)


# In[21]:


article.download()
article.parse()
nltk.download('punkt')
article.nlp()


# In[49]:


text=article.summary
print(text)
hello=TextBlob(text)
hello.translate(to='hi')


# In[41]:


obj=TextBlob(text)
sentiment=obj.sentiment.polarity
print(sentiment)


# In[ ]:





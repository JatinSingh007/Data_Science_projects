#!/usr/bin/env python
# coding: utf-8

# In[4]:


import gensim
import pandas as pd


# In[ ]:


df = pd.read_json('meta_Cell_Phones_and_Accessories.json',lines = True)
df.head(5)


# In[ ]:


df.shape


# In[ ]:


reviewText = df.reviewText.apply(gensim.utils.simple_preprocess)
reviewText


# In[ ]:


df.reviewText.loc[0]


# In[ ]:


model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4,
)


# In[ ]:


model.build_vocab(review_text, progress_per=1000)
model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)
model.save("./word2vec-amazon-cell-accessories-reviews-short.model")


# In[ ]:


model.wv.most_similar("bad")
model.wv.similarity(w1="cheap", w2="inexpensive")
model.wv.similarity(w1="great", w2="good")


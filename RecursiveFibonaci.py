#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rec_fb(n,result):
    if n<2:
        return n
    elif(result[n]!=0):
        return result[n]
    else:
        result[n]=rec_fb(n-1,result)+rec_fb(n-2,result)
        return result[n]
    for i in range(13,25):
        print(rec_fb(i,[0]*(i+1)),end=" ")


# In[9]:


def recMC(coinValueList,change,knowResults):
    minCoins=change
    if(change in coinValueList):
        knowResults[change]=1
        return 1
    else:
        for i in[c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-1,knowResults)
            if(numCoins<minCoins):
                minCoins=numCoins
                knowResults[change]=minCoins
        return minCoins
    for i in range(8,20):
        print(i,recMC([1,5,10,25,50],i,[0]*(i+1)))


# In[10]:





# In[ ]:





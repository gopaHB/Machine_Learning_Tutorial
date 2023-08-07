#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
x_data=np.array([160,171,182,180,154],ndmin=2)
x_data=x_data.reshape(5,1)
y_data=np.array([72,76,77,83,76])
# y_data=y_data.reshape(5,1)

# print(x_data,y_data)
# print(x_data.shape,y_data)
x_mean=np.mean(x_data)
y_mean=np.mean(y_data)
n=len(x_data)
class LinearRegration:
    b0=0
    b1=0
    def LinearRegration_fit(self,x,y):
        upward_function=0
        x_downwrad=0
        for i in range(n):
            upward_function+=(x_data[i]-x_mean)*(y_data[i]-y_mean)
            x_downwrad+=(x_data[i]-x_mean)**2
        self.b1=upward_function/x_downwrad
        self.b0=y_mean-(self.b1*x_mean)
        return self.b0,self.b1
    def LinearRegration_predict(self,xi):
        y_pred=self.b0+(self.b1*xi)
        return y_pred
    
model=LinearRegration()

print(model.LinearRegration_fit(x_data,y_data))
print(model.LinearRegration_predict(176))

            
        


# In[ ]:





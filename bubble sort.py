#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
data=[4,3,6,2,9,1,7,8,5]
bubblesort(data)
print('Sorted array:', data)   


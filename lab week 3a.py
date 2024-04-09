# SERHAT SEFLEK
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    value = b + c
    return value

def second_func(d=40):
    e = 50
    return a + first_func() + d + e

result = second_func()

print(result)

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}

def key_func(k):
    return k.capitalize()

def val_func(v):
    return datetime.datetime.strptime(v, "%m/%d/%Y")
    

answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

print(answer)

#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values
from numpy import mean, std

def zscore(a):
    return [(i-mean(a))/std(a) for i in a]

first_list = [1,2,3,4,5,6]
second_list = [4,9,2,6]
third_list = [232, 54646, 666, 876, 765]    


print(zscore(first_list))
print(zscore(second_list))
print(zscore(third_list))


#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior
from numpy import median, absolute

def zscoremod(a, mad = False):
    if mad == False:
        return [(i-mean(a))/std(a) for i in a]
    else:
        return [(i-mean(a))/median([absolute(i-median(a))for i in a])for i in a]

# Are default calculation equal? 
print(zscoremod(first_list))
print(zscore(first_list) == zscoremod(first_list)==zscoremod(first_list,False))
# When optinal argument changes to true, which means we want function to 
#calculate mad
print(zscoremod(first_list, True))
print(zscore(first_list) == zscoremod(first_list, True))

print(zscoremod(second_list))
print(zscoremod(second_list, False))
print(zscoremod(second_list, True))
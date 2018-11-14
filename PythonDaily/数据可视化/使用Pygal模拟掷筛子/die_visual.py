# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:57:07 2018

@author: Administrator
"""
import pygal

from die import Die
die = Die()
results =[]
for roll_num in range(100):
    result = die.roll()
    results.append(result)
frequencies =[]
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#对比结果进行可视化
hist = pygal.Bar()
hist.title =("Result of rolling one D6 1000 times")
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title =("Result")
hist.y_title =("Frequency of Result")

hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")

    
print(frequencies)

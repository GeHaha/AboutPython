# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:41:47 2018

@author: Administrator
"""

import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'JAanis Joplin')
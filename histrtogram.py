#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:47:44 2020

@author: akshayaksh
"""

fig = data.loan_amnt.hist(bins=50)
fig.set_xlim(1,30)#upto 30 on x axis
fig.set_title('Loan Amount Requested')
fig.set_xlabel('Loan Amount')
fig.set_ylabel('Number of Loans')
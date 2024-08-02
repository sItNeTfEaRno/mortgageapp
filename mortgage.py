# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:35:28 2024

@author: Stefano
"""
# RUN WITH streamlit run "C:/Users/Stefano/iCloudDrive/Stefano/Progetti & Business/Progetti/Streamlit web tool/Simula mutuo/untitled1.py"

import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello")
st.markdown('# This is a mortgage simulator')

x=st.number_input("How much do you want to finance?", value=300000, placeholder="Type a number...", step=10000)

st.write(f"Your motgage is gonna be: {x}")

payment_frequency = 12
#loan_length = st.selectbox('Select the length of the loan', [10,15,20,25,30,35,40], index=1, placeholder="Select a period...")
loan_length_years = st.slider('Loan length',10,40,30,5)
loan_length = loan_length_years*payment_frequency

st.write(f"The loan lenght will be {loan_length_years} and the total number of monthly payments are {loan_length}.")

interest_rate_100=st.number_input("Which is the interest rate? (percentage)", min_value=0.0, max_value=10.0,value=2.0, placeholder="Type an interest rate...", step=0.1)
interest_rate = interest_rate_100/100/payment_frequency

numeratore = (interest_rate*((1+interest_rate)**loan_length))
denominatore = (((1+interest_rate)**loan_length)-1)

periodical_payments = x * numeratore/denominatore
st.markdown(f"### Your total monthly payment will be: {np.round(periodical_payments)}")

capitale_interessi = periodical_payments*loan_length

d0 = {'Capitale': [x], 'Capitale e interessi': [capitale_interessi]}
d = {'Capitale': [x, capitale_interessi]}
df = pd.DataFrame(data=d,  index=['Capitale', 'Capitale e interessi'])
st.bar_chart(df)

balance_left = np.array(x)
first_interest_payment = interest_rate*balance_left
interest_payed = np.array([first_interest_payment])
principal_payment =  np.array([periodical_payments-first_interest_payment])
balance_left = np.append(balance_left, [x-(periodical_payments-first_interest_payment)])
for n in range(1,loan_length):
    interest_payed=np.append(interest_payed,[interest_rate*balance_left[n]])
    principal_payment = np.append(principal_payment, [periodical_payments-interest_rate*balance_left[n]])
    balance_left = np.append(balance_left, [balance_left[n]-principal_payment[n]])
    

#d1 = {'Capitale da rimborsare':balance_left[1:], 'Quota interessi':interest_payed, 'Quota capitale':principal_payment}
d1 = {'Quota interessi':interest_payed, 'Quota capitale':principal_payment}
df1 = pd.DataFrame(data=d1, index=pd.RangeIndex(start=1, stop=loan_length+1, name='index'))#,  index=range(1,loan_length))
st.bar_chart(df1)
# with st.chat_message("user"):
#     st.write("Hello")
#     #st.line_chart(np.random.randn(30, 3))

# # Display a chat input widget.
#     st.chat_input("Say something")



# data=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])


# st.bar_chart(data)
# st.line_chart(data)
# st.write(data)
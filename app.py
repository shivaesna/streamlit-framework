API_KEYS = '1SXC5NCVKRJPOEG6'

import streamlit as st
import requests
import json 
import pandas as pd

def retrieve_data(function: str, symbol: str, api_key: str) -> dict:
    """
    Retrieves data from AlphaVantage's open API.
    Documentation located at: https://www.alphavantage.co/documentation
    """
    # query from API
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)
    
    return parsed


def extract_name(overview) -> str:
    return overview['Name']


def extract_dividend_per_share(overview) -> float:
    try:
        dps = float(overview['DividendPerShare'])
    except:
        # handle "none"
        dps = 0.0
    return dps






def main():
    st.title('Expected stock price based on the Discounted Dividend Model (DDM)')

    ticker = st.text_input('Please input ticker of stock you wish to analyze')
    g = st.number_input('Expected annual growth')
    r = st.number_input('Discount rate')

    calculate_button = st.button('Calculate DDM')

    if calculate_button:
        if ticker == '':
            st.error('Please provide a ticker.')
        else:
            overview = retrieve_data('OVERVIEW', ticker, API_KEYS)

            name = extract_name(overview)
            dividend = extract_dividend_per_share(overview)

            st.header(f'Analysis for {name}')
            
            st.subheader('Expected Stock Price (based on DDM)')
            st.write(str(round(ddm(dividend, r, g), 2)))


def ddm(dividend: float, r: float, g: float) -> float:
    return (dividend * (1 + g))/(r - g)


if __name__ == '__main__':
    main()
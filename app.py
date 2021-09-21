API_KEYS = '1SXC5NCVKRJPOEG6'

import streamlit as st
import requests
import json 
import pandas as pd
import matplotlib.pyplot as plt

def retrieve_data(function: str, symbol: str, output_size:str, api_key: str) -> dict:
    """
    Retrieves data from AlphaVantage's open API.
    Documentation located at: https://www.alphavantage.co/documentation
    """
    # query from API
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={output_size}&apikey={api_key}'
    response = requests.get(url)
    # read output
    data = response.text
    # parse output
    parsed = json.loads(data)
    return parsed


def main():
    st.title('Welcome to Stock Price Plotter')

    ticker = st.text_input('Please input ticker of stock you wish to analyze')
    month_input = st.slider('Month', min_value=1, max_value=12, value=9, step=1)
#     month_input = st.number_input('Month', min_value=1, max_value=12, value=12, step=1)
    
    year_input = st.slider('Year', min_value=2000, max_value=2021, value=2021, step=1)
#     year_input = st.number_input('Year', min_value=2017, max_value=2021, value=12, step=1)

    calculate_button = st.button('Plot Graph')

    if calculate_button:
        if ticker == '':
            st.error('Please provide a ticker.')
        else:
            parsed_data = retrieve_data('TIME_SERIES_DAILY', ticker, 'full', API_KEYS)
            df1= pd.DataFrame(parsed_data['Time Series (Daily)'])
            df2= df1.T
            df2= df2.reset_index()
            df2['index'] = pd.to_datetime(df2['index'])
#             month_input=9
#             year_input=2021
            df3=df2.loc[(pd.DatetimeIndex(df2['index']).year == year_input) & (pd.DatetimeIndex(df2['index']).month == month_input)]
            
            df3['4. close']=df3['4. close'].astype(float,errors='raise')
            
            st.header(f'Analysis for {ticker}')
            st.subheader('Closing price')
            
            fig = plt.figure()
            plt.plot(df3['index'],df3['4. close'])
#             df3.plot(x='index', y='4. close')

            st.pyplot(fig)


#             name = extract_name(overview)
#             dividend = extract_dividend_per_share(overview)


#             st.write(str(round(ddm(dividend, r, g), 2)))


# def ddm(dividend: float, r: float, g: float) -> float:
#     return (dividend * (1 + g))/(r - g)


if __name__ == '__main__':
    main()
import requests
import pandas as pd

def get_data():
          
    dataset_id = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"
    url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id

    all_records = []

    limit = 10000           # Only allow 10K rows to be retrieved at once
    offset = 0
    max_records = 100000

    while offset < max_records:
        params = {"limit": limit, "offset":offset}
    
        response = requests.get(url, params = params)
        data = response.json()
        records = data['result']['records']
        all_records.extend(records)

        if len(records) < limit:
            break

        offset += limit

    df = pd.DataFrame(all_records)
    df = clean_data(df)
    return df

def clean_data(df):

    """Convert data in the following columns to the correct types we need"""

    df['resale_price'] = pd.to_numeric(df['resale_price'])      
    df['floor_area_sqm'] = pd.to_numeric(df['floor_area_sqm'])
    df['lease_commence_date'] = pd.to_numeric(df['lease_commence_date'])
    df['month'] = pd.to_datetime(df['month'])

    return df

""" 
To have a better understanding of the data
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum()) 
print(df.duplicated().sum())
"""

"""
To have a better understanding of the range of resale price
print(df['resale_price'].max())
print(df['resale_price'].mean())
print(df.groupby('flat_type')['resale_price'].mean())
"""

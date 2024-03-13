import pandas as pd
import requests
from datetime import datetime

api_key = 'ZsCol9d9D4nPcF7aSxdENNV2DvBJnsps'

def get_item_sold_price(itemName=None, itemId = None):
    
    base_url = f'https://api.neople.co.kr/df/auction-sold?itemName={itemName}&wordType=full&wordShort=false&limit=100&apikey={api_key}'
    
    if itemId:
        base_url = f'https://api.neople.co.kr/df/auction-sold?itemId={itemId}&limit=100&apikey={api_key}'
    
    
    
    res = requests.get(base_url)
    
    if res.status_code == 200:
        return res
    
    return 
    
itemIds = {
    '페리아' : '87a131e3e8ab68b0e3ff5ea80d9e8975',
    '슈므' : 'b3af05ec93a2832c0b47fde15e3da5f3',
    '에를리히' : '1ca719543274a0ae0b12b478d88c0448',
    '다정한 세리아 알': '72d9413775a62ccd21cd9670fa9b8dfe'
}

# 현재 날짜와 시간을 얻기
current_datetime = datetime.now()

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print(f"GET API Time: {year}-{month}-{day}- {hour}:{minute}:{second}", end='')

for key, value in itemIds.items():
    res = get_item_sold_price(itemId = value)
    tmp_df = pd.DataFrame(res.json()['rows'])
    
    try:
        before_df = pd.read_csv(f'/Users/seokholee/이모저모/dnf/data/creature/trade/{key}_trade.csv')
    except:
        before_df = tmp_df
    
    pd.concat([before_df, tmp_df]).drop_duplicates().to_csv(f'/Users/seokholee/이모저모/dnf/data/creature/trade/{key}_trade.csv', index=False)
    
print("-> SUCCESS")
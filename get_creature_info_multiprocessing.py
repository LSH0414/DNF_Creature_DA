import os
import pandas as pd
import multiprocessing
from tqdm import tqdm
import requests
import time

api_key = 'Enter_Your_API_KEY'

def get_creature_data(info):
    serverId = info['server']
    characterId = info['character_ids']
    base_url = f'https://api.neople.co.kr/df/servers/{serverId}/characters/{characterId}/equip/creature?apikey={api_key}'
    
    try:
        res = requests.get(base_url)
    except:
        time.sleep(3)
        res = requests.get(base_url)
    
    if res.status_code == 200:
        return res
    
    return 

def process_file(file_name):
    path = '/Users/seokholee/이모저모/dnf/data/user_infos/2024PASS_S1/user_info_div/'
    
    user_info = pd.read_csv(path + file_name)
    df_data = []
    print('Start GET API : ', file_name)
    
    for idx, row in tqdm(user_info.iterrows()):
        output = get_creature_data(row)
        if not output:
            continue
        
        creature_info = output.json()['creature']
        if not creature_info:
            continue
        
        user_data = [row['server'], row['character_ids']]
        for col in ['itemId', 'itemName', 'itemRarity', 'clone']:
            clone_itemId, clone_itemName = '', ''
            
            if col == 'clone' and len(creature_info[col]):
                user_data.extend([creature_info[col]['itemId'], creature_info[col]['itemName']])
            else:
                user_data.append(creature_info[col])
                
        df_data.append(user_data)
        
    df = pd.DataFrame(df_data, columns=['serverId', 'characterId', 'itemId', 'itemName', 'itemRarity', 'clone_itemId', 'clone_itemName'])
    save_path = './data/creature/s3/'
    df.to_csv(save_path + file_name, index=False)
    print(f'Processed {file_name}')

def main():
    path = '/Users/seokholee/이모저모/dnf/data/user_infos/2024PASS_S1/user_info_div/'
    file_names = [name for name in os.listdir(path) if '.csv' in name]
    
    pool = multiprocessing.Pool(processes=7)  # 8개의 프로세스를 사용
    pool.map(process_file, file_names)
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()

import pandas as pd
import os

# Загружаем данные из csv файла ( '1.csv' меняем на свое название csv файла )
df = pd.read_csv('1.csv')

# Открываем txt файл и считываем адреса
with open('wallets.txt', 'r') as f:
    wallets = f.read().splitlines()

# Преобразуем все адреса кошельков к нижнему регистру
wallets = [wallet.lower() for wallet in wallets]

# Проверяем, содержится ли каждый из адресов кошельков в столбце 'user_address' 
df['address_match'] = df['user_address'].isin(wallets)

# Выбираем строки, где адреса совпадают
matched_df = df[df['address_match'] == True]

# Сохраняем результат в xlsx файл
matched_df.to_excel('matched_wallets.xlsx', index=False)

print("Risk/Reward - https://t.me/RRband")
import pandas as pd
import os

# Предлагаем пользователю выбрать сценарий
print("Выберите сценарий: ")
print("1 - загрузить данные только по нативным токенам")
print("2 - загрузить данные только по стейблкоинам")
print("3 - загрузить данные по всем токенам")
choice = input("Введите номер выбранного сценария: ")

# Открываем txt файл и считываем адреса
with open('wallets.txt', 'r') as f:
    wallets = f.read().splitlines()

# Преобразуем все адреса кошельков к нижнему регистру
wallets = [wallet.lower() for wallet in wallets]

# Создаем словарь порядковых номеров для адресов
wallets_dict = {wallet: i+1 for i, wallet in enumerate(wallets)}

if choice == '1':
    # Загружаем данные из csv файла
    df = pd.read_csv('1.csv')

    # Выбираем строки, где адреса кошельков совпадают с адресами из файла wallets.txt
    matched_df = df[df['user_address'].isin(wallets)]

elif choice == '2':
    # Загружаем данные из csv файла
    df = pd.read_csv('2.csv')

    # Выбираем строки, где адреса кошельков совпадают с адресами из файла wallets.txt
    matched_df = df[df['sender'].isin(wallets)]
    matched_df.rename(columns = {'sender': 'user_address'}, inplace = True)

elif choice == '3':
    # Загружаем данные из первого csv файла
    df_native = pd.read_csv('1.csv')

    # Загружаем данные из второго csv файла
    df_stable = pd.read_csv('2.csv')

    # Выбираем строки, где адреса кошельков совпадают с адресами из файла wallets.txt
    matched_df_native = df_native[df_native['user_address'].isin(wallets)]
    matched_df_stable = df_stable[df_stable['sender'].isin(wallets)]
    matched_df_stable = matched_df_stable.rename(columns = {'sender': 'user_address'})

    # Объединяем совпадающие строки с дополнительными данными
    matched_df = pd.merge(matched_df_native, matched_df_stable, on='user_address', how='outer')

# Применяем словарь порядковых номеров к столбцу 'user_address' для создания нового столбца 'wallet_number'
if 'user_address' in matched_df.columns:
    matched_df['wallet_number'] = matched_df['user_address'].map(wallets_dict)

# Перемещаем столбец 'wallet_number' в начало DataFrame
cols = matched_df.columns.tolist()
cols.insert(0, cols.pop(cols.index('wallet_number')))
matched_df = matched_df.reindex(columns=cols)

# Сохраняем результат в xlsx файл
matched_df.to_excel('matched_wallets.xlsx', index=False)

print("Risk/Reward - https://t.me/RRband")

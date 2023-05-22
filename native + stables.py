import pandas as pd
import os

# Предлагаем пользователю выбрать сценарий
print("Выберите сценарий: ")
print("1 - загрузить данные только по нативным токенам") #меняем имя csv в 20 строке
print("2 - загрузить данные только по стейблкоинам") #меняем имя csv в 27 строке
print("3 - загрузить данные по всем токенам") #меняем имя csv в 34 и 37 строке
choice = input("Введите номер выбранного сценария: ")

# Открываем txt файл и считываем адреса
with open('wallets.txt', 'r') as f:
    wallets = f.read().splitlines()

# Преобразуем все адреса кошельков к нижнему регистру
wallets = [wallet.lower() for wallet in wallets]

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

elif choice == '3':
    # Загружаем данные из первого csv файла
    df_native = pd.read_csv('1.csv')

    # Загружаем данные из второго csv файла
    df_stable = pd.read_csv('2.csv')

    # Выбираем строки, где адреса кошельков совпадают с адресами из файла wallets.txt
    matched_df_native = df_native[df_native['user_address'].isin(wallets)]
    matched_df_stable = df_stable[df_stable['sender'].isin(wallets)]

    # Переименовываем столбец 'sender' в 'user_address'
    matched_df_stable = matched_df_stable.rename(columns = {'sender': 'user_address'})

    # Объединяем совпадающие строки с дополнительными данными
    matched_df = pd.merge(matched_df_native, matched_df_stable, on='user_address', how='outer')

# Сохраняем результат в xlsx файл
matched_df.to_excel('matched_wallets.xlsx', index=False)

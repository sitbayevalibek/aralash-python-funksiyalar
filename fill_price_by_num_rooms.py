# DataFrame'dagi NaN qiymatlari bor qatorni topib uning o'rniga xonalar soniga mos narxdagi uylarni o'rtacha qiymatini qo'yadi.
# Masalan: 3 xonali uyning o'rtacha narxi 70,000 $ bo'lsa, NaN  qiymatli 3 xonali qatorlarga 70,00 $ narxini qo'yadi
def fill_price_by_num_rooms(df):
    nan_rows = df[pd.isna(df['price'])].index
    orta_prices = df.groupby('rooms')['price'].mean()
    for row in nan_rows:
        num_rooms = df.at[row, 'rooms']
        df.at[row, 'price'] = orta_prices.get(num_rooms)
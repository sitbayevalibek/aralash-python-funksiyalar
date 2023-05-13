import random as r

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))
toq_sonlar = list(filter(lambda son: son % 2 != 0, sonlar))

print(f"Tasodifiy 10 ta sonlar: {', '.join(map(str, sonlar))}")
print(f"Shu ro'yxatdagi juft sonlar: {', '.join(map(str, juft_sonlar))}")
print(f"Shu ro'yxatdagi toq sonlar: {', '.join(map(str, toq_sonlar))}")

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
toq_sonlar = list(filter(lambda son: son%2!=0,sonlar))

print(f"Tasodifiy 10ta sonlar {sonlar}")
print(f"Shu ro'yxatdagi juft sonlar {juft_sonlar}")
print(f"Shu ro'yxatdagi toq sonlar {toq_sonlar}")
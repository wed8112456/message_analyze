# 更換存擋位置
# 需要印出讀取進度
# 計算留言平均

import os

# 更換檔案位置
path = r'/Users/uranus/Documents/Python/message_analyze'
os.chdir(path)

# 創建空列表
data = []

# 計算總共多少筆資訊
count = 0

# 讀取txt
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # 計算共1000筆為一個單位
        if count % 1000 == 0:
            print(len(data))

print(f'檔案讀取完畢，共{len(data)}筆')

sun_len = 0

for i in data:
    sun_len += len(i)

print(f'留言平均長度，{sun_len/len(data)}')

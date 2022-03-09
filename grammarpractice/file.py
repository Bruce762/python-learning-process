#檔案讀取寫入
#open ("檔案位置", mode="開啟模式")
# mode="r" 讀取
# mode="w" 複寫
#mode="a" 在原先資料後寫東西
file = open("123.txt",mode="r")
#print(file.read())#列印一行
#print(file.readline())#列印全部
print(file.readlines())
for line in file:
    print(line)
file.close
#每行不重覆讀
#file = open("456.txt" , mode="w", encoding="utf-8")
#utf-8是中文解碼格式
#file.write("\nhollow你好")

with open("456.txt" , mode="a" ,encoding="utf-8") as file:
    file.write("\n哈哈")
#with這種寫法可以省去close
file.close()
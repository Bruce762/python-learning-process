from cgi import print_directory


scores = [90,76,67,53,75]
things = [90,"小勒",True]
print(things)
print(things[-1])#倒數第一位
print(scores[1:3])
print(scores[1:])
print(scores[:4])
scores.extend(things)
print(scores)
scores = [90,90,76,67,53,75]
things = [90,"小勒",True]
scores.append(345)
print(scores)
scores.insert(2,100)
print(scores)
scores.remove(100)
print(scores)
things.clear()
print(things)
scores.pop()#最後一位取出
print(scores)
scores.sort()
print(scores)
scores.reverse()
print(scores)
print(scores.index(90)) 
print(scores.count(90))
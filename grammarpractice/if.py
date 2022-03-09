from cgi import print_directory


a=True
if a:
    print("good")
b=False
a=0
if a!=90 and b:
    print("90")
elif a>=90 or b:
    print("good")
else:
    print("bad")
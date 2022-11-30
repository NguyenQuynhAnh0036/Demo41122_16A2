a = int(input("Nhập số lượng số nguyên N"))
j = []
for i in range(1,a+1):
    print("Nhập số hạng thứ: ",i)
    b = int(input())
    j.append(b)
c = 0
for v in j:
    c = c + v
print("Tổng",a,"Số hạng là:")
print(c)
a = int(input("Nhập số nguyên N:"))
b = 0
for i in range(1,a+1):
    print("Nhập số hạng thứ:", i)
    b1=int(input())
    b=b+b1
print("Tổng",a,"Số hạng là:",b)
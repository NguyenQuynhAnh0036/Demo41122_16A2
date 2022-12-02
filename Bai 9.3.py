a=float(input("Nhập cân nặng:"))
b=float(input("Nhập chiều cao:"))
c=a/(b*b)
print("Chỉ số BMI cua ban la:",c,end="Kết quả đánh giá theo chỉ số của bạn là:")
if c<18.5:
    print("Gầy")
elif c>=18.5 and c<=24.99:
    print("Bình thường")
elif c>=25:
    print("Thừa cân")
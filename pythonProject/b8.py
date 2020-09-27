                    #Dùng lambda,filter kiểm tra số chẵn lẻ
l1=[1,2,3,4,5]
# Kiểm tra từng phần tử của l1 nếu chia hết cho 2 thì sẽ gán vào l2
# l2 lá 1 kiểu giữ liệu filter: trả từng phần tử về giá trị bool (true/false)
l2=filter(lambda a:a%2,l1)
print(type(l2))
# Ép l2 thành kiểu list
print(list(l2))

                    #Dùng lambda, map trả trả về 1 giá trị
# l3 lá 1 kiểu giữ liệu map: trả từng phần tử về giá trị số
l3=map(lambda a:a*2,l1)
print(type(l3))
print(list(l3))

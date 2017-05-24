code1, num_product1, price1 = raw_input().split(" ")
code2, num_product2, price2 = raw_input().split(" ")

code1 = int(code1)
num_product1 = int(num_product1)
price1 = float(price1)

code2 = int(code2)
num_product2 = int(num_product2)
price2 = float(price2)

total = num_product1 * price1 + num_product2 * price2

print "VALOR A PAGAR: R$ %.2f" %(total)
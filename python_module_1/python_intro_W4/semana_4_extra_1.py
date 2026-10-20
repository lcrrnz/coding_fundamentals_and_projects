#1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que: 1. Si el precio es menor a 100, el descuento es del 2%.2. Si el precio es mayor o igual a 100, el descuento es del 10%.

product_prince = float(input("Ingrese el precio del producto: "))
discount = float()

if product_prince < 100 :
    discount = product_prince * 0.02

else:
    product_prince >= 100
    discount = product_prince * 0.1

final_price = float(product_prince - discount)

print(f'El precio con descuento del producto es {final_price}')
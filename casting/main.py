# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price=2


print ('Leek is '+str(leek_price)+' euro per kilo.')
# (better?) print (f'Leek is {leek_price} euro per piece.')


order1='leek 4'
numberleek =  int(order1[order1.find(' '):])
sum_total = numberleek * leek_price
print(sum_total)

broccoli_price=2.34
order2='broccoli 1.6'
numberbroc = float(order2[order2.find(' '):])
sum_total=numberbroc*broccoli_price
# print(round(sum_total,2))


print(str(numberbroc)+'kg broccoli costs '+str(round(sum_total,2))+'e')
#(better?) print(f'{numberbroc}kg broccoli costs {round(sum_total,2)}e')
# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
# broccoli, leek, potato and brussel_sprout
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
sum_one_each =broccoli+leek+ potato + brussel_sprout
avg_price=sum_one_each/4
#Create a variable num_potatoes that indicates we want 7 potatoes. Do the same for:
num_potatoes=7
#num_broccolis -- we want 5 of those.
num_broccolis=5
#num_leeks -- 2 please.
num_leeks=2
#num_brussel_sprouts -- we'll take 10.
num_brussel_sprouts=10
#Calculate the sum total and store it in a variable aptly named sum_total.
sum_total= num_brussel_sprouts*brussel_sprout+num_potatoes*potato+num_leeks*leek+num_broccolis*broccoli
#Fortunately for us, there's a discount of 30%. Store this in a variable discount_percentage (hint: note the variable name already says 'percent')
discount_percentage=30
#Calculate the amount owed after the discount is applied, rounded to the nearest cent. Store the result in discounted_sum_total.
discounted_sum_total=sum_total-(discount_percentage/100)*sum_total
#Print this amount.
print(discounted_sum_total)

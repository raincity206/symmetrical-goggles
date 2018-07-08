# Program to show the use of lambda functions

double = lambda x: x * 2

##This statement is syntacilly similar to
##def double(x):
##	return x * 2
##

#Output

print(double(5))

# Program to filter out only the even/odd items from a list

my_list = [1,2,3,4,5,6,66,9,17,61]

sign = input("Even or odd?: ")

if lower(sign) == 'even':
	symm = 2
elif lower(sign) == 'odd':
	symm = 3
else:
	symm = 2

print(sign)
# Returns only even values
new_list = list(filter(lambda x: (x%symm == 0), my_list))

print("Only the " + sign + " numbers:")
print(new_list) 
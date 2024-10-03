#write a programe that takes two numbers as in inputs and displays their sum, product and their quocient

#write aprograme that comperes two integers print whether the first number is greater , less than or equal to second number

#write a programme that checks if agiven number is between ten and twety whereby 'tweety is inclusive' using logical operaters 

# write aprogram that prints integers fron one to ten using a four loop
  


#answers  1
#for sum


number_one = int(input("enter the first number : "))
number_two = int(input("enter the second number: "))
sum= number_one  + number_two
print(f"sum of {number_one} and {number_one} is: {sum}")
#or
print('the sum is ' + str(sum))

#difference
difference= number_two - number_one
print(f"difference of {number_two} and {number_one} is: {difference}")

#or
print("the difference is " + str(difference))

#product
product= number_two * number_one
print('the product is ' + str(product))


#NUMBER 2
#if loops (commenting the comparison whether its true or false)

if number_one > number_two:
    print(f" {number_one} is greater {number_two}")
elif number_one < number_two:
    print(f" {number_one} is less than {number_two}")
else:
    print(f" they are equal")
    


















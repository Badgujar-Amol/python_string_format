# string formats
i = 10
j = 20
str = "The sum of i and j is {}."
print(str.format(i+j))

# user inputs
a = int(input("enter a"))
b = int(input("enter b"))
str1 = "The sum of a and b is  {}."
print(str1.format(a+b))

# result with three decimal,one decimal,upto...
a1 = 20
a2 = 30
str2 = "The sum of a1 and a2 is {:.3f}."
res = "The sub of a2 and a1 is {:.1f}."
print(str2.format(a1+a2))
print(res.format(a2-a1))

#
name = 'om'
email = 'om@gmail.com'
contact = 5689745236
str3 = 'Name is {}, Email is {}, Contact is {}.'
print(str3.format(name, email, contact))


# index number in string format
name1 = 'priya'
email1 = 'pri@gmail.com'
contact1 = 4578965236
str4 = "Name is {0}, Email {1}, Contact {2}."
print(str4.format(name1, email1, contact1))


# name index
str5 = "Name is {name}, Email {email}"
print(str5.format(name='jay',email='jay@gmail.com'))
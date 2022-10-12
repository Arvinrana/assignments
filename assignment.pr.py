# In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
#* 
#'hello'
#-87.8
#- 
#/ 
#+

#6 

# answer -->  values are 
# -87.8 which is describe as float pointing number 
#  6  is an integer number 
#  - , / ,+  and *   are arithmetic operators or an expression 
# 'hello' is a string value which comes under in comma ' '


# 2. What is the difference between string and variable?
# answer --> the diffrence between string and variable is that string comes under in " " comma, 
# it can be either alphabets or numbers . 
# A Variable is a store of information, and a String is a type of information you would store in a Variable



#3. Describe three different data types.
# numeric ->> numeric types
# int - 89,85,12
# float - 1.2,5.4  ( a number which have decimal in it)
# complex number - 2j , 455l  ( the complex numbers are including alphabet also)


# booleans --> true [1] or false [0]
# this type of data type tells that the statement is true or false 
# on the basis of condition 

# mapping data type --> dictionary or json  which works on keys and its values 

# 4.  What is an expression made up of? What do all expressions do?
# answer 
#An expression is a construct made up of variables, operators, and method invocations, 
#which are constructed according to the syntax of the language, 
#that evaluates to a single value.

#Expressions are representations of value.
#They are different from statement in the fact that statements do something while expressions
# are representation of value.
#For example any string is also an expressions since it represents the value of the string as well.

 # question 5 .This assignment statements, like spam = 10. What is the difference between an expression and a statement?

#     Answer 
#in programming language terminology, an “expression” 
#is a combination of values and functions that are combined and interpreted by the compiler to create a new value,
 #as opposed to a “statement” which is just a standalone unit of execution and doesn't return anything.


# question 6 
# after running this code 
# bacon is taken as variable and stored a data (22)
# then adding 1 in bacon will result 22 only not 23 
# because  adding 1  without storing info in variable 
# will not result any kind of  changes 
bacon = 22 
bacon + 1 
print(bacon)  

# so the right way to add 1 in variable is 
bacon = 22 
c = bacon+1
print(c) 
# hence proved 

#7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
# there wil be no result  you will get an syntax error
#  because you cant add or multiply with 
# string and int or string with string by  arithmetic operators 


# 8. Why is eggs a valid variable name while 100 is invalid?
# answer -->
#eggs = "you"
#100 = "you"
  # there is a rule in python that the variable will only start with alphabets only 
# otherwise it will throws an syntax error 


#9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# answer -->
#The int() , float() , and str( ) functions will evaluate to the integer,
 #floating-point number,
 #and string versions of the value passed to them.

#10. Why does this expression cause an error? How can you fix it?
#c = 'I have eaten ' + 99 + ' burritos.'
# this will throws an error because string cant be concatenate with interger 

# the correct way to do this 
print( 'i have eaten '+str(99)+' buritos' )





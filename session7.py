'''Write a Python program to count the number of even and odd numbers from a series of numbers. 
	Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
	Expected Output :
	Number of even numbers : 5
	Number of odd numbers : 4
	
'''

n1=int(input("Enter the start of series: "))
n=int(input("enter the end of series: "))
even=0
odd=0
for i in range(n1,(n+1)):
    if (i%2==0):
        even+=1
    else:
        odd+=1
print(f"there are{even} Even and {odd} Odd numbers between {n1} and {n}")

list1=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in list1:
    if (i%2==0):
        even+=1
    else:
        odd+=1
print(f"there are{even} Even and {odd} Odd numbers ")


'''Write a Python program that accepts a string and calculate the number of digits and letters. 
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2'''   

string1="Python 32"
letter_count=0
digit_count=0
#s_count=0
d_count=0
for i in range(0,len(string1)):
    if (string1[i].isdigit()):
        digit_count+=1
    elif (string1[i]==" "):
        pass #s_count=0
    elif (string1[i]=="."):
        pass #d_count+=1
    else:
        letter_count+=1
print(f'letter count: {letter_count}\n Digit count: {digit_count} ')

'''Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)'''
    
def multiple():
    for i in range(1500,2701):
        if (i%7==0 and i%5==0):
            print(i)

multiple()


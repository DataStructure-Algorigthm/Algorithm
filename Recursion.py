#   1) Print N numbers
def printuptoNnumbers(n):
    if n==0:
        return
    printuptoNnumbers(n-1)
    print(n)
    return
printuptoNnumbers(5)


#   1) Print N to 1 numbers
def printNnumbersto1(n):
    if n==0:
        return n
    print(n)
    printNnumbersto1(n - 1)
printNnumbersto1(5)



# Sum of N Natural Numbers
def sumofNnaturalno(n):
    if n==1:
        return 1
    sums=n+sumofNnaturalno(n-1)
    print(sums)
    return sums
sumofNnaturalno(3)




# Calculate factorial of N
def factofNnaturalno(n):
    if n==1:
        return 1
    sums=n*factofNnaturalno(n-1)
    print(sums)
    return sums
print(factofNnaturalno(6))



# Reverse a string
def reversestring(s):
    if len(s)==0:
        return ""
    strr=s[-1]+reversestring(s[:-1])
    print(strr)
    return strr
data=reversestring("racecar")
print("racecar"==data)



# Check if a number is palindrome
def numberispallidrome(n):
    def pallindromecheck(n,left,right):
        # if len(n)==0:
        #     return
        # if left==right:
        #     return True
        # while left<=right:
        if left>=right:
            return True
        if n[left]!=n[right]:
            return False
        else:
            return pallindromecheck(n,left+1,right-1)
        # return True
    return pallindromecheck(str(n),0,len(str(n))-1)
print(numberispallidrome(11211))



#  sum of digits of a number using recursion

def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    data=(n % 10) + sum_of_digits(n // 10)
    return data
print(sum_of_digits(1234))


# Power of a number (a^b)

def power(a,b):
    if b==0:
        return 1
    elif b>0:
        data=a*power(a,b-1)
    else:
        data = 1/a * power(a, b + 1)
    print(data)
    return data
print(power(2,-1))


# Print all subsequences of a string

def print_subsequences(s, index=0, current=""):
    if index == len(s):
        print(current)  # Base case: Print the formed subsequence
        return

    # Include the current character
    print_subsequences(s, index + 1, current + s[index])

    # Exclude the current character
    print_subsequences(s, index + 1, current)

print_subsequences("abc",0)


# Find GCD (Greatest Common Divisor) of two numbers
def GCD(a,b):
    if a==0:
        return b
    return GCD(b%a,a)

print(GCD(20,30))


# Count ways to climb stairs (1 step or 2 steps at a time)

def climb_stairs(n):
    if n==1:
        return n
    if n==2:
        return n
    return climb_stairs(n-1)+climb_stairs(n-2)
print(climb_stairs(4))

# Generate all binary strings of length N (without consecutive 1s)
def binarystring(n,characters="",last="",array=[]):
    if len(characters)==n:
        array.append(characters)
        print(characters)
        return array
    binarystring(n,characters+"0","0",array)
    # if last!="1":
    binarystring(n, characters + "1", "1",array)
    return array

print(binarystring(3))


# Find the nth Fibonacci number
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
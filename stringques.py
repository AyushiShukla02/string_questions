# 1.Create a string and print it.
str="Hello World"
print(str)

# 2.Take a string input and print its length.
str=input("Enter a string:")
print("Total length of the string is:",len(str))

# 3.Print the last word of the string "Python is Great" using slice.
str="Python is Great"
slice=str[10:15]
print(slice)

# 4.Print each word in different line of string "Python is everywhere".
str="Python is everywhere"
x=str.split()
print(x,sep='\n')

# 5.Print the string "Hello World!" in reverse.
str="Hello World!"[::-1]
print(str)

# 6.Convert the string "How are you?" in uppercase.
str="How are you?"
print(str.upper())

# 7.Convert the string "How Is It Going?" in lowercse.
str="How Is It Going?"
print(str.lower())

# 8.Join the following list by spaces() and print the result.
# word=['Python','is','easy','to','learn']
word=['Python','is','easy','to','learn']
print(" ".join(word))

# 9.Print a multiline string using a single print.
str="""Life is a journey travelled on the highway of time.Therefore, time is precious.Every moment in life should be properly utilized, as time, once lost, can never be recovered .And there is no way to stop the hands of time from ticking."""
print(str)

# 10.Print this string to move to new line '\n' is used.(result should look exactly like the provided string)
# 11.Print a variable with some text using a single print function,output should look like following: the variable is 15

var=15
print(f"The variable is",+var)

# 12.Concatenate the following strings and print the result: s1='Python',s2='is',s3='great.'
s1='Python'
s2='is'
s3='great.'
str=s1+" "+s2+" "+s3
print(str)

# 13.Print # 20 times without using a loop.
print("#\n"*20)

# 14.Print number from 1 to 9 , each on a separate line, followed by a dot, output should look like the following:
# 1.
# 2.
# 3.
for i in range(1,10):
    print(i,'.')

# 15. Ask user to input a sentence and print each word on a different line

a=input("Enter a sentence:")
s=a.split()
s=a
print(*s,sep="\n")
# 16. Ask user to input a string and check if the string ends with '?'

a=input("Enter the string:")
print(a.endswith('?'))

# 17.Ask the user to input a string and print how many times e appeared in the string

a=input("Enter the string")
print(a.count('e'))

# 18.Check if the user input is a number

a=int(input("Enter the value:"))
if a.isnumeric():
    print("Is a number")
else:
    print("Not a number")  

# 19.Remove the extra spaces in beginning and in the end of the following string-
# text='   this is not a good string   '

text='   this is not a good string   '
print(text)
print(text.strip())

# 20.Extract names from the following string and store them in a list.
# names='Joe,David,Mark,Tom,Chris,Robert'

names='Joe,David,Mark,Tom,Chris,Robert'
print(names)
res=names.split()
print("The list of the names is:"+str(res))

# 21.Ask user to input string,print found if any of the character is upper case.

str=input("Enter a string:")
for i in str:
    if i.isupper():
        print("found")
        break
    
# 22.In the following string , add aye in the end of every word and print the results
#text='this is some text'

text='this is some text'
print("this","is","some","text",sep="aye ") 

# 23.Ask user to enter a string and check if the string contains fyi

x=input("Enter a string")
y='fyi'
if y in x:
    print("found")
else:
    print("not found")    

# 24.Remove all the special characters and numbers from the following string
# text="%p34@y!*_*!t68h#&on404"

text="%p34@y!*_*!t68h#&on404"
s1="".join(c for c in text if c.isalpha())
print(s1)

# 25.Calculate the average word length of the following paragraph
# this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated
text="this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated"
length_words=0
total_words=0
words=text.split()
for x in words:
    length_words+=len(x)
    total_words+=1
average=length_words/total_words
print(average)    






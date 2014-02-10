
#read from file: fileName.txt within current directory

with open('fileName.txt', 'r') as text:
    for line in text:
        line.split() #or do something else here
    
    #convert text file of numbers into lists of lists conataining ints
    asList = [map(int, line.split()) for line in text]

#work with asList outside of "with" block



#write to file: fileName.txt within current directory

with open('fileName.txt', 'w') as text:
    textToWrite = "Something"
    text.write(textToWrite)  # + "\n" for new line


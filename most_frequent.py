# print ("Hello world!")
# print ("Hello again")
# print ("I like typing this.")
# print ("This is fun.")
# print ('yay! printing.')
# print ("I'd much rather you 'not'.")
# print ('I "said" do not touch this.')

# this is for Assignment of Week 2 - UCSD edx
list = ['a']   # make an empty list
dict = {}
#dict['out'] = 0
stopList = []
# sample text file object, I changed the encoding in Notepad to ANSI
f = open('C:/Users/Mona/98-3.txt', encoding ="utf-8")
# read the first line and append it to our list
#list.append(f.readline())
# remove all unwanted characters
#list[0] = f.readline()
# list[0] = list[0].strip('. \n')
# list[0] = list[0].split(' ')

fstop = open('D:/Projects/Edx UCSD Python for Data science/word_cloud/stopwords', encoding = "utf-8")
for line in fstop:
    stopList.append(line.strip())
# preprocessing
fstop.close()
print('this is our stop list:\n')
print(stopList)

for line in f:
    # remove unwanted characters
    list[0] = ''.join(c for c in line if c not in '.,?!;:&*%^()[]+=\"><')
    # remove \n return sign
    list[0] = list[0].strip('\n')
    # remove trailing and leading spaces of the sentence
    list[0] = list[0].strip()
    #print(list)
    #list[0] = line.strip('. \n')
    list[0] = list[0].split(' ')
    #print(list)
    #print(len(list[0]), '\n')
    #
    for i  in range(0, len(list[0])):
        # check if it is in the dictionary
        # only add the lower case
        tmp = list[0][i]
        myWord = tmp.lower()
        x = dict.get(myWord)
        #print(x)
        if myWord not in stopList:
            if x == None:
                dict[myWord] = 1
            else:
                dict[myWord] = x + 1
f.close()
#for key, value in dict.items():
    #print(key,':', value)
print('Dictionary length is:',len(dict))
# now let's find the most frequent words in the Dictionary
import operator
sorted_dict = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
# next let's try printing the sorted output
numFrequent = 50
# the number of most frequent words in the text
for l in range(0, numFrequent):
        print(sorted_dict[l])

print('done! \n')

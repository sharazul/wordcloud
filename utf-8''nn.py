from wordcloud import WordCloud
from matplotlib import pyplot as plt

dict = {}
lst = []
lst1 = []
lst2 = []

h = open(r'C:\Users\zigbee\PycharmProjects\coursera\wordcloud.txt', encoding='utf8')  ## we have open a file using open() function

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just"]
for line in h:
    p = line.split()  ## here  each line is splited word by word and then inserted in the list p
    lst.append(p)  ## appended in lst
for j in range(len(lst)):
    for k in range(len(lst[j])):
        lst1.append(lst[j][k])  ## lst has more lists inside so it is merged into single list [lst1]
for pp in range(len(lst1)):
    if lst1[pp].isalpha() and lst1[pp] not in uninteresting_words:
        lst2.append(lst1[pp]) ## removed all other character other than alphapets and inserted in list2

for dic in range(len(lst2)):
    if lst2[dic] not in dict:
        s = 1
        dict[lst2[dic]] = s
    elif lst2[dic] in dict:
        z = dict.get(lst2[dic])
        z = z + 1
        dict[lst2[dic]] = z
        ## here lst3 element is counted and inserted in dictonary [dict]

print(dict)

cloud = WordCloud()
p = cloud.generate_from_frequencies(dict)
myimage = p
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()

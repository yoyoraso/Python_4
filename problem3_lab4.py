from collections import Counter
z=open("mockingjay.txt","rt")
data_set = z.read()
split_it = data_set.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(4)
print(most_occur)
#1. Examine the data structures of the given values.
# by using type() function we can reach to type of all variables listed below
x=8 # int (integer)
y=3.2 # float
z= 8j + 18 # complex
b= True # boolean
c= 23 < 22 # it is goingo to return boolean "False" if type type[c]
l=[1,2,3,4] # list
d={"Name": "Jake", "Age":27, "Adress": "Downtown"} # dictionary
t=("Machine Learning", "Data Science") # tuple
s={"Python", "Machine Learning", "Data science"} #set

#2. Capitalize all letters of the given string expression.
# Replace comma and dot with space, separate word by word
text = "The goal is to turn data into information, and information into insight."

a=text.split(sep=' ') #first method
b=[i.upper() for i in a]
print(b)


def split_by_space_and_capitalize(string):
    new_str=[]
    splitted=string.split(sep=" ")
    for i in splitted:
        new_str.append(i.upper())
    print(new_str)

split_by_space_and_capitalize(text)
#3. Apply the following steps to the given list:
# Step1: Check the number of elements in the given list.
# Step2: Remove the elements in the zeroth and tenth items.
# Step3: Create a list [“D”, “A”, “T”, “A”] from the given list.
# Step4: Remove the element in the eighth item.
# Step5: Add a new element.
# Step6: Add the “N” element in the eighth item again.
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst.pop(0)
lst.pop(10)
lst.insert(0, 'D')
lst.insert(10,'E')
lst[0:4]
lst.pop(8)
lst.insert(8, 'N')

#4. Apply the following steps to the given dictionary structure
# Step1: Access the key values.
# Step2: Access the values.
# Step3: Update the 12 value of the Daisy key to 13.
# Step4: Add a new value with key value Ahmet and value value value [Turkey,24].
# Step5: Remove Antonio from the dictionary.

dict = {
    'Christian': ["America", 18],
    'Daisy': ["England", 12],
    'Antonio': ["Spain", 22],
    'Dante': ["Italy", 25]
}
dict.keys()
dict.values()
dict['Daisy'][1]=13
dict['Ahmet']=['Turkiye', 24]
del dict['Antonio'] #or
dict.pop('Antonio')
# 5. Write a function that takes a list as an argument, assigns the numbers and items in the list to separate lists, and returns the list.
l = [2, 13, 18, 93, 22]

def func(list12):
    new_list12=[[],[]]
    for i in list12:
        if i % 2 == 0:
            new_list12[0].append(i)
        else:
            new_list12[1].append(i)
    return new_list12


even_list, odd_list = func(l)



# 6. The list below contains the names of the top-ranked students from the Engineering and Medicine faculties.
# Respectively, the first three students belong to the Faculty of Engineering and the last three students belong to the Faculty of Medicine.
# Write the students' grades by faculty by using the enumerate function.

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, k in enumerate(students, start=1):
    if i<4:
        print(f"Mühendislik fakültesi {i}. öğrenci: {k}")
    else:
        print(f"Tıp fakültesi {i}. öğrenci: {k}")



# 7. There are 3 lists below.
# The lists contain course code, credits and quota information in order.
# Please print the course information using Zip
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]


for code, credit,quota in zip(ders_kodu,kredi, kontenjan):
    print(f"Kredisi {credit} olan {code} kodlu dersin kontenjanı {quota} kişidir")

# 8. Below 2 sets are given.
# You are expected to define a function that will print the difference of the 2nd set from the 1st set if the 1st set covers the 2nd set and does not cover the middle elements.
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def diff_func(cluster1, cluster2):
    if cluster1.issuperset(cluster2):
        print(cluster2.intersection(cluster1))
    else:
        print(cluster2.difference(cluster1))

diff_func(kume1,kume2)







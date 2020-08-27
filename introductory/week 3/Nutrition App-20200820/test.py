ref = open('food_diary.csv','r') 
content = ref.readlines()
print(len(content))
ref.close()
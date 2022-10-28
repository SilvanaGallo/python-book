names = ['alexis', 'aaron', 'jose', 'guadalupe', 'elvis presley']

print(f"Hi! {names[0].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[1].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[2].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[3].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[4].title()}. I send this message to invite you for dinner in my house! :) ")

#Replace Elvis because he can't come. Add Madonna.
names[-1] = 'madonna'

print(f"Hi! {names[0].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[1].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[2].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[3].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[4].title()}. I send this message to invite you for dinner in my house! :) ")



names.insert(0, 'julia roberts') # inserts in first place

names.insert(len(names)//2,'rosalia') # inserts at the middle

names.append('carlos vives') #inserts at the end of the list

print(f"Hi! {names[0].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[1].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[2].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[3].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[4].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[5].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[6].title()}. I send this message to invite you for dinner in my house! :) ")
print(f"Hi! {names[7].title()}. I send this message to invite you for dinner in my house! :) ")

print("Now, I can only invite 2 people :(")

deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")
deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")
deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")
deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")
deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")
deleted_person = names.pop()
print(f"Goodbye {deleted_person.title()}! See you in another moment :( ")

print(f"Hi {names[0].title()}. You're still invited :) ")
print(f"Hi {names[1].title()}. You're still invited :) ")

del names[1]
del names[0]

print(names)


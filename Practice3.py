import pandas as pd
mydataset = {
    'cars' : ["BMW", "volvo", "Ford"],
    'passings' : [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "Y", "Z"])
print(myvar)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

calories = {"day1" : 420, "day2" : 380, "Day3" : 390}
myvar = pd.Series(calories)
print(myvar)

data = {
    "calories" : [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc["day2"])

df = pd.read_csv('data.csv')
print(df.to_string())
print(df.head(10))
print(df.tail(5))

df = pd.read_json('data.json')
print(df.to_string())

print(df.drop_duplicates())



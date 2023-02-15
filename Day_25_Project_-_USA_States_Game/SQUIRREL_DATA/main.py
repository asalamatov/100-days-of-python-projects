import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count_gray = 0
count_black = 0
count_cinnamon = 0
for color in data["Primary Fur Color"]:
    if color == "Gray":
        count_gray += 1
    elif color == "Black":
        count_black += 1
    elif color == "Cinnamon":
        count_cinnamon += 1
print(count_gray, count_black, count_cinnamon)

dictionary = {
    "Fur Color": ['gray', 'cinnamon', 'black'],
    "Count": [count_gray, count_cinnamon, count_black]
}
print(dictionary)

df = pandas.DataFrame(dictionary)
df.to_csv("squirrel_count.txt")
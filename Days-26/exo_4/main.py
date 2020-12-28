import pandas

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {w:len(w) for w in sentence.split()}


print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day: (temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

student_dict= {
    "student": ["angela", "james", "Lily"],
    "score": [50, 90, 78]
}

# looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

student_data = pandas.DataFrame(student_dict)
print(student_data)

# loop through a data frame
for (key, value) in student_data.items():
    print(value)

# loop trhough rows of a data frame

for (index, row) in student_data.iterrows():
    if row.student == "angela":
        print(row.score)
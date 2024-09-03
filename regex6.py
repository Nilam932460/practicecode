import re

txt="The rain in the spain"
x=re.findall('\AThe',txt)

print(x)

if x:
    print("yes,there is a match!")

else:
    print("No Match")


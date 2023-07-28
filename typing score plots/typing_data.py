import json
import matplotlib.pyplot as plt

with open("data.json", "r") as file:
    # Parse the JSON data from each line
    data = json.load(file)

speed = []
i = 1

chara = []


for lesson in data:
    # assuming 5 characters per word
    wpm = lesson["speed"]/5
    # store this in a dict
    speed.append(wpm)

    char_count = 0

    for char in lesson["histogram"]:
        char_count += 1
        #print(char_count)
    chara.append(char_count)
    #print(chara)


# plot the typing speed vs lessons

plt.subplot(2, 1, 1)
plt.plot([x for x in range(1, len(speed)+1)], speed)#, marker='o', linestyle='-')
plt.subplot(2, 1, 2)
plt.scatter([a for a in range(1, len(speed)+1)], chara)
plt.xlabel('lessons')
plt.ylabel('Speed')
plt.title('Plot of Keys vs Values')
plt.grid(True)
plt.show()
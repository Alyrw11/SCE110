colors = ["red", "green", "blue", "yellow"]

#for color in colors:
#    print(color)
#color.pop() == Removes from presented list. If the () is empty, it will remove the last item
#colors.insert(4, "orange") ## add to current list
for i in range(len(colors)):
    color = colors[i]
    humanCount = i + 1
    print(f"{humanCount} - {color}")
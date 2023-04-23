print("\nThis is a shopping list \n")

shopping_list = {
    "bakery": ["bread","bun","baguette"],
    "grocery": ["tomato","orange","apple"]
}

#print(shopping_list)
#print(type(shopping_list))
listlen = 0
for k, v in shopping_list.items():
    print(f"I'm going to the {k.capitalize()} and buying ", end ="")
    listlen +=len(v)
    for i in range(len(v)):
        print(v[i].capitalize(), end = " ")
    print("")
print(f"\nI've bought {listlen} items")
        
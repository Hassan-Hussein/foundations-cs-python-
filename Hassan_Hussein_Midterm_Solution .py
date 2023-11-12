

tabs_List = []

while True:
    print(tabs_List)
    choice = input("""
    1. Open Tab
    2. Close Tab
    3. Switch Tab
    4. Display All Tabs
    5. Open Nested Tab
    6. Clear All Tabs
    7. Save Tabs
    8. Import Tabs
    9. Exit
                
    enter your choice : 
    """)

    if choice == "1":
        tabs_List.append({
        "Title" : input("Tab Title : "),
        "URL" : input("Tab URL : ")
        })

    elif choice == "2":
        choice2 = input("which tab you want to close(1, 2, 3,...)")
        if choice2 == "":
            tabs_List.pop()
        else:
            tabs_List.remove(tabs_List[int(choice2) - 1])
            
    elif choice == "4":
        for tab in tabs_List:
            print(tab['Title'])

    elif choice == "5":
        choice5 = int(input("in which tab you want to enter a tab : "))
        tabs_List[choice5 - 1]["Nested Tab"]={
            "Title" : input("Tab Title : "),
            "URL" : input("Tab URL : ")
            }
    elif choice == "6":
        tabs_List.clear()    





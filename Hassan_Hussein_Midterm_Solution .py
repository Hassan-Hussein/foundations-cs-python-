# You are tasked with developing an advanced browser tabs simulation in Python for a
# cutting-edge browser. The goal is to create a feature-rich system that allows users to perform
# various operations on tabs using a menu-based interface. The implementation should include
# features such as opening, closing, and switching between tabs, handling nested tabs, and
# additional functionalities.
# The program starts by greeting the user and displaying the following menu:
# 1. Open Tab
# 2. Close Tab
# 3. Switch Tab
# 4. Display All Tabs
# 5. Open Nested Tab
# 6. Clear All Tabs
# 7. Save Tabs
# 8. Import Tabs
# 9. Exit
# ● If the admin chooses (1), the system should allow the user to add a new tab by
# asking for the Title and the URL of the website.
# ● If the admin chooses (2), the system should permit the user to input the index of the
# tab they wish to close. If no index is provided, the system will close the last opened
# tab.
# ● If the admin chooses (3), the system should enable the user to enter the index of
# the tab for displaying its content. If no index is provided, the system will display
# the content of the last opened tab. Note: 'Displaying' in this context refers to printing
# the HTML content of the URL associated with the tab. Conduct some research on
# web scraping for more insights.
# ● If the admin chooses (4), the system should print the titles of all open tabs. If there
# are nested tabs, display them hierarchically.
# ● If the admin chooses (5), the system should enable users to create nested tabs by
# specifying the index of the parent tab where they want to insert additional tabs.
# After entering the index, the system should prompt the user to input the titles and
# contents for the new tabs.
# ● If the admin chooses (6), the system should allow users to clear all opened tabs.
# ● If the admin chooses (7), the system should prompt the user to provide a file path as
# a parameter to save the current state of open tabs. Each tab's information, including
# title, content, and any nested tabs, should be written to the file in JSON format.
# Conduct some research for additional insights on JSON.
# ● If the admin chooses (8), the system should prompt the user to input a file path as a
# parameter to load tabs from the specified file.
# ● If the user chooses (9), the program should exit.
# Instructions:
# ● Use dictionaries to represent each tab and a list to maintain the order of open tabs.

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





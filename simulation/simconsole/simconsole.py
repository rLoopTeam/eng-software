#Console app that lets users issue commands and request tests.

#Main menu
print "Choose a test to run, or enter 0 to run all:"
print "0. Run All"
print "1. Test A"
print "2. Test B"
print "3. Test C"

while True:
    selection = raw_input("Enter your selection: ")
    if selection == "0":
        print "Test A"
        print "Test B"
        print "Test C"
        break
    elif selection == "1":
        print "Test A"
        break
    elif selection == "2":
        print "Test B"
        break
    elif selection == "3":
        print "Test C"
        break
    else:
        print "Invalid selection."
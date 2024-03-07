wizard_list = ['spider legs', 'toe of frog', 'bat wing', 'slug butter', 'snake dandruff'] # Simple list of items (Lists start at 0)

print(wizard_list)                                                                        # Print the list
print(wizard_list[2])                                                                     # Print item number 2
wizard_list[2] = 'snail tongue'                                                           # Change item 2 to snail tongue
print(wizard_list)                                                                        # Print the list with item change
print(wizard_list[2])                                                                     # Print item number 2 with change
print(wizard_list[2:5])                                                                   # Print items 2-4
wizard_list.append('bear burp')                                                           # Add item bear burp
print(wizard_list)                                                                        # Print the list
wizard_list.append('mandrake')                                                            # Add item mandrake
wizard_list.append('hemlock')                                                             # Add item hemlock
wizard_list.append('swamp gas')                                                           # Add item swamp gas
print(wizard_list)                                                                        # Print the list
wizard_list.pop(7)                                                                        # Delete item 6
wizard_list.pop(6)                                                                        # Delete item 5
wizard_list.pop(5)                                                                        # Delete item 4
print(wizard_list)                                                                        # Print the list


numbers = [1, 2, 3, 4]                                                                    # List of numbers
strings = ['I', 'like', 'tacos']                                                          # List of strings
mylist = [numbers, strings]                                                               # List combo of numbers/strings
print(numbers)                                                                            # Print numbers list
print(strings)                                                                            # Print strings list
print(mylist[1])                                                                          # Print mylist item 1
mylist2 = numbers + strings                                                               # Add numbers and strings together under variable mylist2
print(mylist2)                                                                            # Print mylist2 variable
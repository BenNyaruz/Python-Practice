print("\t\t\t\t\t\t Hi Friend !!\n\n")

print("\t\t\t\tPlease find any 10 students for this exercise . . .\n")
name_1 = input("Please enter the name of the 1st student : ")
name_2 = input("Please enter the name of the 2nd student : ")
name_3 = input("Please enter the name of the 3rd student : ")
name_4 = input("Please enter the name of the 4th student : ")
name_5 = input("Please enter the name of the 5th student : ")
name_6 = input("Please enter the name of the 6th student : ")
name_7 = input("Please enter the name of the 7th student : ")
name_8 = input("Please enter the name of the 8th student : ")
name_9 = input("Please enter the name of the 9th student : ")
name_10 = input("Please enter the name of the 10th student : ")

print("\n\nNow you need to get their heights\n")
height_1 = input("Enter " + name_1 + "'s height : ")
height_2 = input("Enter " + name_2 + "'s height : ")
height_3 = input("Enter " + name_3 + "'s height : ")
height_4 = input("Enter " + name_4 + "'s height : ")
height_5 = input("Enter " + name_5 + "'s height : ")
height_6 = input("Enter " + name_6 + "'s height : ")
height_7 = input("Enter " + name_7 + "'s height : ")
height_8 = input("Enter " + name_8 + "'s height : ")
height_9 = input("Enter " + name_9 + "'s height : ")
height_10 = input("Enter " + name_10 + "'s height : ")

#change all height inputs to float data type.
avarage = (float(height_1) + float(height_2) + float(height_3) + float(height_4) + float(height_5) + float(height_6) + float(height_7) + float(height_8) + float(height_9) + float(height_10)) / 10
#change the height to string data type.
print("\n\n\t\t\tThe avarage height for the 10 students is = " + str(avarage) + "m")

print("\n\n\t\t\t\t\t\t THANK YOU :)\n\n")
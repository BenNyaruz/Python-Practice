print("\t\t\tHi\n\n")
card_num = list(input("Please enter the card number : "))
Total_Even_Digits = 0
Total_Odd_Digits = 0

if len(card_num) > 19:
    print("\t\t\t\n\nThe card number is too long :(" )
else:
    for n in card_num[0::2] :
            Even_Digits = int(n) * 2
            if Even_Digits > 9 :
                Double_Digit = list(str(Even_Digits))
                Even_Digits=int(str(Double_Digit[0])) + int(str(Double_Digit[1]))
            Total_Even_Digits = int(Total_Even_Digits) + Even_Digits
            
        
    for m in card_num[1::2] :
        Odd_Digits = int(m)
        Total_Odd_Digits = int(Total_Odd_Digits) + Odd_Digits

    SumOfAll_Digits = Total_Odd_Digits + Total_Even_Digits

    if SumOfAll_Digits % 10 == 0 :
        print("\t\t\t\n\nThe card number is VALID :)")
    else:
        print("\t\t\t\n\nThe card number is INVALID :(")


################################################################################
#   a) 4137 8947 1175 5904  = VALID
#   b) 6499 8024 5027 3568  = INVALID
#   c) 8504 1721 9127 3888  = VALID
#   d) 0043 6687 8348 5480  = INVALID
################################################################################
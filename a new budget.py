import os

class budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float (input("what is your budget value \n"))
        self.spending = self.budget * 0.5
        self.main()


    def main(self):
        os.system('cls')
        print(" your total budget is \n$",'{:.2f}'.format(self.budget))
        main_option = int(input('what would you like to do?, \n1. view total budet, \n2. view spending budget \n'))
        if main_option == 1:
            self.total_budget()
        elif main_option == 2:
            self.spending_budget()
        else:
            quit


    def total_budget(self):
        os.system('cls')
        option = int(input('how much do you want to save? \n1. 20% \n2. 30% \n'))
        if option == 1:
            self.saving = 0.2
        elif option == 2:
            self.saving = 0.3
        else:
            print("error, please select 1 or 2")
        self.final_saving = self.budget * self.saving
        self.extra = self.budget - self.final_saving - self.spending
        print ('\nSpending: $', '{:.2f}'.format (self.spending), '\nTo save: $', '{:.2f}'.format (self.final_saving),'\nExtra: $', '{:.2f}'.format(self.extra))
        os.system('pause')
        self.main()



    def spending_budget(self):
        os.system('cls')
        print('spending budget: $', '{:.2f}'.format(self.spending))

        food = float(input('how much food do you consume annually? \n'))

        electricity = float (input('how much is your annual electricty bills? \n'))

        entertainment  = self.spending - food - electricity

        print ('\n Expenses: \n food: $', '{:.2f}'.format(food), '\n electricity: $', '{:.2f}'.format(electricity), '\n entertainment: $', '{:.2f}'.format(entertainment))
        os.system('pause')
        selectOption = int(input('what else would you like to do? \n1. deposit funds, \n2. withdraw funds \n3. transfer \n4. balance \n' ))

        if selectOption == 1:
            self.depositExtraFunds()

        elif selectOption == 2:
            self.withdrawFunds()

        elif selectOption == 3:
            self.transferFunds()

        elif selectOption == 4:
            print ('\n Expenses: \n food: $', '{:.2f}'.format(food), '\n electricity: $', '{:.2f}'.format(electricity), '\n entertainment: $', '{:.2f}'.format(entertainment))
        else:
            print('invalid selection')

            
        self.main()


    def depositExtraFunds(self):
        os.system('cls')
        selectedOption = int(input('which categories do you want to deposit funds? \n1 food \n2 electricity \n3 entertainment \n'))

        if selectedOption == 1:
            add = int(input('how much do you want to deposit to the food budget? \n'))
    
            print ('your food budget for the year is', '{:.2f}'.format (self.spending + add))

        elif selectedOption == 2:
            add2 = int(input('how much do you want deposit into electricity? \n'))
            print('your new electricity budget is ', '{:.2f}'.format (self.spending + add2))

        elif selectedOption == 3:
            add3 = int(input('how much would yo ike to add to entertinment? \n'))
            print ('your new ntertainment budget is ', '{:.2f}'.format (self.spending + add3))

        else:
            print('invalid selection')

        self.main()


    def withdrawFunds (self):
        os.system('cls')
        withdrawal = int(input('which categories do you want to withdraw funds? \n1 food \n2 electricity \n3 entertainment \n'))

        if withdrawal == 1:
            sub = int(input('how much do you want to withdraw from the food budget? \n'))
            print ('your food budget for the year is', '{:.2f}'.format (self.spending - sub ))
            
        elif withdrawal == 2:
            sub2 = int(input('how much do you want withdraw from electricity? \n'))
            print('your new electricity budget is ', '{:.2f}'.format (self.spending - sub2))
            
        elif withdrawal == 3:
            sub3 = int(input('how much would you like to withdraw from entertinment? \n'))
            print ('your new entertainment budget is ', '{:.2f}'.format (self.spending - sub3))
            
        else:
            print('invalid selection')

        self.main()
            

    def transferFunds(self):
        
        os.system('cls')
        Transfer = int(input('which categories do you want to transfer funds? \n1 food \n2 electricity \n3 entertainment \n'))

        if Transfer == 1:
            tran = int(input('how much do you want to transfer from the food budget? \n'))
            tran_1 = int(input('which category do you wanto transfer the fund to? \n1. electricty \n2. entertainment \n'))
            if tran_1 == 1:
    
                print ('you have transferred funds from food budget to electricity budget')
            elif tran_1 == 2:
                print ('you have transferred funds from food budget to entertainment budget')
            else:
                print('invalid selection')
                
            
        elif Transfer == 2:
            tran2 = int(input('how much do you want to transfer from the electricity budget? \n'))
            tran_2 = int(input('which category do you wanto transfer the fund to? \n1. food \n2. entertainment \n'))
            if tran_2 == 1:
                print ('you have transferred funds from  electricity budget food budget')
            elif tran_2 == 2:
                print ('you have transferred funds from electricty budget to entertainment budget')
            else:
                print('invalid selection')
        
            
        elif Transfer == 3:
            tran3 = int(input('how much would you like to transfer from entertinment? \n'))
            tran_3 = int(input('which category do you wanto transfer the fund to? \n1. food \n2. electricty \n'))
            if tran_3 == 1:
               print ('you have transferred funds from  entertainment budget food budget')
            elif tran_3 == 2:
                print ('you have transferred funds from entertainment budget to electricty budget')
            else:
                print('invalid selection')
                
            
        else:
            print('invalid selection')

        self.main()
            
        
        
        









budget()                             

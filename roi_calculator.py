import os

class Calculator:

    income_dict = {}
    utilities_dict = {}
    expenses_dict = {}
    investments_dict = {}

    def __init__(self):
        self.income = None
        self.rental_income = None
        self.expenses = None
        self.cash_flow = None
        self.roi = None
        self.investment = None
    
    def print_income(self, rental=0, laundry=0, storage=0, misc=0):
        print(f"""
    ============ INCOME ============
    1- Rental Income         ${rental}
    2- Laundry               ${laundry}
    3- Storage               ${storage}
    4- Miscellaneous         ${misc}
    --------------------------------
    TOTAL MONTHLY INCOME    ${rental + laundry + storage + misc}
    """)


    def calculate_income(self):
        os.system('cls')
        self.print_income()
        
        # RENTAL
        rental_inc = input("What is your monthly rental income? $")
        while rental_inc.isdigit() == False:
            if rental_inc == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            rental_inc = input("\nPlease enter a whole number. What is your monthly rental income? $")
        rental_inc = int(rental_inc)
        self.income_dict['1'] = rental_inc
        os.system('cls')
        self.print_income(rental_inc)
        self.rental_income = rental_inc
        
        # LAUNDRY
        laundry = input("What is your monthly laundry income? $")
        while laundry.isdigit() == False:
            if laundry == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            laundry = input("\nPlease enter a whole number. What is your monthly laundry income? $")
        laundry = int(laundry)
        self.income_dict['2'] = laundry
        os.system('cls')
        self.print_income(rental_inc, laundry)

        # STORAGE
        storage = input("What is your monthly storage income? $")
        while storage.isdigit() == False:
            if storage == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            storage = input("\nPlease enter a whole number. What is your monthly storage income? $")
        storage = int(storage)
        self.income_dict['3'] = storage
        os.system('cls')
        self.print_income(rental_inc, laundry, storage)

        # MISCELLANEOUS
        misc = input("What is your monthly miscellaneous income? $")
        while misc.isdigit() == False:
            if misc == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            misc = input("\nPlease enter a whole number. What is your monthly miscellaneous income? $")
        misc = int(misc)
        self.income_dict['4'] = misc
        os.system('cls')
        self.print_income(rental_inc, laundry, storage, misc)

        # TOTAL INCOME
        self.income = rental_inc + laundry + storage + misc

        while True:
            os.system('cls')
            self.print_income(self.income_dict['1'], self.income_dict['2'], self.income_dict['3'], self.income_dict['4'])
            okay = input("Does this look okay to submit? \nNote: You cannot undo once you've submitted. (Y/N): ").lower()

            while okay not in {'y','n','q'}:
                okay = input("\nThat didn't work. Does this look okay to submit? (Y/N): ").lower()
            if okay == 'y':
                self.calculate_expenses()
                break

            else:
                if okay == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                change = input("\nWhich income would you like to edit? Enter a number from the list above or type ALL to redo the whole form: ").lower()
                while change not in {'1','2','3','4','all','q'}:
                    change = input("\nThat didn't work. Which income would you like to edit? ")

                if change == 'all':
                    self.calculate_income()
                    return
                elif change == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return

                new_num = input(f"\nWhat would you like to change #{change} to? $")
                while new_num.isdigit() == False:
                    if new_num == 'q':
                        print("Thank you for using the Return on Investment calculator. Goodbye.")
                        return
                    new_num = input(f"\nPlease enter a whole number. What would you like to change #{change} to? $")

                self.income_dict[change] = int(new_num)
            

    def print_expenses(self, tax=0, insurance=0, hoa=0,
                        lawn=0, vacancy=0, repairs=0, capex=0, management=0, mortgage=0, utilities=0, utilities_edit=False,
                        electric=0, water=0, sewage=0, garbage=0, gas=0):
        print(f"""
        ============ EXPENSES ============
        1- Tax                   ${tax}
        2- Insurance             ${insurance}""", end='')
        
        if utilities_edit:
            utilities = electric + water + sewage + garbage + gas
            print(f""" 
        > Utilities              ${utilities}
            A- Electric          ${electric}
            B- Water             ${water}
            C- Sewage            ${sewage}
            D- Garbage           ${garbage}
            E- Gas               ${gas}""", end='')

        else:
            print(f"\n\t> Utilities              ${utilities}",end='')

        print(f"""\n\t3- HOA                   ${hoa}
        4- Lawn/Snow             ${lawn}
        5- Vacancy               ${vacancy}
        6- Repairs               ${repairs}
        7- Capital Expenditures  ${capex}
        8- Property Management   ${management}
        9- Mortgage              ${mortgage}
        ----------------------------------
        TOTAL MONTHLY EXPENSES   ${tax + insurance + utilities + hoa
                                    + lawn + vacancy + repairs
                                    + capex + management + mortgage}
        """)


    def calculate_expenses(self):
        os.system('cls')
        self.print_expenses()

        # TAX
        tax = input("What is your monthly tax? $")
        while tax.isdigit() == False:
            if tax == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            tax = input("\nPlease enter a whole number. What is your monthly tax? $")
        tax = int(tax)
        self.expenses_dict['1'] = tax
        os.system('cls')
        self.print_expenses(tax)

        # INSURANCE
        insurance = input("What is your monthly insurance? $")
        while insurance.isdigit() == False:
            if insurance == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            insurance = input("\nPlease enter a whole number. What is your monthly insurance? $")
        insurance = int(insurance)
        self.expenses_dict['2'] = insurance
        os.system('cls')
        self.print_expenses(tax, insurance)

        # UTILITIES
        util = input("Do you have utilities expenses? (Y/N): ").lower()
        while util not in {'y','n','q'}:
            util = input("\nThat didn't work. Do you have utilities expenses? (Y/N): ")
        if util == 'q':
            print("Thank you for using the Return on Investment calculator. Goodbye.")
            return
        if util == 'y':
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True)

            # ELECTRIC
            elec = input("What is your monthly electric bill? $")
            while elec.isdigit() == False:
                if elec == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                elec = input("\nPlease enter a whole number. What is your monthly electric bill? $")
            elec = int(elec)
            self.utilities_dict['a'] = elec
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec)

            # WATER
            water = input("What is your monthly water bill? $")
            while water.isdigit() == False:
                if water == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                water = input("\nPlease enter a whole number. What is your monthly water bill? $")
            water = int(water)
            self.utilities_dict['b'] = water
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water)
            
            # SEWAGE
            sewage = input("What is your monthly sewage bill? $")
            while sewage.isdigit() == False:
                if sewage == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                sewage = input("\nPlease enter a whole number. What is your monthly sewage bill? $")
            sewage = int(sewage)
            self.utilities_dict['c'] = sewage
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage)

            # GARBAGE
            garbage = input("What is your monthly garbage bill? $")
            while garbage.isdigit() == False:
                if garbage == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                garbage = input("\nPlease enter a whole number. What is your monthly garbage bill? $")
            garbage = int(garbage)
            self.utilities_dict['d'] = garbage
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage, garbage=garbage)
            
            # GAS
            gas = input("What is your monthly gas bill? $")
            while gas.isdigit() == False:
                if gas == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
                gas = input("\nPlease enter a whole number. What is your monthly gas bill? $")
            gas = int(gas)
            self.utilities_dict['e'] = gas
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage, garbage=garbage, gas=gas)

            # TOTAL UTILITIES
            utilities = elec + water + sewage + garbage + gas
            while True:
                os.system('cls')
                self.print_expenses(tax, insurance, utilities_edit=True, electric=self.utilities_dict['a'], water=self.utilities_dict['b'], sewage=self.utilities_dict['c'], garbage=self.utilities_dict['c'], gas=self.utilities_dict['d'])
                    
                okay = input("Does this look okay to submit? \nNote: You cannot undo once you've submitted. (Y/N): ").lower()

                while okay not in {'y','n','q'}:
                    okay = input("\nThat didn't work. Does this look okay to submit? (Y/N): ").lower()

                if okay == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return

                if okay == 'y':
                    os.system('cls')
                    self.print_expenses(tax, insurance, utilities_edit=False, utilities=utilities)
                    break

                else:
                    change = input("\nWhich utility bill would you like to edit? Enter a letter from the list above: ").lower()
                    while change not in {'a','b','c','d','e','q'}:
                        change = input("\nThat didn't work. Which utility bill would you like to edit? ")

                    if change == 'q':
                        print("Thank you for using the Return on Investment calculator. Goodbye.")
                        return

                    new_num = input(f"\nWhat would you like to change {change.upper()} to? $")

                    while new_num.isdigit() == False:
                        if new_num == 'q':
                            print("Thank you for using the Return on Investment calculator. Goodbye.")
                            return
                        new_num = input(f"\nPlease enter a whole number. What would you like to change {change.upper()} to? $")

                    self.utilities_dict[change] = int(new_num)
        else:
            utilities = 0

        # HOA
        hoa = input("What is your monthly Homeowners Association fee? $")
        while hoa.isdigit() == False:
            if hoa == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
            hoa = input("\nPlease enter a whole number. What is your monthly Homeowners Association fee? $")
        hoa = int(hoa)
        self.expenses_dict['3'] = hoa
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, utilities=utilities)

        # LAWN/SNOW
        lawn = input("What is your monthly lawn care expense, including snow plowing, leaf blowing, etc? $")
        while lawn.isdigit() == False:
            if lawn == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return
            lawn = input("\nPlease enter a whole number. What is your monthly lawn care expense, including snow plowing, leaf blowing, etc? $")
        lawn = int(lawn)
        self.expenses_dict['4'] = lawn
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, utilities=utilities)

        # VACANCY
        # TODO: vac = input(f"What is your monthly vacancy expense? \nTIP: We recommend setting aside 5% of your monthly rental charge, or ${self.rental_income * 0.05:.2f}. $")
        vac = input(f"What is your monthly vacancy expense? \nTIP: We recommend setting aside 5% of your monthly rental charge, or ${2000 * 0.05:.2f}. $")
        while vac.isdigit() == False:
            if vac == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            vac = input(f"\nPlease enter a whole number. What is your monthly vacancy expense? $")
        vac = int(vac)
        self.expenses_dict['5'] = vac
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, utilities=utilities)

        # REPAIRS
        repairs = input("What is your monthly repairs expense? $")
        while repairs.isdigit() == False:
            if repairs == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            repairs = input("\nPlease enter a whole number. What is your monthly repairs expense? $")
        repairs = int(repairs)
        self.expenses_dict['6'] = repairs
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, utilities=utilities)

        # CAPITAL EXPENDITURES
        capex = input("What is your monthly capital expenditure? $")
        while capex.isdigit() == False:
            if capex == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            capex = input("\nPlease enter a whole number. What is your monthly capital expenditure? $")
        capex = int(capex)
        self.expenses_dict['7'] = capex
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, utilities=utilities)

        # PROPERTY MANAGEMENT
        mgmt = input("What is your monthly property management expense? $")
        while mgmt.isdigit() == False:
            if mgmt == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            mgmt = input("\nPlease enter a whole number. What is your monthly property management expense? $")
        mgmt = int(mgmt)
        self.expenses_dict['8'] = mgmt
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, mgmt, utilities=utilities)

        # MORTGAGE
        mort = input("What is your monthly mortgage? $")
        while mort.isdigit() == False:
            if mort == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            mort = input("\nPlease enter a whole number. What is your monthly mortgage? $")
        mort = int(mort)
        self.expenses_dict['9'] = mort
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, mgmt, mort, utilities=utilities)

        # TOTAL EXPENSES
        self.expenses = tax + insurance + hoa + lawn + vac + repairs + capex + mgmt + mort + utilities
        while True:
            os.system('cls')
            self.print_expenses(self.expenses_dict['1'], self.expenses_dict['2'], self.expenses_dict['3'], self.expenses_dict['4'], self.expenses_dict['5'], self.expenses_dict['6'], self.expenses_dict['7'], self.expenses_dict['8'], self.expenses_dict['9'], utilities=utilities)


            okay = input("Does this look okay to submit? \nNote: You cannot undo once you've submitted. (Y/N): ").lower()
            if okay == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            while okay not in {'y','n'}:
                okay = input("\nThat didn't work. Does this look okay to submit? (Y/N): ").lower()
            if okay == 'y':
                self.calculate_cash_flow()
                break
            else:
                change = input("\nWhich expense would you like to edit? Enter a number from the list above or type ALL to redo the whole form: ")
                while change not in {'1','2','3','4','5','6',
                '7','8','9','all','q'}:
                    change = input("\nThat didn't work. Which expense would you like to edit? ")
                
                if change == 'all':
                    self.calculate_expenses()
                    return
                elif change == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return

                new_num = input(f"\nWhat would you like to change #{change} to? $")
                while new_num.isdigit == False:
                    if new_num == 'q':
                        print("Thank you for using the Return on Investment calculator. Goodbye.")
                        return
                    new_num = input(f"\nPlease enter a whole number. What would you like to change #{change} to? $")

                self.expenses_dict[change] = int(new_num)


    def calculate_cash_flow(self):
        os.system('cls')
        self.cash_flow = self.income - self.expenses
        print(f"""
        ============================= CASH FLOW =============================
            FORMULA: monthly income - monthly expenses

        Based on the information you entered, your cash flow is as follows:
        ${self.income:.2f} - ${self.expenses:.2f}

        ---------------------------------------------------------------------
        TOTAL CASH FLOW = ${self.cash_flow:.2f}
        ---------------------------------------------------------------------""")
        cont = input("Press ENTER to continue to calculating Investment. ")
        while cont != '':
            if cont == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            cont = input("\nThat didn't work. Press ENTER to continue. ")
        else:
            self.calculate_investment()


    def print_investment(self, down=0, closing=0, rehab=0, misc=0):
        total = down + closing + rehab + misc
        print(f"""
    ============ INVESTMENT ============
    1- Down Payment          ${down}
    2- Closing Costs         ${closing}
    3- Rehab Budget          ${rehab}
    4- Miscellaneous         ${misc}
    ------------------------------------
    TOTAL INVESTMENT        ${total}
    """)


    def calculate_investment(self):
        os.system('cls')
        self.print_investment()

        # DOWN PAYMENT
        down = input("What was your down payment? $")
        while down.isdigit() == False:
            if down == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            down = input("\nPlease enter a whole number. What was your down payment? $")
        down = int(down)
        self.investments_dict['1'] = down
        os.system('cls')
        self.print_investment(down)

        # CLOSING COSTS
        closing = input("What are your closing costs? $")
        while closing.isdigit() == False:
            if closing == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            closing = input("\nPlease enter a whole number. What are your closing costs? $")
        closing = int(closing)
        self.investments_dict['2'] = closing
        os.system('cls')
        self.print_investment(down, closing)

        # REHAB BUDGET
        rehab = input("What is your rehab budget? $")
        while rehab.isdigit() == False:
            if rehab == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            rehab = input("\nPlease enter a whole number. What is your rehab budget? $")
        rehab = int(rehab)
        self.investments_dict['3'] = rehab
        os.system('cls')
        self.print_investment(down, closing, rehab)

        # MISCELLANEOUS
        misc = input("Any miscellaneous investments? $")
        while misc.isdigit() == False:
            if misc == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return
            misc = input("\nPlease enter a whole number. Any miscellaneous investments? $")
        misc = int(misc)
        self.investments_dict['4'] = misc
        os.system('cls')
        self.print_investment(down, closing, rehab, misc)

        # TOTAL
        self.investment = down + closing + rehab + misc
        while True:
            os.system('cls')
            self.print_investment(self.investments_dict['1'], self.investments_dict['2'], self.investments_dict['3'], self.investments_dict['4'])

            okay = input("Does this look okay to submit? \nNote: You cannot undo once you've submitted. (Y/N): ").lower()

            while okay not in {'y','n','q'}:
                okay = input("\nThat didn't work. Does this look okay to submit? (Y/N): ").lower()

            if okay == 'q':
                print("Thank you for using the Return on Investment calculator. Goodbye.")
                return

            if okay == 'y':
                self.calculate_roi()
                break
            else:
                change = input("\nWhich investment would you like to edit? Enter a number from the list above or type ALL to redo the whole form: ")
                while change not in {'1','2','3','4','all','q'}:
                    change = input("\nThat didn't work. Which investment would you like to edit? ")

                if change == 'all':
                    self.calculate_income()
                    return
                elif change == 'q':
                    print("Thank you for using the Return on Investment calculator. Goodbye.")
                    return

                new_num = input(f"\nWhat would you like to change #{change} to? $")
                while new_num.isdigit() == False:
                    if new_num == 'q':
                        print("Thank you for using the Return on Investment calculator. Goodbye.")
                        return
                    new_num = input(f"\nPlease enter a whole number. What would you like to change #{change} to? $")
                
                self.investments_dict[change] = int(new_num)
    

    def calculate_roi(self):
        os.system('cls')
        self.roi = ((self.cash_flow * 12) / self.investment) * 100
        print(f"""
        ============================= ROI =============================
            FORMULA: yearly cash flow / total investment

        Based on the information you entered, your cash flow is as follows:
        ${self.cash_flow * 12:.2f} / ${self.investment:.2f}

        ---------------------------------------------------------------
        RETURN ON INVESTMENT = {self.roi:.2f}%
        ---------------------------------------------------------------""")

        print("Thanks for using the return on investment calculator. Goodbye.")



def start():
    os.system('cls')
    print("======== Welcome to the RETURN ON INVESTMENT CALCULATOR ========")
    print("""
To find your cash on cash return on investment, we will first calculate 
your monthly net income using your MONTHLY INCOME and MONTHLY EXPENSES.
Then, we will divide your yearly net income by your TOTAL INVESTMENT.

TIP: You will be able to review your entries before submitting each form.
    """)
    # TODO: MAYBE LATER = add functionality to the z
    cont = input("Press ENTER to continue, or Q to quit.").lower()
    if cont not in {'','q'}:
        cont = input("\nThat didn't work. \nPress ENTER to continue, or Q to quit.").lower()
    elif cont == 'q':
        print("Thank you for using the ROI calculator. Goodbye.")
    else:
        calc = Calculator()
        calc.calculate_income()



start()
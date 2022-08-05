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
    - Rental Income         ${rental}
    - Laundry               ${laundry}
    - Storage               ${storage}
    - Miscellaneous         ${misc}
    --------------------------------
    TOTAL MONTHLY INCOME    ${rental + laundry + storage + misc}
    """)


    def calculate_income(self):
        os.system('cls')
        self.print_income()
        
        # RENTAL
        rental_inc = input("What is your monthly rental income? $")
        while rental_inc.isdigit() == False:
            rental_inc = input("Please enter a whole number. What is your monthly rental income? $")
        rental_inc = int(rental_inc)
        os.system('cls')
        self.print_income(rental_inc)
        self.rental_income = rental_inc
        
        # LAUNDRY
        laundry = input("What is your monthly laundry income? $")
        while laundry.isdigit() == False:
            laundry = input("Please enter a whole number. What is your monthly laundry income? $")
        laundry = int(laundry)
        os.system('cls')
        self.print_income(rental_inc, laundry)

        # STORAGE
        storage = input("What is your monthly storage income? $")
        while storage.isdigit() == False:
            storage = input("Please enter a whole number. What is your monthly storage income? $")
        storage = int(storage)
        os.system('cls')
        self.print_income(rental_inc, laundry, storage)

        # MISCELLANEOUS
        misc = input("What is your monthly miscellaneous income? $")
        while misc.isdigit() == False:
            misc = input("Please enter a whole number. What is your monthly miscellaneous income? $")
        misc = int(misc)
        os.system('cls')
        self.print_income(rental_inc, laundry, storage, misc)

        # TOTAL INCOME
        self.income = rental_inc + laundry + storage + misc
        okay = input("Does this look okay to submit? Note: You cannot undo into income section once you've submitted it (Y/N): ").lower()
        while okay not in {'y','n'}:
            okay = input("That didn't work. Does this look okay to submit? (Y/N): ").lower()
        if okay == 'y':
            self.calculate_expenses()
        else:
            # TODO: What to change?
            pass


    def print_expenses(self, tax=0, insurance=0, hoa=0,
                        lawn=0, vacancy=0, repairs=0, capex=0, management=0, mortgage=0, utilities=0, utilities_edit=False,
                        electric=0, water=0, sewage=0, garbage=0, gas=0):
        print(f"""
        ============ EXPENSES ============
        - Tax                   ${tax}
        - Insurance             ${insurance}""", end='')
        
        if utilities_edit:
            utilities = electric + water + sewage + garbage + gas
            print(f""" 
        > Utilities             ${utilities}
            - Electric          ${electric}
            - Water             ${water}
            - Sewage            ${sewage}
            - Garbage           ${garbage}
            - Gas               ${gas}""", end='')

        else:
            print(f"\n\t> Utilities             ${utilities}",end='')

        print(f"""\n\t- HOA                   ${hoa}
        - Lawn/Snow             ${lawn}
        - Vacancy               ${vacancy}
        - Repairs               ${repairs}
        - Capital Expenditures  ${capex}
        - Property Management   ${management}
        - Mortgage              ${mortgage}
        ----------------------------------
        TOTAL MONTHLY EXPENSES  ${tax + insurance + utilities + hoa
                                    + lawn + vacancy + repairs
                                    + capex + management + mortgage}
        """)


    def calculate_expenses(self):
        os.system('cls')
        self.print_expenses()

        # TAX
        tax = input("What is your monthly tax? $")
        while tax.isdigit() == False:
            tax = input("Please enter a whole number. What is your monthly tax? $")
        tax = int(tax)
        os.system('cls')
        self.print_expenses(tax)

        # INSURANCE
        insurance = input("What is your monthly insurance? $")
        while insurance.isdigit() == False:
            insurance = input("Please enter a whole number. What is your monthly insurance? $")
        insurance = int(insurance)
        os.system('cls')
        self.print_expenses(tax, insurance)

        # UTILITIES
        util = input("Do you have utilities expenses? (Y/N): ").lower()
        while util not in {'y','n'}:
            util = input("That didn't work. Do you have utilities expenses? (Y/N): ")
        if util == 'y':
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True)

            # ELECTRIC
            elec = input("What is your monthly electric bill? $")
            while elec.isdigit() == False:
                elec = input("Please enter a whole number. What is your monthly electric bill? $")
            elec = int(elec)
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec)

            # WATER
            water = input("What is your monthly water bill? $")
            while water.isdigit() == False:
                water = input("Please enter a whole number. What is your monthly water bill? $")
            water = int(water)
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water)
            
            # SEWAGE
            sewage = input("What is your monthly sewage bill? $")
            while sewage.isdigit() == False:
                sewage = input("Please enter a whole number. What is your monthly sewage bill? $")
            sewage = int(sewage)
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage)

            # GARBAGE
            garbage = input("What is your monthly garbage bill? $")
            while garbage.isdigit() == False:
                garbage = input("Please enter a whole number. What is your monthly garbage bill? $")
            garbage = int(garbage)
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage, garbage=garbage)
            
            # GAS
            gas = input("What is your monthly gas bill? $")
            while gas.isdigit() == False:
                gas = input("Please enter a whole number. What is your monthly gas bill? $")
            gas = int(gas)
            os.system('cls')
            self.print_expenses(tax, insurance, utilities_edit=True, electric=elec, water=water, sewage=sewage, garbage=garbage, gas=gas)

            # TOTAL UTILITIES
            utilities = elec + water + sewage + garbage + gas
            okay = input("Does this look okay to submit? Note: You cannot undo into utilities section once you've submitted it (Y/N): ").lower()
            while okay not in {'y','n'}:
                okay = input("That didn't work. Does this look okay to submit? (Y/N): ").lower()
            if okay == 'y':
                os.system('cls')
                self.print_expenses(tax, insurance, utilities_edit=False, utilities=utilities)
            else:
                # TODO: What to change?
                pass
        else:
            utilities = 0

        # HOA
        hoa = input("What is your monthly Homeowners Association fee? $")
        while hoa.isdigit() == False:
            hoa = input("Please enter a whole number. What is your monthly Homeowners Association fee? $")
        hoa = int(hoa)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, utilities=utilities)

        # LAWN/SNOW
        lawn = input("What is your monthly lawn care expense, including snow plowing, leaf blowing, etc? $")
        while lawn.isdigit() == False:
            lawn = input("Please enter a whole number. What is your monthly lawn care expense, including snow plowing, leaf blowing, etc? $")
        lawn = int(lawn)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, utilities=utilities)

        # VACANCY
        # TODO: vac = input(f"What is your monthly vacancy expense? \nTIP: We recommend setting aside 5% of your monthly rental charge, or ${self.rental_income * 0.05:.2f}. $")
        vac = input(f"What is your monthly vacancy expense? \nTIP: We recommend setting aside 5% of your monthly rental charge, or ${2000 * 0.05:.2f}. $")
        while vac.isdigit() == False:
            vac = input(f"Please enter a whole number. What is your monthly vacancy expense? $")
        vac = int(vac)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, utilities=utilities)

        # REPAIRS
        repairs = input("What is your monthly repairs expense? $")
        while repairs.isdigit() == False:
            repairs = input("Please enter a whole number. What is your monthly repairs expense? $")
        repairs = int(repairs)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, utilities=utilities)

        # CAPITAL EXPENDITURES
        capex = input("What is your monthly capital expenditure? $")
        while capex.isdigit() == False:
            capex = input("Please enter a whole number. What is your monthly capital expenditure? $")
        capex = int(capex)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, utilities=utilities)

        # PROPERTY MANAGEMENT
        mgmt = input("What is your monthly property management expense? $")
        while mgmt.isdigit() == False:
            mgmt = input("Please enter a whole number. What is your monthly property management expense? $")
        mgmt = int(mgmt)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, mgmt, utilities=utilities)

        # MORTGAGE
        mort = input("What is your monthly mortgage? $")
        while mort.isdigit() == False:
            mort = input("Please enter a whole number. What is your monthly mortgage? $")
        mort = int(mort)
        os.system('cls')
        self.print_expenses(tax, insurance, hoa, lawn, vac, repairs, capex, mgmt, mort, utilities=utilities)

        # TOTAL EXPENSES
        self.expenses = tax + insurance + hoa + lawn + vac + repairs + capex + mgmt + mort + utilities
        okay = input("Does this look okay to submit? \nNote: You cannot undo into expenses section once you've submitted it. (Y/N): ").lower()
        while okay not in {'y','n'}:
            okay = input("That didn't work. Does this look okay to submit? (Y/N): ").lower()
        if okay == 'y':
            self.calculate_cash_flow()
        else:
            # TODO: What to change?
            pass
        

    def calculate_cash_flow(self):
        os.system('cls')
        self.cash_flow = self.income - self.expenses
        print(f"""
        ============================= CASH FLOW =============================
            FORMULA: monthly income - monthly expenses

        Based on the information you entered, your cash flow is as follows:
        ${self.income:.2f} - ${self.expenses:.2f}

        --------------------------------------------------------------------
        TOTAL CASH FLOW = ${self.cash_flow:.2f}
        --------------------------------------------------------------------""")
        cont = input("Press ENTER to continue to calculating Investment. ")
        if cont != '':
            cont = input("That didn't work. Press ENTER to continue. ")
        else:
            self.calculate_investment()


    def print_investment(self, down=0, closing=0, rehab=0, misc=0):
        total = down + closing + rehab + misc
        print(f"""
    ============ INVESTMENT ============
    - Down Payment          ${down}
    - Closing Costs         ${closing}
    - Rehab Budget          ${rehab}
    - Miscellaneous         ${misc}
    ------------------------------------
    TOTAL MONTHLY INCOME    ${total}
    """)

    def calculate_investment(self):
        os.system('cls')
        self.print_investment()

        # DOWN PAYMENT
        down = input("What was your down payment? $")
        while down.isdigit() == False:
            down = input("Please enter a whole number. What was your down payment? $")
        down = int(down)
        os.system('cls')
        self.print_investment(down)

        # CLOSING COSTS
        closing = input("What are your closing costs? $")
        while closing.isdigit() == False:
            closing = input("Please enter a whole number. What are your closing costs? $")
        closing = int(closing)
        os.system('cls')
        self.print_investment(down, closing)

        # REHAB BUDGET
        rehab = input("What is your rehab budget? $")
        while rehab.isdigit() == False:
            rehab = input("Please enter a whole number. What is your rehab budget? $")
        rehab = int(rehab)
        os.system('cls')
        self.print_investment(down, closing, rehab)

        # MISCELLANEOUS
        misc = input("Any miscellaneous investments? $")
        while misc.isdigit() == False:
            misc = input("Please enter a whole number. Any miscellaneous investments? $")
        misc = int(misc)
        os.system('cls')
        self.print_investment(down, closing, rehab, misc)

        # TOTAL
        self.investment = down + closing + rehab + misc
        okay = input("Does this look okay to submit? \nNote: You cannot undo into investment section once you've submitted it. (Y/N): ").lower()
        while okay not in {'y','n'}:
            okay = input("That didn't work. Does this look okay to submit? (Y/N): ").lower()
        if okay == 'y':
            self.calculate_cash_flow()
        else:
            # TODO: What to change?
            pass



def start():
    os.system('cls')
    print("======== Welcome to the RETURN ON INVESTMENT CALCULATOR ========")
    print("""
To find your cash on cash return on investment,
we will first calculate your monthly net income using your monthly income,
monthly expenses, and monthly cash flow.
Then, we will divide your yearly net income by your total investment.
TIP: Enter "Z" to undo a response. Enter "Q" at any time to quit.
    """)
    # TODO: MAYBE LATER = add functionality to the z
    cont = input("Press ENTER to continue, or Q to quit.").lower()
    if cont not in {'','q'}:
        cont = input("That didn't work. \nPress ENTER to continue, or Q to quit.").lower()
    elif cont == 'q':
        print("Thank you for using the ROI calculator. Goodbye.")
    else:
        calc = Calculator()
        calc.calculate_income()



start()
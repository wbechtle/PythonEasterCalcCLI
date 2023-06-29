#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 10/31/2022
#Project: MidTerm, Easter Date Calc.
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"1. Write a program, name it “Easter.py” that will ask the user to input a year and calculate
#       the date of Easter for that year.  You may need to verify your programs accuracy by 
#       doing each step by hand then check your programs values at that point.  Your program 
#       should produce a single line of output of the form:
#           (Western) Easter Sunday - 28 March, 1948.
#
#2.	Assume the user always inputs a valid year.
#
#3.	Once your program outputs, it should loop back to the beginning and ask the user for 
#another year. If the user inputs a negative year, stop the program, and say 'Bye…'"
#--------------------------------------------------------------------------------------------
#ALGORYTHM
#-----------------
#Step 1)Display program name and explanation of program.
#Step 2)Prompt user to input the desired year or negative to quit.
#Step 3)While loop used to iterate program as many times as desired.
#          Complete a series Arithmetics to get to the date of Easter.
#          If statement used to determine if April date.
#               If, elif, else statement used to format April date with correct abbreviation.
#               Displays output inside formatted table.
#          If statement used to determine if March date.
#               Absolute value of Easter used in arithmetic to counter act double negatives 
#               canceling out.
#               If, elif, else statement used to format March date with correct abbreviation.
#               Displays output inside formatted table.
#          New line
#          Prompt user to input another year or negative to quit.
#          New line
#
#Step 4)Display good-bye message.
#--------------------------------------------------------------------------------------------
#Display program name and explanation of program.
#Displays output inside formatted table.
print('-' * 100)
print('|' + f'{"Easter Date Finder":^98}' + '|')
print('-' * 100)
print('|' + f'{"The following program will calculate the date of Easter for any year in the twentieth":^98}' + '|')
print('|' + f'{"or twenty-first centuries for Western dates. (Valid years are 1900 to 2099.)":^98}' + '|')
print('-' * 100)
print()

#Prompt user to input the desired year or negative to quit.
input_year = int(input('Enter a year to determine when Easter falls, or enter a negative to quit: '))

#New line
print()

#While loop used to iterate program as many times as desired.
while input_year > 0:

    #Arithmetics to get to the date of Easter.
    valueD = input_year - 1900 
    valueR = valueD % 19
    valueP = (7 * valueR + 1) // 19
    valueS = (11 * valueR + 4 - valueP) % 29
    valueQ = valueD // 4
    valueT = (valueD + valueQ + 31 - valueS) % 7
    Easter = (25 - valueS - valueT)

    #If statement used to determine if April date.
    if Easter > 0:

        #If, elif, else statement used to format April date with correct abbreviation.
        #Displays output inside formatted table.
        if Easter == 1 or Easter == 21 or Easter == 31:
            date = f'{Easter}st. April {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        elif Easter == 2 or Easter == 22:
            date = f'{Easter}nd. April {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        elif Easter == 3 or Easter == 23:
            date = f'{Easter}rd. April {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        else:
            date = f'{Easter}th. April {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)

    #If statement used to determine if March date.
    if Easter <= 0:
        Easter = 31 - abs(Easter) #Absolute value used to counter act double negatives canceling out.

        #If, elif, else statement used to format March date with correct abbreviation.
        #Displays output inside formatted table.
        if Easter == 1 or Easter == 21 or Easter == 31:
            date = f'{Easter}st. March {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        elif Easter == 2 or Easter == 22:
            date = f'{Easter}nd. March {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        elif Easter == 3 or Easter == 23:
            date = f'{Easter}rd. March {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)
        else:
            date = f'{Easter}th. March {input_year}'
            print('-' * 20)
            print('|' + f'{"Easter Day":^18}' + '|')
            print('|' + f'{date:^18}' + '|')
            print('-' * 20)

    #New line
    print()

    #Prompt user to input another year or negative to quit.
    input_year = int(input('Enter another year to determine when Easter falls, or Enter a negative to quit: '))

    #New line
    print()

#Display good-bye message.
print('Bye...')
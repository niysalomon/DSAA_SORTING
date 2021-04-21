import sys

# import sort_data as sd
import sorting_data as document

ALL_THE_LIST = ['sequence', 'size', 'priority']
ORDERING = ['asc', 'desc']

Enter_choice = input('ENTER SORTING YOU WANT BETWEEN SEQUENCE,PRIORITY OR SIZE : ')

if Enter_choice not in ALL_THE_LIST:
    print('Invalid Sort Choice!')
    sys.exit(1)

Enter_order = input("ENTER ORDER YOU WANT :  ")

if Enter_order not in ORDERING:
    print('Invalid Sort Order!')
    sys.exit(1)

FINAL_SORTED = document.sorting_data(Enter_choice, Enter_order)
document.get_final_file(FINAL_SORTED, Enter_choice)
print('Well Done !!!!')

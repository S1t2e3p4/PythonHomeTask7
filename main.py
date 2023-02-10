import user_interface as ui
import defs_check_input as c
import logger as log
import data_display as dd
import html_convert as hc
import csv_viewer as cv

import os
import random
os.system('cls')

print('Choose an operation: ')
print('  finding a contact - 1',
      '  addition of a new contact - 2',
      '  export of a phonebook - 3',
      '  logger journal unload - 4', sep='\n')
user_input = c.check_input_1()

if user_input == '1':
    ui.show_contact()

elif user_input == '2':
    print('Choose an operation: manual addition - 1, import from a file - 2')
    next_input = c.check_input_2()

    if next_input == '1':
        ui.add_contact()
    else:
        ui.import_contact()

elif user_input == '3':
    print('Choose a view format: HTML - 1, CSV.file - 2, terminal - 3')
    next_input = c.check_input_3()

    if next_input == '1':
        hc.create_html()
    elif next_input == '2':
        cv.create_csv()
    else:
        print(*(dd.show_phonebook()))

else:
    print('Choose a view format: CSV.file - 1, terminal - 2')
    next_input = c.check_input_2()
    if next_input == '1':
        log.log_output_data_csv()
    else:
        log.log_output_data_term()
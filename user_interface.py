import logger as log
import data_contact as dc
import data_display as dd
import defs_check_input as dci


def add_contact():
    log.log_input_data('Contact addition requested by user')
    surname = input('Enter a surname: ')
    name = input('Enter a name: ')
    telephone = input('Enter a phone number: ')
    description = input('Enter description: ')
    contact = 'Surname: '+surname+'\n'+'Name: '+name + '\n' + \
        'Telephone: '+telephone+'\n'+'Comment: '+description+'\n'
    dc.add_contact_manually(contact)
    return contact


def import_contact():
    log.log_input_data('Contact import from file requested by user')
    print('Enter a path to file: ')
    name_file = dci.check_filepath()
    dc.import_contact_from_file(name_file)


def show_contact():
    log.log_input_data('Info about contact requested by user')
    print('Enter a surname: ')
    surname = dci.check_text()
    dd.find_contact_in_phonebook(surname)
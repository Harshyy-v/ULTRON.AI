import pywhatkit
from func.Speak import speak, micexecution
from data.contacts import contact_list  # Import the contact list from the separate file



def send_whatsapp_message(contact_name, phone_number, message, now=False):
    try:
        if now:
            pywhatkit.sendwhatmsg_instantly(phone_number, message)
        else:
            pywhatkit.sendwhatmsg(phone_number, message)

        print(f"Message sent to {contact_name} ({phone_number})")
        speak("Message sent")

    except Exception as e:
        print(f"Failed to send message to {contact_name} ({phone_number}): {e}")

def ask_user_and_send_message():

    print("Enter the name of the contact: ")
    speak("Enter the name of the contact: ")
    contact_name = input()

    print("Enter the message to send: ")
    speak("Enter the message to send: ")
    message = input()

    phone_number = contact_list.get(contact_name)
    if phone_number:
        send_whatsapp_message(contact_name, phone_number, message, now=True)
    else:
        print("Contact not found in the contact list.")




# def load_contacts_from_vcf(file_path):
#     contacts = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         vcard_data = file.read()
#
#     # Split the file content into individual vCard entries
#     vcard_entries = vcard_data.split('END:VCARD')
#
#     for entry in vcard_entries:
#         if 'BEGIN:VCARD' in entry:
#             entry = entry + 'END:VCARD'  # Add the delimiter back for the last entry
#             vcard = vobject.readOne(entry)
#             if hasattr(vcard, 'fn') and hasattr(vcard, 'tel'):
#                 name = vcard.fn.value
#                 phone_number = vcard.tel.value
#                 contacts[name] = phone_number
#             # Handle cases where there are multiple phone numbers
#             elif hasattr(vcard, 'fn'):
#                 name = vcard.fn.value
#                 phone_numbers = [tel.value for tel in vcard.contents.get('tel', [])]
#                 contacts[name] = phone_numbers
#
#     return contacts
#
#
# def save_dict_to_file(contact_dict, file_path):
#
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write('contact_list = {\n')
#         for name, number in contact_dict.items():
#             file.write(f'    "{name}": "{number}",\n')
#         file.write('}\n')

#

#
# contacts = load_contacts_from_vcf('contacts.vcf')
# output_file_path = 'contacts.py'
# save_dict_to_file(contacts, output_file_path)

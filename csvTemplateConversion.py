import csv
import os

template = ['Title', 'First Name', 'Middle Name', 'Last Name', 'Suffix', 'Company', 'Department', 'Job Title', 'Business Street', 'Business Street 2', 'Business Street 3', 'Business City', 'Business State', 'Business Postal Code', 'Business Country/Region', 'Home Street', 'Home Street 2', 'Home Street 3', 'Home City', 'Home State', 'Home Postal Code', 'Home Country/Region', 'Other Street', 'Other Street 2', 'Other Street 3', 'Other City', 'Other State', 'Other Postal Code', 'Other Country/Region', "Assistant's Phone", 'Business Fax', 'Business Phone', 'Business Phone 2', 'Callback', 'Car Phone', 'Company Main Phone', 'Home Fax', 'Home Phone', 'Home Phone 2', 'ISDN', 'Mobile Phone', 'Other Fax', 'Other Phone', 'Pager', 'Primary Phone', 'Radio Phone', 'TTY/TDD Phone', 'Telex', 'Account', 'Anniversary', "Assistant's Name", 'Billing Information', 'Birthday', 'Business Address PO Box', 'Categories', 'Children', 'Directory Server', 'E-mail Address', 'E-mail Type', 'E-mail Display Name', 'E-mail 2 Address', 'E-mail 2 Type', 'E-mail 2 Display Name', 'E-mail 3 Address', 'E-mail 3 Type', 'E-mail 3 Display Name', 'Gender', 'Government ID Number', 'Hobby', 'Home Address PO Box', 'Initials', 'Internet Free Busy', 'Keywords', 'Language', 'Location', "Manager's Name", 'Mileage', 'Notes', 'Office Location', 'Organizational ID Number', 'Other Address PO Box', 'Priority', 'Private', 'Profession', 'Referred By', 'Sensitivity', 'Spouse', 'User 1', 'User 2', 'User 3', 'User 4', 'Web Page']

mapping_columns = {0:1, 1:2, 2:3, 3:0, 4:4, 5:70, 6:91, 7:66, 8:52, 9:49, 10:74, 11:73, 12:71, 13:77, 14:57, 15:60, 16:63, 17:44, 18:37, 19:38, 20:40, 21:43, 22:36, 24:15, 25:16, 26:17, 27:69, 28:18, 29:19, 30:20, 31:21, 32:86, 33:55, 34:75, 35:50, 36:84, 37:35, 38:31, 39:32, 40:30, 41:29, 42:5, 43:7, 44:6, 45:78, 46:79, 47:83, 50:8, 51:9, 52:10, 53:53, 54:11, 55:12, 56:13, 58:42, 59:41, 61:22, 62:23, 63:24, 64:80, 65:25, 66:26, 67:27, 68:28, 69:33, 70:34, 71:39, 72:45, 73:46, 74:47, 75:87, 76:88, 77:89, 78:90, 79:72, 80:76, 81:68, 82:51, 83:56, 84:85, 85:81, 86:82, 87:54 }

print('csv extension will be added atuomatically')
def chooseFile():
        global openFile
        openFile = ''
        while len(openFile) == 0:
                print('Type in the file name: ')
                openFile = input() 
        openFile += '.csv'

def nameFile():
        if os.path.isfile(openFile):
                global createFile
                createFile = ''
                while len(createFile) == 0:
                        print('New file name: ')
                        createFile = input()
                createFile += '.csv'
        else: 
                print("quote file missing")
                chooseFile()

def formatting():
        global createFile, openFile
        with open(openFile, 'r') as gglInfo, open(createFile, 'w', newline='') as rightTemplate:
                reader = csv.reader(gglInfo)
                writer = csv.writer(rightTemplate)

                rows = list(reader)

                writer.writerow(template)

                for row in rows[1:]:  
                        new_row = [''] * len(template)  
                        for old_index, new_index in mapping_columns.items():
                                if old_index < len(row):
                                        new_row[new_index] = row[old_index]
                        writer.writerow(new_row)

chooseFile()
nameFile()
formatting()


#student administration tool using python

import csv  #importing csv module from python

def write_into_csv(entries_list) :  #defining a function to convert the entries into csv format
    #to update the rows with new entries
    with open('student_entries.csv', 'a', newline = '') as csv_file :
         writer = csv.writer(csv_file) #for going to next row

         if csv_file.tell() == 0 :
             writer.writerow([ 'Roll no.' , 'Name' , 'DoB' , 'Age' , 'Mobile number' , 'E-mail ID' , 'Residence' ])  #specifying the types of entries(columns) for student to enter
         writer.writerow(entries_list)

if __name__ == '__main__' :  #defining a main function for the entries
    condition = True
    student_count = 1

    while(condition) :
        student_entries = input('enter the information of student {} in the format Roll_no. Name DoB Age Mobile_number E-mail_ID Residence : ' .format(student_count)) #taking input from user

        student_entries_list = student_entries.split(' ')  #converting the entries into list format by using 'split' function
        print('entered information: ' , student_entries_list)

        print('\n\n Confirm your entries --> \n Roll no.: {} \n Name: {} \n DoB: {} \n Age: {} \n Mobile number: {} \n E-mail ID: {} , \n Residence: {}'
              .format(student_entries_list[0] , student_entries_list[1] , student_entries_list[2] , student_entries_list[3] , student_entries_list[4] , student_entries_list[5]
                      , student_entries_list[6]))  #segregating the information for user comfort

        Choice_verification = input('\n\n Verify the entered information and reply (yes/no): ') #giving an extra chance for user to verify his/her entries

        if Choice_verification == 'yes' : 
              write_into_csv(student_entries_list) #updating the info to csv file

              condition_check = input('\n\n Do you want to enter another student information? reply (yes/no) : ')

              if condition_check == 'yes' : 
                  condtion = True
                  student_count +=1 #initializing a loop

              elif condition_check == 'no' :
                  condition = False

        elif Choice_verification == 'no' :
             print('\n\n re-enter the entries--> ')

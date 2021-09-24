import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm
import time

REPROVADO_POR_FALTA = 'Reprovado por Falta' # Constant variable to make the code more dynamic
APROVADO = 'Aprovado'
REPROVADO_POR_NOTA = 'Reprovado por Nota'
EXAME_FINAL = 'Exame Final'

def activating(): # Method that checks and authorizes editing of the spreadsheet
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json') # Initialize the service account credentials with a JSON key
    gc = gspread.authorize(credentials) # Authorize the service account with the credentials
    wks = gc.open_by_key('1ektoUiohPzkgjRxdJDBiBqxIv-jVUb7gzMgwB0Cppyc') # Open the spreadsheet by ID
    worksheet = wks.get_worksheet(0) # Initialize the worksheet object

    return worksheet # Return the worksheet object

def getting_data(worksheet): # Method that takes all necessary data
    test1_aux = worksheet.get('D4:D27')
    test2_aux = worksheet.get('E4:E27')
    test3_aux = worksheet.get('F4:F27')     
    skip_class_aux = worksheet.get('C4:C27')
    
    test1 = []
    test2 = []
    test3 = []
    skip_classes = []

    print("Getting data...")
    for x in tqdm(range(24)):                 
        a = list(map(int,test1_aux[x])) # "map" function that invokes the "int" function on all elements of the list and returns a "map" object, so it needs to be changed to a list again
        b = list(map(int,test2_aux[x]))     
        c = list(map(int,test3_aux[x]))
        d = list(map(int,skip_class_aux[x]))
        
        test1 += a
        test2 += b
        test3 += c
        skip_classes += d
        
    data = []
    data.append(test1) # Add the first list in the data list
    data.append(test2) # Add the second list in the data list
    data.append(test3) # Add the third list in the data list
    data.append(skip_classes) # Add the fourth list in the data list
    
    return data # Return one list of lists
    

def getting_log(students, status): # Log method that tracks application status
    print(" ")
    print("Getting the log..")
    for x in tqdm(range(24)):
        time.sleep(0.02)
 
    print(" ")
    for x in range(24): # For loop that print name and status of students
        print(f"Name: {students[x]} --- Status: {status[x]}")
        
        
def checking_status(worksheet, data):  # Method that checks the status of all students
    students = []
    status = []
    sum = 0
    average = 0
    
    print(" ")
    print("Checking status...")
    for x in tqdm(range(24)):
        p1 = data[0][x] / 10 # Assign the variable p1 to the note of the first list at position x and divide by 10 for easier handling
        p2 = data[1][x] / 10
        p3 = data[2][x] / 10
        
        sum = (p1 + p2 + p3) # Add the 3 notes
        average = sum / 3 # and get the average
        
        if data[3][x] > 15: # Check if skip classe > 15 if not continue the if statement
            worksheet.update_acell(f'G{(x + 4)}', REPROVADO_POR_FALTA) # Update the cell corresponding to the student's status
            worksheet.update_acell(f'H{(x + 4)}', str(0)) # Update the cell referring to what grade it needs to take to be approved and transform from int into a string to write to the spreadsheet
            student = worksheet.acell(f'B{(x + 4)}').value # Takes the student's name and saves it to a list for log control
            students.append(student) # Add name to list
            status.append(REPROVADO_POR_FALTA) # Add approval status to another list
            
        elif average >= 7:
            worksheet.update_acell(f'G{(x + 4)}', APROVADO)
            worksheet.update_acell(f'H{(x + 4)}', str(0))
            student = worksheet.acell(f'B{(x + 4)}').value
            students.append(student)
            status.append(APROVADO)
            
        elif average < 5:
            worksheet.update_acell(f'G{(x + 4)}', REPROVADO_POR_NOTA)
            worksheet.update_acell(f'H{(x + 4)}', str(0))
            student = worksheet.acell(f'B{(x + 4)}').value
            students.append(student)
            status.append(REPROVADO_POR_NOTA)
            
        elif average >= 5 and average < 7:
            worksheet.update_acell(f'G{(x + 4)}', EXAME_FINAL)
            worksheet.update_acell(f'H{(x + 4)}', str((round(((5 * 2) - average) * 10)))) # The inequalities proposed by the challenge resolved, stays that way, rounds the result and turns it into a string
            student = worksheet.acell(f'B{(x + 4)}').value
            students.append(student)
            status.append(EXAME_FINAL)
            
    getting_log(students, status)
    
    return students, status
if __name__ == '__main__':
    worksheet = activating() # Initialize the worksheet object
    try: # Exception treatment
        data = getting_data(worksheet) # Get the data from the spreadsheet
        students, status = checking_status(worksheet, data) # Check the status of students and assign in the students and status list
        
    except IndexError: # Exception for when the number of grades is less than the number of students
        print(" ")
        print("Something is wrong, maybe the number of students has changed.")
      
    except gspread.exceptions.APIError: # Exception for when the number of write requests per minute per use is greater than quota metric
        print(" ")
        print("Google Spreadsheet API has a limit of write requests per minute per user, please restarth the app! Thank you!")
        # Quota exceeded for quota metric 'Write requests' and limit 'Write requests per minute per user' of service 'sheets.googleapis.com'
        
    else: # If everything went fine print "Everything OK!"
        print(" ")
        print("Everything OK!")
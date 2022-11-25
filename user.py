import os

class User:
    def __init__(self):
        if os.path.exists('user_credentials.csv') == False:

            self.first_name = input('First name:\n')
            self.last_name = input('LAst name:\n')
            self.dob = input('Date of birth:\n')
            self.email = input('Email:\n')
            self.password = input('Password:\n')
            self.height = input('Height:\n')
            from csv import writer

            with open('user_credentials.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([self.first_name, self.last_name, self.dob, self.email, self.password, self.height])
                f_object.close()
        else:
            import csv
            with open('user_credentials.csv') as csv_file:
                reader_obj = csv.reader(csv_file)
                for line in reader_obj:
                    if len(line) > 3:
                        self.first_name = line[0]
                        self.last_name = line[1]
                        self.dob = line[2]
                        self.email = line[3]
                        self.password = line[4]
                        self.height = line[5]
                    


def main():
    User()




if __name__ == '__main__':
    main()

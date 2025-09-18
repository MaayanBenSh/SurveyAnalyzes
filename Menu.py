class Menu:
    def __init__(self):
        self.schools = []
        self.users = []

    def print_menu(self):
        print("Choose one of the ooptions below:"
              "1. Answer the survey."
              "2. Get survey results."
              "3. Get survey information."
              "4. Get survey diagram."
              "5. Exit"
              )

    def enter_survey(self):
        pass

    def get_log_results(self):
        option = int(input("Which kind of survey results would you like to see?"
                           "1. All Schools results."
                           "2. Specific Schools results."))
        while option != 1 and option != 2:
            print("Invalid input. Please choose one of the given options.")
            option = int(input("Which kind of survey results would you like to see?"
                               "1. All Schools results."
                               "2. Specific Schools results."))
            if option == 1:
                pass
            if option == 2:
                school_option = int(input("Which school would you like to see the results of? "))



    def get_log_data(self):
        pass

    def get_diagram(self):
        pass

    def manu(self):
        pass
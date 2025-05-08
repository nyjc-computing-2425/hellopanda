from backend import account, event, signup

def initialise():

    #Table initialisation
    account.delete_account_table()
    account.create_account_table()
    event.delete_event_table()
    event.create_event_table()
    signup.delete_signup_table()
    signup.create_signup_table()

    ########Dummy data##########
    account.store_account_data("notjohn@gmail.com", "JuWMqIugOlEtuXLC", "40493376214957570934363042765919812022617836654205352252256196165357072291861", "student", "hehe", 2426, 2025)
    #email: notjohn@gmail.com password: salty
    event.store_event_data(1, "2025-06-12 09:00:00", "2025-06-13 09:00:00", "Bad event", "hi  imagine events", "Home", "hehe@gmail.com")
    event.store_event_data(2, "2025-04-10 09:00:00", "2025-06-13 09:00:00", "Another event", "HAHA!", "Probably in sch", "hehe@gmail.com")
    signup.add_student_to_event("notjohn@gmail.com", 1)

initialise()
###############ACCOUNT######################
# print("Account")
# account.update_class("notjohn@gmail.com", 2426)
# account.update_year("notjohn@gmail.com", 1000)
# print(account.retrieve_byclass(2426))
# print(account.acc_type("john@gmail.com"))

###################EVENT######################
# print("Event")
# event.store_event_data(1, "2025-06-12 09:00:00", "2025-06-13 09:00:00", "Bad event", "hi  imagine events", "Home")
# event.store_event_data(2, "2025-04-10 09:00:00", "2025-06-13 09:00:00", "Another event", "HAHA!", "Probably in sch")
# print(event.retrieve_all_events())
# print("Upcoming: ",event.retrieve_upcoming_events())
# print("Current: ",event.retrieve_current_events())
# print(event.retrieve_byname("bad event"))
#print(event.retrieve_byorganiser("hehe@gmail.com"))

#################SIGNUP#########################
# print("Signup")
# signup.add_student_to_event("john@gmail.com", 1)
# print(signup.get_signed_up_events("john@gmail.com"))
# signup.remove_student_from_event("john@gmail.com" , 1)
# print(signup.get_signed_up_events("hehe@gmail.com"))
# print(signup.get_event_participants(1))
# print(event.participants_to_csv(1, "testcsv.csv"))

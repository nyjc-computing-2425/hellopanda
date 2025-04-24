from backend import account, event, signup

#create_account_table()
#store_account_data("notjohn@gmail.com", "salty", 123, "student", "hehe", 2426, 2025)
#update_class("notjohn@gmail.com", 2426)
#print(retrieve_byclass(2426))
#print(acc_type("john@gmail.com"))

# event.delete_event_table()
# event.create_event_table()
# event.store_event_data(1, "2025-06-12 09:00:00", "2025-06-13 09:00:00", "Bad event", "hi  imagine events", "Home")
# event.store_event_data(2, "2025-04-10 09:00:00", "2025-06-13 09:00:00", "Another event", "HAHA!", "Probably in sch")
# print(event.retrieve_all_events())
# print("Upcoming: ",event.retrieve_upcoming_events())
# print("Current: ",event.retrieve_current_events())
# print(event.retrieve_byname("bad event"))

signup.delete_signup_table()
signup.create_signup_table()
signup.add_student_to_event("john@gmail.com", 1)
print(signup.get_signed_up_events("john@gmail.com"))
#signup.remove_student_from_event("john@gmail.com" , 1)
print(signup.get_signed_up_events("hehe@gmail.com"))
print(signup.get_event_participants(1))

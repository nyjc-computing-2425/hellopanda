from backend import account, event

#create_account_table()
#store_account_data("notjohn@gmail.com", "salty", 123, "student", "hehe", 2426, 2025)
#update_class("notjohn@gmail.com", 2426)
#print(retrieve_byclass(2426))
#print(acc_type("john@gmail.com"))

event.delete_event_table()
event.create_event_table()
event.store_event_data(1, "2025-06-12 09:00:00", "2025-06-13 09:00:00", "Bad event", "hi  imagine events", "Home")
event.store_event_data(2, "2025-04-10 09:00:00", "2025-06-13 09:00:00", "Another event", "HAHA!", "Probably in sch")
print(event.retrieve_event())
print("Upcoming: ",event.retrieve_upcoming_events())
print("Current: ",event.retrieve_current_events())
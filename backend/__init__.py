# account functions are moved to account.py
# if you were using:
#     import backend
# please use instead:
#    from backend import account
#    from backend import event

from . import account, event, sql, validate

# The below usage will be deprecated in Sprint 4
from .account import *
from .event import *



if __name__ == "__main__":
    #create_account_table()
    #store_account_data("notjohn@gmail.com", "salty", 123, "student", "hehe", 2426, 2025)
    #update_class("notjohn@gmail.com", 2426)
    #print(retrieve_byclass(2426))
    #print(acc_type("john@gmail.com"))

    # create_event_table()
    # store_event_data(1, "2025-06-12 09:00:00", "2025-06-13 09:00:00", "Bad event", "hi  imagine events", "Home")
    # print(retrieve_event())
    pass
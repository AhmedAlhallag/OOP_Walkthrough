# TODO: this logic file will be ocnverted into a layer; aka: folder when we go to CA
# later on take the create account logic put it as a control in ECB, and label it as a service in CA, same for login'
 
# we can start it  off like the lab from covbentry 
#idea here: no couplign whatso ever with the DAL; by having a temp variable (memory) that exists only in  this file 

# WHAT I WWOULD HAVE DONE: ususally I would hava a link to dal here (either with an import for the CRUD methods
# or via a direct write operation into the  persistance storage (e.g: Files )


temp_users = [] 

def update_current_users_from_database(alist_from_database):
    # FLAWED:
    # without gloobal whatever is coming from the db (on assignment you need global) will be stored in a local variable
    # + the write operation is useless into db 
    # solution: return it + made a connection to one file (start of associations)
    # with global, the changes from db is to be reflected into the temp_userrs but a link is inistiated;
    # meaning that when the temp get updated (appended) first, the uses list from db gets updated instantly as well
    # no need to write into db
     
    # global temp_users
    temp_users  = alist_from_database
    print("id of temp_users_list_in_logic_layer INSIDE THE UPODATE FUNCTUIIN",id(temp_users), end='\n\n')
    return temp_users
    
    
    

def register(un, ps):
    print("id of temp_users_list_in_logic_layer",id(temp_users), end='\n\n')
    temp_users.append({'un':un, "ps": ps})
    
    
# to return the temp variabel which is only in this file, we need a 'getter'

# TODO: if we had a class we would have this temp (state) variable as an instance/class variable which can be access via the logic object 

def get_users():
    return temp_users 
    

# update_current_users_from_database([2])
    
    
class User:
    """
    Class that generates new instances of users.
    """

    users_list = [] 

    def __init__(self,user_id,first_name,last_name,email):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def save_user(self):
        '''
        save_user method saves our objects into users_list
        '''
        User.users_list.append(self)
    
    def delete_user(self):
        '''
        delete_user method deletes a saved user 
        '''
        User.users_list.remove(self)
    

    
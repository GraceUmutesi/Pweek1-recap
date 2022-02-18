Id = input()
            if check_existing_car(Id):
                the_user = find_car(Id)
                del_car(the_user)
                print('...Successfully deleted...')
            else:
                print('The user you are trying to delete is not available')
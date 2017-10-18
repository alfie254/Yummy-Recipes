class User(object):

    def __init__(self):
        self.users_dict = {}
    def addUser(self, user_data):
        for key in user_data:
            if key in self.users_dict:
                return "Dublicate user"
            else:
                self.users_dict.update(user_data)
    def getUsers(self):
        return self.users_dict
    def deleteUser(self, email):
        if email in self.users_dict.keys():
            return {email : self.users_dict.pop(email)}
        else:
            return "no user found"
    def updateUser(self, email, newdata):
        if email in self.deleteUser(email):
            self.addUser(newdata)
        else:
            return "user not found"
    def getUser(self, email):
        if email in self.users_dict:
            return {email : self.users_dict.get(email)}
        else:
            return "user not found"
    
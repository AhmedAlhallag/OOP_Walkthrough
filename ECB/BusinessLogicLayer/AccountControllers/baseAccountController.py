class baseAccountController:
    
    def __init__(self, accountObj): # association
        self.accountObj = accountObj
        
    def userExists(self, key, value, alist):
        idx = self.accountObj.access_findBy(key, value, alist)
        if idx != -1:
            return idx, True
        return idx, False

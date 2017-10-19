class Categories(object):
    def __init__(self):
        self.categories_dict = {}
    def addCategories(self, name, cat_data):
        if name in self.categories_dict:
            return "Dublicate category"
        else:
            self.categories_dict.update({name:cat_data})
    def getCategories(self):
        return self.categories_dict
    def deleteCategory(self, name):
        if name in self.categories_dict:
            return {name : self.categories_dict.pop(name)}
        else:
            return "category not found"
    def updateCategory(self, name, newdata):
        if name in self.deleteCategory(name):
            self.addCategories(name, newdata)
        else:
            return "category not found"
    def getCategory(self, name):
        if name in self.categories_dict:
            return {name : self.categories_dict.get(name)}
        else:
            return "category not found"

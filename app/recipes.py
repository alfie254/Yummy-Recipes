class Recipes(object):
    def __init__(self):
        self.recipe_dict = {}
    def addRecipes(self, name, rec_data):
        if name in self.recipe_dict:
            return "Dublicate recipe"
        else:
            self.recipe_dict.update({name:rec_data})
    def getRecipes(self):
        return self.recipe_dict
    def deleteRecipe(self, name):
        if name in self.recipe_dict:
            return {name : self.recipe_dict.pop(name)}
        else:
            return "recipe not found"
    def updateRecipe(self, name, newdata):
        if name in self.deleteRecipe(name):
            self.addRecipes(name, newdata)
        else:
            return "recipes not found"
    def getRecipy(self, name):
        if name in self.recipe_dict:
            return {name : self.recipe_dict.get(name)}
        else:
            return "recipe not found"
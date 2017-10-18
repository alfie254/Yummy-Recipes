import unittest

from app.users import User
from app.categories import Categories
from app.recipes import Recipes

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user_data = {
            "user@email":"passwordofuser"
        }

    def testusercreation(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

    def testdublicateuseraddition(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

        self.assertEqual("Dublicate user", self.user.addUser(self.user_data))
    def testmultipleusercreation(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

        self.user.addUser({"new@email.com": "newpassword"})
        self.assertEqual(2, len(self.user.getUsers()))
    def testgetsingleuser(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

        self.assertIn("user@email", self.user.getUser("user@email"))

    def testdeleteuser(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

        self.user.addUser({"new@email.com": "newpassword"})
        self.assertEqual(2, len(self.user.getUsers()))

        self.user.deleteUser("new@email.com")
        self.assertEqual(1, len(self.user.getUsers()))
    def testupdateuser(self):
        self.user.addUser(self.user_data)
        self.assertEqual(1, len(self.user.getUsers()))

        new_data = {
            "another@email.com":"123456"
        }
        self.user.updateUser("user@email", new_data)
        self.assertIn("another@email.com", self.user.getUser("another@email.com"))

class CategoriesTest(unittest.TestCase):
    def setUp(self):
        self.categories = Categories()
        self.cat_data = {
            "pic":"/cat1.png",
            "description":"my pavi recipies"
        }
    def testcartegoryadd(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))
    def testcategorydublicate(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))

        self.assertEqual("Dublicate category", 
                         self.categories.addCategories("testcart", self.cat_data))
    def testmultiplecategoriescreation(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))

        self.categories.addCategories("new cart", self.cat_data)
        self.assertEqual(2, len(self.categories.getCategories()))
    def testdeletecategories(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))

        self.categories.addCategories("new cart", self.cat_data)
        self.assertEqual(2, len(self.categories.getCategories()))

        self.categories.deleteCategory("testcart")
        self.assertEqual(1, len(self.categories.getCategories()))
    def testgetsinglecategory(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))

        self.assertIn("testcart", self.categories.getCategory("testcart"))
    def testupdatecategory(self):
        self.categories.addCategories("testcart", self.cat_data)
        self.assertEqual(1, len(self.categories.getCategories()))

        new_data = {
            "pic":"/cat33.png",
            "description":"my home recipies"
        }
        self.categories.updateCategory("testcart", new_data)
        self.assertIn("/cat33.png", self.categories.getCategory("testcart").get("testcart").get("pic"))

class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipes()
        self.recipe_data = {
            "ingredients":["one", "two", "three"],
            "procedure":["one", "two", "three"],
            "pic":"/recipe1.png"
        }
    def testrecipeadd(self):
        self.recipe.addRecipes("testrecipe", self.recipe_data)
        self.assertEqual(1, len(self.recipe.getRecipes()))
    def testrecipedublicate(self):
        self.recipe.addRecipes("testrecipe", self.recipe_data)
        self.assertEqual(1, len(self.recipe.getRecipes()))

        self.assertEqual("Dublicate recipe", 
                         self.recipe.addRecipes("testrecipe", self.recipe_data))
    def testmultiplerecipecreation(self):
        self.recipe.addRecipes("testrecipe", self.recipe_data)
        self.assertEqual(1, len(self.recipe.getRecipes()))

        self.recipe.addRecipes("new testrecipe", self.recipe_data)
        self.assertEqual(2, len(self.recipe.getRecipes()))
    def testdeleterecipe(self):
        self.recipe.addRecipes("testrecipe", self.recipe_data)
        self.assertEqual(1, len(self.recipe.getRecipes()))

        self.recipe.addRecipes("new testrecipe", self.recipe_data)
        self.assertEqual(2, len(self.recipe.getRecipes()))

        self.recipe.deleteRecipe("testrecipe")
        self.assertEqual(1, len(self.recipe.getRecipes()))
    def testgetsinglerecipe(self):
        self.recipe.addRecipes("testrecipe", self.recipe)
        self.assertEqual(1, len(self.recipe.getRecipes()))

        self.assertIn("testrecipe", self.recipe.getRecipy("testrecipe"))
    def testupdatecategory(self):
        self.recipe.addRecipes("testrecipe", self.recipe)
        self.assertEqual(1, len(self.recipe.getRecipes()))

        new_data = {
            "ingredients":["one1", "two1", "three1"],
            "procedure":["one1", "two1", "three1"],
            "pic":"/recipe12.png"
        }

        self.recipe.updateRecipe("testrecipe", new_data)
        self.assertIn("/recipe12.png", self.recipe.getRecipy("testrecipe").get("testrecipe").get("pic"))
import random

from data import DataClass as data

class DBSimulator:
    def __init__(self):
        self.apps = data.apps
        self.users = data.users
        self.purchases = data.purchases
        self.products = data.products
        self.discounts = data.discounts

    def get_app_by_name(self, app_name):
        """
        :param app_name: Name of the app
        :return: Dict app's representation
        """
        app = [app for app in self.apps if app['name'] == app_name][0]

        return app

    def get_user(self, user_id):
        """
        :param user_id: User id
        :return: Dict user's representation
        """
        breno = [user for user in self.users if user['id'] == user_id][0]

        return breno

    def get_purchases_by_user(self, user_id):
        """
        Method used to fetch all the user's purchases

        :param user_id: User id
        :return: List of user's purchases
        """
        purchases = [purchase for purchase in self.purchases if purchase['user_id'] == user_id]

        return purchases

    def get_product_by_app_id(self, app_id, product_name):
        """
        Method used to fetch a product from app id and product name

        :param app_id: Id of the app
        :param product_name: Name of the product
        :return: Dict product's representation
        """
        product = [product for product in self.products if product['app_id'] == app_id if product['name'] == product_name][0]

        return product

    def get_discount_exponent(self, purchases):
        """
        Method used to fetch a product from app id and product name

        :param purchases: Number of user's purchases
        :return: Dict product's representation
        """
        discount = [discount for discount in self.discounts if discount['purchases'] == purchases][0]

        return discount

    def save_purchase(self, user):
        """
        Method to save the purchase

        :param user: User object
        :return: status_code
        """
        purchase_data = {
            'id': random.randint(1, 1000),
            'user_id': user['id']
        }
        self.purchases.append(purchase_data)

        return 200

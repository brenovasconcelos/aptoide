from data import data

class DBSimulator:
    def __init__(self):
        self.apps = data.apps
        self.users = data.users
        self.purchases = data.purchases
        self.products = data.products

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
        user = [user for user in self.users if user['id'] == user_id][0]

        return user

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

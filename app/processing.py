
class ProcessPurchase:
    def __init__(self, db):
        self.db = db

    def process_purchase(self, app, product, user_id):
        """
        This method executes all method required to do a purchase

        :param app: App name
        :param product: Product name
        :param user_id:
        :return:
        """
        user = self.db.get_user(user_id=user_id)

        # Maybe use a "metadata" to centralize the information
        app = self.db.get_app_by_name(app)

        product = self.db.get_product_by_app_id(app_id=app['id'], product_name=product)

        purchases = self.db.get_purchases_by_user(user['id'])

        discount = self.db.get_discount_exponent(len(purchases))

        price_discounted = self.get_price(product['price'], discount['discount_amount'])

        self.db.save_purchase(user)
        ret = f"PURCHASE TRANSACTION => id: 1; app: {app['name']}; " \
              f"item: {product['name']}; " \
              f"amount: €{product['price']}; " \
              f"sender: {user['id']}; " \
              f"receivers: {app['id']}: €{price_discounted * 0.75}; AptoideStore#1: €{price_discounted * 0.25}"

        return ret

    def get_price(self, product_price, discount):
        """
        Method to calc the price discounted

        :param product_price: Product price
        :param discount: Discount exponent
        :return:
        """
        price = product_price - (discount * product_price)

        return price


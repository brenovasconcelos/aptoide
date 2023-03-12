
class ProcessPurchase:
    def __init__(self, db):
        self.db = db

    def process_purchase(self, app, product, user_id):

        user = self.db.get_user(user_id)

        product = self.db.get_product_by_app_id(app_id=app, product_name=product)

        discount = self.get_discount(user, product)

        return 0

    def get_price(self, user, product):
        purchases = self.db.get_purchases(user['id'])

        if not purchases:
            return product['price']

        purchases = len(purchases)
        if purchases >= 1 and purchases < 10:
            discount = 0.05
        elif purchases >= 10:
            discount = 0.10

        price = product['price'] - (discount * product['price'])

        return price

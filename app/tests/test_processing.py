import pytest
from app.db_simulator import DBSimulator
from app.processing import ProcessPurchase

class TestProcessing:

    def setup_class(self):
        self.processing = ProcessPurchase(db=DBSimulator())

    def test_double_purchase(self):
        user_id = 'User#123'
        ret1 = self.processing.process_purchase(app='TrivialDrive', product='Oil', user_id=user_id)
        ret2 = self.processing.process_purchase(app='TrivialDrive', product='Oil', user_id=user_id)

        assert ret1
        assert ret2

    def test_get_price(self):
        self.processing.get_price(product_price=10, discount=1)
import pytest
from app.db_simulator import DBSimulator

class TestDBSimulator:

    def setup_class(self):
        self.db_simulator = DBSimulator()

    def test_simulator_get_app(self):
        app_name = 'TrivialDrive'
        ret = self.db_simulator.get_app_by_name(app_name=app_name)
        assert ret['name'] == app_name

    def test_simulator_get_user(self):
        user_id = 'User#123'
        ret = self.db_simulator.get_user(user_id=user_id)
        assert ret['id'] == user_id

    def test_simulator_get_purchases(self):
        user_id = 'User#123'
        ret = self.db_simulator.get_purchases_by_user(user_id=user_id)
        assert len(ret) == 1

    def test_simulator_get_product(self):
        product_name = 'Oil'
        ret = self.db_simulator.get_product_by_app_id(app_id=1, product_name='Oil')
        assert ret['name'] == product_name


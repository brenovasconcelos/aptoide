import pytest
from app.db_simulator import DBSimulator
from app.processing import ProcessPurchase

class TestProcessing:

    def setup_class(self):
        self.processing = ProcessPurchase(db=DBSimulator())

    def test_simple_purchase(self):
        self.processing.process_purchase(app='TrivialDrive', product='Oil', user_id='User#1')

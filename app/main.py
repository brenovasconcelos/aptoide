from db_simulator import DBSimulator
from processing import ProcessPurchase

if '__main__':
    processor = ProcessPurchase(db=DBSimulator())
    user_id = 'User#123'
    print(processor.process_purchase(app='TrivialDrive', product='Oil', user_id=user_id))
    print(processor.process_purchase(app='TrivialDrive', product='Antifreeze', user_id=user_id))

"""
For this app, I chose to use a JSON to simulate a
NoSQL database instead of using a mocked DB
"""
class DataClass:
    developer_id1 = 'TrivialDriveDeveloper#2'
    developer_id2 = 'DiamondLegendDeveloper#3'
    developer_id3 = 'AptoideStore#1'
    developers = [
        {
            'id': developer_id1,
            'amount': 10,
        },
        {
            'id': developer_id2,
            'amount': 10,
        },
        {
            'id': developer_id3,
            'amount': 10,
        },
    ]

    app_id1 = 1
    app_id2= 2
    apps = [
        {
            'id': app_id1,
            'developer_id': developer_id1,
            'name': 'TrivialDrive',
        },
        {
            'id': app_id2,
            'developer_id': developer_id2,
            'name': 'DiamondLegend',
        }
    ]

    user_id1 = 'User#123'
    users = [
        {
            'id': user_id1,
            'name': 'User123',
            'amount': 10,
        },
    ]

    products = [
        {
            'id': 1,
            'name': 'Oil',
            'price': 1,
            'app_id': app_id1
        },
        {
            'id': 2,
            'name': 'Antifreeze',
            'price': 1.20,
            'app_id': app_id1
        },
        {
            'id': 3,
            'name': '5x_Diamonds',
            'price': 2,
            'app_id': app_id2
        },
        {
            'id': 4,
            'name': '10x_Diamonds',
            'price': 3,
            'app_id': app_id2
        },
    ]

    # This should have product_id as well
    purchases = []

    discounts = [
        {
            'id': 1,
            'purchases': 0,
            'discount_amount': 0.00
        },
        {
            'id': 2,
            'purchases': 1,
            'discount_amount': 0.05
        },
        {
            'id': 10,
            'purchases': 10,
            'discount_amount': 0.10
        }
    ]

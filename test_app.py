from app import currency_conversion


def test_change():
    assert [{'Euro': 3.128 , 'Won': 4190.6359999999995}] == currency_conversion(3.4)
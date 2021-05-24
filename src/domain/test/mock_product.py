from faker import Faker

from src.domain.models import Product

faker = Faker()


def mock_product() -> Product:
    return Product(
        ean=faker.ean13(),
        category=faker.name(),
        name=faker.name(),
        price=faker.numerify(text='###.##'),
        quantity=faker.random_number(digits=4),
        real_price=faker.numerify(text='###.##'),
        store_id=faker.random_number(digits=9),
        sale_type=faker.lexify(text="?"),
        unit_type=faker.lexify(text="???"),
        typestore=faker.lexify(text="????????????????????????"),
        typestorename=faker.name(),
    )

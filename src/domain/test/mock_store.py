from faker import Faker
from src.domain.models import Store

faker = Faker()


def mock_store() -> Store:
    return Store(
        id=faker.random_number(digits=10),
        name=faker.name(),
        typestore=faker.lexify(text="????????????????"),
        typestorename=faker.name()
    )

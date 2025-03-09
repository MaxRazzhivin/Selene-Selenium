import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year: str
    month: str
    day: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Max', last_name='Razzhivin', email='max.nvo06@gmail.com',
            gender='Male', phone_number='9094618666', year='1989', month='April', day='06',
            subject='Computer Science',
            hobby='Sports', picture='picta.png', address='somewhere in galaxy', state='NCR',
            city='Delhi')
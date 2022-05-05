from app.models import Listing, db

def seed_listings():
    l1 = Listing(
        address='8632 Beacon Ave.', city='New York', state='NY', country='USA address', price=120.00
    )
    l2 = Listing(
        address='30 Ivy St.', city='New York', state='NY', country='USA address', price=12.00
    )
    l3 = Listing(
        address='64 Charles Dr.', city='New York', state='NY', country='USA address', price=222.00
    )
    l4 = Listing(
        address='8626 W. Cleveland Court', city='New York', state='NY', country='USA address', price=20.00
    )
    l5 = Listing(
        address='34 High Noon Court', city='New York', state='NY', country='USA address', price=320.00
    )
    l6 = Listing(
        address='91 Birch Hill Ave.', city='New York', state='NY', country='USA address', price=470.00
    )
    l7 = Listing(
        address='1 Ely Park Blvd', city='New York', state='NY', country='USA address', price=500.00
    )
    l8 = Listing(
        address='25 Robinson St', city='New York', state='NY', country='USA address', price=1200.00
    )
    l9 = Listing(
        address='244 Ballyhack Rd', city='New York', state='NY', country='USA address', price=80.00
    )
    l10 = Listing(
        address='434 State 369 Rte', city='New York', state='NY', country='USA address', price=720.00
    )

    db.session.add(l1)
    db.session.add(l2)
    db.session.add(l3)
    db.session.add(l4)
    db.session.add(l5)
    db.session.add(l6)
    db.session.add(l7)
    db.session.add(l8)
    db.session.add(l9)
    db.session.add(l10)

    db.session.commit()


def undo_listings():
    db.session.execute('TRUNCATE listings RESTART IDENTITY CASCADE;')
    db.session.commit()

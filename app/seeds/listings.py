from app.models import Listing, db


def seed_listings():
    l1 = Listing(
        address='8632 Beacon Ave.', city='New York', state='NY', country='USA address', price=120.00, lat=40.776676, lng=-73.971321
    )
    l2 = Listing(
        address='30 Ivy St.', city='New York', state='NY', country='USA address', price=12.00, lat=40.816357, lng=-73.962898
    )
    l3 = Listing(
        address='64 Charles Dr.', city='New York', state='NY', country='USA address', price=222.00, lat=40.650002, lng=-73.949997
    )
    l4 = Listing(
        address='8626 W. Cleveland Court', city='New York', state='NY', country='USA address', price=20.00, lat=40.750298, lng=-73.993324
    )
    l5 = Listing(
        address='34 High Noon Court', city='New York', state='NY', country='USA address', price=320.00, lat=40.689247, lng=-74.044502
    )
    l6 = Listing(
        address='91 Birch Hill Ave.', city='New York', state='NY', country='USA address', price=470.00, lat=40.748817, lng=-73.985428
    )
    l7 = Listing(
        address='1 Ely Park Blvd', city='New York', state='NY', country='USA address', price=500.00, lat=40.706001, lng=-73.997002
    )
    l8 = Listing(
        address='25 Robinson St', city='New York', state='NY', country='USA address', price=1200.00, lat= 40.729675, lng=-73.996925
    )
    l9 = Listing(
        address='244 Ballyhack Rd', city='New York', state='NY', country='USA address', price=80.00, lat=40.758896, lng=-73.985130
    )
    l10 = Listing(
        address='434 State 369 Rte', city='New York', state='NY', country='USA address', price=720.00, lat=40.837048, lng=-73.865433
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

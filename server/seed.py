from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Bar, Review, User

fake = Faker()


def clear_database():
    with app.app_context():
        Bar.query.delete()
        User.query.delete()
        Review.query.delete()
        db.session.commit()


def create_bars():
    with app.app_context():
        bars = []
        for _ in range(10):
         b = Bar(
            name=fake.sentence(),
        )
        bars.append(b)

    return bars


def create_users():
    users = []
    for _ in range(5):
        u = User(
            name=fake.name(),
            age=rc(range(21, 99))
        )
        users.append(u)

    return users


def create_reviews(bars, users):
    reviews = []
    for _ in range(20):
        r = Review(
            time=rc(range(24)),
            user_id=rc([user.id for user in users]),
            bar_id=rc([bar.id for bar in bars]),
            rating=randint(1, 5)
        )
        reviews.append(r)

    return reviews


if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Bar.query.delete()
        Review.query.delete()
        User.query.delete()

        print("Seeding bars...")
        bars = create_bars()
        db.session.add_all(bars)
        db.session.commit()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding reviews...")
        reviews = create_reviews(bars, users)
        db.session.add_all(reviews)
        db.session.commit()

        print("Done seeding!")
from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Review, User

fake = Faker()


def clear_database():
    with app.app_context():
        Restaurant.query.delete()
        User.query.delete()
        Review.query.delete()
        db.session.commit()


def create_restaurants():
    with app.app_context():
        restaurants = []
        for _ in range(10):
         b = Restaurant(
            name=fake.sentence(),
        )
        restaurants.append(b)

    return restaurants


def create_users():
    users = []
    for _ in range(5):
        u = User(
            name=fake.name(),
            email= fake.email(),
            username= fake.user_name(),

        )
        u.password_hash = fake.password()
        users.append(u)

    return users


def create_reviews(restaurants, users):
    reviews = []
    for _ in range(20):
        r = Review(
            user_id=rc([user.id for user in users]),
            restaurant_id=rc([restaurant.id for restaurant in restaurants]),
            rating=randint(1, 5)
        )
        reviews.append(r)

    return reviews


if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Restaurant.query.delete()
        Review.query.delete()
        User.query.delete()

        print("Seeding restaurants...")
        restaurants = create_restaurants()
        db.session.add_all(restaurants)
        db.session.commit()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding reviews...")
        reviews = create_reviews(restaurants, users)
        db.session.add_all(reviews)
        db.session.commit()

        print("Done seeding!")
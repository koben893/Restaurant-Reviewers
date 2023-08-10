from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Rating, User

fake = Faker()


def clear_database():
    with app.app_context():
        Restaurant.query.delete()
        User.query.delete()
        Rating.query.delete()
        db.session.commit()


def create_restaurants():
    with app.app_context():
        R1= Restaurant(name = 'Als Burger Joint')
        R2= Restaurant(name = 'Connies Drive Through')
        R3= Restaurant(name = 'Hole in the Wall')
        R4= Restaurant(name = 'Bella Sera')
        R5= Restaurant(name = 'Mario and Luigi')
        R6= Restaurant(name = 'Mamma Mias')
        R7= Restaurant(name = 'Jeffs Pancake House')
        R8= Restaurant(name = 'MCdonalds Waffles')
        R9= Restaurant(name = 'The V Cafe')
        R10= Restaurant(name = 'Bobs Gator Shack')

        allrestaurants = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]


        return allrestaurants


def create_users():
    users = []
    for _ in range(20):
        u = User(
            name=fake.name(),
            email= fake.email(),
            username= fake.user_name(),

        )
        u.password_hash = fake.password()
        users.append(u)

    return users


def create_ratings(restaurants, users):
    ratings = []
    for _ in range(20):
        r = Rating(
            user_id=rc([user.id for user in users]),
            restaurant_id=rc([restaurant.id for restaurant in restaurants]),
            rating=randint(1, 5)
        )
        ratings.append(r)

    return ratings


if __name__ == '__main__':

    with app.app_context():
        print("Clearing db...")
        Restaurant.query.delete()
        Rating.query.delete()
        User.query.delete()

        print("Seeding restaurants...")
        restaurants = create_restaurants()
        db.session.add_all(restaurants)
        db.session.commit()

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        print("Seeding ratings...")
        ratings = create_ratings(restaurants, users)
        db.session.add_all(ratings)
        db.session.commit()

        print("Done seeding!")
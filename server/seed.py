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
    reviews = []
    for _ in range(20):
        r = Review(
            user_id=rc([user.id for user in users]),
            restaurant_id=rc([restaurant.id for restaurant in restaurants]),
            rating=randint(1, 5)
        )
        reviews.append(r)

    return reviews

def reviews ():
    with app.app_context():
        V1 = Review(name = 'Best burger I ever had!')
        V2 = Review(name = 'An italian masterpiece in every bite; Bella Sara`s commitment to genuine flavors earns top marks.')
        V3 = Review(name = 'Nostalgic and fun. Mario and Luigi brings a playful twist to Italian cuisine, though flavors could be bolder.')
        V4 = Review(name = 'Cozy spot with surprising culinary gems. The name says it all,  don`t judge this restaurant by its appearance.')
        V5 = Review(name = 'A mixed experience at Hole in the Wall. Some dishes were hits, others misses. A unique dining adventure nonetheless.')
        V6 = Review(name = 'Flavors that remind you of Nonna`s kitchen. Bella Sera`s charm lies in its rustic simplicity.')
        V7 = Review(name = 'A must-visit for gamers and foodies alike. Mario and Luigi marry two worlds seamlessly.')
        V8 = Review(name = 'Eclectic menu, cozy atmosphere. Hole in the Wall is a gastronomic journey you won`t forget.')
        V9 = Review(name = 'Subpar at best.')
        V10 = Review(name = 'A haven for coffee aficionados. The V Cafe`s brews are masterfully crafted, and the atmosphere is inviting.')
        V11 = Review(name = 'A hidden gem for Italian cuisine lovers. Mamma Mia`s is a delightful escape from the ordinary')
        V12 = Review(name = 'Underwhelmed by the taste, but the atmosphere was cozy and inviting. Maybe better for drinks than a full dining experience.')
        V13 = Review(name = 'Budget-friendly waffle fix. McDonald`s Waffles gets the job done without breaking the bank.')
        V14 = Review(name = 'Pleasantly surprised by the presentation and flavors. However, the service was a bit slow and detracted from the overall experience.')
        V15 = Review(name = 'Creative theme, hit-or-miss taste. Mario and Luigi`s execution varies, but the experience is enjoyable.')
        V16 = Review(name = 'Quick and convenient meals at Connie`s Drive Through. A go-to spot for fast comfort food.')
        V17 = Review(name = 'Stale food. Was not worth the 50 min drive.')
        V18 = Review(name = 'The V Cafe`s commitment to quality is evident in every sip. A coffee lover`s paradise.')
        V19 = Review(name = 'Bellissimo! Bella Sera`s menu is a symphony of Italian taste, prepared with passion and skill.')
        V20 = Review(name = 'Breakfast paradise at Jeff`s Pancake House. The pancakes are fluffy perfection, and the variety is impressive.')
        V21 = Review(name = 'A seafood lover`s dream come true. Bob`s Gator Shack is a culinary gem by the water.')
        V22 = Review(name = 'McDonald`s Waffles surprised me with their taste. An enjoyable treat when you`re on the go.')
        V23 = Review(name = 'Flavors at Mamma Mia`s were underwhelming. The ambiance is pleasant, but the taste could use refinement.')
        V24 = Review(name = 'Gulf-inspired dishes that transport you to the coast. Bob`s Gator Shack`s flavors are on point.')
        V25 = Review(name = 'Reliable fast-food fare at Connie`s Drive Through. Quick service and no surprises.')
        V26 = Review(name = 'The V Cafe sets the bar high for coffee excellence. A destination for true coffee connoisseurs.')
        V27 = Review(name = 'A pancake haven worth visiting. Jeff`s Pancake House`s dedication to quality shines through.')
        V28 = Review(name = 'A mixed bag of flavors. Some dishes were a delight, while others left me questioning the choices.')
        V29 = Review(name = 'Amusing atmosphere, moderate taste. Mario and Luigi rely on their theme to stand out.')
        V30 = Review(name = 'A decent experience overall. The ambiance was lovely, but the taste didn`t match the high expectations set by the decor.')

        allreviews = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30]
        return allreviews




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
        reviews = create_ratings(restaurants, users)
        db.session.add_all(reviews)
        db.session.commit()

        print("Done seeding!")
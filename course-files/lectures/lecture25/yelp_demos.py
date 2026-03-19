from apis import yelp

businesses = yelp.get_businesses("Evanston, IL")

counter = 0
for business in businesses:
    print(counter, business)
    print("*"*10)

a_business = businesses[0]

print(a_business['name'], a_business['id'])

reviews = yelp.get_reviews(a_business['id'])

nice_table = yelp.generate_business_table(a_business, reviews)

print(nice_table)

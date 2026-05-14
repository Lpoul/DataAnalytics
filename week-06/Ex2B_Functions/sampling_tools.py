import random
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
            'SurgeProtector']

product_of_the_day = random.choice(products)

print(f"{product_of_the_day} is the Product for today!!")

sample_products = random.sample(products, k=3)

print(sample_products)
random.shuffle(products)
print(products)

transaction_data = random.randint(50,300)
random_num = random.randint(1,1000)
profit = transaction_data * random_num
print(f"We sold {random_num} {product_of_the_day}'s for ${transaction_data:,} and made ${float(profit):,}")
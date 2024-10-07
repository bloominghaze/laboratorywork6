def find_products_not_in_stores(all_products, store_products_list):
    all_store_products = set()

    for store_products in store_products_list:
        all_store_products.update(store_products)

    products_not_in_stores = all_products - all_store_products

    return products_not_in_stores

def input_products():
    products = input("Введіть продукти, розділені комами: ").split(',')
    return {product.strip() for product in products}

def input_stores_products(m):
    stores_products = []
    for i in range(m):
        store_products = input(f"Введіть асортимент товарів для магазину {i + 1} (розділені комами): ").split(',')
        stores_products.append({product.strip() for product in store_products})
    return stores_products


if __name__ == "__main__":
    all_products = input_products()

    while True:
        try:
            m = int(input("Введіть кількість магазинів: "))
            if m <= 0:
                print("Кількість магазинів має бути додатним числом. Спробуйте ще раз.")
            else:
                break
        except ValueError:
            print("Помилка! Введіть ціле число.")

    store_products_list = input_stores_products(m)

    products_not_in_stores = find_products_not_in_stores(all_products, store_products_list)

    result_list = list(products_not_in_stores)

    if result_list:
        print("Продукти, яких немає в жодному магазині:", result_list)
    else:
        print("Всі продукти є в магазинах.")

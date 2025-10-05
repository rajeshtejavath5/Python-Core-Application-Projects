import os
class Auth:
    def __init__(self):
        self.user_file = "users.txt"

    def register(self, username, password, is_admin):
        if not os.path.exists(self.user_file):
            open(self.user_file, "w").close()

        with open(self.user_file, "r") as f:
            users = f.readlines()

        for u in users:
            u = u.strip().split(",")
            if username == u[0]:
                print("❌ User already exists!")
                return

        with open(self.user_file, "a") as f:
            f.write(f"{username},{password},{is_admin}\n")
        print("✅ Registered successfully!")

    def login(self, username, password):
        if not os.path.exists(self.user_file):
            print("No users registered yet!")
            return None

        with open(self.user_file, "r") as f:
            users = f.readlines()

        for u in users:
            u = u.strip().split(",")
            if username == u[0] and password == u[1]:
                return "admin" if u[2] == "yes" else "user"

        print("❌ Invalid credentials")
        return None

    def run(self):
        while True:
            print("\n--- Authentication ---")
            print("1) Register")
            print("2) Login")
            print("3) Exit")
            choice = input("Choose option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                is_admin = input("Admin? (yes/no): ")
                self.register(username, password, is_admin)

            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                role = self.login(username, password)
                if role == "admin":
                    AdminAccess(username).run()
                elif role == "user":
                    UserAccess(username).run()

            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid option")


class ProductManager:
    product_file = "products.txt"

    @classmethod
    def load_products(cls):
        if not os.path.exists(cls.product_file):
            open(cls.product_file, "w").close()
        with open(cls.product_file, "r") as f:
            return [line.strip().split(",") for line in f if line.strip()]

    @classmethod
    def save_products(cls, products):
        with open(cls.product_file, "w") as f:
            for p in products:
                f.write(",".join(p) + "\n")

    @classmethod
    def view_products(cls):
        products = cls.load_products()
        if not products:
            print("No products available!")
            return
        print("\nID   Name        Price   Stock")
        print("--------------------------------")
        for p in products:
            stock = "Out of Stock" if int(p[3]) == 0 else p[3]
            print(f"{p[0]}   {p[1]}   {p[2]}   {stock}")


class AdminAccess:
    def __init__(self, username):
        self.username = username

    def add_product(self):
        products = ProductManager.load_products()
        product_id = str(len(products) + 1)
        name = input("Product Name: ")
        price = input("Price: ")
        qty = input("Quantity: ")
        products.append([product_id, name, price, qty])
        ProductManager.save_products(products)
        print("✅ Product added!")

    def remove_product(self):
        pid = input("Enter Product ID to remove: ")
        products = ProductManager.load_products()
        new_products = [p for p in products if p[0] != pid]
        if len(new_products) == len(products):
            print("❌ Product not found")
        else:
            ProductManager.save_products(new_products)
            print("✅ Product removed")

    def update_product(self):
        pid = input("Enter Product ID to update: ")
        products = ProductManager.load_products()
        updated = False
        for p in products:
            if p[0] == pid:
                p[1] = input("New Name: ")
                p[2] = input("New Price: ")
                p[3] = input("New Quantity: ")
                updated = True
        if updated:
            ProductManager.save_products(products)
            print("✅ Product updated")
        else:
            print("❌ Product not found")

    def view_orders(self):
        if not os.path.exists("orders.txt"):
            print("No orders yet!")
            return
        with open("orders.txt", "r") as f:
            orders = f.readlines()
        print("\nOrderID  User   ProductID  Qty  Status")
        print("---------------------------------------")
        for o in orders:
            print(o.strip())

    def update_order_status(self):
        oid = input("Enter Order ID to update: ")
        if not os.path.exists("orders.txt"):
            print("No orders yet!")
            return
        with open("orders.txt", "r") as f:
            orders = [line.strip().split(",") for line in f if line.strip()]
        updated = False
        for o in orders:
            if o[0] == oid:
                o[4] = input("New Status (Pending/Shipped/Delivered/Cancelled): ")
                updated = True
        if updated:
            with open("orders.txt", "w") as f:
                for o in orders:
                    f.write(",".join(o) + "\n")
            print("✅ Order status updated")
        else:
            print("❌ Order not found")

    def run(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1) View Products")
            print("2) Add Product")
            print("3) Remove Product")
            print("4) Update Product")
            print("5) View Orders")
            print("6) Update Order Status")
            print("7) Logout")
            choice = input("Choose option: ")

            if choice == "1":
                ProductManager.view_products()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.update_product()
            elif choice == "5":
                self.view_orders()
            elif choice == "6":
                self.update_order_status()
            elif choice == "7":
                break
            else:
                print("❌ Invalid option")


class UserAccess:
    def __init__(self, username):
        self.username = username
        self.cart_file = f"cart_{username}.txt"

    def add_to_cart(self):
        pid = input("Enter Product ID to add: ")
        qty = int(input("Quantity: "))
        products = ProductManager.load_products()
        for p in products:
            if p[0] == pid:
                if int(p[3]) >= qty:
                    with open(self.cart_file, "a") as f:
                        f.write(f"{pid},{qty}\n")
                    print("✅ Added to cart")
                else:
                    print("❌ Not enough stock")
                return
        print("❌ Product not found")

    def view_cart(self):
        if not os.path.exists(self.cart_file):
            print("Cart is empty!")
            return []
        with open(self.cart_file, "r") as f:
            cart = [line.strip().split(",") for line in f if line.strip()]
        print("\nYour Cart:")
        print("ProductID   Qty")
        print("----------------")
        for c in cart:
            print(f"{c[0]}         {c[1]}")
        return cart

    def checkout(self):
        cart = self.view_cart()
        if not cart:
            return

        products = ProductManager.load_products()
        orders = []
        oid_start = 1
        if os.path.exists("orders.txt"):
            with open("orders.txt", "r") as f:
                existing = [line.strip().split(",") for line in f if line.strip()]
                if existing:
                    oid_start = int(existing[-1][0]) + 1
                orders.extend(existing)

        for c in cart:
            pid, qty = c
            for p in products:
                if p[0] == pid:
                    if int(p[3]) >= int(qty):
                        p[3] = str(int(p[3]) - int(qty))
                        orders.append([str(oid_start), self.username, pid, qty, "Pending"])
                        oid_start += 1
                    else:
                        print(f"❌ Not enough stock for {p[1]}")

        ProductManager.save_products(products)
        with open("orders.txt", "w") as f:
            for o in orders:
                f.write(",".join(o) + "\n")

        open(self.cart_file, "w").close()
        print("✅ Order placed successfully!")

    def view_orders(self):
        if not os.path.exists("orders.txt"):
            print("No orders yet!")
            return
        with open("orders.txt", "r") as f:
            orders = [line.strip().split(",") for line in f if line.strip()]
        print("\nYour Orders:")
        for o in orders:
            if o[1] == self.username:
                print(f"OrderID: {o[0]}, ProductID: {o[2]}, Qty: {o[3]}, Status: {o[4]}")

    def run(self):
        while True:
            print("\n--- User Menu ---")
            print("1) View Products")
            print("2) Add to Cart")
            print("3) View Cart")
            print("4) Checkout")
            print("5) View Orders")
            print("6) Logout")
            choice = input("Choose option: ")

            if choice == "1":
                ProductManager.view_products()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                self.view_orders()
            elif choice == "6":
                break
            else:
                print("❌ Invalid option")


if __name__ == "__main__":
    Auth().run()

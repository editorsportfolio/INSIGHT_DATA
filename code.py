import sqlite3

DB = "insightops.db"

def connect():
    return sqlite3.connect(DB)


def initialize_db(conn):
    with open("schema.sql","r") as f:
        conn.executescript(f.read())
    conn.commit()
    print("Database initialized")


def total_revenue(conn):

    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(quantity * price)
    FROM sales
    """)

    result = cursor.fetchone()[0]
    print("\nTotal Revenue:", result)


def revenue_by_region(conn):

    cursor = conn.cursor()

    cursor.execute("""
    SELECT r.region_name,
           SUM(s.quantity * s.price) AS revenue
    FROM sales s
    JOIN regions r ON s.region_id = r.region_id
    GROUP BY r.region_name
    ORDER BY revenue DESC
    """)

    print("\nRevenue by Region")
    for row in cursor.fetchall():
        print(row[0], row[1])


def top_products(conn):

    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.product_name,
           SUM(s.quantity) as total_sales
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC
    """)

    print("\nTop Products")
    for row in cursor.fetchall():
        print(row[0], "Units:", row[1])


def category_performance(conn):

    cursor = conn.cursor()

    cursor.execute("""
    SELECT p.category,
           SUM(s.quantity * s.price) as revenue
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.category
    ORDER BY revenue DESC
    """)

    print("\nRevenue by Category")
    for row in cursor.fetchall():
        print(row[0], row[1])


def add_sale(conn):

    product = int(input("product_id: "))
    region = int(input("region_id: "))
    quantity = int(input("quantity: "))
    price = float(input("price: "))
    date = input("sale_date YYYY-MM-DD: ")

    conn.execute("""
    INSERT INTO sales(product_id,region_id,quantity,price,sale_date)
    VALUES (?,?,?,?,?)
    """,(product,region,quantity,price,date))

    conn.commit()
    print("Sale added")


def menu():

    conn = connect()

    while True:

        print("\n--- InsightOps Advanced ---")

        print("1 Initialize database")
        print("2 Total revenue")
        print("3 Revenue by region")
        print("4 Top products")
        print("5 Category analytics")
        print("6 Add new sale")
        print("7 Exit")

        choice = input("Choice: ")

        if choice == "1":
            initialize_db(conn)

        elif choice == "2":
            total_revenue(conn)

        elif choice == "3":
            revenue_by_region(conn)

        elif choice == "4":
            top_products(conn)

        elif choice == "5":
            category_performance(conn)

        elif choice == "6":
            add_sale(conn)

        elif choice == "7":
            break

        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    menu()
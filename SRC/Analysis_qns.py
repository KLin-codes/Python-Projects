import database
import matplotlib.pyplot as plt

def q1():
    # Question 1: Which towns have the highest average resale prices?
    query = """
        SELECT 
            town, 
            ROUND(AVG(resale_price),2) AS Average_Price
        FROM resale_transactions
        GROUP BY town
        ORDER BY AVG(resale_price) DESC
    """

    database.cursor.execute(query)          # Input the commands
    results = database.cursor.fetchall()    # Run the commands
    towns = [r[0] for r in results]
    Average_price = [r[1] for r in results]
    plt.bar(towns, Average_price)
    plt.xticks(rotation=90)
    plt.xlabel("Town")
    plt.ylabel("Average Resale Price")
    plt.title("Average HDB Resale Price by Town")
    plt.tight_layout()
    plt.show()


def q2():
    # Question 2: How does resale price vary across different flat types
    query = """
        SELECT 
            flat_type,
            MIN(resale_price),
            ROUND(AVG(resale_price)),
            MAX(resale_price)
        FROM resale_transactions
        GROUP BY flat_type
    """
    database.cursor.execute(query)
    results = database.cursor.fetchall()

    flat_type = [r[0] for r in results]
    minimum_price = [r[1] for r in results]
    average_price = [r[2] for r in results]
    maximum_price = [r[3] for r in results]

    x = range(len(flat_type))

    plt.bar(x, minimum_price, width=0.25, label="Minimum")
    plt.bar([i + 0.25 for i in x], average_price, width=0.25, label="Average")
    plt.bar([i + 0.5 for i in x], maximum_price, width=0.25, label="Maximum")

    plt.xticks([i + 0.25 for i in x], flat_type)
    plt.xlabel("Flat Type")
    plt.ylabel("Resale Price")
    plt.title("Resale Price by Flat Type")
    plt.legend()
    plt.tight_layout()
    plt.show()

def q3():
    # Question 3: DOes a larger floor area generally correspond to higher resale price?
    query = """
        SELECT
            floor_area_sqm,
            AVG(resale_price) AS Average_Price
        FROM resale_transactions
        GROUP BY floor_area_sqm
    """
    database.cursor.execute(query)
    results = database.cursor.fetchall()
    floor_area = [r[0] for r in results]
    Average_price = [r[1] for r in results]
    plt.scatter(floor_area, Average_price)
    plt.xlabel("Floor Area (sqm)")
    plt.ylabel("Average Resale Price")
    plt.title("Relationship between Floor Area and Average Resale Price")
    plt.show()

def q4():
    # Question 4: How have HDB resale prices changed over time?
    query = """
        SELECT 
            month,
            AVG(resale_price) AS Average_Price
        FROM resale_transactions
        GROUP BY month
    """
    database.cursor.execute(query)
    results = database.cursor.fetchall()
    month_and_time = [r[0] for r in results]
    month = []
    for m in month_and_time:
        months = m.split()
        month.append(months[0])

    Average_price = [r[1] for r in results]

    plt.figure(figsize=(14,7))
    plt.plot(month, Average_price)
    plt.xticks(rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Average Resale Price')
    plt.title('Average HDB Resale Price Over Time')
    plt.tight_layout()
    plt.show()

def q5():
    # Question 5: Which towns offer the best value based on resale price per square metre?
    query = """
        SELECT
            town,
            ROUND(AVG(resale_price / floor_area_sqm),2) AS Average_Price_Per_sqm
        FROM resale_transactions
        GROUP BY town
        ORDER BY AVG(resale_price / floor_area_sqm) ASC
    """
    database.cursor.execute(query)
    results = database.cursor.fetchall()
    towns = [r[0] for r in results]
    Avg_price_per_sqm = [r[1] for r in results]

    plt.figure(figsize=(14,7))
    plt.bar(towns, Avg_price_per_sqm)
    plt.xticks(rotation=90)
    plt.xlabel("Town")
    plt.ylabel("Average Price Per Sqm")
    plt.title("Average Price Per Sqm by Town")
    plt.tight_layout()
    plt.show()

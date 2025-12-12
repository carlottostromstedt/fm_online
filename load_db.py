import sqlite3


def find_card(id):
    try:
        sqliteConnection = sqlite3.connect("YFM.db")
        cursor = sqliteConnection.cursor()

        card = {}  # List to store dictionaries representing cards

        cursor.execute(
            f"SELECT CardID, CardName, CardType, Attack, Defense FROM Cards WHERE CardID='{id}'"
        )
        for row in cursor:
            card = {
                "CardID": str(row[0]),
                "CardName": row[1],
                "CardType": row[2],
                "Attack": row[3],
                "Defense": row[4],
            }
            print("CardID =", card["CardID"])
            print("CardName =", card["CardName"])
            print("CardType =", card["CardType"])
            print("Attack =", card["Attack"])
            print("Defense =", card["Defense"], "\n")

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return card


def find_card_by_name(name):
    try:
        sqliteConnection = sqlite3.connect("YFM.db")
        cursor = sqliteConnection.cursor()

        card = {}

        cursor.execute(
            "SELECT CardID, CardName, CardType, Attack, Defense "
            "FROM Cards WHERE CardName = ? COLLATE NOCASE",
            (name,),
        )

        for row in cursor:
            card = {
                "CardID": str(row[0]),
                "CardName": row[1],
                "CardType": row[2],
                "Attack": row[3],
                "Defense": row[4],
            }

            print("CardID =", card["CardID"])
            print("CardName =", card["CardName"])
            print("CardType =", card["CardType"])
            print("Attack =", card["Attack"])
            print("Defense =", card["Defense"], "\n")

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return card


def find_fusions(id1, id2):
    fusions = []
    try:
        sqliteConnection = sqlite3.connect("YFM.db")
        cursor = sqliteConnection.cursor()

        cursor.execute(
            "SELECT Material1, Material2, Result FROM Fusions WHERE Material1=? AND Material2=?",
            (id1, id2),
        )

        for row in cursor:
            # Convert ALL values to strings
            fusions.append([str(row[0]), str(row[1]), str(row[2])])

        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return fusions


def get_all_card_ids():
    card_ids = []
    try:
        sqliteConnection = sqlite3.connect("YFM.db")
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT CardID FROM Cards")

        rows = cursor.fetchall()
        card_ids = [str(row[0]) for row in rows]

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return card_ids


# def find_fusions2(id1, id2):
#     fusions = []
#     try:
#         sqliteConnection = sqlite3.connect("YFM.db")
#         cursor = sqliteConnection.cursor()
#
#         cursor.execute(
#             f"SELECT Material1, Material2, Result FROM Fusions WHERE Material1='{id1}' AND Material2='{id2}'"
#         )
#         for row in cursor:
#             fusions.append([row[0], row[1], row[2]])
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Error:", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#     return fusions

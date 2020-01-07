import csv

def typo(user_input_, answer_1, answer_2, answer_3, answer_4):
    """Safeguarding against invalid inputs. Ensures program won't shut down"""
    while user_input_ != answer_1 and user_input != answer_2 \
            and user_input != answer_3 and user_input != answer_4:
        user_input_ = input("Wie bitte?\n")
    return user_input


def income():
    """Adding all income to a month"""
    with open(r"C:\Users\s4115\PycharmProjects\EPR\EPR\EP\finanzen_files\income.txt", "r+") as file:
        file.seek(-1)
        file_money = int(file.read())
        file_money += int(input("Was willst du auf dein Konto laden?"))
        print(file_money)
        file.write(str(file_money))

        print(f"sie besitzen {file.read()}€")


def expenditure():  # not finished and full of holes..
    """Adding all expenditures to a month"""
    with open("test_.csv", "r+", newline="") as f_writer:
        with open("test_finance.py") as f:
            row_count = len(f.readlines())
        if row_count == 0:  # If file is empty than we treat it as brand new file.
            categories = ["datum", "pflege", "vergnügung", "nahrung",
                          "familie/geschenke", "gesammt"]
            # Case insensetiv for convinience
            writer = csv.DictWriter(f_writer, fieldnames=categories)

            writer.writeheader()
            # row is constructed as in  writer
            # meaning first is always "datum" than "pfelge" and so on
        else:  # else we will just append stuff to the already existing file
            with open("test_.csv", "a", newline="") as f_appender:
                date = input("Datum:\n")
                p_costs = 0
                v_costs = 3
                n_costs = 2
                fg_costs = 0
                sum_cost = p_costs + v_costs + n_costs + fg_costs
                # I don't know if i can give this way the values, but it's sufficint to let
                # everyone know what i want to do and for them to improve my approach.
                csv.DictWriter(f_appender)


def monthly():
    """re-occuring in/outcomes in a month"""
    """ideally the do it on their own, i just give them names and the costs"""


def next_month():
    """next month is being used for the money change"""
    months = ["Januar", "Februar", "März", "April", "May", "Juni", "Juli",
              "August", "September", "Oktober", "November", "Dezember"]
    number = open("months.txt", "w")
    number.write
    return months[number]


# ----------------------------------------------------------------------------


number = 0
DATE = input("Gib das Datum an\n")
user_input = input("Optionen die ich ändern kann:\n"
                   "Einnahmen (e)\n"
                   "Ausgaben (a)\n"
                   "Monatiliche Ein/Ausgaben (m)\n"
                   "Nächster Monat (n)\n")
# User input into one of those three things

user_input = typo(user_input, "a", "e", " m", "n")
if user_input == "e":
    income()
elif user_input == "a":
    expenditure()
elif user_input == "m":
    monthly()
elif user_input == "n":

    x = open("finance_file.txt", "r")
    y = int(x.read())
    y = y + 10
    x = open("finance_file.txt", "w+")
    x.write(str(y))
    x = open("finance_file.txt", "r")

#Accepting user inptus

ret_date,ret_mon,ret_year = input().split()
due_date,due_mon,due_year = input().split()

#print("Retured Dates",ret_date,ret_mon,ret_year)
#print("Due Dates",due_date,due_mon,due_year)

def calculateFine(ret_date, ret_mon, ret_year, due_date, due_mon, due_year):
    daily_fine = 15
    monthly_fine = 500
    yearly_fine = 10000


    # if int(ret_year) != int(due_year):
    #     if int(ret_year) < int(due_year):
    #         return 0
    # elif int(ret_year) == int(due_year):
    #     if int(ret_mon) != int(due_mon):
    #         if int(ret_mon) < int(due_mon):
    #             return 0
    #     elif int(ret_mon) == int(due_mon):
    #         if int(ret_date) < int(due_date) or (int(ret_date) == int(due_date)):
    #             return 0
    #         elif int(ret_date) > int(due_date):
    #             return monthly_fine * (int(ret_date) - int(due_date))
    #
    #     else:
    #         return monthly_fine * (int(ret_mon) - int(due_mon))
    # else:
    #     return yearly_fine

    # Accepting user inptus

    ret_date, ret_mon, ret_year = input().split()

    due_date, due_mon, due_year = input().split()

    # print("Retured Dates",ret_date,ret_mon,ret_year)

    # print("Due Dates",due_date,due_mon,due_year)

    def calculateFine(ret_date, ret_mon, ret_year, due_date, due_mon, due_year):

        daily_fine = 15

        monthly_fine = 500

        yearly_fine = 10000

        if int(ret_date) == int(due_date) and int(ret_mon) == int(due_mon) and int(ret_year) == int(due_year):

            return 0

        elif ret_date != due_date and ret_mon == due_mon and ret_year == due_year:

            if (int(ret_date) < int(due_date)):

                return 0

            else:

                return daily_fine * (int(ret_date) - int(due_date))

        elif ret_mon != due_mon and ret_year == due_year:

            if (int(ret_mon) < int(due_mon)):

                return 0

            else:

                return monthly_fine * (int(ret_mon) - int(due_mon))

        elif ret_year != due_year:

            if (int(ret_year) < int(due_year)):

                return 0

            else:

                return yearly_fine

    fine = calculateFine(ret_date, ret_mon, ret_year, due_date, due_mon, due_year)

    print(fine)


fine = calculateFine(ret_date,ret_mon,ret_year,due_date,due_mon,due_year)
print(fine)
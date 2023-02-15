# import smtplib
#
# my_mail = "newacc01222023@gmail.com"
# receive_email = "newacc01222023@yahoo.com"
# password = "pobbfhlzozcaczmz"
#
# """connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="newacc01222023@yahoo.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()"""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="newacc01222023@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2004, month=9, day=19, hour=9)
# print(date_of_birth)

import smtplib
import random
import datetime as dt

with open('quotes.txt') as quotes_text:
    quotes_list = quotes_text.readlines()
    quote_of_the_day = quotes_list[random.randint(0, len(quotes_list))]

today = dt.datetime.now().weekday()
print(today)
my_mail = "newacc01222023@gmail.com"
receive_email = "asalamatov@na.edu"
password = "pobbfhlzozcaczmz"

if today == 0:    # 0 = Monday
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=receive_email,
                            msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}")




















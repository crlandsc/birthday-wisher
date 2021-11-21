import datetime as dt
import pandas as pd
import smtplib
import random


# TODO 1. Update the birthdays.csv
# TODO 1a. Load birthday.csv with pandas
birthdays = pd.read_csv("birthdays.csv")


# TODO 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
current_bday = pd.DataFrame()

for index, current_bday in birthdays.iterrows():
    bday_day = current_bday["day"]
    bday_month = current_bday["month"]
    bday_name = current_bday["name"]
    # TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
    #  with the person's actual name from birthdays.csv
    if current_day == bday_day and current_month == bday_month:
        rand_letter_number = random.randint(1, 3)
        # TODO 3a. Load random letter
        with open(f"./letter_templates/letter_{rand_letter_number}.txt", "r") as letter_file:
            random_bday_letter = letter_file.readlines()  # convert to list of strings
            random_bday_letter[0] = random_bday_letter[0].replace("[NAME]", bday_name)  # Replace [Name] with actual name
            random_bday_letter_str = "".join(random_bday_letter)  # Convert to list to string to send in email
            # print(random_bday_letter_str)  # Test print of letter

        # TODO 4. Send the letter generated in step 3 to that person's email address.
        # Initializations of send/receive emails & sender password
        sender_email = "YOUR_EMAIL@gmail.com"  # Enter your email here
        recipient_email = current_bday["email"]  # Grab email from current selection
        sender_password = "YOUR_PASSWORD"  # Enter your email password here

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # address and port number
            connection.starttls()  # start security TLS protocol
            connection.login(user=sender_email, password=sender_password)  # Connect to email
            # Send mail
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birthday!!\n\n{random_bday_letter_str}"
            )

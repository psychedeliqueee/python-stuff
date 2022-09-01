age = input("What is your current age?")

age_int = int(age)

age_in_days = age_int * 365
age_in_weeks = age_int * 52
age_in_months = age_int * 12

days_until_90 = 90 * 365 - age_in_days
weeks_until_90 = 90 * 52 - age_in_weeks
months_until_90 = 90 * 12 - age_in_months

print(f"You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left.")
# Checking Multiple Conditions at the same time.

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False, because age_1 is not greater than or equal to 21.

age_1  = 22
print(age_0 >= 21 and age_1 >= 21)  # True, because both age_0 and age_1 are greater than or equal to 21.


# Using or, only one condition needs to be true for the whole expression to be true.
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)  # True,

age_0 = 18
print(age_0 >= 21 or age_1 >=21)  # False, because neither age_0 nor age_1 is greater than or equal to 21.

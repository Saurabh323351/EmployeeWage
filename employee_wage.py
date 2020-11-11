# welcome to employee_wage problem statement

import random
"""random.randint(0,1) Return random integer in range [a, b], including both end points.
"""
random_no = random.randint(0,2)
# is_present=True if random_no else False

# print(is_present,random_no)

employee_wage_details={
    "wage_per_hour":20,
    "full_day_hour":8,
    "half_day_hour":4
}

def get_working_hour(random_no):
    working_hour=employee_wage_details.get('full_day_hour') if random_no == 1 else employee_wage_details.get('half_day_hour') if random_no == 2 else 0
    return working_hour


compute_daily_wage = lambda wage_per_hour, working_hour: wage_per_hour * working_hour
# print(compute_daily_wage(employee_wage_details.get('wage_per_hour'), employee_wage_details.get('full_day_hour')))
print(compute_daily_wage(employee_wage_details.get('wage_per_hour'), get_working_hour(random_no)))
compute_daily_wage(employee_wage_details.get('wage_per_hour'), get_working_hour(random_no))

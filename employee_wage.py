# welcome to employee_wage problem statement

import random
"""random.randint(0,1) Return random integer in range [a, b], including both end points.
"""
random_no = random.randint(0,1)
is_present=True if random_no else False
print(is_present,random_no)

employee_wage_details={
    "wage_per_hour":20,
    "full_day_hour":8
}

compute_daily_wage = lambda wage_per_hour, full_day_hour: wage_per_hour * full_day_hour if is_present else 0
# print(compute_daily_wage(employee_wage_details.get('wage_per_hour'), employee_wage_details.get('full_day_hour')))
compute_daily_wage(employee_wage_details.get('wage_per_hour'), employee_wage_details.get('full_day_hour'))

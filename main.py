from datetime import date, timedelta

now_date = date.today()


def get_week_days(now_date):
    num_week = now_date.isoweekday() 
    week_start = now_date - timedelta(6 + num_week)
    week_end = now_date - timedelta(0 + num_week)
    print(week_start, '\n' , week_end, sep='')

get_week_days(now_date)

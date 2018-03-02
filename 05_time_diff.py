
def time_difference(year0,month0,day0, year1,month1,day1):
    import datetime
    date1 = datetime.datetime(year0,month0,day0)
    date2 = datetime.datetime(year1,month1,day1)
    return date1 - date2


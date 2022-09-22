import datetime
def convert(n):
    return str(datetime.timedelta(seconds=n))
print(convert(n=60))
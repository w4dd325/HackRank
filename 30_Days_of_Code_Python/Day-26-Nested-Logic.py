# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_day, returned_month, returned_year = [int(x) for x in input().split(' ')]
expected_day, expected_month, expected_year = [int(x) for x in input().split(' ')]

if (returned_year, returned_month, returned_day) <= (expected_year, expected_month, expected_day):
    print(0)
elif (returned_year, returned_month) == (expected_year, expected_month):
    # fine == 15 hakos x number of days late
    print(15 * (returned_day - expected_day))
elif returned_year == expected_year:
    # fine == 500 hackos number of months late
    print(500 * (returned_month - expected_month))
else:
    # fixed fine of 10000 hakos
    print(10000)

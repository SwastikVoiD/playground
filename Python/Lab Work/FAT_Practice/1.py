def gross(hrs,rate):
    pass
    da = 0.14
    hra = 0.10
    pf = 0.04
    basic = hrs * rate
    DA = da*basic
    HRA = hra * basic
    PF = pf * basic
    gross_pay = basic + DA + HRA - PF
    return gross_pay
hrs = float(input())
rate = float(input())
gp = gross(hrs,rate)
print(gp)
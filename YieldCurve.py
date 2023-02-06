### tetetete
from datetime import datetime
import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

bonds = {1: "CAN 2,25 Mar24",
         2: "CAN 1,50 Sep24"
    , 3: "CAN 1,25 Mar25"
    , 4: "CAN 1,50 Apr25"
    , 5: "CAN 2,25 Jun25"
    , 6: "CAN 1,50 Jun26"
    , 7: "CAN 1,00 Sep26"
    , 8: "CAN 1,25 Mar27"
    , 9: "CAN 1,00 Jun27"
    , 10: "CAN 2,00 Jun28"}
##The reasons of selecting these 10 bonds are in the Latex PDF.
bonds_inf = {
    1: [0.0225, "01/03/2024", [97.86], [97.977], [97.93], [97.86], [97.86], [97.84], [97.958], [97.93], [97.84],
        [97.8]],
    2: [0.0150, "01/09/2024", [96.45], [96.58], [96.5], [96.4], [96.4], [96.39], [96.47], [96.48], [96.29], [96.24]],
    3: [0.0125, "01/03/2025", [95.38], [95.42], [95.61], [95.44], [95.38], [95.34], [95.47], [95.5], [95.3], [95.19]],
    4: [0.0150, "01/04/2025", [95.76], [95.96], [95.95], [95.79], [95.72], [95.68], [95.84], [95.87], [95.67], [95.55]],
    5: [0.0225, "01/06/2025", [97.45], [97.7], [97.68], [97.51], [97.43], [97.39], [97.54], [97.56], [97.35], [97.23]],
    6: [0.015, "06/01/2026", [94.94], [95.27], [95.34], [95.02], [94.95], [94.96], [95.1], [95.09], [94.8], [94.7]],
    7: [0.01, "09/01/2026", [92.84], [93.24], [93.29], [92.95], [92.9], [92.91], [93.05], [93.04], [92.77], [92.63]],
    8: [0.0125, "03/01/2027", [93.25], [93.73], [93.78], [93.39], [93.33], [93.35], [93.4], [93.46], [93.14], [93.01]],
    9: [0.01, "06/01/2027", [92.38], [92.87], [92.85], [92.35], [92.36], [92.54], [92.54], [92.5], [92.12], [91.97]],
    10: [0.02, "06/01/2028", [96.02], [96.61], [96.59], [96.04], [95.94], [96.12], [96.12], [96.04], [95.62], [95.45]]}


def total_present_value(face_value, coupon, periods, rate):
    total_pv = 0
    for n in range(1, periods + 1):
        total_pv += coupon / math.pow((1 + rate), n)  # math.pow is 1 over (1+rate) to the power of n.

    total_pv += face_value / math.pow((1 + rate), periods)

    return total_pv


def ytm_calculation(face_value, coupon_rate, periods, price):
    coupon = face_value * coupon_rate
    ytm = coupon_rate
    condition = True
    while condition:
        if (price < face_value):  # When Price of bond < face value, the bond sells at discount, YTM > Coupon rate.
            ytm += 0.00001
        else:  # When Price of bond > face value, the bond sells at premium, YTM < Coupon rate.
            ytm -= 0.00001

        total_pv = total_present_value(face_value, coupon, periods, ytm)

        if (price < face_value):
            condition = total_pv > price
        else:
            condition = total_pv < price
    return ytm * 100


for i in range(1, len(bonds_inf) + 1):
    exec(f"YTM{i}=[]")
    face_value = 100
    start_date = "30/01/2023"
    maturity_date = bonds_inf[i][1]
    s_date = datetime.strptime(start_date, "%d/%m/%Y")
    m_date = datetime.strptime(maturity_date, "%d/%m/%Y")
    diff = (m_date - s_date)
    n = diff.days / 365
    if n >= int(n) + 0.5:
        n = int(n) + 1
    else:
        n = int(n) + 0.5
    coupon_rate = bonds_inf[i][0]
    for j in range(2, 12):
        price = bonds_inf[i][j][0]
        ytm = ytm_calculation(face_value, coupon_rate / 2, int(n * 2), price)
        exec(f"YTM{i}.append(ytm)")
x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
x_interp = np.linspace(0.5, 5, 101)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'black', 'gray']
for i in range(1, 11):
    exec(f"spl = CubicSpline(x, YTM{i})")
    exec(f"y_interp{i} = spl(x_interp)")
    exec(f"plt.plot(x, YTM{i},'o',color=colors[i-1])")
    exec(f"plt.plot(x_interp, y_interp{i},label=bonds[i],color=colors[i-1])")
plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
plt.grid(True)
plt.gca()
plt.xlabel('Maturity')
plt.ylabel('Yield to Maturity')
plt.show()
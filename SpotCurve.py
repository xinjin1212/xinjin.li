def spot_rate(face_value, YTM):
    spot_rate = [YTM[0]] # Since the n period rate of interest is the rate appropriate for discounting a risk-free cash flow that occurs on date n.
    for i in range(1, len(YTM)):

        a = YTM[i] / 100
        b = 0.0
        for j in range(0, i): # Since the n period rate of interest is the rate appropriate for discounting a risk-free cash flow that occurs on date n.
            
            b += a / ((1 + (spot_rate[j] / 100)) ** (j + 1))
        sr = (((1 + a) / (1 - b)) ** (1 / (i + 1))) - 1 #bootstrapping method to calc the spot rate, see the reference of bootstrapping spot rate.
        spot_rate.append(sr * 100)
    spot_rate.pop(0)
    return spot_rate


for i in range(1, 11):
    face_value = 100
    exec(f"spot_rate{i}=spot_rate(face_value,YTM{i})")

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]) #set our maturities into 10 units (asked for 5 years, semiannual coupon).
x_interp = np.linspace(1, 5, 101)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'black', 'gray']
for i in range(1, 11):
    exec(f"spl = CubicSpline(x, spot_rate{i})") #call scipy.interpolate import CubicSpline.
    exec(f"y_interp{i} = spl(x_interp)") # calculates interpolated yield to maturity values for the bond using the spline object. The resulting values are stored in “y_interpi".
    exec(f"plt.plot(x, spot_rate{i},'o',color=colors[i-1])")  
    exec(f"plt.plot(x_interp, y_interp{i},label=bonds[i],color=colors[i-1])") # do the interpolated yield to maturity values for the bond using a line and the color specified in the colors list.
plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5)) #adds a legend to the plot, which shows the bond names. The legend is placed at the center left and anchored to the right.
plt.grid(True) #adds a grid to the plot.
plt.gca() #sets the current axis to the active subplot.
plt.xlabel('Maturity') #set x axis.
plt.ylabel('Spot Rate') #set y axis.
plt.show()
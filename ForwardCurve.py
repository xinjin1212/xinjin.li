def froward_rate(spot_rate):
    F = []
    for i in range(2, len(spot_rate), 2): # froward rate = (1+r(n))^n/(1+r(n-1)^(n-1)-1, where r is relavant spot rate.
        f = (((1 + spot_rate[i] / 100) ** i) / (1 + spot_rate[0] / 100) ** (i - 1)) - 1
        F.append(f * 100)  # 3200

    return F


for i in range(1, 11):
    exec(f"F{i}=froward_rate(spot_rate{i})")

x = np.array([1, 2, 3, 4])
x_interp = np.linspace(1, 4, 101)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'black', 'gray']
for i in range(1, 11):
    exec(f"spl = CubicSpline(x, F{i})")
    exec(f"y_interp{i} = spl(x_interp)")
    exec(f"plt.plot(x, F{i},'o',color=colors[i-1])")
    exec(f"plt.plot(x_interp, y_interp{i},label=bonds[i],color=colors[i-1])")
plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
plt.grid(True)
plt.gca()
plt.xlabel('Maturity')
plt.ylabel('Forward Rate')
plt.xticks(x, ["1yr-1yr", "1yr-2yr", "1yr-3yr", "1yr-4yr"])
plt.show()
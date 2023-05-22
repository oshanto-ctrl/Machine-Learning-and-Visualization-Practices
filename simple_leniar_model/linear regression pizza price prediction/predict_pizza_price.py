x = [6, 8, 12, 14, 18]
y = [350, 775, 1150, 1395, 1675]

lenx = len(x)
leny = len(y)

"""
Formula:
m = xbar. ybar - xybar / xbar^2 - xsquarebar
c = ybar - m . xbar
"""

xbar = sum(x)/lenx
print('xbar = ', xbar)
ybar = sum(y)/leny
print('ybar = ', ybar)

xy = 0
for i in range(5):
    xy += x[i] * y[i]

xybar = xy/lenx
print("xybar = ", xybar)
# xybar = [ xy += x[i]*y[i] for i]

xbarsquared = xbar**2
print("xbarsquared = ", xbarsquared)
xsquaredbar = 0
xsquared = [x[i]**2 for i in range(5)]
xsquaredbar = sum(xsquared) / lenx
print("xsquaredbar = ", xsquaredbar)

m = ((xbar * ybar) - xybar) / (xbarsquared - xsquaredbar)
print('M = ', m)

c = ybar - (m * xbar)
print('c = ', c)

# now we can predict any pizza according to the list of size x[]
# list of price y[]
# formula, calculate:
# y = m * a + c
# here a is the desired pizza size that's price to be predicted
# a = 17 # price predicted = 1674.96
a = 20 # expected: 1969.something, predicted: 1969.6...
predicted_price = m * a + c
print(f"For size of {a} inch pizza, predicted prize = {predicted_price}")

# Now check R squared value .
newylist = [m * x[i] + c for i in range(5)]
print(newylist)

zig = [(newylist[i] - ybar)**2 for i in range(5)]
zag = [(y[i] - ybar)**2 for i in range(5)]
RSQUARED = sum(zig)/sum(zag)

print("Evaluation, R-Squared Value = ", str(RSQUARED)[:4])


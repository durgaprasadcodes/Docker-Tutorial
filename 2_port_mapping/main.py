import matplotlib.pyplot as plt

x = ["A","B","C","D"]
y = [500,450,300,650]

plt.plot(x,y,label="sales",marker='o')
plt.title("Sales Information")
plt.legend()
plt.savefig("sales.png")
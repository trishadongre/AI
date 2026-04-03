import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Artificial Intelligence Lab (N-PCCCS601P)
# Department of Computer Science and Engineering, S.B.J.I.T.M.R., Nagpur

# Sample Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 4, 5, 4, 5])

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, Y)

# Predict
Y_pred = model.predict(X)

# Plot
plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.show()

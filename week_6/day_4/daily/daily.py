import yfinance as yf
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df = yf.download('AAPL', start='2010-01-01', end='2023-01-01')
df = df[['Close']]
scaler = MinMaxScaler(feature_range=(0, 1))
df['Close'] = scaler.fit_transform(df)

def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        seq = data[i:i+seq_length]
        label = data[i+seq_length]
        sequences.append(seq)
        labels.append(label)
    return np.array(sequences), np.array(labels)

seq_length = 50
data = df['Close'].values

X, y = create_sequences(data, seq_length)
X_train, X_test = X[:int(len(X)*0.8)], X[int(len(X)*0.8):]
y_train, y_test = y[:int(len(y)*0.8)], y[int(len(y)*0.8):]

X_train, y_train = torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.float32)
X_test, y_test = torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.float32)

class LSTMStockPredictor(nn.Module):
    def __init__(self):
        super(LSTMStockPredictor, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=50, num_layers=2, batch_first=True)
        self.fc = nn.Linear(50, 1)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        return self.fc(lstm_out[:, -1, :])

model = LSTMStockPredictor()
loss_function = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 50
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    
    y_pred = model(X_train.unsqueeze(-1))
    loss = loss_function(y_pred.squeeze(), y_train)
    
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

model.eval()
with torch.no_grad():
    y_test_pred = model(X_test.unsqueeze(-1)).squeeze()

y_test_pred = scaler.inverse_transform(y_test_pred.view(-1, 1).numpy())
y_test_actual = scaler.inverse_transform(y_test.view(-1, 1).numpy())

plt.plot(y_test_actual, label="Actual Prices")
plt.plot(y_test_pred, label="Predicted Prices")
plt.legend()
plt.title("LSTM Stock Prediction - AAPL")
plt.show()

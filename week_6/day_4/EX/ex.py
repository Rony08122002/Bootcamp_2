import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

file_path = "day_4/EX/household_power_consumption.txt"
df = pd.read_csv(file_path, sep=';', low_memory=False, na_values='?')

print("First 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nShape:", df.shape)

missing = df.isnull().sum()
print("\nMissing values:")
print(missing[missing > 0])

df.fillna(df.mean(numeric_only=True), inplace=True)
print("\nMissing after fill:", df.isnull().sum().sum())

df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format="%d/%m/%Y %H:%M:%S")
df.set_index('Datetime', inplace=True)
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'], errors='coerce')
daily = df['Global_active_power'].resample('D').agg(['mean', 'std'])

plt.figure(figsize=(12, 5))
daily['mean'].plot(label='Mean')
daily['std'].plot(label='Std')
plt.title("Daily Global Active Power - Mean & Std")
plt.legend()
plt.show()

scaler = MinMaxScaler()
df['Global_active_power'] = scaler.fit_transform(df[['Global_active_power']])
data = df[['Global_active_power']].dropna()

train_size = int(len(data) * 0.8)
train_data = data[:train_size].values
test_data = data[train_size:].values

def create_sequences(data, window):
    x, y = [], []
    for i in range(len(data) - window):
        x.append(data[i:i+window])
        y.append(data[i+window])
    return np.array(x), np.array(y)

seq_length = 24
x_train, y_train = create_sequences(train_data, seq_length)
x_test, y_test = create_sequences(test_data, seq_length)

class TimeSeriesDataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

train_ds = TimeSeriesDataset(x_train, y_train)
test_ds = TimeSeriesDataset(x_test, y_test)
train_dl = DataLoader(train_ds, batch_size=32)
test_dl = DataLoader(test_ds, batch_size=32)

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.linear = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        return self.linear(out)

model = LSTMModel(1, 64)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 10
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for xb, yb in train_dl:
        optimizer.zero_grad()
        output = model(xb.unsqueeze(-1))
        loss = criterion(output, yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/len(train_dl):.4f}")

model.eval()
preds, actuals = [], []
with torch.no_grad():
    for xb, yb in test_dl:
        out = model(xb.unsqueeze(-1))
        preds.append(out.numpy())
        actuals.append(yb.numpy())

preds = np.concatenate(preds)
actuals = np.concatenate(actuals)

plt.plot(preds, label='Predicted')
plt.plot(actuals, label='Actual')
plt.title("LSTM Predictions vs Actual")
plt.legend()
plt.show()

score = r2_score(actuals, preds)
print(f"R2 Score: {score:.4f}")

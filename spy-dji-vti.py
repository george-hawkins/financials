import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf

matplotlib.use("TkAgg")
plt.ion()

vti_ticker = yf.Ticker("VTI")
vti_df = vti_ticker.history(period="max")

dji_ticker = yf.Ticker("^DJI")
dji_df = dji_ticker.history(period="max")

spy_ticker = yf.Ticker("SPY")
spy_df = spy_ticker.history(period="max")

plt.figure(1)
dji_df.loc["2001-06-15":]["Close"].plot(title="^DJI")

plt.figure(2)
spy_df.loc["2001-06-15":]["Close"].plot(title="SPY")

plt.figure(3)
vti_df["Close"].plot(title="VTI")

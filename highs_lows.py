import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'filename.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print('Missing data')
        except:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi = 128, figsize(10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolot = 'blue', alpha = 0.1)

plt.title("Daily high and low temperatures, 2021", fontsize = 20)
plt.xlabel("", fontsize = 16)
fog.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

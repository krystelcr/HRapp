## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

considring the context of heart rate monotoring the missing values or values that state "NO SIGNAL" can be due to hardware issues, signal interruptions, errors in recording data, etc. 
filtering these values out could lead to biased data that ignores real world activity and errors that could have underlying information

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The standard deviation describes how far the heart rate values are from the average rate (mean calculated over each window), it measures variability. A higer spike is greater variability, meaning the heart rate changed significantly, and vice versa


## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

 1: hits a peak and then falls
10: hits a bigger peak (wont fall till around 30)
20: peak in all the data set (but not drastic change between 12ish-28ish)
30: falls back to lower rates
36: lowest point and quick sharp peak falling back down

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

the "stdevs.png" graph has corresponding spikes and falls with the "averages.png" graph. When the averages change sharply, the standard deviation spikes. 
1: both peak and drop
10: both spike up
20: peaks but not big compared to 10 and 30
30: both sharp drop
36: both quick sharp peak falling back down quick




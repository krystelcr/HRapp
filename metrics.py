
import statistics
def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        maximums.append(max(window))
    return maximums


def window_average(data: list, n: int) -> list:
    """
    Calculate mean value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    average_list = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        average = sum(window) / len(window)
        average_list.append(round(average, 2))
    return average_list

    
    
def window_stddev(data: list, n: int) -> list:
    """
    Calculate the standard deviation of every "n"-size window without using import statistics.

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[float]: list of standard deviations from each window

    """ 

    if data == []: 
        return data
    stddev_list = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        if len(window) < 2: 
            continue
        stddev = statistics.stdev(window)
        stddev_list.append(round(stddev, 2)) 
    return stddev_list
    

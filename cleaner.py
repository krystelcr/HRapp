def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    lsofd = []
    if len(data) == 0 or "":
        return data
    for rate in data:
        rate = rate.strip()
        if rate.isdigit():
            lsofd.append(int(rate))
        else:
            rate = rate
    return lsofd



def filter_outliers(data: list) -> list:
    """
    Filter out all heart rate samples that are less than 30 and greater than 250

    Args:
        data (list[int]): list of intgers representing heart rate samples.

    Returns:
        list[int]: list of integers, between 31-249
    """
    olsofd = []
    for rate in data:
        if rate > 30 and rate < 250:
            olsofd.append(rate)
    return olsofd

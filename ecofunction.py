def ema(values, size):
    if size < 1:
        return 0
    a = values.iloc[0]
    b = 1
    alfa = 2/(size+1)
    for i in range(1,size+1):
        a += (pow((1-alfa),i)*values.iloc[i])
        b += pow((1-alfa),i)
    return a/b


def signal(values):
    signal = 0
    for i in range(9):
        signal += macd(values)
        values = values.iloc[1:]
    return signal/9


def macd(values):
    ema12 = ema(values['Srednia'], 12)
    ema26 = ema(values['Srednia'], 26)
    return ema12-ema26
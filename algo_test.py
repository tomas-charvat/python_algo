
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symbol_groups=list(chunks(stocks)['Ticker'],100))
symbol_strings=[]
for symbol in range(0,len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))

tens = {10 : 'TEN',
 20 : 'TWENTY',
 30 : 'Thirty',
 40 : 'Fourty',
 50 : 'Fifty',
 60 : 'Sixty',
 70 : 'Seventy',
 80 : 'Eighty',
 90 : 'Ninety',
 100 : 'Hundred'}

for x in range(1,101):
    if (x % 10) == 0:
        if x in tens:
            print(tens[x])
            continue
        x += 1
        continue
    print(x)
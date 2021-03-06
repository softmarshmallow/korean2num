array = [
    "3175만 3235㎡",
    "2247만 4804㎡",
    "1058만 6937㎡",
    "743만 2876㎡",
    "565만 3861㎡",
    "408만 5558㎡",
    "369만 820㎡",
    "353만 4858㎡",
    "350만 4048㎡",
    "321만 1222㎡",
    "297만 1962㎡",
    "239만 6306㎡",
    "201만 620㎡",
    "156만 2244㎡",
    "155만 5124㎡",
    "154만 4812㎡",
    "151만 6419㎡",
    "142만 9218㎡",
    "140만 3000㎡",
    "138만 6456㎡",
    "127만 5247㎡",
    "117만 8779㎡",
    "117만 3418㎡",
    "108만 8959㎡",
    "108만 8447㎡",
    "103만 6915㎡",
    "79만 3523㎡",
    "71만 8223㎡",
    "68만 8448㎡",
    "64만 7028㎡",
    "58만 8313㎡",
    "58만 7525㎡",
    "56만 1124㎡",
    "54만 8937㎡",
    "52만 1334㎡",
    "50만 8720㎡",
    "46만 3011㎡",
    "45만 1133㎡",
    "39만 2560㎡",
    "27만 600㎡",
    "24만 1807㎡",
    "22만 3271㎡",
    "21만 287㎡",
    "20만 2209㎡",
    "18만 9942㎡",
    "18만 9478㎡",
    "18만 3957㎡",
    "17만 6371㎡",
    "15만 6320㎡",
    "14만 7209㎡",
    "14만 4876㎡",
    "14만 2577㎡",
    "14만 1491㎡",
    "12만 6513㎡",
    "10만 8974㎡",
    "10만 155㎡",
    "9만 5868㎡",
    "9만 4151㎡",
    "9만 838㎡",
    "8만 6350㎡",
    "7만 4803㎡",
    "6만 7593㎡",
    "6만 4679㎡",
    "6만 4266㎡",
    "6만 4264㎡",
    "3만 6262㎡",
    "3만 1410㎡",
    "2만 5890㎡"
]

def process_dump(array):
    new_array = []
    for item in array:
        item = process(item)
        new_array.append(item)

    return new_array


def process(item:str):
    item = item.replace("만", '')
    item = item.replace(" ", '')
    item = item.replace("㎡", '')
    return item


if __name__ == "__main__":
    arr = process_dump(array)
    for item in arr:
        print(item)
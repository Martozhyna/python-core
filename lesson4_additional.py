# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

def data_list(arr):
    res = []
    gen = []
    for ar in arr:
        gen.append((i['id'] for i in ar if i['id'] not in res))

    while True:
        for g in gen:
            if len(res) == 5:
                return res
            res.append(next(g))


print(data_list(data))

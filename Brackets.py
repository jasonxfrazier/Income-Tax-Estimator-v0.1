# 2023-2024 tax bracket values, these are not exact as this is an estimation tool
bracket = \
{
    "single": [
            { "rate": 10, "range": [0, 11000], "base": 0 },
            { "rate": 12, "range": [11001, 44725], "base": 1100 },
            { "rate": 22, "range": [44726, 95375], "base": 5100 },
            { "rate": 24, "range": [95376, 182100], "base": 29300 },
            { "rate": 32, "range": [182101, 231250], "base": 66550 },
            { "rate": 35, "range": [231251, 578125], "base": 93250 },
            { "rate": 37, "range": [578126, 999999999], "base": 292250 }
        ],
    "married_separate": [
            { "rate": 10, "range": [0, 11000], "base": 0 },
            { "rate": 12, "range": [11001, 44725], "base": 1100 },
            { "rate": 22, "range": [44726, 95375], "base": 5147 },
            { "rate": 24, "range": [95376, 182100], "base": 16290 },
            { "rate": 32, "range": [182101, 231250], "base": 37104 },
            { "rate": 35, "range": [231251, 346875], "base": 52832 },
            { "rate": 37, "range": [346876, 999999999], "base": 93300.75 }
        ],
    "head_of_household": [
            { "rate": 10, "range": [0, 15700], "base": 0 },
            { "rate": 12, "range": [15701, 59850], "base": 1570 },
            { "rate": 22, "range": [59851, 95350], "base": 6868 },
            { "rate": 24, "range": [95351, 182100], "base": 14678 },
            { "rate": 32, "range": [182101, 231250], "base": 35498 },
            { "rate": 35, "range": [231251, 578100], "base": 51226 },
            { "rate": 37, "range": [578101, 999999999], "base": 172623.50 }
        ],
    "married_joint": [
            { "rate": 10, "range": [0, 22000], "base": 0 },
            { "rate": 12, "range": [22001, 89450], "base": 2200 },
            { "rate": 22, "range": [89451, 190750], "base": 10294 },
            { "rate": 24, "range": [190751, 364200], "base": 32580 },
            { "rate": 32, "range": [364201, 462500], "base": 74208 },
            { "rate": 35, "range": [462501, 693750], "base": 105664 },
            { "rate": 37, "range": [693751, 999999999], "base": 186601.50 }
        ]
}
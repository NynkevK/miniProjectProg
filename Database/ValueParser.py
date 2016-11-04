#Geschreven door Robin


import uuid


def TryParseValue(value):
    "Probeert een waarde te parsen naar types"
    types = [int,bool, uuid, float,str]

    for valueType in types:
        newValue, status = TryParse(value, valueType)

        if(status):
            return newValue


def TryParse(value,type):
    try:
        return type(value), True

    except ValueError:
        return value, False

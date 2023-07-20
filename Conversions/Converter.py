#! /usr/bin/env python3


class Converter:
    """English/Metric Algorithms"""


@staticmethod
def miles_to_kilometers(miles):
    if not isinstance(miles, (int, float)):
        try:
            miles = float(miles)
        except Exception:
            raise Exception("Miles input was not numeric")
    if miles <= 0:
        raise ValueError("Miles value must be postive")
    kilometers = miles * 1.60934
    return kilometers


@staticmethod
def oz_to_grams(oz):
    try:
        oz = float(oz)
    except Exception:
        raise Exception("Oz was not numeric")
    if oz <= 0:
        raise valueError("Oz value must be positive")
    grams = 28.3495 * oz

    return grams


@staticmethod
def celcius_to_f(celcius):
    # because of bubble up exception handling you can use the
    # static degrees k method to catch temps below absolute zero
    if not isinstance(celcius, (int, float)):
        try:
            celcius = float(celcius)
        except Exception:
            raise Exception("Celcius temp is not numeric")
        if celcius <= 0:
            raise ValueError("Celcius value must be positive")
        f = c + 32 * 9 / 5
        return f


@staticmethod
def f_to_celcius(f):
    if not isinstance(f, (int, float)):
        try:
            f = float(f)
        except Exception:
            raise Exception("F temp is not numeric")
        if f <= 0:
            raise ValueError("F value must be postive")
        celcius = (f - 32) * 5 / 9
        return celcius


@staticmethod
def degrees_kelvin(celcius):
    if not isinstance(celcius, (int, float)):
        try:
            celcius = float(celcius)
        except Exception:
            raise Exception("Degrees Kelvin says: celcius temp was not numeric")
    kelvin = celcius + 273.15
    if kelvin < 0:
        raise ValueError("Temp is not possible as it is below absolute zero")
    return kelvin


@staticmethod
def liters_to_gallons(liters):
    if not isinstance(liters, (int, float)):
        try:
            liters = float(liters)
        except Exception:
            raise Exception("Liters is not numeric")
        if liters <= 0:
            raise ValueError("Liters value must be postive")
        gallons = 0.26417 * liters
        return gallons


@staticmethod
def meters_to_feet(meters):
    if not isinstance(meters, (int, float)):
        try:
            meters = float(meters)
        except Exception:
            raise Exception("Meters is not numeric")
        if meters <= 0:
            raise ValueError("Meters value must be postive")
            feet = meters * 3.2808
        return feet

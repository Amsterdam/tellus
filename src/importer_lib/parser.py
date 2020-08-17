import re


def parse_speed_interval(value):
    """
    :param value: String of the form: "< 30 km/u", or "31 - 40 km/u" or "> 100 km/u"
    :return:
    """

    match_smaller = re.match("< (\d+)", value)
    match_larger = re.match("> (\d+)", value)
    match_interval = re.match("(\d+) - (\d+)", value)

    if match_smaller:
        return [None, int(match_smaller[1])]
    elif match_larger:
        return [int(match_larger[1]), None]
    elif match_interval:
        return [int(match_interval[1]), int(match_interval[2])]
    else:
        raise ValueError(f"Unkown interval string: {value}")


def parse_meter_string_to_cm(value):
    return round(100 * float(value))


def parse_length_interval(value):
    """
    :param value: String of the form: "0 - 5,1 m", ... , "10,5 - 12,2 m", "> 12,2 m"
    :return: [min_cm, max_cm]
    """
    interval_str = value.replace(",", ".")
    match_smaller = re.match("< (\d+.?\d*)", interval_str)
    match_larger = re.match("> (\d+.?\d*)", interval_str)
    match_interval = re.match("(\d+.?\d*) - (\d+.?\d*)", interval_str)

    if match_smaller:
        return [None, parse_meter_string_to_cm(match_smaller[1])]
    elif match_larger:
        return [parse_meter_string_to_cm(match_larger[1]), None]
    elif match_interval:
        return [
            parse_meter_string_to_cm(match_interval[1]),
            parse_meter_string_to_cm(match_interval[2]),
        ]
    else:
        raise ValueError(f"Unkown interval string: {value}")

def convert_to_seconds(value, unit):
    if unit == 'sec':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    else:
        raise ValueError(f"Unsupported time unit: {unit}")

def convert_to_rpm(value, unit):
    if unit == 'rpm':
        return value
    elif unit == 'rps':
        return value * 60
    else:
        raise ValueError(f"Unsupported speed unit: {unit}")

def convert_to_celsius(value, unit):
    if unit == '°C':
        return value
    elif unit == 'K':
        return value - 273.15
    elif unit == '°F':
        return (value - 32) * 5.0/9.0
    else:
        raise ValueError(f"Unsupported temperature unit: {unit}")

def convert_volume(value, unit):
    if unit == 'uL':
        return value * 1e-6
    elif unit == 'mL':
        return value * 1e-3
    elif unit == 'L':
        return value
    else:
        raise ValueError(f"Unsupported volume unit: {unit}")
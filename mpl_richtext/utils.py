"""
Utility functions for mpl-richtext
"""


def format_nepali_number(number):
    """
    Format a number using the Nepali/Indian numbering system.
    
    Uses the 3-2-2... grouping pattern from right to left.
    Handles already-formatted input by stripping existing commas first.
    
    Args:
        number: int, float, or string representing a number.
                Can include existing comma formatting.
    
    Returns:
        str: The number formatted with Nepali-style comma placement.
    
    Examples:
        >>> format_nepali_number(2553871)
        '25,53,871'
        >>> format_nepali_number("2,553,871")  # Western format → Nepali
        '25,53,871'
        >>> format_nepali_number(1234567.89)
        '12,34,567.89'
        >>> format_nepali_number(-2553871)
        '-25,53,871'
    """
    # Convert to string and strip existing commas
    num_str = str(number).replace(',', '')
    
    # Handle negative numbers
    is_negative = num_str.startswith('-')
    if is_negative:
        num_str = num_str[1:]
    
    # Separate integer and decimal parts
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.', 1)
    else:
        integer_part = num_str
        decimal_part = None
    
    # Apply Nepali grouping: first 3 digits from right, then 2 digits each
    if len(integer_part) <= 3:
        formatted = integer_part
    else:
        # Take last 3 digits
        result = [integer_part[-3:]]
        remaining = integer_part[:-3]
        
        # Group remaining digits in pairs of 2 from right to left
        while len(remaining) > 2:
            result.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        
        # Add any remaining digits (1 or 2)
        if remaining:
            result.insert(0, remaining)
        
        formatted = ','.join(result)
    
    # Rejoin with decimal part if present
    if decimal_part is not None:
        formatted = f"{formatted}.{decimal_part}"
    
    # Add negative sign back
    if is_negative:
        formatted = f"-{formatted}"
    
    return formatted


# Mappings for convert_to_nepali
_DIGIT_MAP = {
    '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
    '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
}

_DAY_MAP = {
    'sunday': 'आइतबार',
    'monday': 'सोमबार',
    'tuesday': 'मङ्गलबार',
    'wednesday': 'बुधबार',
    'thursday': 'बिहिबार',
    'friday': 'शुक्रबार',
    'saturday': 'शनिबार'
}

_NEPALI_MONTH_MAP = {
    'baishakh': 'वैशाख',
    'jestha': 'जेठ',
    'ashadh': 'असार',
    'shrawan': 'साउन',
    'bhadra': 'भदौ',
    'ashwin': 'असोज',
    'kartik': 'कार्तिक',
    'mangsir': 'मंसिर',
    'poush': 'पुस',
    'magh': 'माघ',
    'falgun': 'फागुन',
    'chaitra': 'चैत'
}

_GREGORIAN_MONTH_MAP = {
    'january': 'जनवरी',
    'february': 'फेब्रुअरी',
    'march': 'मार्च',
    'april': 'अप्रिल',
    'may': 'मे',
    'june': 'जुन',
    'july': 'जुलाई',
    'august': 'अगस्ट',
    'september': 'सेप्टेम्बर',
    'october': 'अक्टोबर',
    'november': 'नोभेम्बर',
    'december': 'डिसेम्बर'
}


def convert_to_nepali(text):
    """
    Convert English digits, days, and months to Nepali Devanagari script.
    
    Args:
        text: String or number to convert.
    
    Returns:
        str: Text with English elements converted to Nepali.
    
    Examples:
        >>> convert_to_nepali("Sunday, 1 Magh")
        'आइतबार, १ माघ'
        >>> convert_to_nepali("15 January 2024")
        '१५ जनवरी २०२४'
        >>> convert_to_nepali(123)
        '१२३'
    """
    import re
    
    result = str(text)
    
    # Replace days (case-insensitive, whole words only)
    for eng, nep in _DAY_MAP.items():
        result = re.sub(rf'\b{eng}\b', nep, result, flags=re.IGNORECASE)
    
    # Replace Nepali months
    for eng, nep in _NEPALI_MONTH_MAP.items():
        result = re.sub(rf'\b{eng}\b', nep, result, flags=re.IGNORECASE)
    
    # Replace Gregorian months
    for eng, nep in _GREGORIAN_MONTH_MAP.items():
        result = re.sub(rf'\b{eng}\b', nep, result, flags=re.IGNORECASE)
    
    # Replace digits last
    for eng, nep in _DIGIT_MAP.items():
        result = result.replace(eng, nep)
    
    return result

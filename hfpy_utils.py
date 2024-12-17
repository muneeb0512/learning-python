def convert2range(v, f_min, f_max, t_min, t_max):
    #f_min is from min which means jis range sei convert ker rahe oska minimum
    #tmin is to min which means jis range mein convert ker rahe oska min
    """Given a value (v) in the range f_min-f_max, convert the value
    to its equivalent value in the range t_min-t_max.

    Based on the technique described here:
        http://james-ramsden.com/map-a-value-from-one-number-scale-to-another-formula-and-c-code/
    """
    return round(t_min + (t_max - t_min) * ((v - f_min) / (f_max - f_min)), 2)
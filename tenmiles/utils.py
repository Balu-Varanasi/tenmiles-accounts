

def diff_in_time(start, end):
    date_delta = end - start
    return date_delta.total_seconds() / 3600

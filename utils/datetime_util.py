import datetime
import time


def _datetime(d):
    # string 转成 datetime
    if isinstance(d, datetime.datetime):
        return d
    if isinstance(d, datetime.date):
        return datetime.datetime(d.year, d.month, d.day)

    try:
        n = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            n = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            try:
                n = datetime.datetime.strptime(d, '%Y-%m-%d')
            except ValueError:
                n = datetime.datetime.strptime(d, "%Y-%m-%d %H:%M")
    return n


def get_time_str(t):
    spark_sql_fmt = 'yyyy-MM-dd HH:mm:ss'
    python_fmt = '%Y-%m-%d %H:%M:%S'
    dt_str = ''
    ts = 0
    warn_msg = ''

    if str(t).isdigit():
        try:
            ts = int(t)
            dt = datetime.datetime.fromtimestamp(ts)
        except (ValueError, TypeError):
            ts = int(t) // 1000
            warn_msg = f"⚠️{t} is out of range, guess it's {ts}."
            dt = datetime.datetime.fromtimestamp(ts)
            dt_str = dt.strftime(python_fmt)
    else:
        dt = _datetime(t)
        ts = time.mktime(dt.timetuple())

    dt_str = dt.strftime(python_fmt)

    ts = int(ts)

    return f"""
{warn_msg}
timestamp: {ts}
datetime: {dt_str}

format:
{spark_sql_fmt}
{python_fmt}
    """

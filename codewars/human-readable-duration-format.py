def format_duration(seconds):

    sim = 60
    sih = sim * 60
    sid = sih * 24
    siy = sid * 365

    cs = seconds

    td = {
        'years': 0,
        'days': 0,
        'hours': 0,
        'minutes': 0,
        'seconds': 0
    }

    if cs // siy > 0:
        td['years'] = cs//siy
        cs -= (siy * (cs//siy))
    if cs // sid > 0:
        td['days'] = cs//sid
        cs -= (sid * (cs//sid))
    if cs // sih > 0:
        td['hours'] = cs//sih
        cs -= (sih * (cs//sih))
    if cs // sim > 0:
        td['minutes'] = cs//sim
        cs -= (sim * (cs//sim))
    td['seconds'] = cs

    str = ''
    if td['years'] > 1:
        str.join('%s years,' % td['years'])
    elif td['years'] == 1:
        str.join('%s year' % td['years'])
    
    if td['days'] > 1:
        str.join('%s days,' % td['days'])
    elif td['days'] == 1:
        str.join('%s day' % td['days'])
    
    if td['hours'] > 1:
        str.join('%s hours,' % td['hours'])
    elif td['hours'] == 1:
        str.join('%s hour' % td['hours'])

    if td['minutes'] > 1:
        str.join('%s minutes,' % td['minutes'])
    elif td['minutes'] == 1:
        str.join('%s minute' % td['minutes'])

    if td['seconds'] > 1:
        str.join('%s seconds,' % td['seconds'])
    elif td['seconds'] == 1:
        str.join('%s second' % td['seconds'])

    print(str)
format_duration(86400 * 365 + 439856348)

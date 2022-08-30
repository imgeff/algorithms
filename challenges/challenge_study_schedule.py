def study_schedule(permanence_period, target_time):
    try:
        presence = 0
        for period in permanence_period:
            if period[1] >= target_time >= period[0]:
                presence += 1
        return presence
    except TypeError:
        return None

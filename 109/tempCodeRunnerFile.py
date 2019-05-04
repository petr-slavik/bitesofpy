    if day.capitalize() in workout_schedule.keys():
        for key, value in workout_schedule.items():
            if key == day.capitalize():
                if value == rest:
                    return chill
                else:
                    return go_train.format(value)
    else:
        return "chyba"
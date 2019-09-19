def vote(to_be_voted, comments):
    """
    to_be_voted = [
        {"value": value1, "confidence": confidence1},
        {"value": value2, "confidence": confidence2},
        {"value": value3, "confidence": confidence3},
    ]
    Same confidence should has same value, or expertise is needed.
    """
    highest = {'value': None, 'confidence': 0, 'count': 0}
    if len(to_be_voted) == 0:
        raise ValueError('has not found any information on {}'.format(comments))
    elif len(to_be_voted) == 1:
        return to_be_voted[0]['value']
    else:
        for vote in to_be_voted:
            if vote['confidence'] > highest['confidence']:
                highest = {'value': vote['value'], 'confidence': vote['confidence'], 'count': 0}
            elif vote['confidence'] == highest['confidence']:
                if highest['count'] == 0:
                    highest['value'] = vote['value']
                    highest['confidence'] = vote['confidence']
                else:
                    if highest['value'] != vote['value']:
                        raise ValueError('bad votes: {}'.format(to_be_voted))
                highest['count'] += 1
            else:
                pass
    return highest['value']

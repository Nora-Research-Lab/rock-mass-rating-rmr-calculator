def ucs_rating(ucs):
    if ucs > 250:
        return 15
    elif ucs >= 100:
        return 12
    elif ucs >= 50:
        return 7
    elif ucs >= 25:
        return 4
    elif ucs >= 5:
        return 2
    elif ucs >= 1:
        return 1
    else:
        return 0

def rqd_rating(rqd):
    if rqd >= 90:
        return 20
    elif rqd >= 75:
        return 17
    elif rqd >= 50:
        return 13
    elif rqd >= 25:
        return 8
    else:
        return 3

def joint_spacing_rating(spacing):
    if spacing > 2:
        return 20
    elif spacing >= 0.6:
        return 15
    elif spacing >= 0.2:
        return 10
    elif spacing >= 0.06:
        return 8
    else:
        return 5

JOINT_CONDITION_MAP = {
    'Very rough surfaces, no separation, hard joint wall': 30,
    'Slightly rough surfaces, <1 mm separation, hard joint wall': 25,
    'Smooth surfaces or 1–5 mm separation': 20,
    'Slickensided or 5–10 mm separation, soft joint wall': 10,
    'Soft gouge >10 mm separation': 0
}

GROUNDWATER_MAP = {
    'Completely dry': 15,
    'Damp': 10,
    'Wet': 7,
    'Dripping': 4,
    'Flowing': 0
}

def joint_condition_rating(condition_str):
    return JOINT_CONDITION_MAP.get(condition_str, 0)

def groundwater_rating(condition_str):
    return GROUNDWATER_MAP.get(condition_str, 0)

def compute_rmr(ucs, rqd, spacing, joint_condition_str, groundwater_str):
    r1 = ucs_rating(ucs)
    r2 = rqd_rating(rqd)
    r3 = joint_spacing_rating(spacing)
    r4 = joint_condition_rating(joint_condition_str)
    r5 = groundwater_rating(groundwater_str)
    total = r1 + r2 + r3 + r4 + r5

    if total >= 81:
        class_name = 'Class I'
    elif total >= 61:
        class_name = 'Class II'
    elif total >= 41:
        class_name = 'Class III'
    elif total >= 21:
        class_name = 'Class IV'
    else:
        class_name = 'Class V'

    ratings = [r1, r2, r3, r4, r5]
    return total, class_name, ratings

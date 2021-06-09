# Counting Valleys
# Problem Statement:
# An avid hiker keeps meticulous records of their hikes.
# During the last hike that took exactly x steps,
# for every step it was noted if it was an uphill, U or a downhill, D step.
# Hikes always start and end at sea level, and each step up or down represents
# a 1 unit change in altitude. We define the following terms:
#   * A mountain is a sequence of consecutive steps above sea level,
#     starting with a step up from sea level and ending with a step down to sea level.
#   * A valley is a sequence of consecutive steps below sea level,
#   starting with a step down from sea level and ending with a step up to sea level.

# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example
# steps = UDDDUDUU
# _ represents sea level, / represents U, \ represents D
# _/\      _
#    \    /
#     \/\/

# Example
# steps = DDUUDDUDUUUD
# _ represents sea level, / represents U, \ represents D
#
# _    _      _/\_
#  \  / \    /
#   \/   \/\/


def counting_valleys(steps):
    level = 0
    valley = 0
    for step in steps:
        if step == "U":
            level += 1
        if step == "D":
            level -= 1
        if level == 0 and step == "U":
            valley += 1
    return valley


if __name__ == "__main__":
    input_string = "DDUUDDUDUUUD"
    valley_count = counting_valleys(input_string)
    print(valley_count)

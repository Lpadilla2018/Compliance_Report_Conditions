# 12/04/2018
# ADA Compliance Report Code
# Author: Louie Padilla

###################################################################################################


# Ramp Width Parallel Perpendicular
# If Data >=48, Compliance = Yes
# If Data < 48, Compliance = No

def rampWidthParPerCheck(data):
    compliance = ""
    if data >= 48:
        compliance = "Yes"
    elif data < 48 and data != 0:
        compliance = "No"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance

# print(rampWidthParPerCheck(0))

###################################################################################################


# Ramp Slope (Parallel & Perpendicular)
# If Data <= 8.3, Compliance = Yes
# If Data >8.3, Compliance = No
def rampRunningSlopes(data):
    compliance = ""
    if data > 8.3:
        compliance = "No"
    elif data <= 8.3 and data != 0:
        compliance = "Yes"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance


# print(rampSlopes(0))


###################################################################################################

# Ramp X Slope (Parallel & Perpendicular)
# If Data <=2, Compliance = Yes
# If Data > 2, Compliance = No


def XSlopesCheck(data):
    compliance = ""
    if data > 2:
        compliance = "No"
    elif data <= 2 and data != 0:
        compliance = "Yes"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance


# print(XSlopesCheck(0))

###################################################################################################
# Flare Slope (LT & RT)
# If Data <=10, Compliance = Yes
# If Data >10, Compliance = No

def flareSlopeCheck(data):
    compliance = ""
    if data > 10:
        compliance = "No"
    elif data <= 10 and data != 0:
        compliance = "Yes"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance

# print(flareSlopeCheck(0))

###################################################################################################
# Landing Length Width (Parallel & Perpendicular)
# If Data >= 48, Compliance = Yes
# If Data <48, Compliance = No


def landingLengthWidthCheck(data):
    compliance = ""
    if data >= 48:
        compliance = "Yes"
    elif data < 48 and data != 0:
        compliance = "No"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance


# print(landingLengthCheck(46.5))


###################################################################################################
# Landing Slope X Slope (Parallel & Perpendicular)
# If Data <=2, Compliance = Yes
# If Data > 2, Compliance = No

def landingSlopeXSlopeCheck(data):
    compliance = ""
    if data > 2:
        compliance = "No"
    elif data <= 2 and data != 0:
        compliance = "Yes"
    elif data == 0 or None:
        compliance = "N/A"

    return compliance


# print(landingSlopeXSlopeCheck(33))
###################################################################################################

# Domes Provided
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No
# Domes Contrast
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No


def domesProvidedContrastCheck(data):
    if data.title() == "Yes":
        return "Yes"
    elif data.title() == "No":
        return "No"
    else:
        return "N/A"


# inputValue = "yes"
# print(domesProvidedContrastCheck(inputValue))
###################################################################################################

# Domes Length
# If Data >= 24, Compliance = Yes
# If Data < 24, Compliance = No


def domesLengthCheck(data):
    if data >= 24:
        return "Yes"
    elif data < 24 and data != 0:
        return "No"
    else:
        return "N/A"

# print(domesLengthCheck(0))
###################################################################################################

# Domes Full Width
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No


def domesFullWidthCheck(data):
    if data.title() == "Yes":
        return "Yes"
    elif data.title() == "No":
        return "No"
    else:
        return "N/A"

# print(domesFullWidthCheck("yes"))
###################################################################################################

# Domes Offset
# If Data >= 1.6 AND <=2.4, Compliance = Yes
# If Data < 1.6 OR >2.4, Compliance = No


def domesOffestCheck(data):
    if data != 0 and data <= 2.4 or data >= 1.6:
        return "Yes"
    elif data != 0 and data < 1.6 or data > 2.4:
        return "No"
    else:
        return "N/A"


# print(domesOffestCheck(1.8))
###################################################################################################

# Gutter Slope
# If Data <=5, Compliance = Yes
# If Data Slope >5, Compliance = No

def gutterRunningSlopeCheck(data):
    if data <= 5 and data != 0:
        return "Yes"
    elif data > 5:
        return "No"
    else:
        return "N/A"

# print(gutterRunningSlopeCheck(0.08))
###################################################################################################

# Gutter X Slope
# If Data <= 2, Compliance = Yes
# If Data >2, Compliance = No


def gutterCrossSlopeCheck(data):
    if data <= 2:
        return "Yes"
    elif data > 2:
        return "No"
    else:
        return "N/A"

# print(gutterCrossSlopeCheck(2.9)
###################################################################################################

# Ramp Inside X Walk2
# If Painted X Walk2 = Yes AND Data = Yes, Compliance = Yes
# If Painted X Walk2 = Yes AND Data = No, Compliance = No
# If Painted X Walk2 = No AND Data = "", Compliance = N/A


def rampInsideXWalk2Check(PaintedXWalk, rampInsideXWalk2):
    if PaintedXWalk.title() == "Yes" and rampInsideXWalk2.title() == "Yes":
        return "Yes"
    elif PaintedXWalk.title() == "Yes" and rampInsideXWalk2.title() == "No":
        return "No"
    elif PaintedXWalk.title() == "No" and rampInsideXWalk2.title() == "":
        return "N/A"
    else:
        return "N/A"

# print(rampInsideXWalk2Check("no", "yes"))


###################################################################################################

# Ramp Inside X Walk1	
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No

def rampInsideXWalk1Check(data):
    if data.title() =="Yes":
        return "Yes"
    elif data.title() =="No":
        return "No"
    else:
        return "N/A"

# print(rampInsideXWalk1Check(""))
###################################################################################################

# X Walk 1&2 X Slope	
# If Stop Condition = Traffic Signal AND Data <= 5, Compliance = Yes
# If Stop Condition = Traffic Signal AND Data >5, Compliance = No
# If Stop Conditon != Traffic Signal AND Data <= 2, Compliance = Yes
# If Stop Condition !=Traffic Signal AND Data >2, Compliance = No


def xWalkCrossSlopeCheck(stopCondition, crossSlope):
    if crossSlope !=0 and stopCondition.title() =="Signal" and crossSlope <=5:
        return "Yes"
    elif stopCondition.title() =="Signal" and crossSlope >5:
        return "No"
    elif crossSlope !=0 and stopCondition.title() !="Signal" and crossSlope <=2:
        return "Yes"
    elif stopCondition.title() !="Signal" and crossSlope >2:
        return "No"
    else:
        return "N/A"
    
    
# print(xWalkCrossSlope("", 0))
###################################################################################################

# Painted X Walk1	
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No

def paintedXWalk1Check(data):
    if data.title() == "Yes":
        return "Yes"
    elif data.title() =="No":
        return "No"
    else:
        return "N/A"

# print(paintedXWalk1Check("yes"))
###################################################################################################        

# Painted X Walk 2	
# If Data = Yes, Compliance = Yes
# If Data = No, Compliance = No
# If Data = "", Compliance = N/A

def paintedXWalk2Check(data):
    if data.title() =="Yes":
        return "Yes"
    elif data.title() == "No":
        return "No"
    else:
        return "N/A"

        
# Z-score
def zscore(length, weight, age):
    """
    Calculates the z-score of a child given their length/height, weight, and if they are over 2 years old or not.
    """
    import pandas as pd
    import math

    # Check the age
    try:
        age = float(age)
    except ValueError:
        print("Please enter an age that is a number.")
        return

    if age <= 5 and age > 2:   # Check if age is 2-5 years od
        over2 = True
    elif age <= 2 and age >= 0:  # Check if age is 0-2 years old
        over2 = False
    else:                       # If age is not 0-2 or 2-5 years old, raise an error
        print("Invalid age")
        return

    # Round down the child's length value to nearest 0.5 interval in WHO data
    length = math.floor(float(length) * 2)*0.5

    # Choose between dataset for 0-2 yrs old or 2-5 yrs old
    if over2 != True:
        df0_2 = pd.read_csv("../assets/wfl_boys_0_to_2_years_zscores.csv")
        try:
            L_val = df0_2.loc[df0_2['Length'] == length, 'L'].iloc[0]
        except IndexError:
            print(
                "Please check whether the child is younger or equal to 24 months old in the form.")
        M_val = df0_2.loc[df0_2['Length'] == length, 'M'].iloc[0]
        S_val = df0_2.loc[df0_2['Length'] == length, 'S'].iloc[0]
    else:
        df2_5 = pd.read_csv("../assets/wfh_boys_2_to_5_years_zscores.csv")
        try:
            L_val = df2_5.loc[df2_5['Length'] == length, 'L'].iloc[0]
        except IndexError:
            print("Please check whether the child is 2 years old or older in the form.")
        M_val = df2_5.loc[df2_5['Length'] == length, 'M'].iloc[0]
        S_val = df2_5.loc[df2_5['Length'] == length, 'S'].iloc[0]

    # Calculate z_score
    Z_score = ((float(weight)/M_val)**L_val - 1) / (L_val * S_val)
    return Z_score

# Acute Malnutrition Classifier


def am_classify(zscore, muac, edema):
    """
    Classifies the child's z-score, MUAC, and presence of edema into a status.
    """
    if edema != True:
        if float(muac) >= 115:
            if float(muac) >= 125:
                status = "NORMAL"
            elif zscore >= -3:
                if zscore < -2:
                    status = "MODERATE Acute Malnutrition"
                else:
                    status = "NORMAL"
            else:
                status = "MODERATE Acute Malnutrition"
        else:
            status = "SEVERE Acute Malnutrition"
    else:
        status = "SEVERE Acute Malnutrition"

    return status

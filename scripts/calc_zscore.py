def calc_zscore(length, weight, over2):
    """
    Calculates the z-score of a child given their length/height, weight, and if they are over 2 years old or not.
    """
    import pandas as pd
    import math

    # Round down the child's length value to nearest 0.5 interval in WHO data
    length = math.floor(float(length) * 2)*0.5

    # Choose between dataset for 0-2 yrs old or 2-5 yrs old
    if over2.lower() != "true":
        df0_2 = pd.read_csv("../assets/wfl_boys_0_to_2_years_zscores.csv")
        L_val = df0_2.loc[df0_2['Length'] == length, 'L'].iloc[0]
        M_val = df0_2.loc[df0_2['Length'] == length, 'M'].iloc[0]
        S_val = df0_2.loc[df0_2['Length'] == length, 'S'].iloc[0]
    else:
        df2_5 = pd.read_csv("../assets/wfh_boys_2_to_5_years_zscores.csv")
        L_val = df2_5.loc[df2_5['Length'] == length, 'L'].iloc[0]
        M_val = df2_5.loc[df2_5['Length'] == length, 'M'].iloc[0]
        S_val = df2_5.loc[df2_5['Length'] == length, 'S'].iloc[0]

    # Calculate z_score
    Z_score = ((float(weight)/M_val)**L_val - 1) / (L_val * S_val)
    return Z_score
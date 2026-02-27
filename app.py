import streamlit as st
import numpy as np
from scipy import stats
from statistics import stdev
from scipy.stats import t

st.title("Two Sample t-Test Calculator")

st.write("Enter sample values separated by commas")

# Inputs
sample1_input = st.text_input("Sample A", "10,12,14,16,18")
sample2_input = st.text_input("Sample B", "8,9,11,13,15")

alternative = st.selectbox(
    "Alternative Hypothesis",
    ["two-sided", "left", "right"]
)

if st.button("Run Test"):
    try:
        a = np.array([float(i.strip()) for i in sample1_input.split(",")])
        b = np.array([float(i.strip()) for i in sample2_input.split(",")])

        xbar1 = np.mean(a)
        xbar2 = np.mean(b)
        sd1 = stdev(a)
        sd2 = stdev(b)
        n1 = len(a)
        n2 = len(b)
        alpha = 0.05 / 2
        df = n1 + n2 - 2
        se = np.sqrt((sd1**2)/n1 + (sd2**2)/n2)
        tcal = ((xbar1 - xbar2) - 0) / se

        if alternative == "two-sided":
            p_value = 2 * (1 - t.cdf(abs(tcal), df))
        elif alternative == "left":
            p_value = t.cdf(tcal, df)
        else:
            p_value = 1 - t.cdf(tcal, df)

        st.subheader("Results")
        st.write(f"t-value: {tcal:.4f}")
        st.write(f"p-value: {p_value:.6f}")

        scipy_result = stats.ttest_ind(a, b, equal_var=False)
        st.write("SciPy verification:")
        st.write(scipy_result)

    except:
        st.error("Please enter valid numeric values separated by commas.")
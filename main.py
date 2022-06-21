import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image

st.title("Streamlit 入門")

st.write("DataFrame")


"""
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.dataframe(df,width=100,height=100)
st.dataframe(df)

st.table(df)
"""


# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns = [1,2,3]
# )

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns = ["lat","lon"]
)

st.map(df)

# img = Image.open("australia.jpeg")

# st.image(img,caption="shota", use_column_width=True)


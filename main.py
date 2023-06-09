import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"START"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration { i + 1 }%")
    bar.progress(i + 1)
    time.sleep(0.01)

"DONE"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに表示")
if button:
    right_column.write("ここは右カラムです")

expander = st.expander("問い合わせ1")
expander.write("問い合わせの1回答")
expander = st.expander("問い合わせ2")
expander.write("問い合わせの2回答")
expander = st.expander("問い合わせ3")
expander.write("問い合わせの3回答")


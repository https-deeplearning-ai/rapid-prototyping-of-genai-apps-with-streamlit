import streamlit as st
import time

st.title("⏱️ Caching Demo")

# Clear cache when needed
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# Cached function using the reset counter to invalidate cache
@st.cache_data
def expensive_computation(sleep_duration, reset_id=0):
    time.sleep(sleep_duration)
    return 42

sleep_time = st.slider("Delay (seconds):", 1, 10, 5)

col1, col2 = st.columns([3, 1])

with col1:
    if st.button("Run Computation"):
        if "first_time" not in st.session_state:
            start = time.time()
            expensive_computation(sleep_time, st.session_state.reset_counter)
            st.session_state.first_time = (time.time() - start) * 1000
            st.write(f"First run: {st.session_state.first_time:.1f} ms")
        else:
            start = time.time()
            expensive_computation(sleep_time, st.session_state.reset_counter)
            second_time = (time.time() - start) * 1000
            st.write(f"First run: {st.session_state.first_time:.1f} ms")
            st.write(f"Second run: {second_time:.1f} ms")
            st.write(f"Speedup: {st.session_state.first_time/max(second_time, 0.1):.1f}x")

with col2:
    if st.button("Reset"):
        st.session_state.reset_counter += 1
        if "first_time" in st.session_state:
            del st.session_state.first_time
        st.rerun()

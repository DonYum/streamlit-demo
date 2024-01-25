# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st


st.set_page_config(page_title="Form Demo", page_icon="📹")
st.markdown("# Form Demo")
st.sidebar.header("Form Demo")
# st.write(
#     """This app shows how you can use Streamlit to build cool animations.
# It displays an animated fractal based on the the Julia Set. Use the slider
# to tune different parameters."""
# )

if st.session_state.get('username'):
    st.title("Streamlit Test App")

    # add a sidebar
    st.sidebar.subheader("Details about you")

    first_name = st.sidebar.text_input(label="First Name")
    last_name = st.sidebar.text_input(label="Last Name")
    age = st.sidebar.number_input(label="Age", min_value=1, step=1)
    gender = st.sidebar.radio(label="Gender", options=['Male', 'Female', 'NA'])
    submit_button = st.sidebar.button(label="Submit")

    if submit_button:
        st.write("first name is  "+first_name)
        st.write('Last Name is '+last_name)
        st.write("Age is "+ str(age))
        st.write('Gender is '+gender)

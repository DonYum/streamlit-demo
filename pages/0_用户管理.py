
from urllib.error import URLError

import pandas as pd
import streamlit as st
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

st.set_page_config(page_title="用户管理", page_icon="📊")
st.markdown("# 用户管理")


def gen_pwd(pwd):
    pwd = pwd or '123'
    # LOGGER.info(f'{pwd}')
    if len(pwd) < 50:
        pwd = stauth.Hasher([pwd]).generate()[0]
    return pwd


user = st.session_state.get('username')
if user:
    user_file = Path('./data/users.pkl')
    if user_file.exists():
        df = pd.read_pickle(user_file)
    else:
        df = pd.DataFrame(columns=['username', 'display_name', 'group', 'password'])
    df = df.reset_index(drop=True)

    edited_df = st.data_editor(df, num_rows="dynamic")      # , key="username"
    if st.button('保存'):
        edited_df['password'] = edited_df.password.map(gen_pwd)
        edited_df.to_pickle(user_file)
        st.write('保存成功！')

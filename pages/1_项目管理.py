
from urllib.error import URLError
from datetime import date
import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

st.set_page_config(page_title="项目管理", page_icon="📊")
st.markdown("# 项目管理")


user = st.session_state.get('username')
if user:
    file = Path('./data/projects.pkl')
    if file.exists():
        df = pd.read_pickle(file)
    else:
        df = pd.DataFrame(columns=['proj_name', 'type', 'PM', 'STO', 'PD', 'start_time'])
    df = df.reset_index(drop=True)

    col_config = {
        "proj_name": "项目名称",
        "type": st.column_config.SelectboxColumn(
            "项目类型", help="", width="medium",
            options=["交付项目", "PoC", "内部项目",],
            required=True,
        ),
        "PM": st.column_config.SelectboxColumn(
            "PM", help="", width="medium", required=True,
            options=["寒江", "锦煊", "从宇", "圆明",],
        ),
        "start_time": st.column_config.DateColumn(
            "启动时间",
            min_value=date(2020, 1, 1),
            max_value=date(2025, 1, 1),
            format="YYYY-MM-DD", step=1,
        ),
    }
    edited_df = st.data_editor(df, column_config=col_config, num_rows="dynamic")      # , key="username"
    if st.button('保存'):
        edited_df.start_time = edited_df.start_time.astype('M')
        edited_df.to_pickle(file)
        st.write('保存成功！')

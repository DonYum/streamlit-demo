
from urllib.error import URLError
from datetime import date
import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

st.set_page_config(page_title="工时管理", page_icon="📊")
st.markdown("# 工时管理")


user = st.session_state.get('username')
if user:
    # 获取项目
    # @st.cache_data
    def get_proj_list():
        file = Path('./data/projects.pkl')
        projs = []
        if file.exists():
            df = pd.read_pickle(file)
            projs = df.proj_name.to_list()
        return projs
    
    file = Path('./data/manhour.pkl')
    if file.exists():
        df = pd.read_pickle(file)
        df.manhour = df.manhour.astype('float32')
    else:
        df = pd.DataFrame(columns=['project', 'week', 'manhour'])
    df = df.reset_index(drop=True)
    
    col_config = {
        "project": st.column_config.SelectboxColumn(
            "项目", help="", width="medium", required=True,
            options=get_proj_list(),
        ),
        "manhour": st.column_config.NumberColumn(
            "工时?",
            help="最小单位是0.5人日",
            min_value=0.5, max_value=6.0, step=0.5,
            format="%.1f", required=True,
        ),
    }
    st.write('最小单位是0.5人日，如果不符合规范，保存的时候会自动处理。')
    st.write('如果同一个项目填写多次，会自动聚合。')
    edited_df = st.data_editor(df, column_config=col_config, num_rows="dynamic")
    st.write(f'本周一共投入{len(edited_df)}个项目，总工时{edited_df.manhour.sum()}人日。')

    if st.button('保存'):
        edited_df.manhour = (edited_df.manhour*2).round() / 2
        edited_df.to_pickle(file)
        st.write('保存成功！')

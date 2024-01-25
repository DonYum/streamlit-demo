
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.logger import get_logger
from pathlib import Path
import pandas as pd

LOGGER = get_logger(__name__)

def run():

    st.write(f"# Hi {1}! 👋")
    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    # _pwd = stauth.Hasher(['123']).generate()[0]
    # credentials = dict(
    #     usernames=dict(
    #         llm={'name': 'LLM领域用户', 'email': 'aaa@mail.com', 'password': _pwd},
    #         Admin={'name': '管理员', 'email': 'aaa@mail.com', 'password': _pwd},
    #     )
    # )
    user_file = Path('./data/users.pkl')
    if not user_file.exists():
        st.error('用户数据文件不存在，请检查！')
    else:
        df = pd.read_pickle(user_file)
        # df = df.reset_index(drop=False)
        credentials = dict(usernames={})
        for i in range(len(df)):
            credentials['usernames'][df.iloc[i].username] = {'name': df.iloc[i].display_name, 'password': df.iloc[i].password}

    authenticator = stauth.Authenticate(credentials, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=1)
    
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:  # 登录成功
        st.write(f'Welcome *{name}*')
        LOGGER.info(f'st.session_state={st.session_state}')

        run()
        authenticator.logout('Logout', 'main')
    elif authentication_status == False:  # 登录失败
        st.error('Username/password is incorrect')
    elif authentication_status is None:  # 未输入登录信息
        st.warning('Please enter your username and password')

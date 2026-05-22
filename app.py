import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title="SnapClass - Making Attendance faster",
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png",
    )


    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        
        case 'student':
            student_screen() 

        case None:
            home_screen()

    join_code = st.query_params.get("join_code")

    if join_code:
        st.session_state["join_code"] = join_code

    if st.session_state.get("join_code"):

        if st.session_state.get("login_type") != "student":
            st.session_state["login_type"] = "student"

        if (
            st.session_state.get("is_logged")
            and st.session_state.get("user_role") == "student"
        ):
            auto_enroll_dialog(st.session_state["join_code"])

try:
    main()

except Exception as e:
    import traceback

    st.error(f"ERROR: {e}")

    st.code(traceback.format_exc())

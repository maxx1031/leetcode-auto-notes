# app.py
import streamlit as st
import os
from main_script import generate_notes # 从我们强大的主脚本导入核心函数

# --- UI 界面布局 ---
st.set_page_config(page_title="LeetCode Note Generator", layout="centered")
st.title("👨‍💻 LeetCode Note Generator")
st.write("Automatically generate in-depth study notes from your solution code.")

# --- 用户输入 ---
# 使用 session state 来记住上次输入的分类
if 'last_category' not in st.session_state:
    st.session_state.last_category = ""

# 题单分类输入框
category = st.text_input(
    "📚 Study List Category (Optional)",
    value=st.session_state.last_category,
    placeholder="e.g., 二叉树-BFS"
)

# 文件上传器
uploaded_file = st.file_uploader(
    "⬆️ Upload your Python solution file",
    type=['py']
)

# 生成按钮
if st.button("✨ Generate Notes", use_container_width=True):
    if uploaded_file is not None:
        # Streamlit 上传的文件在内存中，我们需要先把它保存到本地
        # 这样我们的主脚本才能像原来一样工作
        temp_dir = "temp_solutions"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.session_state.last_category = category # 记住这次的分类

        # 使用 st.spinner 来显示一个加载动画
        with st.spinner("AI is working its magic... Fetching, analyzing, and writing..."):
            try:
                # 调用我们的核心逻辑！
                # 注意：generate_notes 函数会打印日志，在streamlit中看不到
                # 可以修改 generate_notes 让它返回日志信息，但现在保持简单
                generate_notes(file_path, category)
                st.success("🎉 Success! Your note has been generated in the 'notes' folder.")
            except Exception as e:
                st.error(f"😭 An error occurred: {e}")
    else:
        st.warning("Please upload a solution file first.")
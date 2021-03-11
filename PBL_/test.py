import streamlit as st

def main():
    """streamlit app"""
    c="""import streamlit as st
    st.play()
    """
    st.code(c,language='python')
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')
    
    st.spinner("in progress..")
    st.text_area('test', value='', height=130, max_chars=700, key=None)
    
    
    video_file = open('Ant-man-and-wasp.mkv', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

if __name__=='__main__':
    main()

import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("This App is just to test Python on web")
st.write("Ofcourse this is a simple App")

for index, todo in enumerate(todos):
    checked_checkbox = st.checkbox(todo, key=todo)
    if checked_checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


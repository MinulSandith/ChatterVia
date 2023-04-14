import streamlit as st
import pyrebase
import time
import streamlit as st




st.set_page_config(page_title="ChatterVia Chat_Room",page_icon=":smile")
with open ("style.css") as f :
    st.markdown( f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.header("	:smile: ChatterVia Chat room")
name_box=st.text_input("Your Name")
st.sidebar.header("	:smile: ChatterVia Chat room")
global col1,col2,x

chat_display=st.container()
typing_area=st.container()

area1,area2=typing_area.columns(2)

send_button=area2.button("Send") 
refresh=area2.button("Refresh")
type_box=txt = area1.text_area('Enter your massage',key=1)
  





config={
  "apiKey": "AIzaSyAgW2HGJrZ8yWqxE2cHz4-J5zjPC8PXN_E" ,
  "authDomain": "chat-test-88c6d.firebaseapp.com",
  "databaseURL": "https://chat-test-88c6d-default-rtdb.firebaseio.com",
  "projectId": "chat-test-88c6d",
  "storageBucket": "chat-test-88c6d.appspot.com",
  "messagingSenderId": "556391649754",
  "appId": "1:556391649754:web:a4dee4ef7410a31b98b0e3",
  "databaseURl":"https://chat-test-88c6d-default-rtdb.firebaseio.com/"
  }    

firebase=pyrebase.initialize_app(config)
database=firebase.database()

def load_msg():    
    multi_line=""
    for data in database.child("msg").get().val():
         if str(type(data))== "<class 'NoneType'>":
            pass
         else:
              
              single_line="{} : {}".format(data["name"],data["msg"])
              multi_line=multi_line+single_line+"\n"
              
    return(multi_line)




logtxtbox = chat_display.empty()
logtxt = 'start'
display=logtxtbox.text_area("Chat ",load_msg(), height = 400)

if refresh:
   if load_msg()==display:
       pass
   else:
         
     display=logtxtbox.text_area("Chat ",load_msg(), height = 400)
    
    

if send_button:
    

    count=database.child("info").get().val()['last']
    
    database.child("info").set({
    'last':1+count
    }) 

    count=database.child("info").get().val()['last']
    name=name_box
    if name=="":
        name="No Name"
    msg_to_be_sent=type_box
    if msg_to_be_sent[-1]=="\n":
        msg_to_be_sent=msg_to_be_sent.rstrip(msg_to_be_sent[-1])
    if "\n" in msg_to_be_sent:
        
        msg_to_be_sent=msg_to_be_sent.replace("\n","*") 


    database.child("msg").child(count).set({
    'msg': msg_to_be_sent,
    'name': name})
    time.sleep(2)
    st.success("MSG has been Sent.Click refresh to view")




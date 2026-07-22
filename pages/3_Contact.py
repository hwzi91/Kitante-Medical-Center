from urllib.parse import quote
import streamlit as st
from content import CENTER
from style import inject_base, sidebar_contact, pulse_divider, site_footer

inject_base("Contact")
sidebar_contact()

st.markdown('<div class="eyebrow">Contact</div>', unsafe_allow_html=True)
st.title("Get in touch")
st.markdown(
    f""" <div class="emergency-banner"> 🚑 {CENTER['emergency_note']} </div> """,
    unsafe_allow_html=True,
)
pulse_divider()

left, right = st.columns([1, 1.2], gap="large")

with left:
    st.markdown(
        f""" <div class="card"> <h3>📍 Address</h3> <p>{CENTER['address_line1']}<br>{CENTER['address_line2']}<br>{CENTER['address_line3']}</p> </div> """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f""" <div class="card"> <h3>📞 Phone</h3> <p><a href="tel:{CENTER['phone_tel']}">{CENTER['phone_display']}</a></p> </div> """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f""" <div class="card"> <h3>🕒 Hours</h3> <p>{CENTER['hours_note']}</p> </div> """,
        unsafe_allow_html=True,
    )
    if CENTER["email"] and "example" not in CENTER["email"]:
        st.write("")
        st.markdown(
            f""" <div class="card"> <h3>✉️ Email</h3> <p><a href="mailto:{CENTER['email']}">{CENTER['email']}</a></p> </div> """,
            unsafe_allow_html=True,
        )

with right:
    map_url = f"https://maps.google.com/maps?q={quote(CENTER['map_query'])}&z=16&output=embed"
    st.markdown(
        f""" <div class="card" style="padding:0; overflow:hidden;"> <iframe src="{map_url}" width="100%" height="360" style="border:0; display:block;" allowfullscreen="" loading="lazy"> </iframe> </div> """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")

st.markdown('<div class="eyebrow">Send a message</div>', unsafe_allow_html=True)
st.subheader("Request a call back")
st.caption(
    "This form doesn't send anything on its own yet — see the README for a "
    "quick way to connect it to your email. For anything urgent, please call directly."
)

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Full name")
    phone = st.text_input("Phone number")
    reason = st.selectbox(
        "Reason for contact",
        ["General inquiry", "Book an appointment", "Ask about a service", "Other"],
    )
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send request")

    if submitted:
        if name and phone:
            st.success(
                f"Thanks, {name} — please call {CENTER['phone_display']} to confirm, "
                "since this form isn't yet connected to an inbox."
            )
        else:
            st.warning("Please fill in at least your name and phone number.")

site_footer()

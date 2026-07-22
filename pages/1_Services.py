import streamlit as st
from content import CENTER, SERVICES
from style import inject_base, sidebar_contact, pulse_divider, site_footer

inject_base("Services")
sidebar_contact()

st.markdown('<div class="eyebrow">Our Services</div>', unsafe_allow_html=True)
st.title("How we can help")
st.write(
    "From routine check-ups to urgent care, our team is here to support "
    "your family's health. Call ahead if you'd like to confirm availability "
    "for a specific service."
)
pulse_divider()

cols = st.columns(3)
for i, service in enumerate(SERVICES):
    with cols[i % 3]:
        st.markdown(
            f""" <div class="card"> <span class="icon">{service['icon']}</span> <h3>{service['name']}</h3> <p>{service['description']}</p> </div> """,
            unsafe_allow_html=True,
        )
        st.write("")

st.divider()
st.markdown(
    f""" <div class="emergency-banner"> ðŸš‘ {CENTER['emergency_note']} â€” {CENTER['phone_display']} </div> """,
    unsafe_allow_html=True,
)

st.caption(
    "Note to site owner: confirm this service list is accurate and up to date "
    "before publishing â€” edit it any time in content.py."
)

site_footer()

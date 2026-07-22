import streamlit as st
from content import CENTER, TEAM
from style import inject_base, sidebar_contact, pulse_divider, site_footer

inject_base("About Us")
sidebar_contact()

st.markdown('<div class="eyebrow">About Us</div>', unsafe_allow_html=True)
st.title(CENTER["name"])
st.write(CENTER["about_body"])
pulse_divider()

st.markdown('<div class="eyebrow">Our Team</div>', unsafe_allow_html=True)
st.subheader("The people behind your care")

cols = st.columns(3)
for i, member in enumerate(TEAM):
    with cols[i % 3]:
        st.markdown(
            f""" <div class="card"> <span class="icon">ðŸ§‘â€âš•ï¸</span> <h3>{member['role']}</h3> <p>{member['description']}</p> </div> """,
            unsafe_allow_html=True,
        )

st.caption(
    "Note to site owner: this section uses role descriptions rather than "
    "individual names, since none were confirmed. Add real staff names, "
    "titles, and photos in content.py whenever you're ready."
)

st.divider()
st.markdown('<div class="eyebrow">Where we are</div>', unsafe_allow_html=True)
st.write(
    f"{CENTER['address_line1']}, {CENTER['address_line2']}, in Kamwokya â€” "
    "a short distance from the Mawanda Road Police Station."
)

site_footer()

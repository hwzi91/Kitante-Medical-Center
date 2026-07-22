import streamlit as st
from content import CENTER, SERVICES
from style import inject_base, sidebar_contact, pulse_divider, site_footer

inject_base("Home")
sidebar_contact()

# ---- Hero --------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero">
        <div class="eyebrow" style="color:#B9D6CF;">Mawanda Road · Kamwokya · Kampala</div>
        <h1>{CENTER['name']}</h1>
        <p>{CENTER['tagline']}. {CENTER['about_intro']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("📞 Call Us Now", use_container_width=True):
        st.markdown(f"[Tap to call {CENTER['phone_display']}](tel:{CENTER['phone_tel']})")
with col2:
    st.page_link("pages/3_Contact.py", label="📍 Get Directions & Contact Info", use_container_width=True)

pulse_divider()

# ---- Quick info strip ----------------------------------------------------
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f"""<div class="info-strip"><div class="label">Address</div>
        <div class="value">{CENTER['address_line1']}, {CENTER['address_line2']}</div></div>""",
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f"""<div class="info-strip"><div class="label">Phone</div>
        <div class="value">{CENTER['phone_display']}</div></div>""",
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""<div class="info-strip"><div class="label">Hours</div>
        <div class="value">{CENTER['hours_note']}</div></div>""",
        unsafe_allow_html=True,
    )

st.write("")
st.write("")

# ---- Services teaser -----------------------------------------------------
st.markdown('<div class="eyebrow">What we offer</div>', unsafe_allow_html=True)
st.subheader("Care for the whole family")

cols = st.columns(4)
for i, service in enumerate(SERVICES[:4]):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="card">
                <span class="icon">{service['icon']}</span>
                <h3>{service['name']}</h3>
                <p>{service['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
st.page_link("pages/1_Services.py", label="See all services →")

st.write("")
st.write("")

# ---- Why choose us ---------------------------------------------------
st.markdown('<div class="eyebrow">Why patients choose us</div>', unsafe_allow_html=True)
w1, w2, w3 = st.columns(3)
with w1:
    st.markdown(
        """<div class="card"><span class="icon">📍</span>
        <h3>Close to home</h3>
        <p>Conveniently located on Mawanda Road in Kamwokya, easy to reach from across Kampala.</p></div>""",
        unsafe_allow_html=True,
    )
with w2:
    st.markdown(
        """<div class="card"><span class="icon">🤝</span>
        <h3>Community-focused care</h3>
        <p>Personalized attention from a team that knows the neighborhood it serves.</p></div>""",
        unsafe_allow_html=True,
    )
with w3:
    st.markdown(
        """<div class="card"><span class="icon">🕒</span>
        <h3>Ready when you need us</h3>
        <p>Outpatient and emergency support for everyday and urgent medical needs.</p></div>""",
        unsafe_allow_html=True,
    )

site_footer()

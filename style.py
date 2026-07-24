"""
Shared visual design system for the site.
You generally shouldn't need to edit this file — edit content.py instead.
Only come here if you want to change colors, fonts, or layout structure.
"""

import streamlit as st
from content import CENTER

# ---- Design tokens ---------------------------------------------------
COLOR_PRIMARY = "#0E4F49"       # deep teal — trust, calm
COLOR_PRIMARY_DARK = "#073430"
COLOR_ACCENT = "#D9A441"        # warm gold — warmth, optimism
COLOR_URGENT = "#B8432B"        # brick red — used only for emergency/urgent cues
COLOR_BG = "#F5F7F5"            # soft mint-tinted white
COLOR_SURFACE = "#FFFFFF"
COLOR_INK = "#16211D"
COLOR_MUTED = "#5B6B65"
COLOR_BORDER = "#DFE7E3"

HEARTBEAT_SVG = """
<svg class="pulse-divider" viewBox="0 0 600 40" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <polyline points="0,20 130,20 155,20 170,4 185,36 200,20 220,20 600,20"
    fill="none" stroke="currentColor" stroke-width="2.5"
    stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def inject_base(page_title: str, page_icon: str = "🩺"):
    """Call once at the top of every page."""
    st.set_page_config(
        page_title=f"{page_title} | {CENTER['short_name']}",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary: {COLOR_PRIMARY};
                --primary-dark: {COLOR_PRIMARY_DARK};
                --accent: {COLOR_ACCENT};
                --urgent: {COLOR_URGENT};
                --bg: {COLOR_BG};
                --surface: {COLOR_SURFACE};
                --ink: {COLOR_INK};
                --muted: {COLOR_MUTED};
                --border: {COLOR_BORDER};
            }}

            html, body, [class*="css"] {{
                font-family: 'Inter', sans-serif;
                color: var(--ink);
            }}

            .stApp {{
                background-color: var(--bg);
            }}

            h1, h2, h3, .display {{
                font-family: 'Fraunces', serif;
                font-weight: 600;
                color: var(--primary-dark);
                letter-spacing: -0.01em;
            }}

            #MainMenu, footer {{visibility: hidden;}}
[data-testid="stHeader"] {{background-color: {COLOR_PRIMARY_DARK};}}

            section[data-testid="stSidebar"] {{
                background-color: var(--primary-dark);
            }}
            section[data-testid="stSidebar"] * {{
                color: #EAF3F0 !important;
            }}
            section[data-testid="stSidebar"] a {{
                color: #EAF3F0 !important;
            }}

            .eyebrow {{
                font-family: 'Inter', sans-serif;
                text-transform: uppercase;
                letter-spacing: 0.14em;
                font-size: 0.78rem;
                font-weight: 600;
                color: var(--accent);
                margin-bottom: 0.4rem;
            }}

            .hero {{
                background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
                border-radius: 18px;
                padding: 3rem 2.5rem;
                color: #F3F7F5;
                margin-bottom: 2rem;
            }}
            .hero h1 {{
                color: #FFFFFF;
                font-size: 2.6rem;
                margin: 0 0 0.8rem 0;
                line-height: 1.1;
            }}
            .hero p {{
                color: #DCEAE6;
                font-size: 1.05rem;
                max-width: 42rem;
                margin: 0;
            }}

            .pulse-divider {{
                width: 100%;
                height: 24px;
                color: var(--accent);
                margin: 0.4rem 0 1.6rem 0;
                opacity: 0.9;
            }}

            .card {{
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 14px;
                padding: 1.5rem;
                height: 100%;
            }}
            .card .icon {{
                font-size: 1.8rem;
                margin-bottom: 0.6rem;
                display: block;
            }}
            .card h3 {{
                font-size: 1.15rem;
                margin: 0 0 0.4rem 0;
            }}
            .card p {{
                color: var(--muted);
                font-size: 0.92rem;
                line-height: 1.5;
                margin: 0;
            }}

            .info-strip {{
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 14px;
                padding: 1.2rem 1.5rem;
            }}
            .info-strip .label {{
                text-transform: uppercase;
                letter-spacing: 0.1em;
                font-size: 0.72rem;
                color: var(--muted);
                font-weight: 600;
            }}
            .info-strip .value {{
                font-size: 1rem;
                font-weight: 600;
                color: var(--ink);
                margin-top: 0.15rem;
            }}

            .emergency-banner {{
                background: #FBEAE5;
                border: 1px solid var(--urgent);
                color: var(--urgent);
                border-radius: 12px;
                padding: 0.9rem 1.2rem;
                font-weight: 600;
                font-size: 0.92rem;
                margin-bottom: 1.6rem;
            }}

            div.stButton > button, .stLinkButton > a {{
                background-color: var(--accent) !important;
                color: var(--primary-dark) !important;
                border: none !important;
                border-radius: 10px !important;
                font-weight: 600 !important;
                padding: 0.6rem 1.4rem !important;
            }}
            div.stButton > button:hover, .stLinkButton > a:hover {{
                background-color: #C4933A !important;
            }}

            footer.site-footer {{
                margin-top: 3rem;
                padding-top: 1.5rem;
                border-top: 1px solid var(--border);
                color: var(--muted);
                font-size: 0.85rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def sidebar_contact():
    """Consistent contact block at the bottom of the sidebar on every page."""
    with st.sidebar:
        st.markdown(f"### {CENTER['name']}")
        st.caption(CENTER["tagline"])
        st.divider()
        st.markdown(f"📍 {CENTER['address_line1']}, {CENTER['address_line2']}")
        st.markdown(f"📞 [{CENTER['phone_display']}](tel:{CENTER['phone_tel']})")
        st.markdown(f"🕒 {CENTER['hours_note']}")


def pulse_divider():
    st.markdown(HEARTBEAT_SVG, unsafe_allow_html=True)


def site_footer():
    st.markdown(
        f"""
        <footer class="site-footer">
            {CENTER['name']} · {CENTER['address_line1']}, {CENTER['address_line2']} ·
            <a href="tel:{CENTER['phone_tel']}">{CENTER['phone_display']}</a>
        </footer>
        """,
        unsafe_allow_html=True,
    )

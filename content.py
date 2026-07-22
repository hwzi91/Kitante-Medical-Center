"""
============================================================
 EDIT THIS FILE to update the center's information.
 Every page reads its text from here, so you only need to
 make changes in ONE place and the whole site updates.

 Anything tagged "CONFIRM" below was NOT verified from an
 official source — double check it before you publish.
============================================================
"""

CENTER = {
    "name": "Kitante Medical Center",
    "short_name": "Kitante Medical",
    "tagline": "Community healthcare you can trust, on Mawanda Road",
    "about_intro": (
        "Kitante Medical Center has served the Kamwokya community from "
        "Mawanda Road for years, offering outpatient, emergency, and "
        "maternity care close to home."
    ),
    "about_body": (
        "We believe good healthcare should be nearby, dependable, and "
        "delivered with care. Our team supports patients from routine "
        "check-ups through to urgent medical needs, working to keep the "
        "Kamwokya community healthy — CONFIRM/replace this paragraph with "
        "your own words about the center's history and mission."
    ),
    "address_line1": "Plot 641, Mawanda Road",
    "address_line2": "Kamwokya, Kampala",
    "address_line3": "P.O. Box 16586, Kampala, Uganda",
    "phone_display": "+256 41 453 4760",
    "phone_tel": "+25641453476",  # CONFIRM — digits only for tel: links, re-check this number
    "email": "info@kitantemedical.example",  # CONFIRM — placeholder, replace with a real inbox
    "whatsapp_number": "",  # optional, e.g. "256700000000" — leave blank to hide the WhatsApp button
    "hours_note": "Call us to confirm today's opening hours.",  # CONFIRM real hours, then edit this
    "emergency_note": "For a medical emergency, call us directly or come to reception right away.",
    "map_query": "Kitante Medical Center, Mawanda Road, Kamwokya, Kampala, Uganda",
    "lat": 0.3441408,
    "lon": 32.5816583,
    "facebook_url": "",  # add if you have a page, e.g. "https://facebook.com/..."
}

SERVICES = [
    {
        "icon": "🩺",
        "name": "Outpatient Consultations",
        "description": "General medical consultations for adults and children, including diagnosis and treatment of everyday illnesses.",
    },
    {
        "icon": "🚑",
        "name": "Emergency Care",
        "description": "Urgent attention for accidents and acute medical conditions.",
    },
    {
        "icon": "🤰",
        "name": "Maternity Services",
        "description": "Antenatal check-ups, delivery support, and postnatal care for mothers and newborns.",
    },
    {
        "icon": "🧪",
        "name": "Laboratory Services",
        "description": "On-site diagnostic testing to support fast, accurate treatment decisions.",
    },
    {
        "icon": "💊",
        "name": "Pharmacy",
        "description": "Dispensing of prescribed medication on site.",
    },
    {
        "icon": "👶",
        "name": "Family Planning & Child Welfare",
        "description": "Immunization, growth monitoring, and family planning services. CONFIRM this service is currently offered.",
    },
    {
        "icon": "🔬",
        "name": "Specialized Treatments & Referrals",
        "description": "Access to specialist consultations and referral support when needed.",
    },
]
# ^ Delete, edit, or add service entries freely — the page rebuilds automatically.

TEAM = [
    {
        "role": "General Medical Officers",
        "description": "Our doctors handle everyday consultations, diagnosis, and treatment plans.",
    },
    {
        "role": "Maternity & Nursing Team",
        "description": "Dedicated staff supporting mothers through antenatal, delivery, and postnatal care.",
    },
    {
        "role": "Laboratory & Pharmacy Team",
        "description": "Diagnostic testing and medication dispensing, on site.",
    },
]
# We left out individual names/photos since none were confirmed.
# Replace this list with real staff names, titles, and photos whenever you're ready —
# add photo files to assets/team/ and reference them the same way hero_image is used in style.py.

NAV_PAGES = ["Home", "Services", "About Us", "Contact"]

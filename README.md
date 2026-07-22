# Kitante Medical Center — Website

A simple, professional Streamlit website for Kitante Medical Center
(Plot 641, Mawanda Road, Kamwokya, Kampala).

## Before you publish — please check

I built this from what I could find publicly about the center. A few
things I could **not** verify and marked as placeholders — please fix
these in `content.py` before sharing the site:

- **Opening hours** — currently just says "call to confirm."
- **Email address** — placeholder, swap in a real inbox.
- **Team names/photos** — currently shown as roles only (e.g. "General
  Medical Officers"), not individual names, since I had no confirmed source.
- **Services list** — based on what's publicly listed; confirm it's current.
- **Phone number** (+256 41 453 4760) — found via public listings, worth
  double-checking it's still correct.

Everything else (name, address, general service categories) is corroborated
by more than one independent source.

## Project structure

```
kitante-medical-center/
├── Home.py                  ← homepage
├── content.py                ← ALL editable text & contact info lives here
├── style.py                  ← design system (colors, fonts, CSS) — rarely needs edits
├── requirements.txt
├── .streamlit/config.toml    ← theme colors
├── assets/                   ← put your own logo/photos here
└── pages/
    ├── 1_Services.py
    ├── 2_About_Us.py
    └── 3_Contact.py
```

## Editing content

Open `content.py`. Every piece of text on the site (address, phone,
services, team, hours) is a plain Python dictionary/list there — edit the
values, save, and every page updates automatically. You don't need to
touch any other file for text changes.

## Adding real photos

I didn't include stock or scraped photos, since I couldn't confirm any
online image actually shows this clinic, and using someone else's photos
without rights isn't safe for a live business site. To add your own:

1. Drop image files into `assets/` (e.g. `assets/building.jpg`, `assets/logo.png`).
2. In `Home.py` (or any page), add:
   ```python
   st.image("assets/building.jpg", use_container_width=True)
   ```

## Run it locally (optional, before deploying)

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Put it on GitHub

```bash
cd kitante-medical-center
git init
git add .
git commit -m "Initial website"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```
(Create the empty repo on GitHub first at github.com/new — don't add a
README there, since this folder already has one.)

## Deploy for free — Streamlit Community Cloud

1. Go to **share.streamlit.io** and sign in with your GitHub account.
2. Click **"Create app"** → choose your repository and branch (`main`).
3. Set **Main file path** to `Home.py`.
4. Click **Deploy**. It builds in a minute or two and gives you a public
   `https://<something>.streamlit.app` URL.
5. Any time you push new commits to GitHub, the live site updates
   automatically.

## Connecting the contact form to your email (optional)

The "Send a message" form on the Contact page currently just shows a
confirmation on screen — it doesn't email you. The simplest no-backend way
to fix that:

1. Create a free form endpoint at **formspree.io**.
2. In `pages/3_Contact.py`, replace the form's submit logic with a POST
   request to your Formspree endpoint using the `requests` library
   (add `requests` to `requirements.txt`).

Happy to wire this up for you if you'd like — just ask.

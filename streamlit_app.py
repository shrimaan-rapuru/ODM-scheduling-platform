import calendar
from datetime import date, datetime, time, timedelta

import streamlit as st


st.set_page_config(
    page_title="ODM Scheduling Platform",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed",
)


BRAND_GOLD = "#c98f2d"
BRAND_RED = "#9f3c32"
INK = "#151926"
MUTED = "#6f7687"
SOFT_BLUE = "#52657f"


st.markdown(
    f"""
    <style>
        .stApp {{
            background: linear-gradient(180deg, #fffaf2 0%, #f7f9fc 52%, #ffffff 100%);
            color: {INK};
        }}

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        #MainMenu,
        footer {{
            display: none !important;
        }}

        .block-container {{
            max-width: 520px;
            padding: 2.25rem 1.3rem 7rem;
        }}

        h1 {{
            color: #0f1118;
            font-size: 3.15rem !important;
            line-height: 1.03 !important;
            letter-spacing: 0 !important;
            margin-bottom: 0.4rem !important;
        }}

        h2 {{
            color: #111827;
            font-size: 2rem !important;
            letter-spacing: 0 !important;
            margin-top: 1.5rem !important;
        }}

        h3 {{
            color: #111827;
            letter-spacing: 0 !important;
        }}

        .subtitle {{
            color: #4c5261;
            font-size: 1.35rem;
            line-height: 1.45;
            margin: 0 0 2rem;
        }}

        .section-title {{
            font-size: 1.85rem;
            font-weight: 800;
            color: #141824;
            margin: 2.2rem 0 1rem;
        }}

        .empty-state {{
            min-height: 230px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: {SOFT_BLUE};
        }}

        .empty-icon {{
            font-size: 4rem;
            color: {SOFT_BLUE};
            margin-bottom: 1.2rem;
        }}

        .empty-title {{
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
        }}

        .empty-subtitle {{
            color: #a1a8b7;
            font-size: 1.05rem;
        }}

        .stat-row {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.75rem;
            margin: 1.2rem 0 1.8rem;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(20, 24, 36, 0.08);
            border-radius: 16px;
            padding: 1rem 0.85rem;
            box-shadow: 0 10px 28px rgba(16, 24, 40, 0.06);
        }}

        .stat-value {{
            font-size: 1.75rem;
            font-weight: 850;
            color: {BRAND_GOLD};
            line-height: 1;
        }}

        .stat-label {{
            color: {MUTED};
            font-size: 0.82rem;
            margin-top: 0.4rem;
        }}

        .appointment-card,
        .volunteer-card,
        .settings-row {{
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid rgba(20, 24, 36, 0.08);
            border-radius: 18px;
            padding: 1rem;
            margin: 0.75rem 0;
            box-shadow: 0 12px 32px rgba(16, 24, 40, 0.07);
        }}

        .card-title {{
            font-size: 1.08rem;
            font-weight: 800;
            color: #111827;
        }}

        .card-meta {{
            color: {MUTED};
            margin-top: 0.3rem;
        }}

        .pill {{
            display: inline-block;
            border-radius: 999px;
            background: #fff2db;
            color: #8d5f19;
            padding: 0.22rem 0.65rem;
            font-size: 0.78rem;
            font-weight: 800;
            margin-top: 0.65rem;
        }}

        .calendar-shell {{
            margin-top: 1.6rem;
        }}

        .calendar-header {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            color: {MUTED};
            font-weight: 750;
            text-align: center;
            margin-bottom: 0.8rem;
        }}

        .calendar-grid {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 0.9rem 0.55rem;
            text-align: center;
            align-items: center;
        }}

        .day-cell {{
            min-height: 42px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            font-size: 1.05rem;
            color: #222937;
        }}

        .day-cell.is-today {{
            background: linear-gradient(135deg, #e49d26 0%, #b84438 100%);
            color: white;
            font-weight: 850;
            box-shadow: 0 10px 24px rgba(184, 68, 56, 0.24);
        }}

        .bottom-pad {{
            height: 1.5rem;
        }}

        div[data-baseweb="tab-list"] {{
            position: fixed;
            left: 50%;
            bottom: 0;
            transform: translateX(-50%);
            z-index: 999;
            max-width: 520px;
            width: 100%;
            background: rgba(255, 255, 255, 0.96);
            border-top: 1px solid rgba(20, 24, 36, 0.08);
            box-shadow: 0 -12px 30px rgba(16, 24, 40, 0.08);
            display: grid !important;
            grid-template-columns: repeat(4, 1fr);
            padding: 0.45rem 0.15rem 0.7rem;
            gap: 0;
        }}

        button[data-baseweb="tab"] {{
            justify-content: center;
            padding: 0.4rem 0.2rem;
            color: #778198;
            font-weight: 700;
        }}

        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {BRAND_GOLD};
        }}

        .stButton > button,
        [data-testid="stFormSubmitButton"] button {{
            background: linear-gradient(135deg, #d99d34 0%, #b94b3f 100%);
            color: white;
            border: 0;
            border-radius: 14px;
            font-weight: 800;
            padding: 0.7rem 1rem;
        }}

        div[role="radiogroup"] {{
            gap: 0.6rem;
        }}

        div[role="radiogroup"] label {{
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(20, 24, 36, 0.10);
            border-radius: 14px;
            padding: 0.4rem 0.9rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


if "volunteers" not in st.session_state:
    st.session_state.volunteers = []

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "push_notifications" not in st.session_state:
    st.session_state.push_notifications = True


def page_header(title, subtitle):
    st.markdown(f"# {title}")
    st.markdown(f"<p class='subtitle'>{subtitle}</p>", unsafe_allow_html=True)


def empty_state(icon, title, subtitle=""):
    st.markdown(
        f"""
        <div class="empty-state">
            <div class="empty-icon">{icon}</div>
            <div class="empty-title">{title}</div>
            <div class="empty-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def appointment_card(appointment):
    volunteer = appointment["volunteer"] or "Unassigned"
    st.markdown(
        f"""
        <div class="appointment-card">
            <div class="card-title">{appointment["title"]}</div>
            <div class="card-meta">{appointment["date"].strftime("%b %d, %Y")} at {appointment["time"].strftime("%I:%M %p")}</div>
            <div class="card-meta">{volunteer}</div>
            <div class="pill">{appointment["status"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def volunteer_card(volunteer):
    st.markdown(
        f"""
        <div class="volunteer-card">
            <div class="card-title">{volunteer["name"]}</div>
            <div class="card-meta">{volunteer["role"]}</div>
            <div class="card-meta">{volunteer["availability"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_calendar(selected_date):
    month_days = calendar.Calendar(firstweekday=6).monthdayscalendar(selected_date.year, selected_date.month)
    st.markdown("<div class='calendar-shell'>", unsafe_allow_html=True)
    st.markdown(
        "<div class='calendar-header'>" + "".join(f"<div>{day}</div>" for day in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]) + "</div>",
        unsafe_allow_html=True,
    )

    cells = []
    for week in month_days:
        for day in week:
            if day == 0:
                cells.append("<div class='day-cell'></div>")
            else:
                today_class = " is-today" if day == selected_date.day else ""
                cells.append(f"<div class='day-cell{today_class}'>{day}</div>")
    st.markdown("<div class='calendar-grid'>" + "".join(cells) + "</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def upcoming_appointments(days=7):
    end = date.today() + timedelta(days=days)
    return sorted(
        [item for item in st.session_state.appointments if date.today() <= item["date"] <= end],
        key=lambda item: (item["date"], item["time"]),
    )


dashboard_tab, calendar_tab, volunteers_tab, settings_tab = st.tabs(
    ["▦\nDashboard", "▣\nCalendar", "♟\nVolunteers", "⚙\nSettings"]
)


with dashboard_tab:
    page_header("Dashboard", "Today and upcoming appointments")

    today_items = [item for item in st.session_state.appointments if item["date"] == date.today()]
    upcoming_items = upcoming_appointments()
    unassigned_items = [item for item in st.session_state.appointments if not item["volunteer"]]

    st.markdown(
        f"""
        <div class="stat-row">
            <div class="stat-card"><div class="stat-value">{len(today_items)}</div><div class="stat-label">Today</div></div>
            <div class="stat-card"><div class="stat-value">{len(upcoming_items)}</div><div class="stat-label">Next 7 days</div></div>
            <div class="stat-card"><div class="stat-value">{len(unassigned_items)}</div><div class="stat-label">Unassigned</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='section-title'>Today's Appointments</div>", unsafe_allow_html=True)
    if today_items:
        for appointment in today_items:
            appointment_card(appointment)
    else:
        empty_state("▣", "No appointments today")

    st.markdown("<div class='section-title'>Upcoming (Next 7 Days)</div>", unsafe_allow_html=True)
    if upcoming_items:
        for appointment in upcoming_items:
            appointment_card(appointment)
    else:
        empty_state("", "No upcoming appointments")

    st.markdown(f"<div class='section-title'>Unassigned Shifts ({len(unassigned_items)})</div>", unsafe_allow_html=True)
    if unassigned_items:
        for appointment in unassigned_items:
            appointment_card(appointment)
    else:
        st.info("All shifts are assigned.")


with calendar_tab:
    page_header("Calendar", "View your schedule by month, week, or day")
    view_mode = st.radio("Calendar view", ["Month", "Week", "Day"], horizontal=True, label_visibility="collapsed")
    selected_date = st.date_input("Selected date", value=date.today(), label_visibility="collapsed")

    st.markdown(f"## {selected_date.strftime('%B %Y')}")
    if view_mode == "Month":
        render_calendar(selected_date)
    elif view_mode == "Week":
        week_start = selected_date - timedelta(days=(selected_date.weekday() + 1) % 7)
        for offset in range(7):
            day = week_start + timedelta(days=offset)
            st.markdown(f"### {day.strftime('%a, %b %d')}")
            day_items = [item for item in st.session_state.appointments if item["date"] == day]
            if day_items:
                for appointment in day_items:
                    appointment_card(appointment)
            else:
                st.caption("No appointments")
    else:
        st.markdown(f"### {selected_date.strftime('%A, %B %d')}")
        day_items = [item for item in st.session_state.appointments if item["date"] == selected_date]
        if day_items:
            for appointment in day_items:
                appointment_card(appointment)
        else:
            empty_state("▣", "No appointments scheduled")

    st.markdown("<div class='section-title'>Add Appointment</div>", unsafe_allow_html=True)
    with st.form("appointment_form", clear_on_submit=True):
        title = st.text_input("Appointment title", placeholder="Food pantry intake")
        appointment_date = st.date_input("Date", value=date.today())
        appointment_time = st.time_input("Time", value=time(9, 0))
        volunteer_names = [""] + [volunteer["name"] for volunteer in st.session_state.volunteers]
        volunteer = st.selectbox("Assigned volunteer", volunteer_names, format_func=lambda value: "Unassigned" if value == "" else value)
        submitted = st.form_submit_button("Add appointment")
        if submitted and title:
            st.session_state.appointments.append(
                {
                    "title": title,
                    "date": appointment_date,
                    "time": appointment_time,
                    "volunteer": volunteer,
                    "status": "Scheduled" if volunteer else "Unassigned",
                }
            )
            st.success("Appointment added.")


with volunteers_tab:
    page_header("Volunteers", "Manage volunteer roster, availability and assignments")

    st.markdown(f"<div class='section-title'>Active Volunteers ({len(st.session_state.volunteers)})</div>", unsafe_allow_html=True)
    if st.session_state.volunteers:
        for volunteer in st.session_state.volunteers:
            volunteer_card(volunteer)
    else:
        empty_state("♟", "No volunteers registered", "Add volunteers to build your team")

    st.markdown("<div class='section-title'>Add Volunteer</div>", unsafe_allow_html=True)
    with st.form("volunteer_form", clear_on_submit=True):
        name = st.text_input("Volunteer name", placeholder="Full name")
        role = st.selectbox("Role", ["Front Desk", "Meal Service", "Transportation", "Mentorship", "Administration"])
        availability = st.multiselect("Availability", ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        submitted = st.form_submit_button("Add volunteer")
        if submitted and name:
            st.session_state.volunteers.append(
                {
                    "name": name,
                    "role": role,
                    "availability": ", ".join(availability) if availability else "Availability not set",
                }
            )
            st.success("Volunteer added.")


with settings_tab:
    page_header("Settings", "Manage users and preferences")

    st.markdown("<div class='section-title'>Appearance</div>", unsafe_allow_html=True)
    st.session_state.dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, help="Enable dark theme")

    st.markdown("<div class='section-title'>Notifications</div>", unsafe_allow_html=True)
    st.session_state.push_notifications = st.toggle(
        "🔔 Push Notifications",
        value=st.session_state.push_notifications,
        help="Receive alerts for appointments",
    )

    st.markdown(f"<div class='section-title'>Users ({len(st.session_state.volunteers)})</div>", unsafe_allow_html=True)
    if st.session_state.volunteers:
        for volunteer in st.session_state.volunteers:
            volunteer_card(volunteer)
    else:
        st.info("No users have been added yet.")

    st.markdown("<div class='bottom-pad'></div>", unsafe_allow_html=True)

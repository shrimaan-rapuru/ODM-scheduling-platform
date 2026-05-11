# 📅 ODM Volunteer Scheduling Platform

> A full-stack scheduling tool built to solve real coordination problems at a nonprofit serving 70–75 homeless residents weekly.

**Live App:** [scheduling-platform.streamlit.app](https://scheduling-platform.streamlit.app/)

---

## Overview

The ODM Scheduling Platform is a volunteer coordination web app designed for **Open Door Ministries (ODM)**, a nonprofit in High Point, NC. Built independently after observing recurring inefficiencies in volunteer scheduling during my time as a Community Service Leader, this platform was developed as a proposed solution and presented to ODM leadership.

The project taught me as much about organizational constraints and human systems as it did about software — a lesson that shaped how I think about building technology for real communities.

---

## Features

- **Dashboard** — Real-time overview of today's appointments, upcoming shifts (next 7 days), unassigned roles, and scheduling analytics
- **Calendar View** — Month, week, and day views with slot availability tracking and appointment creation
- **Appointment Management** — Create appointments with title, date, time, assigned volunteer, urgency level, slot type, and status
- **Volunteer Roster** — Add and manage volunteers with role assignments and availability settings
- **Push Notifications** — Automated reminders to reduce no-shows and last-minute gaps
- **Settings** — User management, notification preferences, and appearance options

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python |
| Framework | Streamlit |
| Data Storage | Session state / local data layer |
| Notifications | Push notification support |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/shrimaan-rapuru/odm-scheduling-platform.git
cd odm-scheduling-platform

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## Project Background

After joining Open Door Ministries as a volunteer in January 2024, I noticed a consistent pattern: some mornings had too many volunteers, others too few. Food ran short one week and went to waste the next. As someone drawn to systems thinking, I mapped the inefficiencies and built this platform as a proposed solution.

The platform was presented to ODM's operating director. It wasn't implemented — not because of the software, but because of organizational constraints I hadn't fully accounted for: data privacy considerations, staff capacity to onboard a new system, and existing workflows that a new tool would have to integrate with.

That experience — building something technically sound that still didn't fit — was one of the most formative lessons of my engineering education so far.

> *"My solution didn't fit a system I hadn't fully understood."*

---

## Status

This is an independent project built as a proposal for ODM. It is not officially affiliated with or deployed by Open Door Ministries.

---

## Author

**Shrimaan Rapuru**
[LinkedIn](https://linkedin.com/in/shrimaan-rapuru-439689329) · [GitHub](https://github.com/shrimaan-rapuru)

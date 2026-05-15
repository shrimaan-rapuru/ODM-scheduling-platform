# 📅 ODM Volunteer Scheduling Platform

> A full-stack scheduling and coordination tool built to solve real operational problems at a nonprofit serving 70–75 homeless residents weekly.

**Live App:** [scheduling-platform.streamlit.app](https://scheduling-platform.streamlit.app/)


---

## 🧩 The Problem

Volunteer scheduling and coordination for meal service operations at **Open Door Ministries (ODM)** — a nonprofit in High Point, NC serving 70–75 homeless residents weekly — was inefficient and difficult to manage manually.

After joining ODM as a volunteer in January 2024, I observed the same pattern repeatedly:

- Some mornings had too many volunteers crowding the kitchen; other mornings had too few
- Food ran short one week and went to waste the next
- Shift gaps weren't caught until the day of service
- There was no centralized system for tracking who was coming, what roles needed filling, or where shortages were forming in advance

Coordination relied on informal communication — group texts, word of mouth, manual sign-up sheets — creating unnecessary friction for a team doing important community work.

---

## 💡 The Solution

I built the **ODM Volunteer Scheduling Platform** — a centralized, web-based scheduling and coordination system designed to streamline volunteer management and reduce manual overhead.

The platform gives organizers a single place to manage shifts, track availability, assign roles, and send automated reminders — replacing fragmented communication with a structured digital workflow.

---

## 📸 Screenshots

### Dashboard — Shift Overview & Analytics
<img width="389" height="874" alt="dashboard" src="https://github.com/user-attachments/assets/60fac4da-35fc-4728-8012-986da8d6b2ae" />

> *Real-time view of today's appointments, next 7 days, unassigned shifts, and scheduling analytics.*

### Calendar — Slot Availability & Appointment Booking
<img width="333" height="855" alt="calender" src="https://github.com/user-attachments/assets/4d9efdac-93c5-4626-ab6a-33a08e179209" />

> *Month, week, and day views with available time slots. Staff can create appointments with assigned volunteers, urgency levels, and status tracking.*

### Volunteer Roster — Role & Availability Management
<img width="362" height="678" alt="volunteers" src="https://github.com/user-attachments/assets/d593d5e2-9026-4cc5-97f6-d87524832eb2" />

> *Add volunteers, assign roles (e.g. Front Desk, Kitchen), and set availability for scheduling.*

### Settings — Users & Notifications
<img width="372" height="459" alt="settings" src="https://github.com/user-attachments/assets/8b484bfb-4faf-404d-ae5c-cd30aee5bbd7" />

> *Manage users, toggle push notifications, and configure appearance preferences.*


---

## ✨ Features

- **Shift Dashboard** — Real-time overview of today's appointments, next 7 days, unassigned roles, and scheduling analytics
- **Calendar View** — Month, week, and day views with slot availability tracking
- **Appointment Management** — Create appointments with title, date, time, assigned volunteer, urgency level, slot type, and status
- **Volunteer Roster** — Add and manage volunteers with role assignments and availability settings
- **Push Notifications** — Automated reminders to reduce no-shows and last-minute coordination gaps
- **User Management** — Settings panel for managing users, notification preferences, and appearance

---

## 🏗️ Architecture

```
User Interface (Streamlit)
        ↓
App Logic (Python)
  ├── Dashboard module    → Aggregates shift data, flags unassigned roles
  ├── Calendar module     → Slot availability, appointment CRUD
  ├── Volunteer module    → Roster management, role/availability assignment
  └── Notification module → Push notification triggers for upcoming shifts
        ↓
Data Layer (Streamlit session state / local storage)
```

### Key Technical Decisions

- **Streamlit** chosen for rapid deployment and accessible UI without requiring a separate frontend framework
- **Session state management** used to maintain app state across user interactions without a persistent database — appropriate for a prototype/proposal context
- **Push notification layer** designed as an optional module that can be connected to a real notification service (e.g. Twilio, SendGrid) once the platform is adopted
- **Modular 4-view structure** (Dashboard, Calendar, Volunteers, Settings) mirrors how nonprofit staff actually think about coordination — by day, by role, and by person

### Technical Challenges Solved

- **Slot conflict detection** — Calendar logic checks for overlapping appointments and flags unassigned slots before they become day-of problems
- **Role-based availability** — Volunteer module supports multiple role types and availability windows, enabling smarter assignment rather than first-come-first-served signup
- **Intuitive UI for non-technical users** — The platform was designed for nonprofit staff, not developers. Every interaction was simplified to minimize onboarding friction

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.10+ | Core application logic |
| Framework | Streamlit | Frontend UI and deployment |
| Data Layer | Session state | In-app state management (prototype) |
| Notifications | Push notification module | Automated shift reminders |
| Deployment | Streamlit Cloud | Public hosting |

---

## 📁 Project Structure

```
odm-scheduling-platform/
├── app.py                  # Main Streamlit application
├── pages/
│   ├── dashboard.py        # Shift overview and analytics
│   ├── calendar.py         # Slot availability and booking
│   ├── volunteers.py       # Roster and role management
│   └── settings.py         # User and notification settings
├── assets/
│   ├── dashboard.jpg       # Screenshots for README
│   ├── calendar.jpg
│   ├── volunteers.jpg
│   └── settings.jpg
├── requirements.txt
└── README.md
```

---

## 📊 Impact

- Designed to support weekly coordination for meal service operations serving **75–100 homeless residents** per week
- Addresses scheduling gaps that previously caused food shortages and volunteer overcrowding
- Built and **presented to ODM's operating director** as a formal proposal with written documentation
- Demonstrates how a single-developer tool can reduce operational friction for community organizations running on limited resources

---

## 🔭 Future Improvements

- [ ] **Database integration** — Replace session state with a persistent backend (SQLite or Firebase) so data carries across sessions and users
- [ ] **SMS/email notifications** — Connect notification module to Twilio or SendGrid for real reminder delivery to volunteers' phones
- [ ] **Volunteer self-signup** — Allow volunteers to claim open shifts directly from a public-facing view without admin involvement
- [ ] **Recurring shift templates** — Let admins create repeating weekly schedules instead of manually entering each week
- [ ] **Attendance tracking** — Log who showed up vs. who was assigned to build historical reliability data per volunteer
- [ ] **Role-based access control** — Separate admin and volunteer views with login authentication
- [ ] **Analytics dashboard** — Track trends over time: volunteer utilization, peak demand periods, no-show rates

---

## 💬 Why I Built This

I didn't start this project to build software. I started it because I showed up every Saturday morning to serve breakfast and kept watching the same problems repeat themselves.

The real lesson came when I presented the platform and it wasn't adopted — not because of the code, but because I hadn't fully understood the organizational constraints I was designing for. That experience shaped how I think about engineering more than any successful deployment would have.

> *"My solution didn't fit a system I hadn't fully understood."*

Building something technically correct and building something that actually works for a community are two different things. Closing that gap is the work I want to keep doing.

---

## ⚠️ Status

This is an **independent project built as a proposal** for Open Door Ministries. It is not officially affiliated with or deployed by ODM.

---

## 👤 Author

**Shrimaan Rapuru**
[LinkedIn](https://linkedin.com/in/shrimaan-rapuru-439689329) · [GitHub](https://github.com/shrimaan-rapuru) · [Live App](https://scheduling-platform.streamlit.app/)

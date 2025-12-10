# Project Chors: A Family Chore Tracker
Project Chors is a cloud-native web app designed to help families manage and track household chores with transparency, accountability, and ease. Built with AWS and modern web technologies, it automates chore scheduling, tracks completion history, and flags overdue tasks — all behind secure login and session management.

## 

## Features
-Secure login/logout via Amazon Cognito

-Scheduled updates using EventBridge + Lambda

-Chore data stored in DynamoDB, protected and versioned

-Interactive UI built with HTML, CSS, and JavaScript

-Due chores and history logs rendered dynamically

-Session-aware access control — no data shown after logout

## Tech Stack
1) Frontend: HTML, CSS, JavaScript, GitHub Pages

2) Backend: AWS Lambda, API Gateway, Cognito, S3

3) Automation: EventBridge scheduled rules

4) Security: Token-based access, session clearing on logout

## Purpose
Designed for families who want a lightweight, reliable way to stay on top of chores — with built-in accountability and a clean, educational interface. Ideal for parents, kids, or roommates who want to gamify responsibility and reduce friction.

## Getting Started

To try out the Family Chore Tracker yourself, follow these steps:

1. **Create an account**
   - Go to the app’s login page.
   - Click **Sign Up**.
   - Enter your email and password (this becomes your family account).
   - Verify your email if prompted.

2. **Log in**
   - Use your new credentials to log in.
   - You’ll be taken to your family dashboard.

3. **Add your first chore**
   - Click **Add Chore**.
   - Fill in details like:
     - Chore name
     - Instructions
     - Due date
     - Interval (days)
     - Assigned family member
   - Save the chore.

4. **Manage chores**
   - Mark chores as complete when finished.
   - Edit chores to change assignments or due dates.
   - Delete chores if they’re no longer needed.

5. **Stay organized**
   - Use the dashboard to see what’s due next.
   - Notifications (email) will remind family members of upcoming chores.
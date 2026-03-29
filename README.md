# Invoice Notifier

An automated email reminder system that sends scheduled emails to vendors every Monday for payment follow-ups or receipt confirmations.

## Overview

VendorPulse is designed to eliminate manual follow-ups by automatically notifying vendors about pending payments or missing receipts. It ensures consistent communication and helps maintain smooth financial operations. The system can also be connected to Google Sheets, allowing real-time updates to control email reminders dynamically.

## Features

### Automated Weekly Emails
- Sends reminder emails automatically every Monday  
- No manual intervention required once configured  

### Vendor Management
- Store vendor details including name, email, and transaction type  
- Supports multiple vendors simultaneously  

### Reminder Types
- Payment reminders for pending dues  
- Receipt reminders for missing confirmations  

### Google Sheets Integration
- Connects directly to Google Sheets as a data source  
- Automatically reads updated vendor data  
- Sends emails based on the latest sheet updates  
- Eliminates the need to modify code for data changes  

### Custom Email Content
- Dynamic email templates  
- Personalization using vendor name and context  

### Scheduling System
- Runs on a weekly schedule  
- Can be extended to support custom schedules  

## Tech Stack

- Backend: Python  
- Scheduling: schedule / cron jobs  
- Email Service: SMTP (Gmail or other providers)  
- Data Storage: Google Sheets / CSV / JSON / Database  

## How It Works

1. Vendor data is stored in Google Sheets or a local data source  
2. The scheduler runs every Monday  
3. The system fetches the latest data from the sheet  
4. It checks pending actions (payment/receipt)  
5. Emails are generated using templates  
6. Emails are sent automatically to respective vendors  

## Installation

```bash
git clone https://github.com/your-username/vendorpulse.git
cd vendorpulse
pip install -r requirements.txt

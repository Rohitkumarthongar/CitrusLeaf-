# Item Email Functionality

This document describes the email functionality implemented for the Item doctype in the testapp.

## Overview

A "Send Email" button has been added to the Item details page under the Actions menu. When clicked, this button sends an email to the current user with the latest 5 sales invoices for that item as PDF attachments.

## Implementation Details

### Files Created/Modified

1. **`testapp/api/email.py`** - Contains the main email sending logic
2. **`testapp/public/js/item.js`** - Custom JavaScript for the Item form
3. **`testapp/hooks.py`** - Updated to include the custom script
4. **`testapp/api/test_email.py`** - Test script for the functionality

### Features

- **Custom Button**: Added "Send Email" button under Actions menu in Item form
- **Email Template**: Uses Jinja template for HTML email formatting
- **PDF Attachments**: Automatically generates and attaches PDFs of the latest 5 sales invoices
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Confirmation Dialog**: Asks for user confirmation before sending email

### Email Template

The email includes:
- Item code in the subject and body
- Table with invoice details (number, date, customer, amount)
- PDF attachments for each invoice
- Professional HTML formatting

### Usage

1. Navigate to any Item in the system
2. Click the "Send Email" button under the Actions menu
3. Confirm the action in the dialog
4. The system will send an email with the latest 5 sales invoices

### API Method

The main API method is `testapp.api.email.send_item_invoices_email(item_code)` which:
- Fetches the latest 5 sales invoices for the item
- Generates PDFs for each invoice
- Creates an HTML email with invoice details
- Sends the email with attachments

### Error Handling

- Handles cases where no invoices exist for the item
- Manages PDF generation errors gracefully
- Provides user feedback for all operations
- Logs errors for debugging

## Testing

Use the test script `testapp/api/test_email.py` to test the functionality:

```python
from testapp.api.test_email import test_email_functionality
test_email_functionality()
```

## Requirements

- Frappe/ERPNext system with Item and Sales Invoice doctypes
- Proper email configuration in the system
- User must have permissions to access Item and Sales Invoice data

# Installation Guide for Item Email Functionality

## Prerequisites

- Frappe/ERPNext system installed and running
- Email configuration set up in the system
- Access to create custom scripts and API methods

## Installation Steps

### 1. Install the App

If not already installed, install the testapp:

```bash
bench get-app testapp
bench install-app testapp
```

### 2. Restart the System

After installation, restart the system to load the new files:

```bash
bench restart
```

### 3. Clear Cache

Clear the system cache to ensure new JavaScript files are loaded:

```bash
bench clear-cache
```

### 4. Verify Installation

1. Navigate to any Item in the system
2. Look for the "Send Email" button under the Actions menu
3. If the button is not visible, check the browser console for JavaScript errors

## Configuration

### Email Settings

Ensure email is properly configured in the system:

1. Go to **Setup > Email > Email Account**
2. Configure your email account settings
3. Test the email configuration

### Permissions

Ensure the user has the following permissions:
- Read access to Item doctype
- Read access to Sales Invoice doctype
- Access to send emails

## Testing

### Manual Testing

1. Open any Item that has sales invoices
2. Click the "Send Email" button
3. Confirm the action
4. Check your email for the message with attachments

### Automated Testing

Run the test script:

```python
# In Frappe console
from testapp.api.test_email import test_email_functionality
test_email_functionality()
```

## Troubleshooting

### Common Issues

1. **Button not visible**: Check if the JavaScript file is loaded correctly
2. **Email not sent**: Verify email configuration and permissions
3. **No invoices found**: Ensure the item has associated sales invoices
4. **PDF generation errors**: Check if the Sales Invoice doctype has proper print format

### Debug Steps

1. Check browser console for JavaScript errors
2. Check Frappe logs for server-side errors
3. Verify email configuration
4. Test with a different item that has sales invoices

## Support

For issues or questions:
- Check the Frappe logs
- Verify all files are in the correct locations
- Ensure proper permissions are set
- Test with a fresh browser session

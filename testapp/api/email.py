import frappe
from frappe.utils import get_files_path
from frappe import _
import os


@frappe.whitelist()
def send_item_invoices_email(item_code):
	try:
		invoices = frappe.get_all('Sales Invoice Item',
			filters={'item_code': item_code},
			fields=['parent'],
			order_by='creation desc',
			limit_page_length=5
		)

		if not invoices:
			frappe.msgprint(_('No sales invoices found for this item.'))
			return False

		invoice_names = [inv['parent'] for inv in invoices]

		invoice_details = frappe.get_all('Sales Invoice',
			filters={'name': ['in', invoice_names]},
			fields=['name', 'posting_date', 'customer', 'grand_total']
		)

		attachments = []
		for invoice in invoice_details:
			try:
				pdf_data = frappe.get_print('Sales Invoice', invoice.name, as_pdf=True)
				attachments.append({
					'fname': f"{invoice.name}.pdf", 
					'fcontent': pdf_data
				})
			except Exception as e:
				frappe.log_error(f"Error generating PDF for {invoice.name}: {str(e)}")
				continue

		email_template = get_email_template()
		message = frappe.render_template(email_template, {'invoices': invoice_details, 'item_code': item_code})

		frappe.sendmail(
			recipients=frappe.session.user,
			subject=f"Latest Sales Invoices for Item: {item_code}",
			message=message,
			attachments=attachments
		)

		frappe.msgprint(_('Email sent successfully with latest 5 sales invoices.'))
		return True

	except Exception as e:
		frappe.log_error(f"Error sending item invoices email: {str(e)}")
		frappe.msgprint(_('Error sending email. Please try again.'))
		return False


def get_email_template():
	return """
	<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
		<h2 style="color: #2c3e50;">Latest Sales Invoices for Item: {{ item_code }}</h2>
		
		<p>Dear User,</p>
		
		<p>Please find attached the latest five sales invoices for the item <strong>{{ item_code }}</strong>.</p>
		
		<h3>Invoice Details:</h3>
		<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
			<thead>
				<tr style="background-color: #f8f9fa;">
					<th style="border: 1px solid #dee2e6; padding: 12px; text-align: left;">Invoice Number</th>
					<th style="border: 1px solid #dee2e6; padding: 12px; text-align: left;">Date</th>
					<th style="border: 1px solid #dee2e6; padding: 12px; text-align: left;">Customer</th>
					<th style="border: 1px solid #dee2e6; padding: 12px; text-align: right;">Amount</th>
				</tr>
			</thead>
			<tbody>
				{% for invoice in invoices %}
				<tr>
					<td style="border: 1px solid #dee2e6; padding: 12px;">{{ invoice.name }}</td>
					<td style="border: 1px solid #dee2e6; padding: 12px;">{{ invoice.posting_date }}</td>
					<td style="border: 1px solid #dee2e6; padding: 12px;">{{ invoice.customer or 'N/A' }}</td>
					<td style="border: 1px solid #dee2e6; padding: 12px; text-align: right;">{{ "₹{:,.2f}".format(invoice.grand_total) if invoice.grand_total else 'N/A' }}</td>
				</tr>
				{% endfor %}
			</tbody>
		</table>
		
		<p style="margin-top: 30px;">
			<strong>Note:</strong> The PDF attachments contain the complete invoice details for each of the above invoices.
		</p>
		
		<p>Best regards,<br>
		<strong>Your Company</strong></p>
	</div>
	"""

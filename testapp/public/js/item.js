frappe.ui.form.on('Item', {
	refresh: function(frm) {
		frm.add_custom_button(__('Send Email'), function() {
			frappe.confirm(
				__('Do you want to send an email with the latest 5 sales invoices for this item?'),
				function() {
					frm.dashboard.set_headline_alert(__('Sending email...'), 'blue');
					
					frappe.call({
						method: 'testapp.api.email.send_item_invoices_email',
						args: {
							item_code: frm.doc.item_code
						},
						callback: function(response) {
							frm.dashboard.clear_headline();
							
							if (response.message) {
								frappe.msgprint({
									title: __('Success'),
									message: __('Email sent successfully with the latest 5 sales invoices.'),
									indicator: 'green'
								});
							} else {
								frappe.msgprint({
									title: __('Error'),
									message: __('Failed to send email. Please try again.'),
									indicator: 'red'
								});
							}
						},
						error: function(err) {
							frm.dashboard.clear_headline();
							
							frappe.msgprint({
								title: __('Error'),
								message: __('An error occurred while sending the email. Please try again.'),
								indicator: 'red'
							});
						}
					});
				},
				__('Send Email'),
				__('Cancel')
			);
		}, __('Actions'));
	}
});

frappe.pages['fund-list'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Fund List',
		single_column: true
	});
		
	page.set_primary_action('Refresh Data', function() {
		frappe.call({
			method: 'sipplanner.sipplanner.api.fetch_fund_data',
			callback: function(r) {
				frappe.msgprint(r.message);
				loadFundData();
			}
		});
	});

	function loadFundData() {
		frappe.call({
			method: 'frappe.client.get_list',
			args: {
				doctype: 'Fund',
				fields: ['name', 'dividend_type', 'scheme_type', 'plan', 'last_price']
			},
			callback: function(r) {
				if (r.message) {
					var html = '<table class="table table-bordered">';
					html += '<tr><th>Name</th><th>Code</th><th>Company</th><th>Amount</th></tr>';
					r.message.forEach(function(fund) {
						html += '<tr>';
						html += '<td>' + fund.name + '</td>';
						html += '<td>' + fund.dividend_type + '</td>';
						html += '<td>' + fund.scheme_type + '</td>';
						html += '<td>' + fund.plan + '</td>';
						html += '<td>' + fund.last_price + '</td>';
						html += '</tr>';
					});
					html += '</table>';
					$(wrapper).find('.layout-main-section').html(html);
				}
			}
		});
	}

	loadFundData();
	
}
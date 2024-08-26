// Copyright (c) 2024, Drishya R and contributors
// For license information, please see license.txt

frappe.ui.form.on("SIP", {
    refresh(frm) {

        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Sip Membership', {
                library_member: frm.doc.name
            })
        })
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Sip Transaction', {
                library_member: frm.doc.name
            })
        })
    },
});

def open_customer_dashboard():
	customer_dashboard_window.show()
	customerlogin_window.hide()

employee_dashboard_window = Window(app, title = "Employee Dashboard")
employee_dashboard_window.hide()
text_blank = Text(app, text=" ")
text_blank = Text(app, text=" ")
emdash_title = Text(employee_dashboard_window, text ="Employee Dashboard")
emdash_title.text_size = 20

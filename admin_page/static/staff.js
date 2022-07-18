function edit_staff(username, first_name, last_name, other_names, email, phone, salary) {
	$("#id").val(username);
	$("#fname").val(first_name);
	$("#lname").val(last_name);
	$("#onames").val(other_names);
	$("#email").val(email);
	$("#phone").val(phone);
	$("#salary").val(salary);
}

function delete_staff() {
	let id = $("#id").val();
	var a = confirm(
		"Are you sure you want to delete user: " +
			id +
			"\nNote: The staff will not beable to login to the portal again."
	);
	if (!a) return;
	fetch("/delete-staff/"+id)
	.then((res) => {
		location.reload()
	});
}

function edit(id, first_name, last_name, email, phone) {
	$("#id").val(id);
	$("#fname").val(first_name);
	$("#lname").val(last_name);
	$("#email").val(email);
	$("#phone").val(phone);
}

function delete_contact() {
	let id = $("#id").val();
	var a = confirm(
		"Are you sure you want to delete this contact"
	);
	if (!a) return;
	fetch("/delete-contact/"+id)
	.then((res) => {
		location.reload()
	});
}

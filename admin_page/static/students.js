function edit_student(username, first_name, last_name, other_names, email, phone) {
	$("#id").val(username);
	$("#fname").val(first_name);
	$("#lname").val(last_name);
	$("#onames").val(other_names);
	$("#email").val(email);
	$("#phone").val(phone);
}

function delete_student() {
	let id = $("#id").val();
	var a = confirm(
		"Are you sure you want to delete STUDENT: " +
			id +
			"\nNote: The student will not beable to login to the portal again."
	);
	if (!a) return;
	$("#delete_student_btn").prop("disabled", true);
	fetch("/delete-student/"+id)
	.then((res) => {
		location.reload()
	});
}

$("#update_student").submit((e) => {
	$("#update_student_btn").prop("disabled", true);
});
$("#create_student").submit((e) => {
	$("#create_student_btn").prop("disabled", true);
});

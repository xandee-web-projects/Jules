function alert_mesage(message, category) {
	return `<div class="card-body p-3 pb-0">
    <div class="container">
    <div class="alert alert-${category} alert-dismissible text-white" role="alert">
      <span class="text-sm">${message}</span>
      <button type="button" class="btn-close text-lg py-3 opacity-10" data-bs-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  </div>`;
}

function edit_staff(s) {
	$("#id").val(s._id);
	$("#fname").val(s.fname);
	$("#lname").val(s.lname);
	$("#onames").val(s.onames);
	$("#email").val(s.email);
	$("#phone").val(s.phone);
	$("#salary").val(s.salary);
}

function delete_staff() {
	var _id = $("#id").val();
	var a = confirm(
		"Are you sure you want to delete user: " +
			_id +
			"\nNote: The staff will not beable to login to the portal again."
	);
	if (!a) return;
	$("#delete_staff_btn").prop("disabled", true);
	fetch("/a/delete-staff", {
		method: "POST",
		body: JSON.stringify({ id: _id }),
	}).then((res) => {
		window.location.href = "/a/staff";
	});
}

$("#update_staff").submit((e) => {
	$("#update_staff_btn").prop("disabled", true);
});
$("#create_staff").submit((e) => {
	$("#create_staff_btn").prop("disabled", true);
});

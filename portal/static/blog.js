function edit_blog(blog) {
	$("#id").val(blog._id);
	$("#heading").val(blog.heading);
	$("#desc").val(blog.desc);
}

function delete_blog() {
	var _id = $("#id").val();
	var a = confirm("Are you sure you want to delete this blog");
	if (!a) return;
	$("#delete_blog_btn").prop("disabled", true);
	fetch("/a/delete-blog", {
		method: "POST",
		body: JSON.stringify({ id: _id }),
	}).then((res) => {
		window.location.href = "/a/edit-blogs";
	});
}

$("#update_blog").submit((e) => {
	$("#update_blog_btn").prop("disabled", true);
});
$("#create_blog").submit((e) => {
	$("#create_blog_btn").prop("disabled", true);
});

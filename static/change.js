const na_re = new RegExp("^ *[a-zA-Z]+ *$");
const ph_re = new RegExp("^ *[0-9]{10} *$");
const em_re = new RegExp("^ *[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+ *$");
var ph_old_ = "";

async function request_update(na, ph_new, em, ph_old) {
	const response = await fetch(`/api/update/?na=${na}&ph=${ph_new}&em=${em}&with=${ph_old}`, {
		method: "UPDATE",
	});
	return await response.status;
}

async function request_delete(ph) {
	const response = await fetch(`/api/delete/?with=${ph}`, {
		method: "DELETE",
	});
	return await response.status;
}

async function request(ph) {
	const response = await fetch(`/api/search?ph=${ph}`);
	return await response.json();
}
async function on_change_name() {
	let name_temp = document.getElementById("name");
	if (na_re.test(name_temp.value)) {
		name_temp.style.border = "green solid 2px";
		return 1;
	}
	name_temp.style.border = "red solid 2px";
	return 1;
}

async function on_change_phone() {
	let phone_temp = document.getElementById("phone");
	if (ph_re.test(phone_temp.value)) {
		phone_temp.style.border = "green solid 2px";
		return 1;
	}

	phone_temp.style.border = "red solid 2px";
	return 0;
}

async function on_change_email() {
	let email_temp = document.getElementById("email");
	if (em_re.test(email_temp.value)) {
		email_temp.style.border = "green solid 2px";
		return 1;
	}
	email_temp.style.border = "red solid 2px";
	return 0;
}

async function fill(data) {
	let game_list = document.getElementById("ta_hold");
	game_list.innerHTML = "";
	if (data.length == 0) {
		game_list.innerHTML = "No record found";
		document.getElementById("c2").style.visibility = "hidden";
		return;
	}

	let table_temp = document.createElement("table");
	table_temp.setAttribute("id", "list_phone");

	table_temp.innerHTML =
		"<tr> \
        <th>Id</th> \
        <th>Name</th> \
        <th>Phone</th> \
        <th>Email</th> \
      </tr>";

	let alist = document.createElement("tr");
	alist.setAttribute("class", "ltr");
	alist.innerHTML = `<tr> \
                        <td>${data[0].id}</td> \
                        <td>${data[0].name}</td> \
                        <td>${data[0].phone}</td> \
                        <td>${data[0].email}</td> \
                       </tr>`;
	table_temp.appendChild(alist);
	game_list.appendChild(table_temp);
	document.getElementById("c2").style.visibility = "visible";
	ph_old_ = data[0].phone;
}
async function check_phone() {
	if (!on_change_phone()) {
		return 0;
	}
	let phone_temp = document.getElementById("phone").value;
	request(phone_temp).then((data) => {
		fill(data.data);
	});
}

async function update_phone() {
	let name = document.getElementById("name");
	let phone = document.getElementById("phone_1");
	let email = document.getElementById("email");

	if (!on_change_name() || !on_change_phone() || !on_change_email()) {
		return 0;
	}
	console.log(name.value);
	console.log(phone.value);
	console.log(email.value);
	request_update(name.value, phone.value, email.value, ph_old_).then((data) => {
		alert("successfully updated");
		name.value = "";
		email.value = "";
		phone.value = "";
		ph_old_ = "";
	});

}
async function delete_phone() {
	request_delete(ph_old_).then((data) => {
		alert("successfully deleted");
		ph_old_ = "";
	});
}
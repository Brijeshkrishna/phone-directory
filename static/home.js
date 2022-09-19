const na_re = new RegExp("^ *[a-zA-Z]+ *$");
const ph_re = new RegExp("^ *[0-9]{10} *$");
const em_re = new RegExp("^ *[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+ *$");

fill();

async function request() {
	const response = await fetch("/api/getAllRecord");
	return await response.json();
}

async function upload_phone(name, ph, email) {
	const response = await fetch(`/api/addRecord/?na=${name}&ph=${ph}&em=${email}`, {
		method: "POST",
	});
	return await response.status;
}

async function appendChildtohtml(data) {
	let game_list = document.getElementById("list_phone");

	for (let i in data) {
		let alist = document.createElement("tr");
		alist.setAttribute("class", "ltr");
		alist.innerHTML = `<tr> \
        <td>${data[i].id}</td> \
        <td>${data[i].name}</td> \
        <td>${data[i].phone}</td> \
        <td>${data[i].email}</td> \
    </tr>`;
		game_list.appendChild(alist);
	}
}

async function fill() {
	request().then((data) => {
		appendChildtohtml(data.data);
	});
}

async function clear_fill() {
	let game_list = document.getElementById("list_phone");
	game_list.innerHTML = "";
	game_list.innerHTML =
		"<tr> \
      <th>Id</th> \
      <th>Name</th> \
      <th>Phone</th> \
      <th>Email</th> \
    </tr>";
}

async function refresh() {
	clear_fill();
	fill();
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

async function addPhone() {
	let name = document.getElementById("name");
	let phone = document.getElementById("phone");
	let email = document.getElementById("email");

	if (!on_change_name() || !on_change_phone() || !on_change_email()) {
		return 0;
	}

	upload_phone(name.value, phone.value, email.value).then((data) => {});

	alert("successfully submitted");
	name.value = "";
	email.value = "";
	phone.value = "";
}
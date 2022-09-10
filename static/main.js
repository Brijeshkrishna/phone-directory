async function request() {
  const response = await fetch("/api/getPhones");
  return await response.json();
}

async function upload_phones(name, cc, ph) {
  const response = await fetch(`/addPhone/?na=${name}&cc=${cc}&ph=${ph}`, {
    method: "POST",
  });
  return await response.status;
}

function appendChildtohtml(data) {
  let game_list = document.getElementById("list_phone");

  console.log(data);
  for (let i in data) {
    let alist = document.createElement("tr");
    alist.setAttribute("class", "ltr");
    alist.innerHTML = `<tr> \
        <td>${data[i].name}</td> \
        <td>${data[i].country_code}</td> \
        <td>${data[i].phone_num}</td> \
    </tr>`;
    game_list.appendChild(alist);
  }
}

async function fill() {
  request().then((data) => {
    appendChildtohtml(data.data);
  });
}

function clear_fill() {
  let game_list = document.getElementById("list_phone");
  game_list.innerHTML = "";
  game_list.innerHTML =
    "<tr> \
      <th>Name</th> \
      <th>Country Code</th> \
      <th>Phone</th> \
    </tr>" ;
    console.log(game_list.innerHTML);

}

function refresh() {
  clear_fill();
  fill();
}
fill();

async function addPhone() {
  let name = document.getElementById("name");
  let country = document.getElementById("country_code");
  let phone = document.getElementById("phone_number");
  

  upload_phones(name.value, country.value, phone.value).then((data) => {

  });

  name.value="";
  country.value="";
  phone.value="";
}

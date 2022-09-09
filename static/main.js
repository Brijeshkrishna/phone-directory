async function request() {
  const response = await fetch("/api/getPhones");
  return await response.json();
}

function appendChildtohtml(data) {
  let game_list = document.getElementById("list_phone");
  let alist = document.createElement("tr");

  for (let i in data) {
    alist.innerHTML =
      "<tr> \
        <td>${i.name}</td> \
        <td>${i.country_code}</td> \
        <td>${i.phone_num}</td> \
    </tr>";
    game_list.appendChild(alist);
  }
}

async function fill() {
  request().then((data) => {
    appendChildtohtml(data);
  });
}


fill();
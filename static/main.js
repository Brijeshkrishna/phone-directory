

const na_re = new RegExp('^[a-zA-Z]+$');
const ph_re = new RegExp('^[0-9]{10}$');
const cc_re = new RegExp('^[0-9]{2}$');


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
        <td>${data[i].id}</td> \
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
      <th>Id</th> \
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

function change_name(){
  let name = document.getElementById("name");
  if (! na_re.test(name.value) ){
    name.style.border = "red solid 2px"
    
  }
  else{
    name.style.border ="green solid 2px";
    check_3=check_3+1;
    btnsubmit.disabled = 1;


  }
 
 
}

function change_country(){
  let country = document.getElementById("country_code");
  if (! cc_re.test(country.value) ){
    country.style.border = "red solid 2px"
    check_3=check_3-1;

  }
  else{
    country.style.border ="green solid 2px";
    check_3=check_3+1;
    btnsubmit.disabled = 1;

  }

  
}

function change_phone(){
  let phone = document.getElementById("phone_number");
  if (! ph_re.test(phone.value) ){
    phone.style.border = "red solid 2px"
    check_3=check_3-1;
    btnsubmit.disabled = 1;


  }
  else{
    phone.style.border ="green solid 2px";
    check_3=check_3+1;

  }


}

async function addPhone() {

  let name = document.getElementById("name");
  let country = document.getElementById("country_code");
  let phone = document.getElementById("phone_number");
  
  if (! na_re.test(name.value) ){
    name.style.border = "red solid 2px"
    return;
  }
  name.style.border ="green solid 2px";
 
  if (! cc_re.test(country.value) ){
    country.style.border = "red solid 2px"
    return;
    
  }
  country.style.border ="green solid 2px";

  if (! ph_re.test(phone.value) ){
    phone.style.border = "red solid 2px"
    return;
    
  }
  phone.style.border ="green solid 2px";

  upload_phones(name.value, country.value, phone.value).then((data) => {

  });

  name.value ="" ;
  country.value="";
  phone.value="";
  alert("successfully submitted");


}

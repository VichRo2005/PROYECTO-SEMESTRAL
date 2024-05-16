let tbody = document.getElementById("data-out")

//fetch function

fetch("http://localhost:3000/user")
.then(res=>res.json())
.then(json=>{
    json.map(data=>{
        console.log(data)
        tbody.append(td_function(data.itnombre,data.itapellido,data.itcorreo,data.ittelefono,data.u_id,data.permisos));
    })
})



// create td
function td_function(itnombre,itapellido,itcorreo,ittelefono,u_id,permisos){
    let td = document.createElement('tr');
    td.innerHTML = `

    <td>${itnombre}</td>
    <td>${itapellido}</td>
    <td>${itcorreo} </td>
    <td>${ittelefono} </td>
    <td>${u_id} </td>
    <td>${permisos} </td>

    
    `;
    return td
}


$(document).ready(function () {
    $.getJSON('/api/propertylist', function (data) {
      var htm = `<table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Birth</th>
          <th scope="col">Contact Details</th>
          <th scope="col">Address</th>
          <th scope="col">Picture</th>
          <th scope="col">Update</th>
        </tr>
      </thead>
     <tbody>`
  
      data.map((item) => {
        htm += `<tr>
  <th th scope = "row" > ${item.id}</th> 
  <td>${item.property_name}</td>
  <td>${item.description}</td>       
  <td>${item.area_sq_feet} </td>
  <td>${item.num_bedrooms}</td>       
  <td>${item.num_bathrooms}</td>       
  <td>${item.hospitals_nearby}</td>       
  <td>${item.colleges_nearby}</td>       
  <td>${item.created_at}</td>       
  <td>${item.seller_name}</td>       
  <td>${item.dob}</td>       
  <td>${item.dob}</td>       
  <td>${item.email_id} <br>${item.mobile_no}</td>       
  <td>${item.address} <br>${item.cityname}<br>${item.statename}</td>              
  <td><a href='/api/displaypropertyimage?sellerid=${item.id}&sellername=${item.firstname} ${item.lastname}&picture=${item.image}'><img src="/${item.image}" width="30" ></a></td>
  <td><a href='/api/propertybyid?propertyid=${item.id}'>Update/Delete</a></td>`
      })
  
      htm += `</tbody ></table > `
      $('#PropertyData').html(htm)
  
    })
  })
  
  


$(document).ready(function () {
    $.getJSON("http://localhost:8000/api/property_list", function (data) {


        data.map((item) => {
            $('#propertyid').append($('<option>').text(item.roperty_name).val(item.id))



        })
    })
})
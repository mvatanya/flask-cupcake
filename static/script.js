const BASE_URL = "http://localhost:5000"

$(document).ready(async function(){
    const response = await axios.get(`${BASE_URL}/cupcakes`)
    for (let cupcake of response.data.cupcakes){
        $("#cupcake-container").append(`<li>Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating} </li>`);
    }

    $("#add-form").on("submit", async function(evt){
        evt.preventDefault();
        let flavor = $("#flavor").val();
        let size = $("#size").val();
        let rating = $("#rating").val();
        let img = $("#img-url").val();
    
        const response = await axios.post(`${BASE_URL}/cupcakes`, {
            "flavor" : flavor,
            "size" : size,
            "rating": rating,
            "image": img
        })
    
        let cupcake = response.data.cupcake
        $("#cupcake-container").append(`<li>Flavor: ${cupcake.flavor}, Size: ${cupcake.size}, Rating: ${cupcake.rating} </li>`);
        

    })
})





$('.delete-cupcake').click(deleteCupcake)


async function deleteCupcake() {

    const id =$(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()

}

$('form').on('submit', async function (evt) {
    evt.preventDefault()
    const flavor = $('#flavor').val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val();
   
   
    var res = await axios.post( '/api/cupcakes', {     
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image
    })
    cupcake = res.data.cupcake
    $('ul').append(`<li> ${cupcake.size} ${cupcake.flavor} cupcake <img src="${cupcake.image}" class="img-thumbnail"><button class=" style="max-width: 150px" class="delete-cupcake btn-danger" data-id="${cupcake.id}">x</button> </li>`)
}) 


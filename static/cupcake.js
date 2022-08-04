



$('.delete-cupcake').click(deleteCupcake)


async function deleteCupcake() {

    const id =$(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()

}

$('form').on('submit', addCupcake) 


async function addCupcake() {
    const flavor = $('#flavor').val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val();
    var resp = await axios.post( '/api/cupcakes', {     
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image
    })

    return 

}
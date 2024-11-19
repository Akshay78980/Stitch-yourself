
document.addEventListener('DOMContentLoaded', async function (){
    try{
        const response = await fetch('/api/product-variant/')

        if (response.ok){
            data = await response.json();
            productsContainer = document.getElementById('mainDiv')
            productsContainer.innerHTML = ""
            let content = `<div class="container my-5">
                            <div class="row">`
            data.forEach(function(product){
                let productCard = `
                                <div class="col-md-2 col-sm-6 mb-4">
                                    <a href="" class='product_link text-decoration-none text-dark' data-id=${product.id}>
                                        <div class="card h-100">
                                            <img src="${product.image1}" class="card-img-top h-75" style="object-fit:cover" alt="Product Image">
                                            <div class="card-body">
                                                <h5 class="card-title">${product.product.name}</h5>
                                                <p class="card-text">Rs. ${product.variant_price || product.product.price || ""}</p>
                                                <p class="card-text fs-6">${(product.description || product.product.description).slice(0,20) + "..."}</p>  
                                            </div>
                                        </div>
                                    </a>
                                </div>
                            
                        `
                content += productCard
            })
            productsContainer.innerHTML = content + `</div></div>`

            const productTiles = document.querySelectorAll('.product_link');
            
            productTiles.forEach(tile => {
                const productId = tile.getAttribute('data-id');
                tile.href = `/product/${productId}/`;
            });
            
            

        }
        else{
            console.log("Error")
        }
    }
    catch(error){
        console.log(error)
    }
})
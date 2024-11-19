document.addEventListener("DOMContentLoaded", function(event){
    event.preventDefault();
    
    const pathParts = window.location.pathname.split('/')
    const productVariantId = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2]

    const mainDiv = document.getElementById('mainDiv');
    mainDiv.classList.add('card');

    getProductDetails(productVariantId)

    
})


async function getProductDetails(productVariantId){
    try{
        const response = await fetch(`/api/product-variant/${productVariantId}/`)
        const sizesDiv = document.getElementById('sizesAvailable')
        const stockAvailableDiv = document.getElementById('availableStocksDiv')
        sizesDiv.innerHTML = ""

        if (response.ok) {
            product = await response.json();
            document.getElementById("productImage").src = product.image1;
            document.getElementById("productName").textContent = product.product.name;
            document.getElementById("productPrice").textContent = `Rs. ${product.variant_price || product.product.price}`;
            document.getElementById("productDescription").textContent = product.description || product.product.description;
            if (!product.quantity){
                stockAvailableDiv.innerHTML = `Currently out of stock`
                stockAvailableDiv.classList.replace("text-success", 'text-danger')
                stockAvailableDiv.style.fontWeight = "normal"
            }
            else if (product.quantity<=7){
                stockAvailableDiv.innerHTML = `Only ${product.quantity} left in stock`
                if(product.quantity<5)
                    stockAvailableDiv.classList.replace("text-success", 'text-warning')
                else if(product.quantity<=3)
                    stockAvailableDiv.classList.replace("text-success", 'text-danger')
            }
            const sizes = await getSizesAvailable(product.product.group_sku_number, product.color)
            if(sizes){
                sizes.forEach(size => {
                    sizesDiv.innerHTML += `<button id='btn-${size}' onclick="changeSize(event)" class="btn btn-outline-primary m-2">${size}</button>`
                })
                document.getElementById(`btn-${product.size}`).classList.add('btn-primary', 'text-light');
            }
        }

        else {
            console.error("Failed to load product data.");
        }
    }
    catch(error){
        console.log(error)
    }

}

async function changeSize(event){
    const currentSizeBtn = document.getElementById('sizesAvailable').querySelector('.btn-primary.text-light')
    const clickedSizeBtn = event.target; 
    if(currentSizeBtn){
        currentSizeBtn.classList.remove('btn-primary','text-light');
    }
    clickedSizeBtn.classList.add('btn-primary', 'text-light');
    const targetSize = clickedSizeBtn.innerText;
    const response = await fetch(`/api/product`, {
        method: 'POST', // Adjust to the appropriate HTTP verb
        headers: { 'Content-Type': 'application/json' }, // Adjust if sending data
        body: JSON.stringify({ selectedSize: targetSize }) // Optional: Include size in request body
      });
}




async function getSizesAvailable(groupSkuNumber, productColor) {
    try {
        const response = await fetch(`/api/product-sizes/${groupSkuNumber}/${productColor}/`);
        if (response.ok) {
            const data = await response.json();
            return data.sizes;
        } else {
            console.error("Failed to fetch available sizes");
            return [];
        }
    } catch (error) {
        console.error("Error fetching sizes:", error);
        return [];
    }
}

// async function getAvailableStockCount(productVariantId){
//     const response = await fetch(`/api/product-variant/${productVariantId}/count/`);
//     const availableStocksDiv = document.get
// }



document.addEventListener('DOMContentLoaded', function() {
    const addButtonElements = document.querySelectorAll('.add-button');
    const selectedItemsBody = document.getElementById('selected-items-body');
    const totalPriceElement = document.getElementById('total-price');
    const checkoutButton = document.getElementById('checkout-button');
    let totalPrice = 0.00;
    const selectedItems = {};

    console.log("DOM fully loaded and parsed");

    addButtonElements.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-id');
            const itemName = this.getAttribute('data-name');
            const itemPrice = parseFloat(this.getAttribute('data-price'));

            if (selectedItems[itemId]) {
                selectedItems[itemId].quantity += 1;
                selectedItems[itemId].totalPrice += itemPrice;
                const row = document.querySelector(`#selected-items-body tr[data-id="${itemId}"]`);
                row.querySelector('.selected-quantity').textContent = selectedItems[itemId].quantity;
                row.querySelector('.selected-total').textContent = selectedItems[itemId].totalPrice.toFixed(2);
            } else {
                selectedItems[itemId] = {
                    itemId: itemId,
                    itemName: itemName,
                    itemPrice: itemPrice,
                    quantity: 1,
                    totalPrice: itemPrice
                };
                const newRow = document.createElement('tr');
                newRow.setAttribute('data-id', itemId);
                newRow.innerHTML = `
                    <td>${itemName}</td>
                    <td>${itemPrice.toFixed(2)}</td>
                    <td class="selected-quantity">1</td>
                    <td class="selected-total">${itemPrice.toFixed(2)}</td>
                `;
                selectedItemsBody.appendChild(newRow);
            }

            totalPrice += itemPrice;
            totalPriceElement.textContent = totalPrice.toFixed(2);

            console.log(`Added item ${itemName} with ID ${itemId}`);
        });
    });

    checkoutButton.addEventListener('click', function() {
        const items = Object.values(selectedItems);
        const total = totalPrice;

        console.log("Checkout button clicked");

        fetch(checkoutUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({items: items, total: total})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Checkout successful");
                window.location.href = saleCheckoutUrl;
            } else {
                alert('Something went wrong. Please try again.');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


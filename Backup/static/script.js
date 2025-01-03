// const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");

if (bar) {
  bar.addEventListener("click", () => {
    nav.classList.add("active");
  });
}

if (close) {
  close.addEventListener("click", () => {
    nav.classList.remove("active");
  });
}

// Single Product

var mainImg = document.getElementById("mainimg");
var smallImg = document.getElementsByClassName("small-img");

smallImg[0].onclick = function () {
  mainImg.src = smallImg[0].src;
};

smallImg[1].onclick = function () {
  mainImg.src = smallImg[1].src;
};

smallImg[2].onclick = function () {
  mainImg.src = smallImg[2].src;
};

smallImg[3].onclick = function () {
  mainImg.src = smallImg[3].src;
};

document.addEventListener("DOMContentLoaded", () => {
  const cart = [];

  function addToCart(product) {
    const existingProduct = cart.find((item) => item.name === product.name);
    if (existingProduct) {
      existingProduct.quantity += 1;
    } else {
      cart.push({ ...product, quantity: 1 });
    }
    renderCart();
  }

  function removeFromCart(productName) {
    const productIndex = cart.findIndex((item) => item.name === productName);
    if (productIndex !== -1) {
      cart.splice(productIndex, 1);
    }
    renderCart();
  }

  function renderCart() {
    const cartTableBody = document.querySelector("#cart tbody");
    cartTableBody.innerHTML = "";

    cart.forEach((product) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td><img src="pro-img/one.jpg" alt=""></td>
                <td>${product.name}</td>
                <td>₹${product.price}</td>
                <td><input type="number" value="${
                  product.quantity
                }" data-name="${product.name}" class="cart-quantity"></td>
                <td>₹${product.price * product.quantity}</td>
                <td><a href="#" class="remove-from-cart" data-name="${
                  product.name
                }"><i class="fa-regular fa-circle-xmark"></i></a></td>
            `;
      cartTableBody.appendChild(row);
    });

    updateTotal();
  }

  function updateTotal() {
    const subtotal = cart.reduce(
      (sum, product) => sum + product.price * product.quantity,
      0
    );
    document.querySelector(
      "#subtotal td:last-child"
    ).textContent = `₹${subtotal}`;
    document.querySelector("#total td:last-child").textContent = `₹${subtotal}`;
  }

  document.querySelectorAll(".add-to-cart").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      const productElement = button.closest(".pro");
      const product = {
        name: productElement.getAttribute("data-name"),
        price: parseFloat(productElement.getAttribute("data-price")),
      };
      addToCart(product);
    });
  });

  document.querySelector("#cart tbody").addEventListener("click", (e) => {
    if (e.target.closest(".remove-from-cart")) {
      e.preventDefault();
      const productName = e.target
        .closest(".remove-from-cart")
        .getAttribute("data-name");
      removeFromCart(productName);
    }
  });

  document.querySelector("#cart tbody").addEventListener("change", (e) => {
    if (e.target.classList.contains("cart-quantity")) {
      const productName = e.target.getAttribute("data-name");
      const newQuantity = parseInt(e.target.value, 10);
      const product = cart.find((item) => item.name === productName);
      if (product) {
        product.quantity = newQuantity;
        renderCart();
      }
    }
  });
});

// ---------------------------> add to cart items
function addToCart() {
  // Get all selected menu items
  const selectedItems = [];
  const checkboxes = document.querySelectorAll(
    'input[name="menu-item"]:checked'
  );

  checkboxes.forEach((checkbox) => {
    selectedItems.push(checkbox.value);
  });

  // Save selected items to local storage
  localStorage.setItem("cartItems", JSON.stringify(selectedItems));

  // Redirect to cart page
  window.location.href = "cart.html";
}

document.addEventListener("DOMContentLoaded", function() {
  // Obtén todos los botones de "Agregar al carrito"
  const addToCartButtons = document.querySelectorAll(".add-to-cart");

  // Crea un array para almacenar los valores de los productos agregados al carrito
  const cartItems = [];

  // Agrega un evento de clic a cada botón de "Agregar al carrito"
  addToCartButtons.forEach(function(button) {
    button.addEventListener("click", function() {
      const item = this.parentNode;
      const itemName = item.querySelector("h3").textContent;
      const itemPrice = parseFloat(item.querySelector(".price").textContent);

      // Agrega el nombre y el precio del item al array del carrito
      cartItems.push({
        name: itemName,
        price: itemPrice
      });

      // Actualiza el carrito de compras y el total
      updateCart();
    });
  });

  // Actualiza el carrito de compras y el total
  function updateCart() {
    const cart = document.getElementById("cart");
    const total = document.getElementById("total");

    // Reinicia los contenidos del carrito y el total
    cart.innerHTML = "";
    total.textContent = "";

    // Recorre los items en el carrito y muestra su nombre y precio
    cartItems.forEach(function(item) {
      const cartItem = document.createElement("p");
      cartItem.textContent = item.name + " - $" + item.price.toFixed(2);
      cart.appendChild(cartItem);
    });

    // Calcula el total de la compra sumando los precios de los items en el carrito
    const totalPrice = cartItems.reduce(function(acc, item) {
      return acc + item.price;
    }, 0);

    // Muestra el total de la compra
    total.textContent = "Total: $" + totalPrice.toFixed(2);
  }
});
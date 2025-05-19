document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault(); // 🔁 Prevent page reload

      const formData = new FormData(form);

      fetch("/contact", {
        method: "POST",
        body: formData
      })
        .then((response) => response.text())
        .then((data) => {
          document.getElementById("form-message").innerText = data; // ✅ Show response
          form.reset(); // ✅ Clear form
        })
        .catch((error) => {
          document.getElementById("form-message").innerText = "Something went wrong.";
          console.error(error);
        });
    });
  }
});

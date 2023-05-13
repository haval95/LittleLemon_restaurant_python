const button = document.getElementById("menu");
const mobileMenu = document.getElementById('mobile-menu');

    button.addEventListener("click", () => {
        mobileMenu.classList.toggle('hidden');
    });
        const navbar = document.querySelector("nav");

        window.addEventListener("scroll", () => {
            if (window.scrollY > 100) {
                navbar.classList.remove("bg-transparent");
                navbar.classList.add("bg-white");
                navbar.classList.add("shadow");
            } else {
                navbar.classList.remove("bg-white");
                navbar.classList.remove("shadow");
                navbar.classList.add("bg-transparent");
            }
        });
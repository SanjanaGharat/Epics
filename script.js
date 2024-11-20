const menuIcon = document.getElementById('menu-icon');
        const mobileMenu = document.getElementById('mobile-menu');
        let hideTimeout;

        // Toggle the mobile menu
        menuIcon.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent click event from propagating to document
            menuIcon.querySelector('i').classList.toggle('bx-x');
            mobileMenu.classList.toggle('hidden');
        });

        // Close mobile menu when clicking anywhere on the document except the menu
        document.addEventListener('click', (e) => {
            if (!mobileMenu.contains(e.target) && !menuIcon.contains(e.target)) {
                mobileMenu.classList.add('hidden');
                menuIcon.querySelector('i').classList.remove('bx-x');
            }
        });

        function toggleDropdown(dropdownId) {
            const dropdown = document.getElementById(dropdownId);
            dropdown.classList.toggle('hidden');
        }

        // Delayed hiding of dropdown
        function handleMouseLeave(dropdownId) {
            hideTimeout = setTimeout(() => {
                document.getElementById(dropdownId).classList.add('hidden');
            }, 1000);
        }

        function clearHideTimeout() {
            clearTimeout(hideTimeout);
            document.getElementById('login-dropdown').classList.remove('hidden');
        }
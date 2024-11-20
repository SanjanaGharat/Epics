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


          // FAQ Toggle functionality with icon change
  const faqButtons = document.querySelectorAll('button[id^="faq"]');
  faqButtons.forEach(button => {
    button.addEventListener('click', () => {
      const content = document.querySelector(`#${button.id.replace('btn', 'content')}`);
      const icon = document.querySelector(`#${button.id.replace('btn', 'icon')}`);

      content.classList.toggle('hidden');
      const isHidden = content.classList.contains('hidden');
      button.classList.toggle('font-semibold', isHidden);
      button.classList.toggle('font-medium', !isHidden);

      // Toggle icon (open/close)
      icon.textContent = isHidden ? '+' : '−';
    });
  });



    // Array of service data (you can easily add more services by adding new objects to this array)
 const services = [
    {
        title: "Electrician",
        description: "Get professional electrical services from certified experts.",
        link: "electrician.html",
    },
    {
        title: "Plumber",
        description: "Reliable plumbing services, from pipe repairs to installation.",
        link: "plumber.html",
    },
    {
        title: "Computer Repair",
        description: "Get your computers fixed with top-notch hardware and software services.",
        link: "computer-repair.html",
    },
    {
        title: "Cleaning Services",
        description: "Our team provides thorough cleaning for homes and offices.",
        link: "cleaning-services.html",
    },
    {
        title: "Carpentry",
        description: "Expert carpentry services for furniture, repairs, and custom woodwork.",
        link: "carpentry.html",
    },
    {
        title: "Landscaping",
        description: "Transform your outdoor spaces with professional landscaping services.",
        link: "landscaping.html",
    },
    {
        title: "Pest Control",
        description: "Comprehensive pest control services to eliminate unwanted pests from your property.",
        link: "pest-control.html",
    },
    {
        title: "Painting Services",
        description: "Get your home or office painted with high-quality, long-lasting finishes.",
        link: "painting-services.html",
    },
    {
        title: "Air Conditioning Repair",
        description: "Ensure your AC is running efficiently with our expert repair and maintenance services.",
        link: "ac-repair.html",
    },
    {
        title: "Moving Services",
        description: "Professional moving services to help you relocate with ease and efficiency.",
        link: "moving-services.html",
    },
    {
        title: "Home Renovation",
        description: "Transform your living spaces with expert home renovation services.",
        link: "home-renovation.html",
    },
    {
        title: "Gardening Services",
        description: "Complete gardening services to keep your garden looking its best.",
        link: "gardening-services.html",
    },
    {
        title: "Security Systems",
        description: "Install and maintain advanced security systems for your home or business.",
        link: "security-systems.html",
    },
    {
        title: "Roofing Services",
        description: "Professional roofing solutions for repairs, replacements, and new installations.",
        link: "roofing-services.html",
    }
];


    // Function to create and append service cards dynamically
    function generateServiceCards() {
        const container = document.getElementById('services-grid');
        
        // Loop through each service and create the card HTML structure
        services.forEach(service => {
            const serviceCard = document.createElement('div');
            serviceCard.classList.add('service-card', 'rounded-lg', 'overflow-hidden', 'shadow-lg', 'hover:scale-105', 'transition-transform', 'duration-300', 'bg-indigo-600');
            
            const serviceContent = document.createElement('div');
            serviceContent.classList.add('service-content', 'p-6', 'text-white', 'text-center');
            
            const serviceTitle = document.createElement('h3');
            serviceTitle.classList.add('text-2xl', 'font-semibold', 'mb-2');
            serviceTitle.textContent = service.title;
            
            const serviceDescription = document.createElement('p');
            serviceDescription.classList.add('mb-4');
            serviceDescription.textContent = service.description;
            
            const learnMoreButton = document.createElement('a');
            learnMoreButton.classList.add('bg-transparent', 'border-2', 'border-white', 'text-white', 'px-6', 'py-2', 'rounded-full', 'hover:bg-white', 'hover:text-indigo-600', 'transition-all', 'duration-300');
            learnMoreButton.setAttribute('href', service.link);
            learnMoreButton.textContent = 'Learn More';

            // Append the title, description, and button to the service card
            serviceContent.appendChild(serviceTitle);
            serviceContent.appendChild(serviceDescription);
            serviceContent.appendChild(learnMoreButton);
            
            // Append the service card to the grid container
            serviceCard.appendChild(serviceContent);
            container.appendChild(serviceCard);
        });
    }

    // Generate the service cards when the page loads
    window.onload = generateServiceCards;

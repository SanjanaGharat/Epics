import requests

service_providers = [
{ 'name': 'John Doe', 'category': 'residential', 'service': 'electrician', 'image': 'https://placehold.co/300', 'rating': 4.5, 'cost': 'medium', 'description': 'Expert in home electrical repairs and installations.' },
{ 'name': 'Jane Smith', 'category': 'commercial', 'service': 'plumber', 'image': 'https://placehold.co/300', 'rating': 4.8, 'cost': 'high', 'description': 'Specialist in office and commercial space plumbing.' },
{ 'name': 'Mike Johnson', 'category': 'industrial', 'service': 'computer-repair', 'image': 'https://placehold.co/300', 'rating': 4.2, 'cost': 'low', 'description': 'Experienced in large-scale industrial computer repairs.' },
{ 'name': 'Sarah Lee', 'category': 'residential', 'service': 'cleaning-services', 'image': 'https://placehold.co/300', 'rating': 5.0, 'cost': 'medium', 'description': 'Trusted by hundreds for her quick and efficient cleaning service\'s.' },
{ 'name': 'Tom Harris', 'category': 'residential', 'service': 'electrician', 'image': 'https://placehold.co/300', 'rating': 4.7, 'cost': 'high', 'description': 'Skilled in home automation and electrical system upgrades.' },
{ 'name': 'Linda Green', 'category': 'commercial', 'service': 'plumber', 'image': 'https://placehold.co/300', 'rating': 4.9, 'cost': 'high', 'description': 'Commercial plumbing contractor with extensive experience in office buildings.' },
{ 'name': 'Alex Williams', 'category': 'industrial', 'service': 'computer-repair', 'image': 'https://placehold.co/300', 'rating': 4.6, 'cost': 'low', 'description': 'Expert in industrial computer repairs for large machinery.' },
{ 'name': 'Jessica Brown', 'category': 'residential', 'service': 'cleaning-services', 'image': 'https://placehold.co/300', 'rating': 4.3, 'cost': 'medium', 'description': 'Professional cleaner specializing in home cleanups and repairs.' },
{ 'name': 'Paul Davis', 'category': 'residential', 'service': 'gardening', 'image': 'https://placehold.co/300', 'rating': 4.8, 'cost': 'medium', 'description': 'Expert in garden maintenance and landscaping.' },
{ 'name': 'Emily Clark', 'category': 'commercial', 'service': 'pest-control', 'image': 'https://placehold.co/300', 'rating': 4.5, 'cost': 'medium', 'description': 'Specialist in eco-friendly pest control solutions for offices.' },
{ 'name': 'Mark Lewis', 'category': 'industrial', 'service': 'welding', 'image': 'https://placehold.co/300', 'rating': 4.9, 'cost': 'high', 'description': 'Industrial-grade welding expert for heavy machinery.' },
{ 'name': 'Anna Scott', 'category': 'residential', 'service': 'painting', 'image': 'https://placehold.co/300', 'rating': 4.7, 'cost': 'medium', 'description': 'Professional painter for homes and interiors.' },
{ 'name': 'Daniel Walker', 'category': 'commercial', 'service': 'HVAC-repair', 'image': 'https://placehold.co/300', 'rating': 4.6, 'cost': 'high', 'description': 'Experienced HVAC technician for commercial buildings.' },
{ 'name': 'Sophia Turner', 'category': 'residential', 'service': 'carpentry', 'image': 'https://placehold.co/300', 'rating': 4.4, 'cost': 'medium', 'description': 'Skilled carpenter for home furniture and repairs.' },
{ 'name': 'James Wright', 'category': 'industrial', 'service': 'machinery-repair', 'image': 'https://placehold.co/300', 'rating': 4.3, 'cost': 'high', 'description': 'Expert in repairing industrial-grade machinery.' },
{ 'name': 'Laura Adams', 'category': 'residential', 'service': 'babysitting', 'image': 'https://placehold.co/300', 'rating': 4.9, 'cost': 'medium', 'description': 'Trusted babysitter with years of experience.' },
{ 'name': 'Ethan Phillips', 'category': 'commercial', 'service': 'security-systems', 'image': 'https://placehold.co/300', 'rating': 5.0, 'cost': 'high', 'description': 'Expert in installing and maintaining security systems for offices.' },
{ 'name': 'Chloe Edwards', 'category': 'residential', 'service': 'pet-grooming', 'image': 'https://placehold.co/300', 'rating': 4.8, 'cost': 'medium', 'description': 'Specialized in grooming pets with care and attention.' },
{ 'name': 'Nathan Martin', 'category': 'commercial', 'service': 'window-cleaning', 'image': 'https://placehold.co/300', 'rating': 4.7, 'cost': 'low', 'description': 'Efficient window cleaner for office buildings.' },
{ 'name': 'Victoria Hill', 'category': 'industrial', 'service': 'logistics', 'image': 'https://placehold.co/300', 'rating': 4.5, 'cost': 'high', 'description': 'Expert in industrial logistics and transportation.' },
{ 'name': 'Chris Carter', 'category': 'residential', 'service': 'plumber', 'image': 'https://placehold.co/300', 'rating': 4.6, 'cost': 'low', 'description': 'Reliable plumber for all home plumbing needs.' },
{ 'name': 'Lucy Moore', 'category': 'residential', 'service': 'elderly-care', 'image': 'https://placehold.co/300', 'rating': 5.0, 'cost': 'medium', 'description': 'Compassionate caregiver for the elderly.' },
{ 'name': 'Ryan Nelson', 'category': 'industrial', 'service': 'electrician', 'image': 'https://placehold.co/300', 'rating': 4.3, 'cost': 'medium', 'description': 'Experienced in electrical systems for factories.' },
]

for service_provider in service_providers:
    response = requests.post("http://localhost:8000/services/add", json=service_provider)
    print(response.json())
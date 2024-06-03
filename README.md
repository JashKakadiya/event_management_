# Event Management System

An event management site with dynamic modifications, site settings, and white labeling features. This application allows the admin to add events from the Admin panel, and users can book events and pay for tickets using Razorpay. Additionally, admins can check booked tickets with scanners.

## Features

- **Dynamic Modifications**: Allows admins to make real-time changes to the site.
- **Site Settings & White Labeling**: Customize the site appearance and branding.
- **Admin Panel**: Manage events, bookings, and site settings.
- **Event Booking**: Users can browse events, book tickets, and make payments.
- **Razorpay Integration**: Secure and efficient payment gateway for ticket purchases.
- **Ticket Scanning**: Admins can verify booked tickets using scanners.

## Tools & Technology

- **Django**: Web framework for rapid development and clean design.
- **Python**: Backend programming language.
- **Razorpay**: Payment gateway for handling transactions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/event-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd event-management-system
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- **Admin Panel**: Access the admin panel at `http://localhost:8000/admin/` to manage events and site settings.
- **Event Booking**: Users can browse and book events at the main site URL.
- **Payment**: Integrated with Razorpay for secure payments.
- **Ticket Scanning**: Admins can scan tickets to verify bookings.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:jashcontact750@gmail.com).

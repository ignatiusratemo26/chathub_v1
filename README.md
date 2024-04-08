---
# ChatHub

ChatHub is a web application built with Django Channels that allows users to chat in hubs in real-time. With ChatHub, users can join different hubs and engage in conversations with other users simultaneously.

## Features

- Real-time chat functionality using WebSocket communication.
- Multiple hubs for users to join and participate in discussions.
- Simple and intuitive user interface for easy navigation and interaction.

## Getting Started

To run ChatHub locally on your machine, follow these steps:

### Prerequisites

- Python (>=3.6)
- Django (>=3.2)
- Django Channels (>=3.0)
- Redis (for production deployments)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ignatiusratemo26/chathub_v1.git
   ```

2. Navigate to the project directory:
   ```bash
   cd chathub
   ```

3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Configure the database settings in `chathub/settings.py`.
   
2. Set up the Django Channels layer backend in `chathub/settings.py` for production deployments.

### Running the Application

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Access ChatHub in your web browser at `http://localhost:8000`.

## Usage

1. Create an account or log in to an existing account.
2. Browse the list of available hubs and join one.
3. Start chatting with other users in the hub in real-time.

## Contributing

Contributions are welcome! If you'd like to contribute to ChatHub, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add your feature description'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new pull request.


## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django Channels](https://channels.readthedocs.io/en/stable/) - For real-time WebSocket communication

---

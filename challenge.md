### Running This Project Locally
1. Install uv (https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv sync` to setup your local environment
3. Run `python manage.py runserver` to start the server (debug mode).
4. Create a superuser by running `python manage.py createsuperuser`
5. Access http://localhost:8000/api-auth/ and login with your user
6. Open your browser and access http://localhost:8000/challenge/api/ to view and use the API
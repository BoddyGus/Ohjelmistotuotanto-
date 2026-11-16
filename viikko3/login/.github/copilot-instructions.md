# Copilot instructions

## Project overview

This is a Python 3.14+ Flask application for Ohtu login and registration
flows. Dependencies and the development environment are managed with `uv`.

- `src/index.py` is the development entry point. It starts the Flask
  application on `0.0.0.0:5001` with debug mode enabled.
- `src/app.py` defines Flask routes, renders templates, handles form
  submissions, redirects, and flash messages.
- `src/services/user_service.py` contains the `UserService` class.
  Username and password validation is implemented in
  `UserService.validate`.
- `src/repositories/user_repository.py` provides the in-memory user store.
- `src/entities/user.py` defines the `User` entity.
- `src/templates/` contains the Jinja templates.
- `src/tests/` contains Robot Framework acceptance tests using Browser.

## Environment and commands

This is a `uv` project. Run project commands with `uv run ...`.

Synchronize dependencies:

```bash
uv sync
```

Install the Chromium browser used by Robot Framework Browser:

```bash
uv run rfbrowser install chromium
```

Start the application from the project root:

```bash
uv run python3 src/index.py
```

The application runs at:

```text
http://localhost:5001
```

The application must be running while Robot Framework tests execute.

Run all acceptance tests:

```bash
uv run robot src/tests
```

Run the tests without opening a browser window:

```bash
uv run robot --variable HEADLESS:true src/tests
```

Run one test suite:

```bash
uv run robot src/tests/login.robot
```

Run one test case:

```bash
uv run robot \
  --test "Login With Correct Credentials" \
  src/tests/login.robot
```

## Codebase conventions

- Keep Flask routes, form handling, redirects, and flash messages in
  `src/app.py`.
- Keep validation and authentication rules in
  `src/services/user_service.py`, especially in `UserService.validate`.
- Keep user collection and persistence operations in
  `src/repositories/user_repository.py`.
- The repository is intentionally in-memory. Test state is reset through
  `POST /tests/reset`.
- Registration requires:
  - a non-empty username and password
  - a username of at least three characters
  - a password of at least eight characters
  - a password that is not made only of letters
  - matching password confirmation
  - a username that is not already in use
- Login requires a username and password matching an existing user.
- Failed form submissions display an error message and redirect back to the
  relevant form.
- Successful registration redirects to `/welcome`.
- Successful login redirects to `/ohtu`.
- Preserve the routes and form fields used by the Robot tests:
  `/`, `/login`, `/register`, `/welcome`, `/ohtu`, `/logout`, `/ping`,
  `/tests/reset`, `username`, `password`, and `password_confirmation`.
- Reuse shared keywords from
  `src/tests/resource.robot`.
- Keep tests independent by resetting application state in test setup.
- Make focused changes only and run the relevant Robot tests after changes.

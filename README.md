# the-telescreen

Event notification app that connects to a Linux VPS to monitor the web periodically and alert users when specific events are announced.

## Local database

The project uses a local SQLite database for development. The database is created at:

```text
back/data/telescreen.sqlite
```

Initialize it with:

```bash
python main.py init-db
```

This creates the first table, `requests`, which stores user notification requests with:

- `user_id`
- `request_title`
- `request_summary`
- `information_source_analysis`

The generated SQLite file is ignored by git so each developer or deployment can create its own local database.

## Terminal port

Run the project entry point to open the developer terminal port:

```bash
python main.py
```

The terminal port is an interactive local console for testing and basic project intelligence. It can:

- initialize the database,
- show database path, size, tables, and request count,
- create test notification requests,
- list stored notification requests.

It can also be opened explicitly:

```bash
python main.py terminal-port
```

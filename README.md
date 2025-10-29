# construct-deck
Python CLI and interface for the construct-cache (previously holocron-db) system.

## Setup

### 1. Sync Protos from `sprawl-protocol`

```bash
$ make sync-protos
```

### 2. Setup venv

```bash
$ python3 -m venv .
$ source bin/activate
```

### 3. Install dependencies

```bash
$ pip3 install -e .
```

### 4. Run the CLI

```bash
$ python3 src/construct_deck/cli.py
```

## Syncing protobufs with `sprawl-protocol`

When developing features, you might want to sync your protobufs to the main
`spawl-protocol` repository as well. This will allow other repositories to use
the same protobuf structures when accessing the Construct Cache / Deck.

To sync protobufs, do the following:

1. Setup the `sprawl-protocol` repository through a `git clone`.
2. Set the `SPRAWL_PROTOCOLS_LOCAL_PATH` variable in your `.rc` file (`.zshrc`
for example) to point to the root of the repository
3. Run `make sync-protos-local` to sync the protobufs from the `sprawl-protocol`
repo to this project.
4. If any changes are made in this repo to the protobuf structures and should be
committed to the `sprawl-protocol` repository, run `make push-protos` and commit
the changes in that repository.

New features coming soon! Check out the issues tab.
<p align="center">
  <img src="https://img.icons8.com/ios-filled/500/000000/cloud-database.png" width="200" alt="NEBULA-DB-CORE Cloud Database Icon"/>
</p>

# NEBULA-DB-CORE

Nebula DB Core is an experimental embedded database engine implemented in Python. The project explores the internal architecture of database systems including storage management, indexing structures, query planning, and execution pipelines.

The repository is designed as a structural demonstration of how database engines are organized internally. It models several fundamental components found in relational database systems such as query parsers, execution engines, storage managers, and index structures.

The project emphasizes modular architecture and separation of responsibilities between components.

---

# System Architecture

The database follows a layered architecture similar to modern relational database engines.

```
Client Interface
      │
SQL Parser
      │
Query Planner
      │
Execution Engine
      │
Transaction Manager
      │
Storage Pager
      │
Disk Persistence
```

Each layer operates independently and communicates through well defined interfaces.

---

# Core Components

## SQL Parser

The parser converts textual query statements into structured tokens.

Responsibilities include:

- lexical tokenization
- statement classification
- table identification
- value extraction

The parser output is passed to the query planner.

---

## Query Planner

The query planner transforms parsed tokens into executable query plans.

Plans describe how a query should be executed and which storage operations are required.

Typical plan operations include:

- sequential table scan
- record insertion
- simple key lookup

More advanced planners may implement cost based optimization and index selection.

---

## Execution Engine

The execution engine interprets query plans and performs the required storage operations.

Responsibilities include:

- executing scan operations
- performing insert operations
- producing result sets
- coordinating storage access

Execution plans are processed sequentially by the engine.

---

## Storage Pager

The pager is responsible for reading and writing data pages to persistent storage.

Responsibilities include:

- page allocation
- page serialization
- disk file management
- storage abstraction

Pages represent the fundamental unit of disk storage used by the database.

---

## B-Tree Index Structure

The index subsystem implements a simplified B-Tree used to organize indexed values.

B-Trees provide balanced search tree structures optimized for disk based storage.

Supported operations include:

- key insertion
- key lookup
- node traversal

B-Trees are widely used in database engines due to their efficient search performance and disk friendly layout.

---

## Transaction Manager

The transaction manager coordinates transactional operations.

Responsibilities include:

- transaction initialization
- commit operations
- rollback handling

Although simplified, the component illustrates how database systems manage stateful operations.

---

# Query Execution Flow

A typical query follows this execution sequence.

1. client submits query
2. parser tokenizes query
3. planner generates execution plan
4. executor processes plan
5. storage layer performs disk operations
6. results returned to client

This pipeline mirrors the workflow used in many relational database systems.

---

# Repository Layout

```
engine/
    database.py
    planner.py
    executor.py
    transaction.py

storage/
    pager.py
    buffer.py
    page.py

index/
    btree.py
    node.py

query/
    parser.py
    tokenizer.py

utils/
    serializer.py
```

Each module focuses on a specific responsibility within the database architecture.

---

# Running the Database

Launch the interactive database shell.

```
python server.py database.db
```

Example session:

```
nebula> insert into users values 1 alice
nebula> insert into users values 2 bob
nebula> select * from users
```

---

# Design Objectives

The project aims to illustrate:

- database engine architecture
- storage layer abstraction
- query planning concepts
- indexing data structures
- execution pipeline design

The implementation favors readability and architectural clarity over raw performance.

---

# Potential Extensions

Future improvements could include:

- page level B-Tree node splitting
- buffer cache management
- write ahead logging
- query optimizer
- concurrency control
- multi version concurrency control
- secondary indexing
- replication layer

---

# License

MIT License

---

# Author

Yonathan  
aka Witwizard

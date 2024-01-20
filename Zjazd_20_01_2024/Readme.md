# synchronous req

```mermaid
sequenceDiagram
    actor User
    User ->> Internet: download Yt.com
    activate Internet
    Internet ->> User: masz
    deactivate Internet
    User ->> Internet: download onet.pl
    activate Internet
    Internet ->> User: masz
    deactivate Internet
```

# asynchronous req

```mermaid
sequenceDiagram
    actor User
    User ->> Internet: download Yt.com
    User ->> Internet: download onet.pl
    activate Internet
    Internet ->> User: masz
    Internet ->> User: masz
    deactivate Internet
```
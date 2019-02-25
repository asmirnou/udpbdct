# udpbdct

Simple utility to verify how UDP broadcast works in various networks.

## Usage:

In one or more terminal run the listener:
```bash
python udpbdct.py
```
In another terminal run the sender:
```bash
python udpbdct.py sender
```

The sender will broadcast the messages to all listeners on port 3000.

To see how it works in Docker run:
```bash
docker build . --tag udpbdct

docker-compose up
```

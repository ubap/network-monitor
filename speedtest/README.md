Designed to run on DELL WYSE 5060


```
echo "<TOKEN>" | docker login ghcr.io -u USERNAME --password-stdin
docker push ghcr.io/ubap/network-monitor:latest

docker run ghcr.io/ubap/network-monitor:latest
```
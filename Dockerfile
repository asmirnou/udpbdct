FROM alpine:latest

RUN \
  apk add --update python && \
  rm -rf /var/cache/apk/*

ADD udpbdct.py ./

EXPOSE 3000/udp

ENTRYPOINT ["python", "udpbdct.py"]

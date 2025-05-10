FROM alpine:latest

RUN apk add --no-cache keepalived haproxy bash iproute2 curl

RUN mkdir -p /etc/keepalived && \
    chmod 644 /etc/keepalived/keepalived.conf || true

CMD ["sh"]

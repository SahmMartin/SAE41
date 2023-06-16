docker run --rm -it --network=host -h=127.0.0.1 deb-cli-1 bash
RUN mysql -u root -p'foo' -h 127.0.0.1

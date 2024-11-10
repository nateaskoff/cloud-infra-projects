FROM i386/debian:stretch-slim as builder

ARG NWN_VERSION=8152

RUN apt-get update
RUN apt-get -y install unzip wget
RUN mkdir -p /nwn/nwnx

# Use wget instead of ADD
RUN wget https://nwnx.io/nwnee-dedicated-${NWN_VERSION}.zip -O /nwn/tmp/nwnee-dedicated.zip
RUN unzip /nwn/tmp/nwnee-dedicated.zip -d /nwn/data

FROM i386/debian:stretch-slim
LABEL maintainer "niv@beamdog.com"

RUN apt-get update && \
  apt-get --no-install-recommends -y install \
    libc6:i386 libstdc++6:i386 && \
  rm -r /var/cache/apt /var/lib/apt/lists

RUN mkdir -p /nwn/data /nwn/home /nwn/run

# Copy the server binaries from builder image
COPY --from=builder /nwn/data/data /nwn/data/data

ENV NWN_ARCH linux-x86

COPY --from=builder /nwn/data/bin/${NWN_ARCH} /nwn/data/bin/${NWN_ARCH}
RUN chmod +x /nwn/data/bin/${NWN_ARCH}/nwserver-linux

COPY /docker/run-server.sh /docker/prep-nwn-ini.awk /docker/prep-nwnplayer-ini.awk /nwn/
RUN chmod +x /nwn/run-server.sh

# Create a non-root user
RUN groupadd -r nwn && useradd --no-log-init -r -g nwn nwn
RUN chown -R nwn:nwn /nwn

# Switch to the non-root user
USER nwn

VOLUME /nwn/home

EXPOSE ${NWN_PORT:-5121}/udp

ENV NWN_TAIL_LOGS=y
ENV NWN_EXTRA_ARGS="-userdirectory /nwn/run"

WORKDIR /nwn/data/bin/${NWN_ARCH}

# Add HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:${NWN_PORT:-5121} || exit 1

ENTRYPOINT ["/nwn/run-server.sh"]

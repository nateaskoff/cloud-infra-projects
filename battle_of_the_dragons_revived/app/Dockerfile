#checkov:skip=CKV_DOCKER_2:no way to do health check with nwserver
FROM 32bit/ubuntu:20.04

# Install dependencies
RUN apt-get update && \
  apt-get -y install \
    libc6:i386 libstdc++6:i386 wget unzip awscli supervisor && \
  rm -r /var/cache/apt /var/lib/apt/lists

# Make directory /nwserver
RUN mkdir /nwserver

# Make nwserver-user with home directory
RUN useradd nwserver-user -s /bin/bash -m -d /home/nwserver-user

# Add nwserver-user to group nwserver-group
RUN groupadd nwserver-group
RUN usermod -a -G nwserver-group nwserver-user

# Change owner of /nwserver to nwserver-user
RUN chown nwserver-user:nwserver-group /nwserver

# Download NWN:EE server for linux to /tmp
RUN wget -O /tmp/nwserver-linux.zip https://nwn.beamdog.com/downloads/nwnee-linux.zip

# Unzip the downloaded file to /nwserver
RUN unzip /tmp/nwserver-linux.zip -d /nwserver

# Set nwserver-linux to mode a+x for nwserver-user
RUN chmod a+x /nwserver/bin/linux-x86/nwserver-linux

# Change to nwserver-user
USER nwserver-user

# If the path ~/.local/share/Neverwinter Nights/modules/ does not exist, create it
RUN mkdir -p ~/.local/share/Neverwinter\ Nights/modules/

# copy supervisord.conf to default location
COPY supervisord.conf /etc/supervisor/supervisord.conf

# copy supervisor.sh to /nwserver
COPY supervisor.sh /nwserver/supervisor.sh

CMD ["/bin/bash", "supervisor.sh"]

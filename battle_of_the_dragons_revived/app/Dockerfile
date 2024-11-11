#checkov:skip=CKV_DOCKER_2:no way to do health check with nwserver
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libc6-i386 libstdc++6-i386-cross wget unzip supervisor python3
RUN python3 -m pip install boto3

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
RUN wget -O /tmp/nwserver-linux.zip https://nwn.beamdog.net/downloads/nwnee-dedicated-8193.34.zip

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

# copy nw_server.py to /nwserver
COPY nw_server.py /nwserver/nw_server.py

CMD ["python3", "nw_server.py"]

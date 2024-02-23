# Use the base image
from docker.models.images import Image
image = Image.from_base_image('modenaf360/gotty', 'latest')

# Expose the desired port
image.expose_port(8880)

# Start Gotty with the specified command
image.start_command('gotty', '--port', '8888', '/bin/bash')

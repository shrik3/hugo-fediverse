#!/usr/bin/bash

# THIS IS AN EXAMPLE
# DON'T RUN ME WITHOUT MODIFYING!

# FOOLPROOF
echo "do you know what you are doing?"
exit()

cd <PATH_TO_TIMELINE_BOT>
echo "Fetching Timeline from fedi..."
./timelinebot.py
cp tl.json <PATH_TO_SITE_ROOT_DATA>

cd <PATH_TO_SITE_ROOT>
echo "Rendering blog..."
hugo

echo "Sync blog to remote server..."
rsync -avh -og --chown=http:http --info=progress2 --info=name0 --update --delete-after \
    <PATH_TO_SITE_ROOT_PUBLIC> \
    user@remote_server:<PATH_TO_WEB_DOC_ROOT>

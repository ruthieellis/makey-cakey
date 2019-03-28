import uuid
# Jekyll will import posts from Blogger, but they still contain links to larger
# image formats as references to Blogger's CDN. This script:
# - Finds all linked image references in an imported blogger page
# - Downloads the images into the assets/ directory
# - Rewrites the page with the appropriate image link

import re
import sys
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

IMG_RE = re.compile('<a[^>]+href="(?P<src2>[^"]+)"')
DATE_RE = re.compile('(?P<date>[0-9]+\-[0-9]+\-[0-9]+)')

for filename in sys.argv[1:]:
    date_prefix = DATE_RE.search(filename).group('date')
    with open(filename, 'r') as f:
        file_index = 0
        contents = f.read()
        for match in IMG_RE.finditer(contents):
            try:
                sourceurl = match.group('src2')
                extstart = sourceurl.rfind('.')
                extension = sourceurl[extstart:]
                newfile = date_prefix + str(uuid.uuid4())[:8] + '-large-image-{:04d}{}'.format(file_index, extension)
                file_index += 1
                print('{} => {}'.format(sourceurl, newfile))
                urlretrieve(sourceurl, '../assets/large/' + newfile)
                contents = contents.replace(sourceurl, '{{ site.url }}/assets/large/' + newfile)
            except:
                pass


    with open(filename, 'w') as f:
        f.write(contents)

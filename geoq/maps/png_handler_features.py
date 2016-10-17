from django.conf import settings
from django.templatetags.static import static
import os
import zipfile
import shutil

def save_png_file(png_file):
    # figure out where the repository is, create folder, and extract kmz to there
    PNG_FILE_TYPE = unicode('image/png')

    rootdir = getattr(settings, 'STATIC_ROOT')
    markerdir = 'images/markers/user_generated/'
    #kmldir = getattr(settings, 'KML_REPOSITORY_ROOT', "kml/")
    #dirname = kmz_file.name.rsplit(".",1)[0] + "/"
    path = rootdir + markerdir
    #filename = 'doc.kml'

    try:
        os.mkdir(path)
    except OSError as e:
        print "Error creating path",path,"due to",e
        shutil.rmtree(path)
        os.mkdir(path)

    if png_file.content_type == PNG_FILE_TYPE:
        #z = zipfile.ZipFile(kmz_file)
        #for name in z.namelist():
        #    z.extract(name, path)

        #rename file with random number at end
        #return response of file all set
    else:
        filename = kmz_file.name
        with open(path + filename, 'wb+') as destination:
            for chunk in kmz_file.chunks():
                destination.write(chunk)


    # see if we have a doc.kml file in the root directory
    if os.path.isfile(path + filename):
        return static(kmldir + dirname + filename)
    else:
        return None

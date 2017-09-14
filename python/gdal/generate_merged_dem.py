import os
import glob
import gdal
import subprocess


def is_left_from_dateline(input_file):
    result = False
    raster = gdal.Open(input_file)
    geotransform = raster.GetGeoTransform()
    originX = geotransform[0]
    result = originX > 0
    raster = None
    return result


def merge_with_additional_move(merged_file, input_files):
    EAST_WEST_DIFF = 360
    MOVE_DIST = 10

    def move(input_file, output_file):
        input_ds = gdal.Open(input_file)
        geotransform = list(input_ds.GetGeoTransform())
        originX = geotransform[0]
        if originX > 0:
            originX -= EAST_WEST_DIFF
        originX += MOVE_DIST
        geotransform[0] = originX

        driver = gdal.GetDriverByName("GTiff")
        output_ds = driver.CreateCopy(output_file, input_ds, strict=0)
        output_ds.SetGeoTransform(tuple(geotransform))
        output_ds = None
        input_ds = None

    def move_back(merged_file):
        merged_ds = gdal.Open(merged_file, gdal.GA_Update)
        geotransform = list(merged_ds.GetGeoTransform())
        originX = geotransform[0]
        originX += (EAST_WEST_DIFF - MOVE_DIST)
        geotransform[0] = originX
        merged_ds.SetGeoTransform(tuple(geotransform))
        merged_ds = None

    output_files = []
    for input_file in input_files:
        filename, extension = os.path.splitext(os.path.basename(input_file))
        root = os.path.dirname(input_file)
        output_file = os.path.join(root, filename + '_intermediary' + extension)
        output_files.append(output_file)
        move(input_file, output_file)

    merge(merged_file, output_files)
    map(os.remove, output_files)
    move_back(merged_file)


def merge(output_file, input_files):
    cmd = ['gdal_merge.py',
           '-co', 'COMPRESS=LZW',
           '-co', 'BIGTIFF=YES',
           '-o', output_file] + input_files

    print " ".join(cmd)
    process = subprocess.Popen(cmd,
                               shell=False,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    status = process.poll()
    if process.returncode == 0:
        print stdout
    else:
        raise Exception("%s failed with an exitcode of %s: %s" % (
            str(cmd), status, stderr))


if __name__ == '__main__':
    dem_files = glob.glob('elevation*.tif')
    merged_name = os.path.join(os.path.dirname(dem_files[0]), 'highVariance_dem.tif')
    left_to_dateline = map(is_left_from_dateline, dem_files)
    if any(left_to_dateline) and not all(left_to_dateline):
        merge_with_additional_move(merged_name, dem_files)
    else:
        merge(merged_name, dem_files)


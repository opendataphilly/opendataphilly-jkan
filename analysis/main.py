from db import DB
import os
import frontmatter
import wget

def main():
    # find geojson resource urls
    cwd = os.getcwd()
    md_datasets_path = os.path.join(cwd, "..", "_datasets")
    geojson_paths = []
    for md_dataset_filename in os.listdir(md_datasets_path):
        if len(geojson_paths) >= 2:
            break
        md_dataset_path = os.path.join(md_datasets_path, md_dataset_filename)
        if os.path.isfile(md_dataset_path):
            try:
                md_dataset = frontmatter.load(md_dataset_path)
                resources = md_dataset.metadata.get("resources")
                for resource in resources:
                    if resource.get("format") == "GeoJSON":
                        resource_name = resource.get("name")
                        url = resource.get("url")
                        downloaded_geojson_path = (
                            f"working_files/{md_dataset_filename}-{resource_name}.geojson"
                        )
                        if not os.path.exists(downloaded_geojson_path):
                            print(f"Downloading {url} to {downloaded_geojson_path}...")
                            wget.download(url, downloaded_geojson_path)
                            print("\nDownload complete.")
                        else:
                            print(
                                f"File {downloaded_geojson_path} already exists. Skipping download."
                            )
                        geojson_paths.append(downloaded_geojson_path)
            except Exception as e:
                print(f"Error loading {md_dataset_filename}: {e}")
    db = DB()
    db.connect()
    db.prepare_datasets_table()
    db.import_census_tracts()
    for geojsonpath in geojson_paths:
        db.import_dataset(geojsonpath)
    db.derive_census_tracts_from_datasets()
    db.close()

if __name__ == "__main__":
    main()